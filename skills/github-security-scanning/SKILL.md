# GitHub Security Scanning Skill

**Implement comprehensive security scanning with Dependabot, secret scanning, CodeQL analysis, and vulnerability management.**

## Overview

GitHub provides integrated security tools for vulnerability detection, dependency management, and secret scanning. This skill covers implementation and best practices.

**What it does:**
- Configures Dependabot for dependency updates
- Enables secret scanning to prevent credential leaks
- Implements CodeQL for code vulnerability analysis
- Manages SARIF security reports
- Handles vulnerability alerts and patches
- Enforces security policies in CI/CD
- Generates security reports and dashboards
- Integrates with security workflows

**Perfect for:**
- Proactive vulnerability detection
- Dependency management at scale
- Preventing credential leaks
- Meeting security compliance requirements
- Automated patching

---

## When to Use This Skill

Use GitHub Security Scanning when you need to:

- **Detect vulnerable dependencies** automatically
- **Keep dependencies updated** with security patches
- **Prevent secret leaks** to git repositories
- **Scan code for vulnerabilities** before release
- **Manage CVSS scores** and risk assessment
- **Generate compliance reports** for audits
- **Enforce security policies** in CI/CD
- **Monitor supply chain security**

---

## Quick Start (10 Minutes)

### 1. Enable Dependabot

GitHub Repo → Settings → Security and analysis → Enable Dependabot:

```
✓ Dependabot alerts
✓ Dependabot security updates
✓ Dependabot version updates
```

### 2. Create Dependabot Config

Create `.github/dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    allow:
      - dependency-type: "direct"

  - package-ecosystem: "pip"
    directory: "/backend"
    schedule:
      interval: "weekly"
```

### 3. Enable Secret Scanning

Settings → Security and analysis → Secret scanning:

```
✓ Push protection (blocks pushes with secrets)
✓ Secret scanning alerts
```

### 4. Enable CodeQL

Create `.github/workflows/codeql.yml`:

```yaml
name: CodeQL

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v2
        with:
          languages: 'javascript,python'
      - uses: github/codeql-action/autobuild@v2
      - uses: github/codeql-action/analyze@v2
```

### 5. View Security Dashboard

Settings → Security → Security overview:
- Vulnerability count
- Secret leaks
- CodeQL issues
- Dependency health

---

## How It Works

### 1. Dependabot Configuration

**Update Schedule Options:**

```yaml
schedule:
  interval: "daily"     # Every day
  time: "03:00"         # 3 AM UTC
  day: "monday"         # Weekly on Monday
```

**Semantic Versioning Control:**

```yaml
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    # Control patch/minor/major updates
    versioning-strategy: "auto"  # Default
    # Or:
    versioning-strategy: "increase"       # 1.0.0 -> 1.0.1
    versioning-strategy: "increase-if-necessary"
```

**Filtering Dependencies:**

```yaml
allow:
  - dependency-type: "all"          # All deps
  - dependency-type: "direct"       # Direct only
  - dependency-type: "indirect"     # Transitive

ignore:
  - dependency-name: "express"      # Skip this package
    versions: ["1.x"]               # Skip version range
  - dependency-name: "lodash"
    update-types: ["version-update:semver-major"]
```

**Commit Settings:**

```yaml
commit-message:
  prefix: "chore"
  prefix-development: "chore"
  include: "scope"  # Include package name in scope

pull-request-branch-name:
  separator: "/"  # Branch: "dependabot/npm/express-4.0.0"

reviewers:
  - "security-team"
assignees:
  - "automation"
```

### 2. Secret Scanning

**Detected Secret Types:**

```
- GitHub tokens
- AWS credentials
- Private keys (RSA, DSA, etc.)
- API keys (Slack, Stripe, etc.)
- Database passwords
- OAuth tokens
- Google API keys
- Custom patterns
```

**Custom Secret Patterns:**

Create `.github/secret_scanning.json`:

