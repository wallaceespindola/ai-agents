---
name: version-bump
description: Bump the release version of the repo the session is working in (only that repo), updating every version file and its lockfile entry, then commit, tag and push following that repo's workflow. Use when asked to "increase version", "bump version", "release new version" or "tag a release".
---

# Version Bump (current project only)

Bumps the version of **the repo the session is working in** — the git root of the primary working
directory (`git rev-parse --show-toplevel`). Never bump any other repo unless the user names it
explicitly; no repo is paired with another. Not inside a git repo → ask which repo.

## Procedure

1. **Pull first**: `git pull --ff-only` (skip if there's no upstream). If another session's uncommitted
   edits block the pull or sit in a version file, bump in a temporary `git worktree` on `origin/main`, or
   stage only the version line (`git show HEAD:f | sed … | git hash-object -w --stdin` + `git update-index --cacheinfo`).
2. **Find version files**: check "Known repos" below; otherwise discover them, ignoring `node_modules/`,
   `.venv/` and vendored dirs:
   `git ls-files | grep -E '(^|/)(package\.json|pyproject\.toml|pom\.xml|build\.gradle(\.kts)?|Cargo\.toml|Chart\.yaml|version\.txt|VERSION)$'`
   Also `git tag --sort=-v:refname | head -3` for the last released tag.
3. **New version**: default **patch** (1.0.19 → 1.0.20) unless the user asks minor/major. If the files
   disagree with each other or with the latest tag, or a manifest is independently versioned (shared
   package, sub-lib), **ask** which to bump and to which number.
4. **Edit** the version line in each file. Lockfiles: only the project's own entry —
   `npm version X --no-git-tag-version` for package.json + package-lock; the line under the project's
   `name` in `uv.lock` / `Cargo.lock` (do not run `uv lock`); `mvn versions:set -DnewVersion=X -DgenerateBackupPoms=false` for Maven.
   Never re-serialise a lockfile by hand.
5. **Verify**: `git diff --stat` shows exactly the expected files, each diff only the version line(s).
   Python + uv: `uv lock --check`; if it fails, sync in a separate `chore(deps)` commit, never in the bump.
6. **Checks**: the repo's own target (`make pre-commit` — twice if it reformats —, `npm run lint && npm test`, …).
7. **Workflow**: read the repo's `CLAUDE.md` / `CONTRIBUTING.md`. If `main` is PR-only, branch
   `chore/bump-X`, open the PR, wait for CI, merge, then tag the merge commit. Otherwise commit to `main`.
8. **Commit**: `chore: bump version to X` — never co-author/AI lines.
9. **Tag**: `vX` (match the repo's existing tag style). A bump without its tag is not done.
10. **Push**: `git push && git push origin vX`, then `gh run list --branch main --limit 3`.
11. **Deploy is separate**: never deploy without an explicit request; offer it in one line if the
    version shows on a live site.
12. **New repo?** Once done, add it to "Known repos" so the next bump is explicit.

## Known repos (file lists)

- **skipy** (`~/git/skipy`), 7 files: `package.json` (root), `apps/skipy-{client,admin,manager}/package.json`,
  `apps/skipy-manager/package-lock.json` (only the first two `"version"` lines — the image runs `npm ci` from it),
  `apps/skipy-api/pyproject.toml`, `apps/skipy-api/uv.lock` (line under `name = "skipy-api"`).
  Never touch `packages/i18n-config/package.json` (independent). Pushes build images only, no deploy.
- **hiddenbeer** (`~/git/hiddenbeer`), 3 files: `hiddenbeer_backend/pyproject.toml`,
  `hiddenbeer_frontend/package.json`, `hiddenbeer_backend/uv.lock` (line under `name = "hiddenbeer-api"`).
- **wtech-website** (`~/git/wtech-website`), 2 files via `npm version X --no-git-tag-version`.
  Checks: `npm run lint && npm run typecheck && npm test` (no make). Live footer updates only after `./deploy.sh`.
- **House-Hunter** (`~/git/House-Hunter`), 4 files: `backend/pyproject.toml`, `backend/uv.lock`
  (line under `name = "househunter-backend"`), `frontend-next/package.json` + `package-lock.json`
  (`npm version`). **`main` is PR-only** (`docs/MERGE_DISCIPLINE.md`): branch → PR → `gh pr checks --watch`
  → merge → tag on main. Deploy via `deploy.py` only on request.
