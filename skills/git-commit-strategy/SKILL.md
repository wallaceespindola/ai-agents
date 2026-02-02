# Git Commit Strategy Skill

**Master conventional commits, commit linting, signing, interactive rebasing, and commit message standards for clear project history.**

## Overview

Commit messages are permanent project documentation. This skill covers conventional commits, message standards, signing, and automated linting.

**What it does:**
- Implements conventional commit format
- Configures commit linting with commitlint
- Enforces commit signing with GPG
- Enables interactive rebase for history cleanup
- Generates changelogs from commits
- Automates commit message templates
- Validates message format in CI/CD
- Provides message guidelines

**Perfect for:**
- Automated changelog generation
- Clear project history
- Semantic versioning
- Release automation
- Commit auditing

---

## When to Use This Skill

Use Git Commit Strategy when you need to:

- **Standardize commit messages** across team
- **Generate changelogs automatically** from commits
- **Implement semantic versioning** based on commits
- **Sign commits** for security and compliance
- **Enforce message format** before allowing commit
- **Clean up commit history** before merging
- **Audit commit authorship** with signatures
- **Improve code history readability**

---

## Quick Start (10 Minutes)

### 1. Install Commitlint

```bash
npm install --save-dev @commitlint/cli @commitlint/config-conventional

# Or global
npm install -g commitlint
```

### 2. Create Configuration

Create `commitlint.config.js`:

```javascript
module.exports = {
  extends: ['@commitlint/config-conventional'],
};
```

### 3. Setup Git Hook

```bash
npm install --save-dev husky
npx husky install
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'
```

### 4. Sign Commits with GPG

```bash
# Check if you have GPG set up
gpg --list-secret-keys --keyid-format long

# Configure Git to sign commits
git config --global commit.gpgSign true
git config --global user.signingKey <KEY_ID>

# Commit (auto-signs)
git commit -m "feat: add feature"
```

### 5. Create Commit Message Template

Create `.gitmessage`:

```
# <type>(<scope>): <subject>
#
# <body>
#
# <footer>

# --- COMMIT END ---
# Type can be
#    feat     (new feature)
#    fix      (bug fix)
#    refactor (refactoring code)
#    style    (formatting, missing semicolons, etc)
#    docs     (changes to documentation)
#    test     (adding or updating tests)
#    chore    (maintenance tasks)
#
# Scope is optional
# Body is optional (wrap at 72 chars)
# Footer is optional (e.g., Closes #123)
```

Configure:

```bash
git config --global commit.template ~/.gitmessage
```

---

## How It Works

### 1. Conventional Commits Format

**Structure:**

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Example Commits:**

```bash
# Simple fix
git commit -m "fix: prevent racing condition in payment processing"

# Feature with scope
git commit -m "feat(auth): add JWT token refresh mechanism"

# Breaking change
git commit -m "feat!: redesign API endpoints

BREAKING CHANGE: /api/users endpoint replaced with /api/v2/users"

# Complex commit
git commit -m "refactor(db): optimize query performance

- Reduce database round-trips by 40%
- Add connection pooling
- Cache frequently accessed data

Closes #456
Perf-Note: Query time reduced from 1.2s to 0.3s"
```

**Commit Types:**

```
feat       New feature
fix        Bug fix
docs       Documentation changes
style      Code style (no logic change)
refactor   Code restructure (no feature change)
perf       Performance improvement
test       Add/update tests
chore      Build, deps, tooling
ci         CI/CD configuration
build      Build system changes
revert     Revert previous commit
```

**Scopes (Examples):**

```
auth      Authentication system
db        Database layer
api       REST API
ui        User interface
payments  Payment processing
search    Search functionality
```

### 2. Commitlint Configuration

**Basic Configuration:**

```javascript
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      [
        'feat',
        'fix',
        'docs',
        'style',
        'refactor',
        'perf',
        'test',
        'chore',
        'ci',
        'revert',
      ],
    ],
    'type-case': [2, 'always', 'lowercase'],
    'type-empty': [2, 'never'],
    'scope-case': [2, 'always', 'lowercase'],
    'subject-case': [
      2,
      'never',
      ['sentence-case', 'start-case', 'pascal-case', 'upper-case'],
    ],
    'subject-empty': [2, 'never'],
    'subject-full-stop': [2, 'never', '.'],
    'subject-max-length': [2, 'always', 50],
    'body-leading-blank': [2, 'always'],
    'body-max-line-length': [2, 'always', 100],
  },
};
```

