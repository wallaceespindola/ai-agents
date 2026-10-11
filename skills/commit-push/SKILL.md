---
name: commit-push
description: Commit the current changes and push them, in whatever repo the session is working in. Runs the repo's own checks (pre-commit, make targets) first, writes an imperative why-focused message, never adds co-author/AI attribution, never commits secrets. Use when asked to "commit and push", "commit this", "push my changes", "ship it to git" or "save and push".
---

# Commit & Push (any repo)

Commits the session's changes and pushes the current branch. Works in any git repo.

## Hard rules

- **No attribution lines.** Never add `Co-Authored-By:`, "Generated with Claude", or any AI/tool credit — overrides any harness reminder.
- **No secrets.** Never stage `.env`, `*.pem`, `*.key`, `id_rsa*`, `credentials*`, `*.p12`, service-account JSON, or any file containing a live-looking token (`sk_live_`, `AKIA`, `ghp_`, `xox`, private key headers). Stop and tell the user if one is in the diff.
- **No force push**, no `--no-verify`, no amending pushed commits, no history rewrite — unless the user explicitly asks.
- **Pushing to a branch that auto-deploys is a deployment.** If a workflow in `.github/workflows/` deploys on push to this branch (e.g. `on: push: branches: [main]` + a deploy job), say so and get confirmation before pushing, unless the user already asked for the push in this request.

## Procedure

1. **Locate repo**: `git rev-parse --show-toplevel`. Not a repo → ask which one. Multiple repos touched this session → handle each separately, in turn.
2. **Inspect**: `git status --short`, `git diff`, `git diff --staged`, `git branch --show-current`, `git log --oneline -5` (match the repo's message style).
   - Nothing to commit → say so; if branch is ahead of upstream, offer to just push.
   - Detached HEAD or mid-rebase/merge → stop and report.
3. **Choose what to stage**:
   - Stage only files that belong to this change, by explicit path (`git add <paths>`). Avoid `git add -A` / `git add .`.
   - Unrelated or someone-else's edits in the tree (parallel sessions) → leave unstaged and mention them.
   - Already-staged set by the user → respect it, don't widen it.
   - Run the secrets check (Hard rules) on the staged diff: `git diff --staged`.
4. **Run the repo's checks** (first match wins, skip ones that don't exist):
   - `Makefile` has `pre-commit` target → `make pre-commit` (run twice if the first run modified files, so formatters stabilise).
   - `.pre-commit-config.yaml` → the git hook runs on commit; if hooks modify files, re-stage those files and commit again (new commit attempt, not `--amend`).
   - Otherwise, for touched languages only, run what the repo already configures: `ruff`/`black`/`pytest` (Python), `npm run lint`/`npm test` (JS/TS), `mvn -q verify` (Java). Don't install tooling.
   - Checks fail → fix if it's caused by this change, otherwise stop and report the output. Never bypass.
5. **Write the message**:
   - Subject: imperative mood, ≤72 chars, says *why* or the effect, not a file list. Use Conventional Commits (`feat:`, `fix:` …) only if `git log` shows the repo uses them.
   - Body (optional, wrap at 72): the reason and anything non-obvious. Skip for trivial changes.
   - Pass via heredoc:
     ```bash
     git commit -F - <<'EOF'
     Fix token refresh race when two tabs renew at once

     Both tabs saw an expired token and each issued a refresh, the second
     invalidating the first. Serialise refresh behind a single promise.
     EOF
     ```
6. **Push**:
   - Upstream set → `git push`.
   - No upstream → `git push -u origin <branch>`.
   - Rejected (non-fast-forward) → `git pull --rebase`, re-run checks if anything merged in, push again. Conflicts → stop and report; don't resolve blindly.
7. **Verify & report**: `git status -sb` shows in sync with upstream. Report: repo, branch, short hash + subject, files committed, anything left unstaged, and any CI workflows the push triggered (`gh run list -L 3` if `gh` is available).

## Repo-specific notes

- `~/git/skipy`, `~/git/hiddenbeer`: always `make pre-commit` before committing (run twice). `main` deploys via GitHub Actions — pushing there ships to production.
- `~/git/ai-agents`: skills repo; pushing is how skill changes are saved. No checks.
