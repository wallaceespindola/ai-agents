# GitHub CLI Automation Skill

**Automate GitHub operations with command-line tools. Master scripting, batch operations, custom extensions, and workflow automation.**

## Overview

GitHub CLI (gh) provides powerful command-line interface for GitHub operations. This skill covers automation scripting, batch operations, and custom extensions.

**What it does:**
- Executes GitHub operations from command line
- Automates repetitive tasks with scripts
- Manages issues, PRs, releases programmatically
- Creates custom gh extensions
- Integrates with CI/CD pipelines
- Generates reports and data exports
- Manages repository configuration
- Implements complex workflows with jq

**Perfect for:**
- Automation scripts
- Batch operations
- Release management
- Data analysis
- Custom integrations

---

## When to Use This Skill

Use GitHub CLI Automation when you need to:

- **Automate PR creation** for multiple repositories
- **Bulk manage issues** and labels
- **Generate release notes** automatically
- **Create reports** on repository statistics
- **Sync data** with external systems
- **Manage team workflows** at scale
- **Extract data** from GitHub with jq
- **Create custom commands** via extensions

---

## Quick Start (10 Minutes)

### 1. Install GitHub CLI

```bash
# macOS
brew install gh

# Linux
sudo apt-get install gh

# Windows
choco install gh

# Verify
gh --version
```

### 2. Authenticate

```bash
gh auth login

# Choose:
# GitHub.com or GitHub Enterprise
# HTTPS or SSH
# Paste token or login via browser
```

### 3. Create Simple Issue

```bash
gh issue create \
  --title "Add user authentication" \
  --body "Implement JWT-based auth system" \
  --label "feature" \
  --assignee "@me"
```

### 4. List PRs with Filtering

```bash
gh pr list \
  --state open \
  --label "bug" \
  --search "is:ready" \
  --json title,author,url

# Output as table (default) or JSON
```

### 5. Create Release

```bash
gh release create v1.0.0 \
  --title "Version 1.0.0" \
  --notes-file CHANGELOG.md \
  --draft false
```

---

## How It Works

### 1. Core Commands

**Issues:**
```bash
gh issue create --title "Title" --body "Description"
gh issue list --state open --label "bug"
gh issue view 123
gh issue comment 123 --body "Comment text"
gh issue close 123
gh issue edit 123 --title "Updated title"
gh issue reopen 123
gh issue pin 123
gh issue delete 123
```

**Pull Requests:**
```bash
gh pr create --title "Title" --body "Description"
gh pr list --state open --draft false
gh pr view 123
gh pr merge 123 --squash --delete-branch
gh pr review 123 --approve
gh pr comment 123 --body "LGTM"
gh pr diff 123
gh pr checks 123
```

**Releases:**
```bash
gh release create v1.0.0
gh release list
gh release view v1.0.0
gh release download v1.0.0 --dir ./downloads
gh release delete v1.0.0
```

**Repositories:**
```bash
gh repo list
gh repo view
gh repo clone owner/repo
gh repo create my-repo --public
gh repo delete owner/repo
gh repo fork owner/repo
```

### 2. Output Formats

**Table Format (default):**
```bash
gh pr list --state open
# Shows: ID, Title, Branch, Updated, State
```

**JSON Format:**
```bash
gh pr list --state open --json number,title,author,state

# Output:
[
  {
    "number": 42,
    "title": "Add feature",
    "author": { "login": "alice" },
    "state": "OPEN"
  }
]
```

**Plain Text Format:**
```bash
gh issue list --state open --json title --template '{{range .}}{{.title}}{{"\n"}}{{end}}'
```

### 3. Advanced Filtering

**Search with Queries:**
```bash
# Issues opened in last week
gh issue list --search "created:>2026-01-26"

# Open PRs with label and status check
gh pr list --state open --label "ready-to-review" --search "is:draft=false"

# Issues assigned to you
gh issue list --assignee "@me"

# PRs by specific author
gh pr list --search "author:alice"

# Issues with multiple labels
gh issue list --label "bug,critical"
```

### 4. API Queries with jq

**Chain gh commands with jq:**