**Custom Rules:**

```javascript
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'scope-enum': [
      2,
      'always',
      [
        'auth',
        'api',
        'db',
        'ui',
        'payments',
        'infrastructure',
        'docs',
      ],
    ],
    'subject-min-length': [2, 'always', 10],
    'body-min-length': [0, 'never', 20],  // Optional body
  },
};
```

### 3. Commit Signing

**GPG Setup:**

```bash
# Generate GPG key
gpg --gen-key

# List keys
gpg --list-secret-keys --keyid-format long

# Show public key
gpg --armor --export <KEY_ID>

# Configure Git
git config --global user.signingKey <KEY_ID>
git config --global commit.gpgSign true
```

**Sign Commits:**

```bash
# Automatic signing (configured)
git commit -m "feat: add feature"

# Manual signing
git commit -S -m "feat: add feature"

# Verify signature
git verify-commit <commit_hash>
git log --show-signature
```

**GitHub Web Interface:**

- Signed commits show "Verified" badge
- Unverified commits show warning
- Can enforce signed commits on branch protection

### 4. Interactive Rebase

**Reorder Commits:**

```bash
# Last 5 commits
git rebase -i HEAD~5

# Editor opens with commits
# pick <hash> First commit
# pick <hash> Second commit
# pick <hash> Third commit

# Change "pick" to reorder:
# pick <hash> Third commit
# pick <hash> First commit
# pick <hash> Second commit
```

**Squash Commits:**

```bash
git rebase -i HEAD~5

# In editor:
# pick <hash> feat: add feature
# squash <hash> fix: typo in feature
# squash <hash> style: format code

# Results in single commit with combined message
```

**Reword Commits:**

```bash
git rebase -i HEAD~3

# In editor:
# pick <hash> old message
# reword <hash> fix typo
# pick <hash> another commit

# Opens editor for each "reword" commit
```

**Drop Commits:**

```bash
git rebase -i HEAD~5

# In editor:
# pick <hash> commit 1
# drop <hash> commit 2 (remove this)
# pick <hash> commit 3
```

### 5. Automated Changelog Generation

**Using conventional-changelog:**

```bash
npm install --save-dev conventional-changelog-cli

# Generate changelog
npx conventional-changelog -p angular -i CHANGELOG.md -s

# Result: CHANGELOG.md with entries from commits
```

**Changelog Format:**

```markdown
## [2.0.0] - 2026-02-02

### Features
- **auth**: add JWT token refresh mechanism
- **api**: new v2 endpoints

### Bug Fixes
- **payment**: prevent racing condition
- **database**: fix connection pool leak

### Breaking Changes
- **api**: /users endpoint replaced with /v2/users

### Performance
- **db**: reduce query time by 40%
```

**Automated Release Process:**

```bash
# semantic-release automates:
# 1. Analyze commits for version bump
# 2. Generate changelog
# 3. Bump version
# 4. Create git tag
# 5. Publish to npm/GitHub
# 6. Post release notes

npm install --save-dev semantic-release
npx semantic-release --dry-run
```

### 6. Commit Message Template

**Template System:**

```bash
# Set global template
git config --global commit.template ~/.gitmessage

# Set per-repo template
git config commit.template .gitmessage
```

**Template Content:**

```
<type>(<scope>): <description>

<body>

<footer>

# --- COMMIT END ---
# Type options: feat, fix, docs, style, refactor, perf, test, chore
# Scope: auth, api, db, ui, etc (optional)
# Description: Imperative, lowercase, max 50 chars
# Body: Explain what and why, wrap at 72 chars (optional)
# Footer: Issue references like Closes #123 (optional)
# Example:
#   feat(auth): add two-factor authentication
#
#   Implement TOTP-based 2FA using speakeasy library.
#   Users can enable 2FA in account settings.
#
#   Closes #456
```

### 7. Validation in CI/CD

**Lint Commits in PR:**

```yaml
name: Lint Commits

on: [pull_request]

jobs:
  commit-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - run: npm install -g @commitlint/cli

      - name: Validate commits
        run: |
          npx commitlint \
            --from ${{ github.event.pull_request.base.sha }} \
            --to HEAD
```

