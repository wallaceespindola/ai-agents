# GitHub PR Management Skill

**Master pull request workflows, templates, code reviews, auto-merge, labels, and GitHub Projects integration for streamlined collaboration.**

## Overview

GitHub pull requests are the core of team collaboration. This skill covers advanced PR management, code review workflows, automation, and project integration.

**What it does:**
- Designs PR templates for consistency
- Implements code review workflows
- Configures auto-merge for efficiency
- Manages labels and milestones
- Integrates with GitHub Projects boards
- Automates PR closing and cleanup
- Implements CODEOWNERS for domain experts
- Tracks PR metrics and statistics

**Perfect for:**
- Structured code review process
- Team collaboration at scale
- Automated PR triage and routing
- Release coordination
- Tracking feature progress

---

## When to Use This Skill

Use GitHub PR Management when you need to:

- **Standardize PR format** across team
- **Route PRs to right reviewers** automatically
- **Auto-merge PRs** when checks pass
- **Organize PRs with labels** for filtering
- **Track feature progress** in Projects board
- **Generate changelog** from PR titles
- **Request specific reviewers** from code owners
- **Block PR merge** based on certain files

---

## Quick Start (10 Minutes)

### 1. Create PR Template

Create `.github/pull_request_template.md`:

```markdown
## Description
Brief description of changes

## Type of change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Manual testing completed
- [ ] Unit tests added
- [ ] Integration tests passed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated

## Related Issues
Closes #123
```

### 2. Create CODEOWNERS

Create `.github/CODEOWNERS`:

```
* @default-owner
src/auth/** @auth-team
src/payments/** @payments-team
docs/** @tech-writers
```

### 3. Set Auto-Merge in Workflow

Add to `.github/workflows/ci.yml`:

```yaml
- name: Enable auto-merge
  if: success()
  run: gh pr merge ${{ github.event.pull_request.number }} --auto --squash
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 4. Add PR Labels

Create `.github/labeler.yml`:

```yaml
feature:
  - changed-files:
    - any-glob-to-any-file: 'src/features/**'

bug:
  - head-branch: ['bugfix/', 'hotfix/']

documentation:
  - changed-files:
    - any-glob-to-any-file: 'docs/**'
```

---

## How It Works

### 1. PR Templates

**Standard Template Structure:**

```markdown
## What

[Brief description of what changed]

## Why

[Motivation and context]

## How

[Implementation approach]

## Links

- Closes #123
- Related to #456

## Type

- [ ] Bug fix
- [ ] Feature
- [ ] Breaking change
- [ ] Docs

## Testing

- [ ] Unit tests
- [ ] Manual testing
- [ ] No tests needed

## Checklist

- [ ] Code review self-check
- [ ] Tests pass
- [ ] Documentation updated
```

**Multiple Templates:**

Create specific templates for different PR types:

```
.github/pull_request_template/
├── bug_report.md
├── feature_request.md
└── documentation.md
```

Link in GitHub UI: Settings → Pull Requests → PR template

### 2. Code Review Process

**Request Reviewers:**

```bash
# Automatic via CODEOWNERS
# Or manual
gh pr view 101 --json reviewDecisionState

# Request specific reviewer
gh pr review 101 --request-review @alice

# Multi-reviewer required
# Settings: Require 2 approvals before merge
```

**Review States:**

```yaml
APPROVED:        Reviewer approves changes
CHANGES_REQUESTED: Reviewer requests modifications
COMMENTED:       Reviewer left feedback
DISMISSED:       Review dismissed/no longer needed
PENDING:         Awaiting reviewer action
```

**Conversation Workflow:**

```bash
# Reviewer suggests change
gh pr comment 101 -b "Consider adding error handling here"

# Developer responds
gh pr comment 101 -b "Good point, added in latest commit"

# Reviewer checks update
gh pr view 101

# Reviewer approves
gh pr review 101 --approve
```

### 3. Auto-Merge Configuration

**Branch Protection Settings:**

```yaml
Allow auto merge: enabled
Dismiss stale approvals: yes
Require branches up to date: yes
```

**In Workflow:**

```yaml
- name: Auto-merge
  if: |
    success() &&
    github.event.pull_request.draft == false
  run: |
    gh pr merge ${{ github.event.pull_request.number }} \
      --auto \
      --squash \
      --delete-branch
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**Requirements for Auto-Merge:**

