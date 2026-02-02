# Git Workflow Strategy Skill

**Master Git Flow, GitHub Flow, trunk-based development, branch protection, merge strategies, and release management for team collaboration.**

## Overview

Git workflow strategy defines how your team collaborates on code. This skill covers industry-standard branching patterns, protection rules, merge strategies, and release management.

**What it does:**
- Implements Git Flow for large-scale projects
- Enables GitHub Flow for rapid releases
- Optimizes trunk-based development for CI/CD
- Configures branch protection rules
- Chooses optimal merge strategies (merge, squash, rebase)
- Manages versioning and release branches
- Handles hotfixes and emergency patches
- Enforces code review workflows

**Perfect for:**
- Team collaboration workflows
- Multiple environment deployments
- Semantic versioning and releases
- Preventing accidental main branch changes
- Maintaining stable release branches

---

## When to Use This Skill

Use Git Workflow Strategy when you need to:

- **Choose a branching model** for your project (Git Flow vs GitHub Flow vs Trunk)
- **Protect main branch** from direct commits
- **Require code reviews** on pull requests
- **Enforce commit conventions** (conventional commits)
- **Manage multiple environments** (dev, staging, production)
- **Release software** with version tags
- **Handle hotfixes** to production
- **Prevent conflicts** from long-lived branches
- **Establish team standards** for merging

---

## Quick Start (10 Minutes)

### 1. Initialize Git Flow (Local)

```bash
# Install git-flow extension
brew install git-flow

# Initialize project
cd your-repo
git flow init

# Accept default branch names:
# main -> main, develop -> develop, hotfix -> hotfix/
```

### 2. Configure Branch Protection (GitHub)

Go to Settings → Branches → Branch protection rules → Add rule

```yaml
Pattern: main
Require pull request reviews: Yes (1 reviewer)
Require status checks: Yes (build, test, lint)
Require branches up to date: Yes
Allow force pushes: No
Allow deletions: No
```

### 3. Start Feature Branch (Git Flow)

```bash
# Create feature branch
git flow feature start user-authentication

# This creates: feature/user-authentication

# When done, finish feature
git flow feature finish user-authentication

# Merges back to develop, deletes feature branch
```

### 4. Create Release Branch

```bash
git flow release start 1.0.0
# Edits version numbers, changelog
git flow release finish 1.0.0
# Tags version on main, merges back to develop
```

---

## How It Works

### 1. Git Flow (Complex Projects)

Best for large teams, multiple versions in production:

**Branch structure:**
```
main (production)
  ├─ v1.0.0 (tagged)
  ├─ v1.0.1 (tagged)
  └─ v1.1.0 (tagged)

develop (staging)
  ├─ feature/auth
  ├─ feature/payments
  └─ bugfix/error-handling

hotfix/
  └─ hotfix/security-patch (fixes main, merges to main + develop)
```

**Workflow:**

```bash
# Start new feature
git flow feature start feature-name
# Work: git commit, push
git push origin feature/feature-name

# Create pull request: feature/feature-name -> develop
# Code review, merge with --no-ff (keeps branch history)

# When ready to release
git flow release start 1.0.0
# Update version numbers, CHANGELOG.md
git commit -am "Bump version to 1.0.0"
git flow release finish 1.0.0
# Creates tag v1.0.0 on main
# Merges back to develop

# Hotfix for production
git flow hotfix start 1.0.1
# Fix bug
git commit -am "Fix critical bug"
git flow hotfix finish 1.0.1
# Tags v1.0.1 on main
# Merges back to develop
```

**Advantages:**
- Clear separation: features, releases, hotfixes
- Multiple versions in production
- Stable main branch
- Detailed history with merge commits

**Disadvantages:**
- Complex workflow
- More merge conflicts
- Slower release cycle
- Not ideal for continuous deployment

### 2. GitHub Flow (Fast-Moving Teams)

Best for continuous deployment, simple workflow:

**Branch structure:**
```
main (production)
  ├─ feature-1 (PR #101)
  ├─ feature-2 (PR #102)
  └─ bugfix-1 (PR #103)
```

**Workflow:**

```bash
# Create feature branch from main
git checkout -b feature/user-dashboard

# Work and commit
git commit -am "Add user dashboard"
git push origin feature/user-dashboard

# Create pull request: feature/user-dashboard -> main
# Code review and discussions in PR
# Run automated checks (tests, lint, build)

# Merge with squash (one commit per feature)
# GitHub: "Squash and merge"
# Or: git merge --squash feature/user-dashboard

# Deploy main immediately
# Production = main branch
```

**Advantages:**
- Simple, intuitive workflow
- Fast feedback loop
- Continuous deployment friendly
- Fewer merge conflicts

**Disadvantages:**
- Requires very good test coverage
- No staging environment
- All code must be production-ready
- Harder to manage multiple versions

