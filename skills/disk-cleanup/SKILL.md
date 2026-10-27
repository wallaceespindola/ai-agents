---
name: disk-cleanup
description: Free disk space on Wallace's Mac (macOS, Apple Silicon) by surveying usage and deleting only regenerable caches, build outputs and unused Docker data, in tiers - zero-risk caches run straight away, anything with side effects is offered first, personal files are listed for approval and never auto-deleted. Use when asked to "free space", "free disk", "clean up my computer/mac", "disk is full", "what is using my disk", "find garbage to delete", or when a build fails with "No space left on device".
---

# Disk Cleanup (macOS)

Frees space in tiers. Survey, delete what is safe, ask about the rest, report before/after.

## Hard rules

- **Never touch user data.** Downloads, Documents, Desktop, Pictures, Movies, Music, `.git` dirs, DB backups (`*/backups/*`, `*.archive.gz`, dumps), `.env` files: list them for approval, never delete on your own.
- **Never delete `~/.claude/` contents** (`projects/` = session history, `plugins/` cache = live hooks broke when removed on 2026-10-20), `~/.claude-mem/`, or `~/.npm/_npx` (plugin MCP servers start from it).
- **Keep the running and previous Claude Code versions** in `~/.local/share/claude/versions/`. Only older ones go. Find the running one with `readlink $(which claude)`.
- **Don't delete build output under a running dev server.** First run `pgrep -fl "next dev|next start|mvn|gradle|uvicorn|gunicorn|vite|mypy"`. On a hit, skip that repo's `.next`/`target`/`dist`.
- **Keep running Docker containers and their images.** `docker image prune -a` already keeps images in use. Don't pass `--volumes` to `system prune` without asking.
- **No sudo.** No sudo means no `/Library`, `/private/var`, or system-wide prune. Mention them as manual steps.
- `rm -rf` only on paths you have listed and sized. Never use globs over `~` or `~/Library` without a fixed subpath.

## Procedure

### 1. Survey

Run `scripts/scan.sh` (read-only, takes 1-3 min). It prints free space and the top dirs in home, `~/Library`, Caches, Application Support and `~/.cache`. It also covers repo build/dependency dirs, Docker usage, large stray files and installer leftovers.

`Operation not permitted` on Downloads/Documents/Trash is macOS TCC. To scan them, the terminal app needs **System Settings → Privacy & Security → Full Disk Access**, and Claude Code must be restarted. The `!` prefix doesn't help because it runs in the same process.

### 2. Tier 1: run without asking (regenerable caches, no side effects)

Record `df -h /System/Volumes/Data` first.

```bash
uv cache clean
npm cache clean --force          # EACCES on root-owned files -> mention `sudo chown -R $(whoami) ~/.npm`
uvx pre-commit gc                # pre-commit is often not on PATH; uvx works
pnpm store prune
brew cleanup -s --prune=all
pip3 cache purge
go clean -cache
bun pm cache rm
rm -f ~/.sdkman/tmp/*.zip        # SDKMAN installer leftovers
rm -rf ~/Library/Caches/{pip,go-build,Homebrew,pnpm,virtualenv,node-gyp,colima}
rm -rf ~/Library/Caches/*.ShipIt ~/Library/Caches/*-updater   # app self-update downloads
rm -rf ~/Library/Logs/JetBrains/*
rm -rf ~/Library/Application\ Support/Google/GoogleUpdater/crx_cache/*
rm -rf $TMPDIR/pytest-of-* $TMPDIR/node-compile-cache
```

Old Claude Code versions: delete everything in `~/.local/share/claude/versions/` except the newest two.

Repo build outputs (dev-server check first), down to depth 4 under `~/git`:

```bash
find ~/git -maxdepth 4 -type d \( -name .next -o -name target -o -name .mypy_cache \
  -o -name .pytest_cache -o -name .ruff_cache \) -not -path "*/node_modules/*" -prune -exec rm -rf {} +
```

### 3. Tier 2: ask first (AskUserQuestion, multiSelect, with sizes)

Offer only the items the scan found at a meaningful size (>200 MB):

| Item | Side effect to state |
|---|---|
| Docker unused images + volumes: `docker image prune -a -f; docker volume prune -f; docker builder prune -af` | Images re-pull on next compose. Name any custom/local-only image (e.g. `*-old`), since it can't be re-pulled |
| After Docker prune with colima: `colima ssh -- sudo fstrim -av` | **Required**, otherwise the host disk file doesn't shrink. Gave back 14 GB on 2026-10-27 |
| App caches: `~/Library/Caches/{JetBrains,Google,com.spotify.client,ms-playwright*,SiriTTS,com.openai.atlas}/*`, `~/Library/Application Support/Claude/Cache/*` | IDE reindexes, Playwright re-downloads browsers |
| Claude desktop `~/Library/Application Support/Claude/vm_bundles` (~10 GB) | Cowork VM re-downloads. Quit Claude desktop first |
| Chrome `OptGuideOnDeviceModel` (~4 GB) | Re-downloads unless `chrome://flags/#optimization-guide-on-device-model` is disabled |
| `node_modules` / `.venv` in repos | Only where a lockfile exists (`uv.lock`, `package-lock.json`, `pnpm-lock.yaml`). Check `git log -1 --format=%cr` and don't call a repo "inactive" without it. Leave daily repos (skipy, hiddenbeer, House-Hunter) unless asked |
| Old JDKs in `~/Library/Java/JavaVirtualMachines` | Only if a newer patch of the same major exists. First `grep -rl <jdk-dir> ~/Library/Application\ Support/JetBrains ~/git/*/.idea` |

When the user says "delete all safe ones", that means the rows without data loss whose side effect is only a re-download/rebuild. Items the user declined earlier in the session stay declined.

### 4. Tier 3: list only, never delete

Downloads/Documents contents (old `.dmg`/`.pkg`/`.zip` installers, big files), DB backups in repos, big app logs (offer `: > file` to truncate), WhatsApp media (clear in-app), app data like Atlas/Spotify profiles, `~/.claude/projects`.

### 5. Report

Lead with free space before → after. Then show a table of what was removed with sizes, what happens next (reindex, re-pull, `uv sync`/`npm ci`), and what is left with its trade-off. Point out anything that failed (e.g. npm EACCES).

## Reference: 2026-10-27/28 run

149 MB → 39 GB free on a 228 GB disk. Biggest wins: `uv cache` 13.6 GB, Docker images + colima fstrim ~14 GB, app caches ~4 GB, repo build outputs 2.7 GB, repo deps 1.7 GB, old Claude versions 820 MB, Google Updater crx_cache 755 MB.