```bash
# Get all open PRs and extract information
gh pr list --state open --json number,title,author \
  | jq '.[] | {number, title, author: .author.login}'

# Count PRs by author
gh pr list --state open --json author \
  | jq 'group_by(.author.login) | map({author: .[0].author.login, count: length})'

# Extract PR URLs
gh pr list --state open --json url \
  | jq '.[].url' --raw-output
```

### 5. Creating Issues Programmatically

**Create from Template:**

```bash
# Create multiple issues from CSV
while IFS=',' read title description; do
  gh issue create --title "$title" --body "$description" --label "feature"
done < issues.csv
```

**Create with Labels and Assignees:**

```bash
gh issue create \
  --title "Bug: Login timeout" \
  --body "Users logged out after 5 minutes" \
  --label "bug,critical" \
  --assignee alice,bob \
  --milestone "v1.5.0"
```

### 6. PR Operations at Scale

**Merge all ready PRs:**

```bash
gh pr list --state open --label "ready-to-merge" --json number \
  | jq '.[] | .number' \
  | while read pr_number; do
      gh pr merge "$pr_number" --squash --auto
    done
```

**Close stale PRs:**

```bash
gh pr list --state open --search "updated:<2025-12-01" --json number \
  | jq '.[] | .number' \
  | while read pr_number; do
      gh pr close "$pr_number" --comment "Closing stale PR"
    done
```

### 7. Custom Extensions

**Create Extension Directory:**

```bash
mkdir -p ~/.config/gh/extensions/gh-myscript
cd ~/.config/gh/extensions/gh-myscript
```

**Create executable script (executable):**

```bash
#!/bin/bash
# gh-myscript

# Usage: gh myscript [args]

echo "Running custom script..."
# Your code here
```

**Install extension:**

```bash
# Extensions in ~/.config/gh/extensions/ auto-discovered
gh myscript arg1 arg2
```

**Popular Extension Patterns:**

```bash
# gh-stats: Repository statistics
# gh-team: Team management
# gh-copilot: AI assistance
# gh-query: Advanced queries

# Install from repository
gh extension install owner/gh-extension-name

# List installed extensions
gh extension list
```

### 8. Release Management

**Create Release with Artifacts:**

```bash
gh release create v1.0.0 \
  --title "Version 1.0.0" \
  --notes "Major feature release" \
  dist/app.zip dist/app.tar.gz \
  --draft false \
  --prerelease false
```

**Upload Artifacts to Release:**

```bash
gh release upload v1.0.0 \
  dist/app-linux.tar.gz \
  dist/app-macos.zip \
  dist/app-windows.exe
```

**Generate Release Notes:**

```bash
# Previous tag must exist
gh release create v2.0.0 \
  --generate-notes \
  --title "Version 2.0.0"

# Auto-generates from commits since last release
```

---

## Configuration

### .gitconfig for gh

```bash
git config --global gh.pager ""
git config --global gh.editor vim
```

### gh Configuration File

`~/.config/gh/config.yml`:

```yaml
# GitHub.com configuration
github.com:
  # Git protocol
  git_protocol: https

  # Editor
  editor: vim

  # Pager
  pager: less

  # Aliases
  aliases:
    co: pr checkout
    prs: pr list --assignee "@me"
    issues: issue list --assignee "@me"
```

### Custom Aliases

```bash
# Add aliases to config
gh alias set prs 'pr list --state open --assignee "@me"'
gh alias set issues 'issue list --state open --assignee "@me"'
gh alias set my-pulls 'pr list --state open --author "@me"'
gh alias set review 'pr list --state open --label "ready-for-review"'

# List aliases
gh alias list

# View alias
gh alias list --verbose
```

---

## Examples

### Example 1: Automated Release Script

`scripts/release.sh`:

```bash
#!/bin/bash
set -e

VERSION=$1
REPO=$2

if [ -z "$VERSION" ] || [ -z "$REPO" ]; then
  echo "Usage: ./release.sh <version> <repo>"
  exit 1
fi

echo "Creating release for $REPO version $VERSION..."

# Build application
npm run build

# Create and push tag
git tag -a "v$VERSION" -m "Release $VERSION"
git push origin "v$VERSION"

# Create GitHub release
gh release create "v$VERSION" \
  --repo "$REPO" \
  --title "Version $VERSION" \
  --generate-notes \
  dist/* \
  --draft false

echo "Release $VERSION created successfully!"

# Notify team
gh issue comment 42 -b "@team Release $VERSION is live!"
```