### 3. Trunk-Based Development (High-Performing Teams)

Best for CI/CD, small teams, feature flags:

**Branch structure:**
```
main (production)
  ├─ short-lived branch (24 hours max)
  ├─ short-lived branch
  └─ short-lived branch
```

**Workflow:**

```bash
# Create short-lived branch
git checkout -b feat/fast-feature
# Work: 1-2 hours max
git commit -am "Add feature behind flag"

# Create pull request
# Code review: fast turnaround
# Merge quickly

# Use feature flags for incomplete features
if (featureFlags.isEnabled('new-dashboard')) {
  showNewDashboard();
}

# Deploy continuously to production
# Revert quickly if issues arise
```

**Advantages:**
- Fastest feedback
- Minimal merge conflicts
- Continuous delivery ready
- Better code integration

**Disadvantages:**
- Requires strong CI/CD
- Feature flags essential
- No traditional staging
- Team discipline needed

### 4. Branch Protection Rules

**Basic Protection:**

```yaml
Require pull request reviews: 1-2 reviewers
Require status checks:
  - ci/build
  - ci/test
  - ci/lint
Require branches up-to-date: Yes
Require signed commits: (optional)
```

**GitHub Configuration (via API):**

```bash
# Apply branch protection
gh api repos/:owner/:repo/branches/main/protection \
  -f required_pull_request_reviews.required_approving_review_count=2 \
  -f required_pull_request_reviews.require_code_owner_reviews=true \
  -f required_status_checks.strict=true \
  -f required_status_checks.contexts='["ci/build","ci/test"]' \
  -f enforce_admins=true \
  -f allow_force_pushes=false \
  -f allow_deletions=false
```

### 5. Merge Strategies

**Merge Commit (--no-ff)**
```bash
git merge --no-ff feature/auth

# Preserves branch history
# Shows what was merged together
# Larger history, harder to read
```

**Squash and Merge (--squash)**
```bash
git merge --squash feature/auth
git commit -m "Add authentication"

# Linear history, clean
# Loses branch history
# Good for: GitHub Flow
```

**Rebase and Merge (--ff-only)**
```bash
git rebase main feature/auth
git merge --ff-only feature/auth

# Clean linear history
# No merge commits
# Rewrites commit history
# Good for: Trunk-based, small teams
```

**Interactive Rebase for Cleanup**
```bash
# Get last 5 commits
git rebase -i HEAD~5

# Options in editor:
# pick   - use commit
# reword - change message
# squash - combine with previous
# fixup  - combine, discard message
# drop   - remove commit
```

### 6. Release Management

**Semantic Versioning (semver)**
```
MAJOR.MINOR.PATCH
v1.0.0

- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes
```

**Release Branch Workflow:**

```bash
# Create release branch
git checkout -b release/1.0.0

# Update version numbers
npm version minor  # Updates package.json, creates tag

# Or manually
# Edit:
#   package.json: version = 1.0.0
#   CHANGELOG.md: Add release notes
git commit -am "Release 1.0.0"

# Create annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Merge to main and develop
git checkout main
git merge --no-ff release/1.0.0
git tag v1.0.0

git checkout develop
git merge --no-ff release/1.0.0

# Delete release branch
git branch -d release/1.0.0
git push origin --delete release/1.0.0
```

### 7. Hotfix Workflow

**Production Emergency Fix:**

```bash
# Create hotfix branch from main
git checkout -b hotfix/security-patch main

# Fix the issue
git commit -am "Fix security vulnerability"

# Patch version number
npm version patch

# Merge to main with tag
git checkout main
git merge --no-ff hotfix/security-patch
git tag -a v1.0.1 -m "Hotfix 1.0.1"

# Merge back to develop
git checkout develop
git merge --no-ff hotfix/security-patch

# Clean up
git branch -d hotfix/security-patch
```

### 8. Code Review Integration

**Pull Request Workflow:**

```bash
# 1. Developer creates PR
git push origin feature/auth

# 2. Reviewer checks changes
gh pr view 101

# 3. Conversations and suggestions
gh pr comment 101 -b "Please add error handling"

# 4. Developer pushes changes
git commit -am "Add error handling as suggested"
git push origin feature/auth

# 5. Reviewer approves
gh pr review 101 --approve

# 6. Automated checks pass
# GitHub displays: "All checks have passed"

# 7. Merge pull request
gh pr merge 101 --squash

# 8. Delete branch
git branch -d feature/auth
git push origin --delete feature/auth
```

---

## Configuration

### .github/CODEOWNERS

```
# Define code owners for automatic assignment
* @wallace

src/auth/** @alice @bob
src/payments/** @carol

docs/** @david
.github/workflows/** @eve
```

### .gitconfig (Team Standards)

