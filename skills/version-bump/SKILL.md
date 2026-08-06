---
name: version-bump
description: Bump the release version in hiddenbeer and skipy (all frontend/backend config files), tag, commit and push. Use when asked to "increase version", "bump version", "release new version" or "tag a release" for these repos.
---

# Version Bump Skill (hiddenbeer + skipy)

Bumps the synchronized app version across all config files, creates the git tag, commits and pushes. Both repos always share the same version number and move together unless the user says otherwise.

## Procedure

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

## Notes

- Never add co-author lines to the commit.
- If versions have drifted between the two repos, ask the user which number to converge on before editing.
