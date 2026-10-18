---
name: server-migration
description: Migrate Wallace's production apps (skipy, hiddenbeer, House Hunter, LoveMail, CabinetFlow, movie-helper, W-Tech website, skipy.io) from one Ubuntu VPS to a new one — inventory, provisioning, hardening, clone-in-standby, verification of old vs new origin, resync and cutover. Use when asked to "prepare a new server", "migrate apps to the new VPS", "clone server X to Y", "compare old and new server", "resync the new server" or "cut over to the new server".
---

# Server Migration (old VPS → new VPS)

Battle-tested on the 2026-10 move **server-be (194.31.150.176, Ubuntu 22.04) → server-vps (82.180.155.136,
Ubuntu 26.04)**. Canonical scripts and the config mirror live in the skipy repo:
`~/git/skipy/infra/scripts/server/vps/` (`setup-server-vps.sh`, `harden-db.sh`, `env_resync.py`,
`resync-from-server-be.sh`, `cutover-enable.sh`, `etc/`, `root/`). Copy that folder to
`infra/scripts/server/<new-alias>/` and adapt names/IPs: never rewrite from scratch.
Verification tools are in this skill: `scripts/smoke.sh`, `scripts/http_compare.py`.

## Ground rules (user decisions, non-negotiable)

- **Copy, never move.** The old server stays live and receives deploys until cutover. Read-only there, except
  removing temp files you created. Its deploy scripts / GitHub workflows / test-all must keep working.
- All apps live under **`/srv/<app>`** on the new server (on the old one HH/lovemail/cabinetflow were in
  `/var/www`, movie-helper in `/opt`).
- **Do not copy**: WordPress, Apache, PHP, MySQL, House Hunter `.next/cache`. Do copy backups (`/srv/*/backups`,
  `/srv/backup`, `/srv/offsite`, `/var/backups/mongo`), uploads/assets first (no other off-disk copy).
- New users/keys/passwords → mailed to **wallace.espindola@gmail.com** (exactly one recipient), written to
  `/root/.db-credentials` (600). Never print secrets in chat; print env var **names** only.
- Backups policy: Hostinger free weekly VPS backup + per-app mongodump scripts. Don't propose paid backups.
- Every server config change is mirrored into the repo and committed (no co-author lines). **Push only with
  explicit approval.** Never deploy to the old server.
- Security hardening applies to the new server only.

## Phase 0 — Inventory the old server (read-only)

```bash
ssh OLD 'ls /etc/nginx/sites-enabled; systemctl list-units --type=service --state=running --no-pager --plain;
  docker ps --format "{{.Names}}\t{{.Image}}"; crontab -l; ls /etc/systemd/system/*.service;
  du -sh /srv/* /var/www/* /opt/*; ls /etc/letsencrypt/live /etc/ssl'
```
Dump every vhost, unit, compose file, `nginx.conf`, crontab. List DBs with sizes and per-DB document counts
(keep them for the restore check). Note apps that are **not** on the server (immo-search = Mac launchd job,
clipz4u = no deploy) and tell the user instead of inventing a deploy.

## Phase 1 — Base provisioning

Run the adapted `setup-server-vps.sh` (idempotent). Hard-won gotchas:
- **MongoDB**: Ubuntu 26.04 has no server package → use the **noble** repo; 8.3 repo is signed with the
  `server-8.0.asc` key. Kernel ≥ 6.19: packaged `GLIBC_TUNABLES=glibc.pthread.rseq=0` trips mongod's guard →
  drop-in `UnsetEnvironment=GLIBC_TUNABLES`. 8.0/8.2 don't start on kernel 7 at all. Add `mongodb-thp.service`,
  swappiness 1, overcommit 1. `cacheSizeGB 1.5`, bind 127.0.0.1.
- postfix Gmail relay needs **`postfix-lmdb`** (lmdb maps on 26.04); copy `sasl_passwd`, `sender_canonical`,
  aliases from the old server; set `/etc/mailname`.
- Generate `en_US.UTF-8` (Mac forwards `LC_CTYPE=UTF-8` → perl warnings).
- fail2ban sshd: `backend = systemd` + `journalmatch = _SYSTEMD_UNIT=ssh.service`. Copy ufw REJECTs and allowlist.
- **Docker-published ports bypass ufw** → containers on host network / bound to 127.0.0.1 only.
- Disable `certbot.timer` (the cron `certbot-renew.sh` is the only renewal path).
- uv + Python 3.12 system-wide in `/opt/uv/python`; Node LTS (NodeSource) + `npm i -g serve pnpm`; JDK 21.
- Copy oh-my-zsh config, GHCR `/root/.docker/config.json`, GitHub deploy keys to `authorized_keys`, github.com
  known_hosts. Key-only root SSH.