```bash
# Configure merge strategy globally
git config --global pull.ff only  # Fast-forward only

# Rebase by default
git config --global pull.rebase true

# Sign commits
git config --global commit.gpgSign true
git config --global user.signingKey <KEY_ID>
```

### Branch Protection Rules (via code)

`scripts/setup-branch-protection.sh`:

```bash
#!/bin/bash

REPO=$1
BRANCH=${2:-main}

# Main branch protection
gh api repos/$REPO/branches/$BRANCH/protection \
  -f required_pull_request_reviews.required_approving_review_count=2 \
  -f required_pull_request_reviews.require_code_owner_reviews=true \
  -f required_status_checks.strict=true \
  -f required_status_checks.contexts='["ci/build","ci/test","ci/lint"]' \
  -f enforce_admins=true \
  -f allow_force_pushes=false \
  -f allow_deletions=false \
  -f restrictions='{"users":[],"teams":[],"apps":[]}'
```

### Commit Message Convention

`.commitlintrc.json`:

```json
{
  "extends": ["@commitlint/config-conventional"],
  "rules": {
    "type-enum": [
      2,
      "always",
      [
        "feat",
        "fix",
        "docs",
        "style",
        "refactor",
        "perf",
        "test",
        "chore"
      ]
    ],
    "subject-case": [2, "never", ["start-case", "pascal-case"]],
    "subject-empty": [2, "never"],
    "subject-full-stop": [2, "never", "."]
  }
}
```

---

## Examples

### Example 1: Complete Git Flow Release

```bash
#!/bin/bash

# Start release
git flow release start 1.5.0

# Update version everywhere
npm version minor --no-git-tag-version
echo "## [1.5.0] - 2026-02-02" >> CHANGELOG.md
echo "### Added" >> CHANGELOG.md
echo "- New feature X" >> CHANGELOG.md

git add package.json CHANGELOG.md
git commit -m "Bump version to 1.5.0"

# Finish release (creates tag, merges back)
git flow release finish 1.5.0

# Push everything
git push origin main develop --tags

# Create GitHub Release
gh release create v1.5.0 \
  --title "Version 1.5.0" \
  --notes-file CHANGELOG.md
```

### Example 2: GitHub Flow with Auto-Merge

```bash
# Create feature branch
git checkout -b feature/new-dashboard

# Work and commit
echo "function dashboard() { ... }" >> src/dashboard.js
git commit -am "feat: add user dashboard component"

# Push and create PR
git push origin feature/new-dashboard
gh pr create \
  --title "feat: add user dashboard" \
  --body "Implements new user dashboard with charts and statistics"

# Enable auto-merge (when checks pass)
gh pr merge 102 --auto --squash

# Once checks pass, PR merges automatically
# Feature branch deletes automatically
```

### Example 3: Protected Branch Workflow

```bash
# Team member tries to commit directly to main
git checkout main
git commit -am "Quick fix"
git push origin main
# ERROR: Protected branch - requires pull request!

# Correct approach
git checkout -b bugfix/login-bug
git commit -am "Fix login timeout issue"
git push origin bugfix/login-bug

# Create PR
gh pr create --title "Fix login timeout"

# Requires:
# ✓ 2 approvals
# ✓ CI checks pass
# ✓ Up to date with main
# ✓ No merge conflicts

# Once requirements met
gh pr merge 105 --squash
```

### Example 4: Trunk-Based with Feature Flags

```bash
# Create short-lived branch (max 24 hours)
git checkout -b feat/experimental-search

# Hide incomplete feature with flag
// src/features.js
export const FEATURES = {
  experimentalSearch: process.env.FEATURE_EXPERIMENTAL_SEARCH === 'true',
};

// src/search.js
import { FEATURES } from './features.js';

function SearchComponent() {
  if (FEATURES.experimentalSearch) {
    return <NewSearchUI />;
  }
  return <LegacySearchUI />;
}

# Commit and create PR
git commit -am "feat: add experimental search behind feature flag"
git push origin feat/experimental-search
gh pr create --title "feat: experimental search"

# Code review (fast)
# Merge to main immediately
gh pr merge 108 --squash

# Deploy to production
# Feature flag disabled: LegacySearchUI shows
# Team tests new code in production (traffic 0%)

# Enable for 10% of users
FEATURE_EXPERIMENTAL_SEARCH=true (roll out gradually)

# Once stable, remove feature flag
# Keep new code, delete flag
```

### Example 5: Hotfix Emergency Process