```
✓ All checks pass
✓ Required approvals
✓ Up-to-date with base branch
✓ No conflicts
✓ Not a draft
✓ Author has merge rights
```

### 4. Label Management

**Standard Labels:**

```yaml
priority:
  - critical: "#FF0000" # Block release
  - high: "#FF8800"
  - medium: "#FFFF00"
  - low: "#00FF00"

type:
  - bug: "#D73A49"
  - feature: "#0366D6"
  - enhancement: "#A2EEEF"
  - documentation: "#0075CA"
  - refactor: "#FBCA04"

status:
  - blocked: "#D93F0B"
  - in-review: "#0366D6"
  - ready-to-merge: "#00AA00"
  - wontfix: "#EEEEEE"

team:
  - backend: "#0366D6"
  - frontend: "#00AA00"
  - devops: "#FF8800"
```

**Automated Labeling:**

```yaml
# .github/workflows/auto-label.yml
name: Auto Label

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v4
        with:
          configuration-path: .github/labeler.yml

      - name: Label by title
        uses: actions/github-script@v7
        with:
          script: |
            const title = context.payload.pull_request.title;
            const labels = [];

            if (title.startsWith('fix:')) labels.push('bug');
            if (title.startsWith('feat:')) labels.push('feature');
            if (title.startsWith('docs:')) labels.push('documentation');

            if (labels.length > 0) {
              github.rest.issues.addLabels({
                issue_number: context.issue.number,
                labels: labels
              });
            }
```

### 5. GitHub Projects Integration

**Automate PR to Project:**

```yaml
# .github/workflows/pr-to-project.yml
name: Add PR to Project

on:
  pull_request:
    types: [opened, reopened]

jobs:
  add-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/add-to-project@v0.5
        with:
          project-url: https://github.com/orgs/myorg/projects/1
          github-token: ${{ secrets.GITHUB_TOKEN }}
          labeled: 'feature'
```

**Move PR on Status Change:**

```yaml
# .github/workflows/pr-status-update.yml
name: Update Project Status

on:
  pull_request:
    types: [ready_for_review, converted_to_draft, synchronize]

jobs:
  update-project:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v7
        with:
          script: |
            const pr = context.payload.pull_request;
            const status = pr.draft ? 'In Progress' : 'In Review';
            // Update project field with gh cli or API
```

### 6. CODEOWNERS Workflow

**Define Owners:**

```
# .github/CODEOWNERS

# Backend team owns all backend code
src/api/** @backend-team
src/db/** @backend-team @dba-team

# Frontend team owns UI
src/ui/** @frontend-team
src/components/** @frontend-team

# Security team reviews auth
src/auth/** @security-team
src/permissions/** @security-team

# Default fallback
* @engineering-lead
```

**Auto-Request from CODEOWNERS:**

```yaml
# Branch Protection: Required reviewers
Pattern: main
Require code owner reviews: ✓
```

**Manual Request:**

```bash
# GitHub automatically requests owners
# Or manually:
gh pr view 123  # Shows required owners

# Dismiss owner review if no change needed
gh pr review 123 --dismiss "No changes to owned files"
```

### 7. PR Checks and Status

**Require Status Checks:**

```yaml
# Branch Protection Settings
required_status_checks:
  strict: true
  contexts:
    - ci/build
    - ci/test
    - ci/lint
    - codeql/analysis
    - codecov/coverage
    - sonarcloud/quality-gate
```

**Show Check Status in PR:**

```bash
# View checks for PR
gh pr checks 123

# View specific check
gh run view <RUN_ID> --log

# Trigger re-run
gh run rerun <RUN_ID>
```

### 8. PR Cleanup and Automation

**Auto-Merge Stale PRs:**

```yaml
# .github/workflows/stale.yml
name: Close Stale PRs

on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          stale-pr-message: 'This PR is stale'
          stale-pr-label: 'stale'
          days-before-stale: 14
          days-before-close: 7
```

**Automatically Delete Merged Branches:**

```bash
# Enable in Branch Protection:
# Automatically delete head branches
```