**Usage:**
```bash
./scripts/release.sh 1.5.0 owner/repo
```

### Example 2: Bulk Issue Creator

`scripts/bulk-issues.sh`:

```bash
#!/bin/bash

# Create issues from CSV
# Format: title,description,label,assignee

CSV_FILE=$1

if [ ! -f "$CSV_FILE" ]; then
  echo "File not found: $CSV_FILE"
  exit 1
fi

while IFS=',' read -r title description label assignee; do
  echo "Creating: $title"

  gh issue create \
    --title "$title" \
    --body "$description" \
    --label "$label" \
    --assignee "$assignee"
done < "$CSV_FILE"

echo "Bulk issue creation complete!"
```

**CSV File Format:**
```
Add authentication,Implement JWT auth,feature,alice
Fix login bug,Users can't login,bug,bob
Update docs,Add API documentation,docs,carol
```

**Usage:**
```bash
./scripts/bulk-issues.sh issues.csv
```

### Example 3: PR Report Generator

`scripts/pr-report.sh`:

```bash
#!/bin/bash

# Generate PR statistics

echo "=== Pull Request Report ==="
echo "Total open PRs:"
gh pr list --state open --json number | jq '. | length'

echo ""
echo "PRs by author:"
gh pr list --state open --json author \
  | jq 'group_by(.author.login) |
        map({author: .[0].author.login, count: length}) |
        sort_by(.count) |
        reverse[]'

echo ""
echo "PRs awaiting review:"
gh pr list --state open --json reviewDecisionState \
  | jq 'map(select(.reviewDecisionState == "REVIEW_REQUIRED")) | length'

echo ""
echo "PR age distribution:"
gh pr list --state open --json createdAt \
  | jq '.[] |
        (now - (. | fromdate) | . / 86400 | floor) as $days |
        if $days < 1 then "less than 1 day"
        elif $days < 3 then "1-3 days"
        elif $days < 7 then "3-7 days"
        else "7+ days" end' \
  | sort | uniq -c

echo ""
echo "Oldest open PR:"
gh pr list --state open --json number,createdAt,title \
  | jq 'sort_by(.createdAt) | first'
```

### Example 4: Auto-Merge Ready PRs

`scripts/auto-merge.sh`:

```bash
#!/bin/bash

REPO=$1
LABEL=${2:-"ready-to-merge"}

echo "Auto-merging PRs with label: $LABEL"

# Get all PRs with the label
gh pr list \
  --repo "$REPO" \
  --state open \
  --label "$LABEL" \
  --json number \
  | jq '.[] | .number' \
  | while read -r pr_number; do
      echo "Processing PR #$pr_number..."

      # Check if all checks passed
      if gh pr checks "$pr_number" --required | grep -q "pass"; then
        echo "Merging PR #$pr_number..."
        gh pr merge "$pr_number" \
          --squash \
          --delete-branch \
          --auto || echo "Failed to merge PR #$pr_number"
      else
        echo "PR #$pr_number has failing checks, skipping"
      fi
    done

echo "Auto-merge complete!"
```

### Example 5: Repository Statistics

`scripts/repo-stats.sh`:

```bash
#!/bin/bash

REPO=$1

echo "=== Repository Statistics for $REPO ==="

# Clone stats
echo ""
echo "Issues:"
gh issue list --repo "$REPO" --state all --json number | jq '. | length'

echo ""
echo "Pull Requests:"
gh pr list --repo "$REPO" --state all --json number | jq '. | length'

echo ""
echo "Releases:"
gh release list --repo "$REPO" --json name | jq '. | length'

echo ""
echo "Top Contributors:"
gh api repos/"$REPO"/contributors \
  --paginate \
  | jq -s 'sort_by(.contributions) | reverse[] |
           {login: .login, contributions: .contributions}' \
  | head -10

echo ""
echo "Languages:"
gh api repos/"$REPO"/languages | jq 'to_entries[] | {language: .key, bytes: .value}'
```

### Example 6: Workflow Automation