```bash
# Production bug detected
# Branch from main (current production)
git checkout -b hotfix/payment-processing main

# Fix critical issue
# src/payments.js - add validation
git commit -am "fix: prevent duplicate payment processing"

# Increment patch version
npm version patch --no-git-tag-version

# Fast merge to main
git checkout main
git merge --no-ff hotfix/payment-processing -m "Merge hotfix/payment-processing"
git tag -a v1.0.2 -m "Hotfix: payment processing"

# Deploy immediately
npm run deploy

# Merge back to develop
git checkout develop
git merge --no-ff hotfix/payment-processing

# Clean up
git branch -d hotfix/payment-processing

# Push
git push origin main develop --tags
```

### Example 6: Multi-Environment Workflow

```bash
# Standard workflow
develop  -> staging environment
main     -> production environment

# Deploy process
git push origin feature/dashboard
# PR review -> merge to develop
# Staging deploys automatically
# QA tests on staging
# Create release PR: develop -> main
# Final approval -> merge to main
# Production deploys automatically
```

---

## Best Practices

### 1. Keep Branches Short-Lived

```bash
# Good: 1-3 day feature branches
git checkout -b feat/password-reset
# Work 8 hours, create PR same day

# Bad: Month-long branches
# Many conflicts, hard to merge, risky
```

### 2. Require Code Review

```yaml
# Branch Protection: Require Reviews
required_approving_review_count: 2
require_code_owner_reviews: true
dismiss_stale_pull_request_approvals: true
```

### 3. Use Conventional Commits

```bash
# Good messages
git commit -m "feat: add user authentication system"
git commit -m "fix: handle null pointer in parser"
git commit -m "docs: update installation guide"
git commit -m "refactor: simplify payment logic"

# Bad messages
git commit -m "fix stuff"
git commit -m "update"
git commit -m "asdf"
```

### 4. Automate Version Bumping

```bash
# Use semantic-release
npm run semantic-release
# Analyzes commits, bumps version, creates tag, publishes

# Or manual with npm version
npm version minor  # Bumps version, creates tag
git push origin main --tags
```

### 5. Protect Against Force Push

```yaml
# Branch Protection: No Force Push
allow_force_pushes: false

# Also for admins
enforce_admins: true  # Admins must follow rules too
```

### 6. Require Status Checks

```yaml
required_status_checks:
  strict: true  # Must be up-to-date with main
  contexts:
    - ci/build
    - ci/test
    - ci/lint
    - sonarcloud/quality-gate
    - codecov/coverage
```

### 7. Use CODEOWNERS

```
# .github/CODEOWNERS
* @default-owner
src/auth/** @auth-team
src/payments/** @payments-team
docs/** @tech-writers
```

---

## Integration with Other Skills

Git Workflow Strategy integrates with:

- **github-actions-workflows** - Run checks on PRs
- **github-pr-management** - Review and merge flows
- **git-commit-strategy** - Enforce message conventions
- **build-optimization** - Check build status
- **github-security-scanning** - Security gates on main
- **secrets-management** - Manage deployment secrets

---

## Complete Command Reference

```bash
# Git Flow Commands
git flow init
git flow feature start <name>
git flow feature finish <name>
git flow release start <version>
git flow release finish <version>
git flow hotfix start <version>
git flow hotfix finish <version>

# Branch Management
git branch -d <branch>           # Delete local branch
git push origin --delete <branch> # Delete remote branch
git branch -m <old> <new>        # Rename branch

# Merging
git merge --no-ff <branch>       # Merge with commit
git merge --squash <branch>      # Squash commits
git rebase main feature/auth     # Rebase on main

# Tagging
git tag v1.0.0                   # Create lightweight tag
git tag -a v1.0.0 -m "Release"   # Create annotated tag
git push origin --tags           # Push all tags

# Pull Request (GitHub CLI)
gh pr create --title "Title" --body "Description"
gh pr merge <number> --squash
gh pr view <number>
gh pr close <number>
gh pr review <number> --approve

# Workflow Info
git log --oneline --graph --all
git show <commit>
git diff <branch1> <branch2>
```

---

## Troubleshooting

### Problem: Merge conflicts

**Solution:**
```bash
# View conflicts
git status

# Edit files to resolve conflicts
vim src/file.js

# Mark resolved
git add src/file.js
git commit -m "Resolve merge conflicts"
```

### Problem: Accidental commit to main

**Solution:**
```bash
# Before push: undo commit
git reset --soft HEAD~1
# Changes now staged, branch unchanged

# Or: move commit to new branch
git branch feature/moved-feature
git reset --hard origin/main
git checkout feature/moved-feature
```

### Problem: Need to cherry-pick from another branch

**Solution:**
```bash
# Find the commit hash
git log feature/auth

# Cherry-pick to current branch
git cherry-pick <commit-hash>
```

---

## File Organization

```
.github/
├── CODEOWNERS
├── ISSUE_TEMPLATE/
├── PULL_REQUEST_TEMPLATE.md
└── workflows/
    └── ci.yml

scripts/
└── setup-branch-protection.sh

CONTRIBUTING.md
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