```json
{
  "patterns": [
    {
      "name": "Company API Key",
      "pattern": "company_[0-9a-zA-Z]{32}",
      "secret_group": 0
    },
    {
      "name": "Internal Token",
      "pattern": "internal-token[0-9]{6}"
    }
  ]
}
```

**Handle Secret Leaks:**

```bash
# If secret leaked to repo
gh secret-scanning list-secrets

# Rotate in your systems
# Remove from git history
git filter-branch --tree-filter 'find . -name "secrets.env" -delete'
git push origin --force-with-lease

# Or use BFG Repo-Cleaner
bfg --delete-file secrets.env .
```

### 3. CodeQL Analysis

**Supported Languages:**

```
- JavaScript/TypeScript
- Python
- Java
- C/C++
- C#
- Go
- Ruby (beta)
```

**Custom CodeQL Queries:**

Create `.github/codeql/queries/my-queries.ql`:

```ql
/**
 * Finds potential SQL injection vulnerabilities
 */

import javascript

from DataFlow::Source source, DataFlow::Sink sink
where source.flowsTo(sink)
select source, "Potential data flow issue"
```

**Run Custom Queries:**

```yaml
- uses: github/codeql-action/analyze@v2
  with:
    queries: .github/codeql/queries
    category: "/codeql/custom"
```

### 4. Vulnerability Alerts

**Alert Workflow:**

```
1. Dependabot detects vulnerability (CVE)
2. Creates security advisory
3. Sends GitHub notification
4. Creates issue/PR with fix
5. Shows CVSS score and severity
```

**CVSS Severity Levels:**

```
CRITICAL (9.0-10.0) - Immediate action required
HIGH     (7.0-8.9)  - Apply patch soon
MEDIUM   (4.0-6.9)  - Plan to patch
LOW      (0.1-3.9)  - Review and plan
```

**Manage Alerts:**

```bash
# List vulnerabilities
gh api repos/owner/repo/dependabot/alerts

# Dismiss alert
gh api repos/owner/repo/dependabot/alerts/{alert_number} \
  -X PATCH \
  -f state=dismissed \
  -f dismissed_reason=tolerable_risk

# Reopen alert
gh api repos/owner/repo/dependabot/alerts/{alert_number} \
  -X PATCH \
  -f state=open
```

### 5. SARIF Reports

**Generate SARIF from Tools:**

```bash
# ESLint with SARIF
npx eslint . --format json --output-file eslint-results.json

# Convert to SARIF
npx @microsoft/sarif-multitool convert eslint-results.json --output-file results.sarif
```

**Upload SARIF to GitHub:**

```yaml
- name: Upload SARIF
  uses: github/codeql-action/upload-sarif@v2
  with:
    sarif_file: results.sarif
    wait-for-processing: true
```

**SARIF Format Example:**

```json
{
  "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
  "version": "2.1.0",
  "runs": [
    {
      "tool": {
        "driver": {
          "name": "SecurityScanner",
          "version": "1.0"
        }
      },
      "results": [
        {
          "ruleId": "SEC001",
          "message": {
            "text": "Potential SQL injection"
          },
          "level": "error",
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": {
                  "uri": "src/db.js"
                },
                "region": {
                  "startLine": 42,
                  "startColumn": 10
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### 6. Security Workflows

**Check Vulnerability Status:**

```yaml
name: Security Check

on: [pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check for vulnerabilities
        run: |
          npm audit --audit-level=moderate
          exit_code=$?
          if [ $exit_code -ne 0 ]; then
            echo "Security vulnerabilities found!"
            exit 1
          fi

      - name: Secret scanning
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.pull_request.base.sha }}
          head: HEAD
```

**Enforce Vulnerability Gates:**

```yaml
- name: Check dependencies
  run: |
    vulnerabilities=$(gh api repos/owner/repo/dependabot/alerts \
      --jq 'map(select(.state=="open")) | length')

    if [ "$vulnerabilities" -gt 0 ]; then
      echo "Found $vulnerabilities open vulnerabilities!"
      exit 1
    fi
```

---

## Configuration

### Complete Dependabot Configuration

`.github/dependabot.yml`:

```yaml
version: 2

