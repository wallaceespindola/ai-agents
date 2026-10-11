---
name: version-bump
description: Bump the release version of the repo the session is working in — hiddenbeer + skipy together, wtech-website, House-Hunter, or any other repo (version files discovered) — then commit, tag and push following that repo's workflow. Use when asked to "increase version", "bump version", "release new version" or "tag a release".
---

# Version Bump Skill (session's current project)

Bumps the app version across all config files, creates the git tag, commits and pushes.

## Which repos?

Bump the project the session is working in: the git root of the primary working
directory (`git rev-parse --show-toplevel`), unless the user names repos explicitly.
Never bump a repo other than the session's one just because a table row says "default".

| Session repo | Bump |
|---|---|
| `~/git/hiddenbeer` or `~/git/skipy` | **hiddenbeer + skipy** together (they share a version) |
| `~/git/wtech-website` | **wtech-website only** |
| `~/git/House-Hunter` | **House-Hunter only** (PR workflow, see below) |
| any other repo | **that repo only** — follow "Any other repo" |
| not inside a git repo | ask which repo |

"Bump all" / "every repo" = hiddenbeer + skipy + wtech-website, each following its own section.

## hiddenbeer + skipy

hiddenbeer and skipy share the same version number and move together unless the user says otherwise.

### Procedure

1. **Pull first**: `git pull --ff-only` in each repo.
2. **Find current version**: read it from `hiddenbeer_backend/pyproject.toml` (both repos are kept in sync). Default bump is **patch** (1.0.19 → 1.0.20) unless the user asks for minor/major.
3. **Edit exactly these files** (replace OLD with NEW version):

   **hiddenbeer** (`~/git/hiddenbeer`):
   - `hiddenbeer_backend/pyproject.toml` — `version = "X"`
   - `hiddenbeer_frontend/package.json` — `"version": "X"`

   **skipy** (`~/git/skipy`):
   - `package.json` (root) — `"version": "X"`
   - `apps/skipy-client/package.json`
   - `apps/skipy-admin/package.json`
   - `apps/skipy-manager/package.json`
   - `apps/skipy-api/pyproject.toml` — `version = "X"`
   - `apps/skipy-api/uv.lock` — the `version = "X"` line directly under `name = "skipy-api"` (only that one line; do not run `uv lock`)

   Do **NOT** touch `packages/i18n-config/package.json` (skipy) — it is versioned independently.
   Backends read the version dynamically from pyproject via `get_app_version()` — no Python source edits needed.

4. **Verify**: `git diff --stat` must show exactly 2 files (hiddenbeer) and 6 files (skipy).
5. **Pre-commit**: run `make pre-commit` in each repo before committing (twice in skipy if anything reformats).
6. **Commit** (message style is fixed): `chore: bump version to X`
7. **Tag**: `git tag vX` (e.g. `v1.0.20`).
8. **Push**: `git push && git push origin vX`.
9. **Verify CI**: `gh run list --branch main --limit 3` in each repo — pushes trigger pre-commit, security-scan and build-and-push-images (skipy) / frontend+backend CI (hiddenbeer). Images go to the registry only; nothing deploys to servers.

## wtech-website

`~/git/wtech-website` (Next.js site for wtechitsolutions.com) has its **own** version, independent of hiddenbeer/skipy. The footer shows it (`components/Footer.tsx` reads `version` from `package.json`).

1. **Pull first**: `git pull --ff-only`.
2. **Find current version**: `node -p "require('./package.json').version"`. Default bump is **patch** unless the user asks for minor/major.
3. **Edit**: `npm version X --no-git-tag-version`. This updates exactly `package.json` and `package-lock.json` (top-level `version` and `packages[""].version`). Do not edit anything else.
4. **Verify**: `git diff --stat` must show exactly 2 files.
5. **Checks** (no `make pre-commit` here): `npm run lint && npm run typecheck && npm test`.
6. **Commit**: `chore: bump version to X`.
7. **Tag**: `git tag vX`.
8. **Push**: `git push && git push origin vX`.
9. **Verify CI**: `gh run list --branch main --limit 3` (CI: lint, typecheck, test, build, Docker build).
10. **Deploy is separate**: the new version only appears on https://wtechitsolutions.com after `./deploy.sh`. Never deploy without the user's explicit request; offer it in one line.

## Notes

- Never add co-author lines to the commit.
- If versions have drifted between the two repos, ask the user which number to converge on before editing.

## House-Hunter

`~/git/House-Hunter` (FastAPI + Next.js). Footer shows the version (`next.config.mjs`
inlines `package.json` version as `NEXT_PUBLIC_APP_VERSION`). **`main` takes PRs only**
(`docs/MERGE_DISCIPLINE.md`) — never commit or push to `main` directly.

1. **Branch**: if on `main`, `git pull --ff-only` then `git switch -c chore/bump-X`;
   otherwise commit on the current feature branch if the user prefers that.
2. **Find current version**: `backend/pyproject.toml` `version = "X"`. Default **patch**.
3. **Edit exactly these** (4 files):
   - `backend/pyproject.toml` — `version = "X"`
   - `backend/uv.lock` — the `version` line directly under `name = "househunter-backend"` (do not run `uv lock`)
   - `frontend-next/package.json` + `package-lock.json` — `cd frontend-next && npm version X --no-git-tag-version`
4. **Verify**: `git diff --stat` = 4 files; `cd backend && uv lock --check`.
5. **Commit**: `chore: bump version to X`.
6. **Push the branch / open the PR only when the user asks.** Tag `vX` **after** the PR merges,
   on the merge commit in `main` (`git pull && git tag vX && git push origin vX`).
7. Deploy is separate (`deploy.py`) — never without an explicit request.

## Any other repo

1. **Pull first**: `git pull --ff-only` (skip if there's no upstream).
2. **Discover version files** — every hit is a candidate, ignoring `node_modules/`, `.venv/`, vendored dirs:
   `git ls-files | grep -E '(^|/)(package\.json|pyproject\.toml|pom\.xml|build\.gradle(\.kts)?|Cargo\.toml|Chart\.yaml|version\.txt|VERSION)$'`
   Lockfiles follow their manifest: `npm version X --no-git-tag-version` for package.json; the
   project's own entry in `uv.lock` / `Cargo.lock`; `mvn versions:set -DnewVersion=X -DgenerateBackupPoms=false` for Maven.
   Also check `git tag --sort=-v:refname | head -3` for the last released tag.
3. **If versions disagree** across files or with the latest tag, or a manifest is clearly
   independently versioned (shared packages, sub-libs), **ask** which to bump and to which number.
4. **Workflow**: read the repo's `CLAUDE.md` / `CONTRIBUTING.md`. If `main` is PR-only, use a branch and
   tag after merge (as House-Hunter); otherwise commit to `main`, tag, push.
5. **Checks**: run the repo's pre-commit / lint / test target if one exists (`make pre-commit`, `npm test`, …).
6. **Commit**: `chore: bump version to X`; tag `vX` (match existing tag style, e.g. no `v` if the repo uses none).
7. **Once done, add a section for this repo** to this skill so the next bump is explicit.