`scripts/deploy-workflow.sh`:

```bash
#!/bin/bash

# Trigger deployment workflow with parameters

WORKFLOW=$1
ENVIRONMENT=$2
VERSION=$3

echo "Triggering workflow: $WORKFLOW"
echo "Environment: $ENVIRONMENT"
echo "Version: $VERSION"

gh workflow run "$WORKFLOW" \
  --ref main \
  -f environment="$ENVIRONMENT" \
  -f version="$VERSION"

# Monitor workflow
echo "Waiting for workflow to complete..."

sleep 5

# Get latest run
RUN_ID=$(gh run list --workflow "$WORKFLOW" --limit 1 --json databaseId --jq '.[0].databaseId')

# Wait for completion
while true; do
  STATUS=$(gh run view "$RUN_ID" --json status --jq '.status')

  if [ "$STATUS" = "completed" ]; then
    CONCLUSION=$(gh run view "$RUN_ID" --json conclusion --jq '.conclusion')
    echo "Workflow completed with status: $CONCLUSION"
    break
  fi

  echo "Workflow status: $STATUS..."
  sleep 10
done
```

---

## Best Practices

### 1. Use jq for Complex Filtering

```bash
# Good: Complex query with jq
gh pr list --state open --json number,title,author,reviews \
  | jq '.[] | select(.reviews | length > 0) | {number, title}'

# Bad: Filtering output with grep/awk
gh pr list --state open | grep "reviewed"
```

### 2. Handle Errors in Scripts

```bash
#!/bin/bash
set -e  # Exit on error
set -u  # Exit on undefined variable

# Or explicit error handling
if ! gh issue create --title "Test"; then
  echo "Failed to create issue"
  exit 1
fi
```

### 3. Use Environment Variables

```bash
# Good: Secure sensitive data
GH_TOKEN=$(gh auth token)

# Or use gh auth directly
gh pr create --title "Title"  # Uses configured auth

# Bad: Hardcoding secrets
GH_TOKEN="ghp_1234567890abcdef"
```

### 4. Cache Results When Possible

```bash
# Good: Store results for multiple operations
OPEN_PRS=$(gh pr list --state open --json number,title)

# Use results multiple times
echo "$OPEN_PRS" | jq '.[].number'
echo "$OPEN_PRS" | jq '.[].title'

# Bad: Multiple API calls
gh pr list --state open --json number
gh pr list --state open --json title
```

### 5. Document Custom Extensions

```bash
#!/bin/bash
# gh-custom-command
# Custom extension for batch operations
# Usage: gh custom-command [options]

# Description of what it does
# Examples of usage
```

### 6. Batch Operations Responsibly

```bash
# Good: Add confirmation step
read -p "Merge 10 PRs? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
  # Proceed with batch operation
fi

# Bad: No confirmation, auto-runs on many items
# Could accidentally close all issues
```

---

## Integration with Other Skills

GitHub CLI Automation integrates with:

- **github-actions-workflows** - Trigger workflows programmatically
- **github-pr-management** - Automate PR operations
- **git-workflow-strategy** - Enforce branch rules
- **github-security-scanning** - Query security data
- **build-optimization** - Trigger builds

---

## Complete Command Reference

```bash
# Authentication
gh auth login
gh auth logout
gh auth status

# Issues
gh issue create [--title] [--body] [--label] [--assignee]
gh issue list [--state] [--label] [--assignee]
gh issue view <number>
gh issue comment <number> --body "text"
gh issue close <number>
gh issue edit <number> [--title] [--body]

# Pull Requests
gh pr create [--title] [--body] [--draft]
gh pr list [--state] [--label]
gh pr view <number>
gh pr merge <number> [--squash] [--delete-branch] [--auto]
gh pr review <number> [--approve] [--comment]

# Releases
gh release create [version] [--title] [--notes] [files...]
gh release list
gh release view [version]
gh release download [version]

# Extensions
gh extension create [name]
gh extension install [owner/repo]
gh extension list
gh extension upgrade [name]

# Aliases
gh alias set [name] '[command]'
gh alias list
gh alias delete [name]

# API (advanced)
gh api [endpoint] [-F field=value] [-H header]
gh api repos/owner/repo/pulls --paginate
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