---

## Configuration

### Complete PR Template with All Sections

`.github/pull_request_template.md`:

```markdown
## 📝 Description

Brief description of what this PR does.

## 🎯 Type of Change

- [ ] 🐛 Bug fix (non-breaking)
- [ ] ✨ New feature (non-breaking)
- [ ] 💥 Breaking change
- [ ] 📖 Documentation only
- [ ] ♻️ Refactoring (no behavior change)

## 🔗 Related Issues

Closes #123
Related to #456

## 🧪 Testing

- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] No tests needed (explain why)

## ✅ Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] No breaking changes

## 📊 Screenshots (if applicable)

## 🚀 Deployment Notes

Any deployment or configuration changes needed?

## 📋 Reviewers

@mention specific reviewers if needed
```

### Comprehensive CODEOWNERS

```
# Global owner
* @engineering-lead

# Backend services
src/api/ @backend-team
src/db/ @backend-team @dba-team
src/jobs/ @backend-team

# Frontend
src/ui/ @frontend-team
src/components/ @frontend-team
public/ @frontend-team

# Mobile
src/mobile/ @mobile-team
src/native/ @mobile-team

# Infrastructure
.github/workflows/ @devops-team
Dockerfile @devops-team
docker-compose.yml @devops-team
terraform/ @devops-team

# Security
src/auth/ @security-team
src/permissions/ @security-team
.github/secret* @security-team

# Documentation
docs/ @tech-writers
*.md @tech-writers

# Package management
package.json @frontend-team
package-lock.json @frontend-team
poetry.lock @backend-team
requirements.txt @backend-team
```

### Auto-Merge Workflow Configuration

`.github/workflows/auto-merge.yml`:

```yaml
name: Auto-Merge

on:
  pull_request:
    types: [opened, synchronize, labeled, unlabeled]
  pull_request_review:
    types: [submitted]
  check_run:
    types: [completed]
  workflow_run:
    types: [completed]

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - name: Auto-merge when ready
        uses: actions/github-script@v7
        with:
          script: |
            const pr = context.payload.pull_request;

            // Check conditions
            const canMerge =
              pr.draft === false &&
              pr.mergeable === true &&
              pr.review_decision === 'APPROVED' &&
              pr.labels.some(l => l.name === 'ready-to-merge');

            if (canMerge) {
              await github.rest.pulls.merge({
                owner: context.repo.owner,
                repo: context.repo.repo,
                pull_number: pr.number,
                merge_method: 'squash'
              });
            }
```

---

## Examples

### Example 1: Complete PR Workflow

```bash
# Create feature branch
git checkout -b feat/user-profiles

# Make changes and commit
git commit -am "feat: add user profile pages"

# Push and create PR
git push origin feat/user-profiles
gh pr create \
  --title "feat: add user profile pages" \
  --body "Implements user profile dashboard with edit capabilities"

# Add labels
gh pr edit 42 --add-label "feature,frontend,ready-to-review"

# Add to project
gh pr edit 42 --add-project "MyProject"

# Request reviewers
gh pr review 42 --request-review @alice @bob

# Monitor PR status
gh pr view 42 --json status,checks,reviews

# Once approved and checks pass
gh pr merge 42 --squash --auto --delete-branch
```

### Example 2: CODEOWNERS Auto-Request

```bash
# Create PR that modifies auth code
git checkout -b fix/auth-timeout
echo "export const AUTH_TIMEOUT = 30000;" > src/auth/timeout.js
git commit -am "fix: increase auth timeout"

# Create PR
gh pr create --title "fix: increase auth timeout"

# GitHub automatically requests @security-team as reviewer
# (because .github/CODEOWNERS specifies: src/auth/ @security-team)

# Security team gets notification
# Reviews and approves
gh pr review 45 --approve

# Once all checks pass, auto-merge can happen
```

### Example 3: Automated PR to Project

```bash
# PR is created with 'feature' label
# Automatically added to "Features" project
# Status: "Backlog"

# PR moved to "In Review" section
# Status tracked in project board

# PR approved
# Status moves to "Ready to Merge"

# PR merged
# Auto-archived or moved to "Done"
```

### Example 4: Complex Review Workflow