updates:
  # NPM packages
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "03:00"
    open-pull-requests-limit: 10
    reviewers:
      - "security-team"
    assignees:
      - "automation"
    commit-message:
      prefix: "chore(deps)"
      include: "scope"
    labels:
      - "dependencies"
      - "npm"
    allow:
      - dependency-type: "all"
    versioning-strategy: "auto"

  # Python packages
  - package-ecosystem: "pip"
    directory: "/backend"
    schedule:
      interval: "weekly"
    reviewers:
      - "backend-team"

  # Docker images
  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"
    reviewers:
      - "devops-team"

  # GitHub Actions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

### CodeQL Configuration

`.github/codeql/codeql-config.yml`:

```yaml
name: "CodeQL Configuration"

disable-default-queries: false

# Enable additional queries
additional-queries:
  - uses: security-and-quality

# Query suites
queries:
  - uses: javascript/ql/src/qlpack.yml
    from: codeql-javascript

paths-ignore:
  - node_modules
  - dist
  - build
  - .git
  - tests

# Maximum time for analysis
query-filters:
  - exclude:
      kind: Metric
```

### Security Policy

Create `SECURITY.md`:

```markdown
# Security Policy

## Reporting Security Vulnerabilities

Please email security@company.com with:
- Description of vulnerability
- Steps to reproduce
- Potential impact

We will respond within 24 hours.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 2.x     | ✓ Yes     |
| 1.x     | ✓ Patches |
| 0.x     | ✗ No      |

## Security Process

1. Vulnerability reported
2. Assessment and acknowledgment (24h)
3. Fix development (varies)
4. Security advisory published
5. Patch released

## Automated Security Checks

- Dependabot checks dependencies daily
- CodeQL analysis on every push
- Secret scanning prevents credential leaks
- SAST scans for code vulnerabilities
```

---

## Examples

### Example 1: Comprehensive Security Workflow

`.github/workflows/security.yml`:

```yaml
name: Security Scanning

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM

permissions:
  contents: read
  security-events: write

jobs:
  codeql:
    name: CodeQL Analysis
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v2
        with:
          languages: javascript,python
          config-file: .github/codeql/codeql-config.yml

      - name: Autobuild
        uses: github/codeql-action/autobuild@v2

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v2
        with:
          category: "/linting"

  dependencies:
    name: Check Dependencies
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check npm audit
        run: npm audit --audit-level=moderate

      - name: Check pip vulnerabilities
        run: |
          pip install safety
          safety check --json

  secrets:
    name: Secret Scanning
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run Trivy
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload Trivy results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'

  license:
    name: License Compliance
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check licenses
        run: |
          npm install -g license-checker
          license-checker --json > licenses.json
          # Verify against approved licenses
```

### Example 2: Automated Patch Management

`scripts/apply-security-patches.sh`:

```bash
#!/bin/bash

# Apply critical security patches automatically

REPO=$1
BRANCH_BASE="security/patch"

# Get critical vulnerabilities
CRITICAL=$(gh api repos/"$REPO"/dependabot/alerts \
  --jq 'map(select(.severity=="critical")) | length')

if [ "$CRITICAL" -eq 0 ]; then
  echo "No critical vulnerabilities found"
  exit 0
fi

echo "Found $CRITICAL critical vulnerabilities"
echo "Creating patch branch..."

# Create branch for patches
BRANCH="$BRANCH_BASE-$(date +%s)"
git checkout -b "$BRANCH"

# Install and update
npm install
npm audit fix --force

# Commit changes
git add package*.json
git commit -m "chore(security): apply critical security patches"

# Create PR
gh pr create \
  --title "Security: Apply critical patches" \
  --body "Automatic security patch PR" \
  --label "security,critical" \
  --draft false

echo "Patch PR created: $BRANCH"
```

### Example 3: Vulnerability Report

`scripts/security-report.sh`:

```bash
#!/bin/bash

# Generate security report

REPO=$1

echo "=== Security Report for $REPO ==="
echo ""

# Dependabot alerts
echo "Vulnerability Summary:"
ALERTS=$(gh api repos/"$REPO"/dependabot/alerts)
CRITICAL=$(echo "$ALERTS" | jq 'map(select(.severity=="critical")) | length')
HIGH=$(echo "$ALERTS" | jq 'map(select(.severity=="high")) | length')
MEDIUM=$(echo "$ALERTS" | jq 'map(select(.severity=="medium")) | length')

echo "Critical: $CRITICAL"
echo "High: $HIGH"
echo "Medium: $MEDIUM"

echo ""
echo "Top Vulnerabilities:"
echo "$ALERTS" | jq -r '.[] |
  "\(.severity | ascii_upcase): \(.security_advisory.summary) (\(.security_advisory.cve_id))"' \
  | sort | uniq

echo ""
echo "Affected Packages:"
echo "$ALERTS" | jq -r '.[] |
  "\(.dependency.package.name): \(.dependency.manifest_path)"' \
  | sort | uniq

echo ""
echo "Last updated: $(date)"
```

### Example 4: CodeQL Custom Queries

`.github/codeql/custom-queries.ql`:

```ql
/**
 * Find hardcoded API keys
 */

import javascript

from StringLiteral str
where
  (
    str.getValue().matches("sk-[A-Za-z0-9]{20,}") or
    str.getValue().matches("api_key=.*") or
    str.getValue().matches("password=.*")
  )
  and not str.getFile().getRelativePath().matches(".*/test.*")
select str, "Potential hardcoded credential detected"
```

### Example 5: Enforce Security Gates

`.github/workflows/security-gate.yml`:

```yaml
name: Security Gate

on: [pull_request]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check for secrets
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.pull_request.base.sha }}
          head: HEAD

      - name: Verify dependencies
        run: npm audit --audit-level=moderate

      - name: Check for CVEs
        run: |
          npm install -g npm-check-updates
          ncu --doctor --doctorTest 'npm audit --audit-level=high'

      - name: Block if vulnerabilities
        if: failure()
        run: |
          echo "::error::Security vulnerabilities detected - PR cannot be merged"
          exit 1
```

---

## Best Practices

### 1. Configure Dependabot Proactively

```yaml
# Good: Regular updates prevent accumulation
schedule:
  interval: "weekly"

# Bad: Monthly updates = bigger jumps, more conflicts
schedule:
  interval: "monthly"
```

### 2. Review Security Alerts Quickly

```bash
# Set up notifications
# GitHub → Settings → Notifications →
# "Security alerts" → "Watch"
```

### 3. Separate Critical from Minor Updates

```yaml
# Use multiple configurations
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"  # Critical patches
    labels: ["security"]

  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "monthly"  # Minor/patch updates
    labels: ["dependencies"]
```

### 4. Implement Dismiss Policy

```bash
# Dismiss known acceptable risks
gh api repos/owner/repo/dependabot/alerts/{id} \
  -X PATCH \
  -f state=dismissed \
  -f dismissed_reason=tolerable_risk \
  -f dismissed_comment="Reviewed and accepted risk"
```

### 5. Track Security Metrics

```bash
# Create dashboard of open vulnerabilities
gh api repos/owner/repo/dependabot/alerts \
  --jq 'group_by(.severity) |
        map({severity: .[0].severity, count: length})'
```

---

## Integration with Other Skills

GitHub Security Scanning integrates with:

- **github-actions-workflows** - Run security checks in CI/CD
- **build-optimization** - Security gates in build pipeline
- **docker-compose-setup** - Scan container images
- **secrets-management** - Manage API keys securely
- **git-workflow-strategy** - Require security checks before merge

---

## Complete Command Reference

```bash
# Dependabot
gh api repos/:owner/:repo/dependabot/alerts
gh api repos/:owner/:repo/dependabot/alerts/{id}

# Secret scanning
gh secret-scanning list-alerts
gh secret-scanning list-locations {id}

# CodeQL
gh codeql database create
gh codeql database analyze

# Vulnerability
gh api repos/:owner/:repo/vulnerability-alerts
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