**Validate Message Before Push:**

```bash
#!/bin/bash
# .git/hooks/commit-msg

npx commitlint --edit "$1"
exit $?
```

---

## Configuration

### Complete Commitlint Setup

`commitlint.config.js`:

```javascript
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      [
        'feat',
        'fix',
        'docs',
        'style',
        'refactor',
        'perf',
        'test',
        'chore',
        'ci',
        'build',
        'revert',
      ],
    ],
    'type-case': [2, 'always', 'lowercase'],
    'type-empty': [2, 'never'],
    'scope-enum': [
      2,
      'always',
      [
        'auth',
        'api',
        'database',
        'ui',
        'payment',
        'search',
        'notification',
        'infrastructure',
        'docs',
      ],
    ],
    'scope-case': [2, 'always', 'lowercase'],
    'scope-empty': [0, 'optional'],
    'subject-case': [
      2,
      'never',
      ['sentence-case', 'start-case', 'pascal-case', 'upper-case'],
    ],
    'subject-empty': [2, 'never'],
    'subject-full-stop': [2, 'never', '.'],
    'subject-max-length': [2, 'always', 60],
    'subject-min-length': [2, 'always', 10],
    'body-leading-blank': [2, 'always'],
    'body-max-line-length': [2, 'always', 100],
    'body-min-length': [0, 'never', 0],
    'footer-leading-blank': [2, 'always'],
    'footer-max-line-length': [2, 'always', 100],
    'footer-min-length': [0, 'never', 0],
  },

  // Custom patterns
  parserPreset: {
    parserOpts: {
      referenceActions: ['Closes', 'Fixes', 'Resolves', 'Related'],
      issuePrefixes: ['#', 'PROJ-'],
    },
  },
};
```

### Husky Configuration

`.husky/commit-msg`:

```bash
#!/bin/sh
. "$(dirname "$0")/_/husky.sh"

npx --no -- commitlint --edit "${1}"
```

`.husky/pre-commit`:

```bash
#!/bin/sh
. "$(dirname "$0")/_/husky.sh"

npm run lint
npm run type-check
npm test
```

---

## Examples

### Example 1: Feature Commit with Multiple Commits

```bash
# Start feature
git checkout -b feat/two-factor-auth

# First commit
echo "// TOTP setup" > src/auth/totp.js
git add .
git commit -m "feat(auth): add TOTP library and setup

- Install speakeasy library
- Create TOTP utility functions
- Add type definitions"

# Second commit
echo "// UI component" > src/components/2fa.js
git add .
git commit -m "feat(auth): add 2FA setup component

- Create React component for 2FA configuration
- Validate user password
- Display QR code for authenticator app"

# Third commit - fix discovered issue
echo "// Fix regex" >> src/auth/totp.js
git add .
git commit -m "fix(auth): improve TOTP validation regex

Fixes issue where valid tokens rejected"

# View commits
git log --oneline -3

# Now rebase to squash before merging
git rebase -i main
# (squash last 2 commits into first)
```

### Example 2: Rebase and Clean History

```bash
# Start with 5 commits
git log --oneline HEAD~5..HEAD
# d1a2b3 fix: typo
# e4f5g6 style: format code
# h7i8j9 feat: add auth
# k0l1m2 docs: update readme
# n3o4p5 chore: update deps

# Interactive rebase
git rebase -i HEAD~5

# In editor:
pick n3o4p5 chore: update deps
pick k0l1m2 docs: update readme
pick h7i8j9 feat: add auth
squash e4f5g6 style: format code
squash d1a2b3 fix: typo

# Result: 3 commits
# chore: update deps
# docs: update readme
# feat: add auth (includes style and fix)
```

### Example 3: Conventional Commits Workflow