## Phase 2 — Hardening (new server only)

`harden-db.sh`: Mongo auth on, `mongoadmin` (root), `backup` (backup/restore/clusterMonitor), one user per app
DB (readWrite+dbAdmin, authSource=admin): skipy→skipy_db, hiddenbeer, househunter→immobusiness, lovemail,
cabinetflow, **wtech** (the W-Tech site needs its own user; it used unauthenticated Mongo before). Redis
`requirepass` (`redis-cli -u redis://:pw@` fails on the empty user, redis-py/kombu are fine). Backup scripts read
`MONGO_AUTH=(...)` from `server.env`. movie-helper runs as system user `moviehelper`, not root.

**Before auth goes on, make sure no app logs its DB URI**: `grep -rn "MONGO_URI}\|MONGODB_URI}"` in each app.
skipy/hiddenbeer used to log it verbatim. Both now mask it with `mask_uri()` (skipy `app/core/logging_config.py`,
hb `app/logger.py`, 2026-10-19). Then grep the new server's logs for `mongodb://user:<not ***>@` and scrub hits
**in place** (Python `open(f, "r+")` → `re.subn` → `truncate()`). `sed -i` swaps the inode, the app keeps writing
to the deleted file, and new lines vanish. `docker logs` hits go away when the container is recreated.
If anything leaked, rotate that app's DB password.

## Phase 3 — Clone apps

Transfer old → new directly with agent forwarding (`ssh-add ~/.ssh/id_ed25519`, then `ssh -A OLD 'rsync ... root@NEW:...'`).
No `--delete`; always `--exclude=.env --exclude='.env.*'` and venvs. Mapping:
`/srv/{skipy,hiddenbeer,wtech-website}` → same; `/var/www/{househunter,lovemail,cabinetflow,skipy-io}` → `/srv/…`;
`/opt/movie-helper` → `/srv/movie-helper`; `/var/www/demo` → `/srv/wtech-website/demo`; `/etc/letsencrypt`,
`/etc/ssl/{cabinet-flow,househunter,lovemail}` (Cloudflare origin certs).