```bash
# Team lead creates feature PR
gh pr create --title "Major refactoring" --draft

# Adds todos for reviewers
gh pr comment 50 -b "Review checklist:
- [ ] Architecture makes sense
- [ ] No performance regressions
- [ ] Test coverage adequate
- [ ] Error handling complete"

# Frontend reviewer checks
gh pr review 50 --comment "LGTM from frontend perspective"

# Backend reviewer requests changes
gh pr review 50 --request-changes "Need database migration review"

# Developer responds
gh pr comment 50 -b "@backend-reviewer, added migration in latest commit"

# Backend reviewer checks again
gh pr review 50 --approve

# Team lead approves
gh pr review 50 --approve

# Auto-merge kicks in
# PR merged automatically
```

### Example 5: Release PR Workflow

```bash
# Create release PR manually
git checkout -b release/v1.5.0
npm version minor
git commit -am "Release 1.5.0"

# Create PR
gh pr create \
  --title "Release: v1.5.0" \
  --body "# Changelog\n- Feature X\n- Bug fix Y" \
  --label "release,critical"

# Add to project
gh pr edit 55 --add-project "Releases"

# Require multiple approvals for release
# Settings: Require 2 approvals for PRs to main

# Once approved
gh pr merge 55 --auto --merge
# (use --merge for releases, not --squash)
```

### Example 6: Automated Cleanup

```bash
# Stale PR detection (14 days no activity)
# Automatic comment: "This PR is stale"
# Auto-close after 7 more days

# Merged PR branches auto-deleted
# (Enable in branch protection settings)

# Draft PRs auto-converted to ready after update
# Re-request reviews automatically

# All automated via:
# .github/workflows/stale.yml
# .github/workflows/auto-merge.yml
```

---

## Best Practices

### 1. Descriptive PR Titles

```bash
# Good: Clear, specific
git commit -m "feat: add payment retry logic with exponential backoff"

# Bad: Vague
git commit -m "fix stuff"
git commit -m "update"
```

### 2. One Feature Per PR

```bash
# Good: Single feature
PR: Add two-factor authentication

# Bad: Multiple unrelated changes
PR: Add 2FA, refactor database layer, update documentation
```

### 3. Small, Reviewable PRs

```bash
# Good: 200-400 lines of code
# Reviews complete in 30 minutes

# Bad: 5000+ lines
# Reviews take days, harder to catch bugs
```

### 4. Meaningful Commit Messages

```bash
# Good: What and why
git commit -m "feat: implement caching layer

Reduces database queries by 60% for frequently accessed data.
Implements TTL of 5 minutes for cache invalidation."

# Bad: No context
git commit -m "add cache"
```

### 5. Self-Review Before Requesting

```bash
# Best practice:
1. Create PR as draft
2. Review your own changes
3. Fix issues you find
4. Mark as ready for review
5. Request reviewers

# This prevents reviewer fatigue
```

### 6. Respond Promptly to Feedback

```bash
# Good: Address feedback within 24 hours
# Bad: Let PR sit for a week

# This keeps momentum and prevents stale PRs
```

### 7. Link to Related Issues

```markdown
Closes #123          # PR closes issue
Fixes #456           # PR fixes issue
Related to #789      # Context only

# GitHub auto-closes issues when PR merges
```

---

## Integration with Other Skills

GitHub PR Management integrates with:

- **github-actions-workflows** - Run checks on PRs
- **git-workflow-strategy** - Branch protection rules
- **git-commit-strategy** - Conventional commit messages
- **github-security-scanning** - Security checks on PRs
- **build-optimization** - Build status checks

---

## Complete Command Reference

```bash
# PR Operations
gh pr create [--draft] [--title] [--body]
gh pr view <number>
gh pr edit <number> [--add-label] [--add-project]
gh pr merge <number> [--squash] [--auto] [--delete-branch]
gh pr close <number>
gh pr reopen <number>
gh pr list [--state] [--label] [--assignee]

# Reviews
gh pr review <number> [--approve] [--comment] [--request-changes]
gh pr view <number> --json reviews

# Comments
gh pr comment <number> --body "comment text"

# Status
gh pr checks <number>
gh pr view <number> --json status,checks
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
