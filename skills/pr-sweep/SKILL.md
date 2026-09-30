---
name: pr-sweep
description: Sweep every repo Wallace owns under ~/git for open GitHub PRs, merge the safe ones, close the unsafe ones, then sync local clones. Use when asked to "check open PRs in all my repos", "merge the safe PRs", "clean up dependabot PRs" or "sweep PRs across projects" (including hiddenbeer and skipy).
---

# PR Sweep (all owned repos in ~/git)

Finds open PRs across every owned repo, classifies each as SAFE / UNSAFE / REVIEW, merges SAFE, closes UNSAFE with a comment, reports REVIEW, then fast-forwards local clones.

## 1. Inventory

```bash
cd ~/git
for d in */; do d=${d%/}; [ -d "$d/.git" ] || continue
  url=$(git -C "$d" remote get-url origin 2>/dev/null) || continue
  repo=$(echo "$url" | sed -E 's#.*github.com[:/]##; s#\.git$##')
  echo "== $d ($repo)"
  gh pr list -R "$repo" --state open \
    --json number,title,author,headRefName,isDraft,mergeable,statusCheckRollup \
    --jq '.[] | "#\(.number) [\(.author.login)] \(.title) | draft=\(.isDraft) mergeable=\(.mergeable) checks=\([.statusCheckRollup[]? | (.conclusion // .state)] | group_by(.) | map("\(.[0])x\(length)") | join(","))"'
done
```

**Skip non-owned repos**: `awesome-claude-skills` (fork of BehiSecc), `skills` (anthropics clone), and any repo whose owner is not `wallaceespindola`, `W-Tech-IT-Solutions` or `Vinci-Trends`. Never merge or close PRs on upstream projects.

## 2. Classify

**SAFE** (all must hold):
- `mergeable=MERGEABLE`, not draft
- every check `SUCCESS`/`SKIPPED`/`NEUTRAL` and at least one check ran
- dependabot/renovate: patch or minor bump, or a GitHub Action version bump
- human PR from owner/collaborator: diff read (`gh pr view N --json files,body`, `gh pr diff N`), and it has tests, touches no `.github/workflows`, no secrets/`.env`, no infra/deploy config

**UNSAFE**, close with an explanatory comment:
- failing CI with no fix in sight, or the PR is superseded by a newer one (e.g. an older dependabot PR for the same dep)
- unknown external author, or the PR adds secrets, credentials or suspicious scripts
- stale and conflicting, where the branch no longer makes sense

**REVIEW**: ask the user, don't act:
- major version bumps (framework majors like Spring Boot, Next.js, React, FastAPI, Python/Java runtime)
- human PR changing auth, payments, DB migrations, workflows or deploy config
- `CONFLICTING` or checks still `PENDING`/`IN_PROGRESS`

When unsure, choose REVIEW. Closing a PR is reversible, but a bad merge can ship.

## 3. Deploy guard

Before merging, check whether a push to the base branch deploys anything:

```bash
grep -lE "deploy|ssh |scp |rsync|kubectl|helm upgrade" <repo>/.github/workflows/*.y*ml
```

If a workflow deploys to a server on push to main, **stop and confirm with the user** (global rule: never deploy without explicit permission). Building/pushing images to a registry is fine; hiddenbeer and skipy only push images, and servers are updated manually.

## 4. Act

```bash
gh pr merge N -R owner/repo --squash --delete-branch
gh pr close N -R owner/repo --delete-branch --comment "Closing: <reason>."
```

- Merge PRs in the same repo one at a time. If the next one turns `CONFLICTING` (typical for two dependabot bumps in one `pom.xml`/`package.json`), comment `@dependabot rebase` and report it as pending instead of forcing.
- Verify: `gh pr view N -R owner/repo --json state --jq .state` should be `MERGED`/`CLOSED`.

## 5. Sync local clones

For each touched repo: `git fetch --prune`; if on `main`/`master` and clean, `git pull --ff-only`. If the tree is dirty or on a feature branch, don't touch it and report it.
In hiddenbeer/skipy, run `make pre-commit` before any local commit or push.
Commits never carry co-author lines.

## 6. Report

Table: repo | PR | action (merged / closed / needs review / rebase requested) | reason. Then list the skipped non-owned repos.