- **DBs**: per-DB stream, never all-in-one (`--nsExclude` doesn't exist in mongodump):
  `mongodump --archive --gzip --db=X | ssh NEW 'mongorestore --archive --gzip --drop --uri="mongodb://mongoadmin:…@127.0.0.1:27017/?authSource=admin"'`.
  ⚠️ A URI **with a db path** (`…/admin?…`) makes mongorestore filter namespaces and restore **nothing** while
  reporting success. Compare per-DB `countDocuments` against Phase 0.
- **.env**: `env_resync.py` takes the old server's current file and re-applies only the new-server overrides
  (keys whose value differs from the `.bak-preauth-*` copy, i.e. DB/Redis credentials) + the standby block.
- **nginx**: copy old `nginx.conf` + `conf.d/cloudflare-real-ip.conf` + vhosts; sed `/var/www/<app>` and
  `/opt/movie-helper` → `/srv/…`, old IP → new IP, `/demo/` `root /var/www` → `alias /srv/wtech-website/demo/`;
  `listen 443 ssl http2` → `listen 443 ssl;` + `http2 on;`. Real files in sites-available, symlinks in sites-enabled.
- **systemd units**: same sed; `npx serve` → `/usr/bin/serve` and bind `tcp://127.0.0.1:<port>`; movie-helper
  `User=moviehelper` + sandboxing; cabinetflow `.env` gets `SERVER_ADDRESS=127.0.0.1`.
- **Runtimes**: rebuild venvs, never copy them (absolute paths, other Python): HH
  `sudo -u www-data uv sync --frozen --no-dev --python 3.12` (UV_CACHE_DIR=/var/www/.cache/uv, `/var/www`
  = www-data home, create it); movie-helper `uv venv --python 3.12 && uv pip install -r requirements.txt`.
  Node `node_modules` / Next standalone copy as-is.
- **Docker**: skipy + hiddenbeer `docker compose pull && up -d` (GHCR); locally built images (wtech-website) via
  `docker save | gzip | ssh NEW 'gunzip | docker load'`, then `up -d --no-build`. `chmod 777` the log dirs.
- `chown -R www-data` HH/lovemail/cabinetflow; `moviehelper` movie-helper.

## Phase 4 — Standby: nothing may run twice ⚠️

With a copied DB, schedulers on the new server would mail/charge real users a second time. Before starting apps:

| App | Job with side effects | Switch on the new server |
|---|---|---|
| skipy | in-process scheduler: onboarding/trial/deletion emails | `EMAILS_ENABLED=false`, `USE_REAL_SMS=false` (env block) |
| hiddenbeer | Stripe payouts 06:00, voucher mails, social posts, statements | DB copy: `platform_settings{key:"features"}` `vouchers_enabled=false, social_posting_enabled=false` (DB beats env); env `USE_REAL_SMS=false`, `VOUCHER_EXPIRING_EMAIL_ENABLED=false`, `SOCIAL_POSTING_ENABLED=false` |
| House Hunter | celery beat: alerts, digests, price-drop mails, scraping | install `househunter-worker`/`-scraper` units **disabled** |
| LoveMail | `processScheduledEmails` every 60 s (no env switch) | check `emailSent:false` count in copy; resync before cutover |
| CabinetFlow | waitlist nurture emails via Brevo | `APP_WAITLIST_SCANCRON=-` |
| movie-helper, W-Tech | none | — |

Env switches live between `# >>> server-vps standby` / `# <<< server-vps standby <<<` markers so cutover can
delete them. Crontab: install the old crontab but prefix `#CUTOVER# ` on `app_monitor.py` (checks public URLs
→ duplicate alerts), `certbot-renew.sh` (HTTP-01 only passes where DNS points), `offsite-sync.sh` (no peer).
Dry-run monitors with `MAIL_DRY_RUN=1` before leaving cron on. Inbound webhooks (Stripe/Twilio) keep hitting
whatever DNS points to — fine.

## Phase 5 — Verify old vs new

1. Local upstreams on the new server (`curl 127.0.0.1:<port>/health`), `systemctl --failed`, container health,
   error grep in journal/docker logs.
2. `scripts/smoke.sh <ip>` for both IPs side by side (`paste <(smoke.sh OLD) <(smoke.sh NEW)`).
3. `scripts/http_compare.py <sites>`: sitemaps + every param-less GET from OpenAPI, both origins, diff
   status/size. OpenAPI is disabled in prod for skipy/HH → generate inside the runtime:
   `docker exec skipy-api python -c "import json,logging; logging.disable(50); from app.main import app; print(json.dumps(app.openapi()))"`
   (HH: same with the venv + `set -a; . ./.env`), hb serves `/openapi.json`. Save as `oa-<app>.json` in
   `$OPENAPI_DIR`. **Pacing matters**: fail2ban `nginx-404` bans at 20×404/60 s and `nginx-limit-req` too — the
   script caps 404s at 8/min and skips auth/side-effect routes. Retest `000` (timeouts) once before calling it a diff.
4. Real browser: dispatch a `qa-tester` agent running Playwright Chromium twice with
   `--host-resolver-rules=MAP <domain> <ip>,…` + `ignore_https_errors`, read-only (no login/forms), diffing
   console errors, failed requests, first-party API statuses. Run it in the background while doing 2–3.
5. Don't compare skipy/hb while the user is deploying to the old server — resync first.
6. Expected diffs while in standby: hiddenbeer Beer Pass / promoter / voucher / social routes return 404
   `feature_disabled` on the new server (the payout flag also hides the feature). Everything else must match.

**Letting the user test before DNS:** `/etc/hosts` line mapping all domains to the new IP (only faithful method:
login, OAuth, cookies, client-side API calls). Optional temp IP ports (`listen 8441..8447 ssl` per vhost +
`ufw allow 8441:8447/tcp`, marked `TEMP pre-cutover`) are page/health-only: Google OAuth rejects IP origins,
skipy-manager builds its API URL from the hostname **without the port**, frontends with a baked domain call the
old server.

## Phase 6 — Resync and cutover

- Any time: `resync-from-<old>.sh` from the Mac = full refresh (code, images, `.env`, uploads, DBs, restart),
  stays in standby. Ask before running it if the user may be mid-deploy.
- Cutover (user-approved, before the old server expires): freeze deploys → stop old schedulers
  (`househunter-worker/-scraper`, `lovemail-backend`) → `resync … --final` → `cutover-enable.sh` on the new server
  (removes standby blocks, recreates APIs, enables HH workers, uncomments `#CUTOVER#`, closes test ports) →
  Cloudflare A records → replace the old IP in GitHub workflows (skipy `deploy.yml`, `smoke.yml`,
  `status-be.yml`; hiddenbeer `deploy.yml`, `email-smoke.yml`) → update memory `project_servers`.

## Partial cutover (per app) — learned 2026-10-18

- Per app: final DB sync of that app only → drop its standby switches on the new server → disable its
  duplicate scheduler on the old one (e.g. CabinetFlow `APP_WAITLIST_SCANCRON=-` there; LoveMail: confirm
  `emailSent:false` count is 0) → switch DNS → prove routing with a unique query marker grepped in both
  nginx access logs. Then **remove the app from `resync-from-*.sh` / `env_resync.py`** (a later resync would
  overwrite its newer data) and repoint that app's deploy script (wtech `deploy.py`).
- Cloudflare: the dashboard's internal API (`fetch('/api/v4/...', {headers:{'x-cross-site-security':'dash'}})`)
  reads zones/records fine but **writes return 403**; edit A records in the UI (Edit → IPv4 → Save), keep proxied.
  www CNAMEs to the apex follow automatically. Leave mail/DKIM/hosting records alone.
- **HTTP 525 on Ubuntu 26.04 origins**: OpenSSL 3.5 prefers X25519MLKEM768; Cloudflare origin pulls get a
  HelloRetryRequest and fail with `bad cipher` (seen with `error_log … info`). Fix: `ssl_ecdh_curve
  X25519:prime256v1:secp384r1;` in `conf.d/tls-ciphers.conf` (already in setup script). Test every migrated
  domain through Cloudflare, not only with `--resolve`.
- **Let's Encrypt** (W-Tech is the only LE domain besides skipy/hb): once its DNS points to the new server,
  `certbot renew --cert-name <domain> --dry-run` there (HTTP-01 passes through the Cloudflare proxy). Then drop
  the `#CUTOVER#` prefix from the `certbot-renew.sh` cron line only. `certbot renew` skips certs that aren't due,
  so it's safe while the other apps' DNS still points to the old server. Until the old server goes away, both send
  the weekly SSL report.
- **Old-IP sweep per migrated app** (grep the old IP, `server-be`, `/var/www/<app>`, `/opt/<app>`):
  - On the new server:
    - app `.env` CORS/origin lists (LoveMail `FRONTEND_URL` had `http://<old-ip>:1415`), back up then restart;
    - `.env` comments;
    - crontab header label (`SERVER-BE · <old-ip>` → new name/IP) and "BE only" notes;
    - stale server-side copies of deploy files (`/srv/wtech-website/deploy.py`, README).
  - In the repos: README/CLAUDE.md, deploy scripts, compose comments, the other-apps backup scripts
    (they must check `/srv/<app>` before `/var/www/<app>`; House-Hunter `deploy/ops-scripts` keeps copies).
  - **CabinetFlow, LoveMail and movie-helper have no source repo** (not on GitHub, not on the Mac, and `/srv`
    has no `.git`), so they're edited on the server only. Ask the user before saying a repo is missing.
  - Skip old-server `*.bak*` / `_archive` files and the skipy/hb/HH refs until their own cutover.
- **Nothing to migrate**:
  - skipy.com.br / hiddenbeer.com.br: proxied A records to the dead server-br plus Cloudflare 301 redirect rules
    to .online/.com. They work as-is (check with `curl -I`).
  - immo-search: a Mac launchd job (`com.immo-search`, disabled 2026-10-18).
  - clipz4u: no deployment and no zone.

## Known issues to surface

- skipy-api / hiddenbeer-api logged the full Mongo URI with its password at startup. Fixed in code on 2026-10-19
  (skipy 72d97db, hb 9b59c64) and live after their next deploy. If a new server ran an older image with auth on,
  check its logs (Phase 2) and rotate the passwords.
- `cabinet-flow.com/api/waitlist/count` 500s on both servers (pre-existing).

## Report

End with: what was copied, what was deliberately not, standby list, test URLs (hosts-file block + IP ports),
verification table old vs new, open decisions (push, cutover date). Save state in memory
`server_vps_migration_*`.