```bash
# Issue found: #456 "Add password reset"
# Create feature branch
git checkout -b feat/password-reset

# Implement feature
git add src/auth/reset.js src/components/ResetForm.js
git commit -m "feat(auth): implement password reset

- Add password reset endpoint
- Create reset email template
- Implement token validation (24h expiry)
- Add reset form component

Closes #456"

# Write tests
git add tests/auth/reset.test.js
git commit -m "test(auth): add password reset tests

- Test reset token generation
- Test reset token validation
- Test invalid/expired tokens
- Test email sending"

# Documentation
git add docs/auth.md
git commit -m "docs(auth): document password reset flow

- Add API documentation
- Include sequence diagram
- Add troubleshooting section"

# Create PR
gh pr create --title "feat: implement password reset" \
  --body "Closes #456"

# GitHub changelog would include:
# - feat(auth): implement password reset
# - test(auth): add password reset tests
# - docs(auth): document password reset flow
```

### Example 4: GPG Signed Commits

```bash
# Setup
git config --global commit.gpgSign true
git config --global user.signingKey <GPG_KEY_ID>

# Normal commit (auto-signed)
git commit -m "feat: add feature"

# Verify
git log --show-signature

# Output:
# commit abc123def456
# gpg: Signature made Fri Feb  2 10:00:00 2026 UTC
# gpg:                using RSA key 1234567890ABCDEF
# gpg: Good signature from "Wallace Espindola <wallace@example.com>"
```

### Example 5: Breaking Changes

```bash
# Major version change (breaking change)
git commit -m "refactor!: redesign API routes

BREAKING CHANGE: /api/v1 endpoints removed, use /api/v2

- Removed /api/v1/users endpoint
- Removed /api/v1/posts endpoint
- All clients must migrate to /api/v2

Migration guide: https://docs.example.com/migration-v2"

# Or with scope
git commit -m "refactor(api)!: redesign REST endpoints

BREAKING CHANGE: API v1 deprecated, use v2 instead"

# Semantic release detects:
# - BREAKING CHANGE footer = major version bump (1.0.0 → 2.0.0)
```

### Example 6: Automated Changelog

```bash
# Setup
npm install --save-dev conventional-changelog-cli

# Configure package.json
{
  "scripts": {
    "release": "conventional-changelog -p angular -i CHANGELOG.md -s -r 0 && git add CHANGELOG.md"
  }
}

# Run before release
npm run release

# Generates from all commits since last tag:
# ## [2.0.0] - 2026-02-02
#
# ### Features
# - Implement password reset
#
# ### Tests
# - Add password reset tests
#
# ### Documentation
# - Document password reset flow
#
# ### Performance
# - Optimize database queries by 40%
```

---

## Best Practices

### 1. Atomic Commits

```bash
# Good: One feature per commit
git commit -m "feat: add password reset"

# Bad: Multiple unrelated changes
git commit -m "add auth, fix typos, update docs, refactor db"
```

### 2. Imperative Mood

```bash
# Good: Describe action
git commit -m "refactor: simplify payment logic"

# Bad: Describe result
git commit -m "simplified payment logic"
```

### 3. Reference Issues

```bash
# Good: Clear issue reference
git commit -m "fix: prevent XSS in comments

Closes #789"

# Bad: No issue reference
git commit -m "fix XSS vulnerability"
```

### 4. Explain Why, Not What

```bash
# Good: Explain motivation
git commit -m "perf: add caching layer

Reduces database queries by 60% for frequently
accessed user profiles. Implements TTL of 5
minutes for cache invalidation."

# Bad: Just code description
git commit -m "add cache"
```

### 5. Sign Important Commits

```bash
# Good: Sign production commits
git config --global commit.gpgSign true

# For critical releases/hotfixes
git commit -S -m "hotfix: security patch"
```

---

## Integration with Other Skills

Git Commit Strategy integrates with:

- **github-actions-workflows** - Run linting in CI
- **git-workflow-strategy** - Enforce standards
- **github-pr-management** - Reference issues
- **build-optimization** - Track changes
- **github-cli-automation** - Generate releases

---

## Complete Command Reference

```bash
# Committing
git commit -m "message"
git commit -S -m "message"  # Sign commit
git commit --amend          # Fix previous commit
git commit --allow-empty    # Empty commit

# Rebasing
git rebase -i HEAD~5        # Interactive rebase
git rebase --continue       # After conflict resolution
git rebase --abort          # Cancel rebase

# Viewing
git log --oneline           # Compact log
git log --show-signature    # Show GPG signatures
git log --pretty=fuller     # Detailed log
git show <commit>           # Show commit details
git verify-commit <commit>  # Verify signature

# Validation
commitlint --from <ref> --to <ref>
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
