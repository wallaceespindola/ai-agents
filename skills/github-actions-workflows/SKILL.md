# GitHub Actions Workflows Skill

**Design, build, and deploy with GitHub Actions CI/CD pipelines. Master workflow triggers, secrets management, matrix builds, custom actions, and reusable workflows.**

## Overview

GitHub Actions enables automated testing, building, and deployment directly from your GitHub repository. This skill covers professional-grade workflow design for production environments.

**What it does:**
- Designs event-driven workflows (push, pull_request, schedule, manual)
- Implements matrix strategies for multi-version testing
- Manages secrets, environment variables, and configuration
- Creates reusable workflows for code reuse
- Develops custom composite and JavaScript actions
- Integrates with external services (Docker, AWS, Slack)
- Optimizes workflow performance and caching
- Implements status checks and deployment protection

**Perfect for:**
- Automated testing and code quality checks
- Building and publishing Docker images
- Multi-platform builds (Linux, macOS, Windows)
- Scheduled maintenance tasks
- Deployment pipelines
- Release automation

---

## When to Use This Skill

Use GitHub Actions Workflows when you need to:

- **Automate testing** on every push and pull request
- **Build Docker images** and push to registries
- **Deploy applications** to cloud providers
- **Run jobs across multiple OS/runtime versions** (Node 18, 20, 22)
- **Publish packages** to npm, PyPI, or Maven Central
- **Generate reports** and upload artifacts
- **Enforce code quality** standards
- **Release software** with automated versioning and changelog
- **Schedule periodic tasks** (weekly backups, dependency updates)

**Not for this skill:**
- Complex business logic (use your application code instead)
- Sensitive secrets management without proper vaulting
- Long-running jobs (15+ minutes should be optimized or split)

---

## Quick Start (10 Minutes)

### 1. Create Basic Workflow

Create `.github/workflows/test.yml`:

```yaml
name: Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm install
      - run: npm test
```

### 2. Add Secret

GitHub UI → Settings → Secrets and variables → Actions → New repository secret

Or via GitHub CLI:
```bash
gh secret set DOCKER_PASSWORD --body "mypassword"
```

### 3. Add Matrix Strategy

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest]
        node: ['18', '20', '22']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm test
```

### 4. Create Reusable Workflow

Create `.github/workflows/test-reusable.yml`:

```yaml
name: Reusable Test

on:
  workflow_call:
    inputs:
      node-version:
        required: true
        type: string

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
      - run: npm test
```

Call from another workflow:

```yaml
uses: ./.github/workflows/test-reusable.yml
with:
  node-version: '20'
```

---

## How It Works

### 1. Workflow Events and Triggers

GitHub Actions workflows respond to repository events:

**Push/Pull Request Triggers:**
```yaml
on:
  push:
    branches: [main, develop]
    paths: ['src/**', 'package.json']
    tags: ['v*']
  pull_request:
    branches: [main]
  workflow_dispatch:  # Manual trigger
```

**Scheduled Triggers:**
```yaml
on:
  schedule:
    - cron: '0 2 * * MON'  # Mondays at 2 AM UTC
  workflow_run:
    workflows: [build]
    types: [completed]
```

### 2. Jobs and Steps Execution

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.version.outputs.tag }}
    steps:
      - id: version
        run: echo "tag=$(git describe --tags)" >> $GITHUB_OUTPUT

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: echo "Deploying ${{ needs.build.outputs.version }}"
```

Job properties:
- `runs-on`: Runner environment (ubuntu-latest, macos-latest, windows-latest)
- `needs`: Job dependencies (run sequentially)
- `outputs`: Share data between jobs
- `environment`: Protection rules and secrets

### 3. Matrix Strategy

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    node: ['18', '20', '22']
    exclude:
      - os: macos-latest
        node: '18'
    include:
      - os: ubuntu-latest
        node: '20'
        experimental: true
```

Matrix features:
- Creates job for each combination
- `exclude`: Skip specific combinations
- `include`: Add custom combinations
- `fail-fast`: Cancel other jobs on failure (default: true)

### 4. Secrets and Environment Variables

**Using Secrets:**
```yaml
steps:
  - run: npm publish
    env:
      NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```

**Environment Variables:**
```yaml
env:
  NODE_ENV: production

jobs:
  build:
    env:
      LOG_LEVEL: debug
    steps:
      - run: echo $NODE_ENV $LOG_LEVEL
```

**Repository Secrets vs Environment Secrets:**
```yaml
# Available to all workflows
env:
  GLOBAL_VAR: ${{ secrets.GLOBAL_SECRET }}

jobs:
  deploy:
    environment: production
    steps:
      # Available only in production environment
      - run: aws s3 sync
        env:
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

### 5. Reusable Workflows

**Define reusable workflow** `.github/workflows/test.yml`:

```yaml
on:
  workflow_call:
    inputs:
      coverage-threshold:
        required: false
        type: number
        default: 80
    outputs:
      coverage:
        value: ${{ jobs.test.outputs.coverage }}
    secrets:
      CODECOV_TOKEN:
        required: true

jobs:
  test:
    runs-on: ubuntu-latest
    outputs:
      coverage: ${{ steps.coverage.outputs.percent }}
    steps:
      - uses: actions/checkout@v4
      - run: npm test -- --coverage
      - id: coverage
        run: echo "percent=85" >> $GITHUB_OUTPUT
      - uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
```

**Call reusable workflow:**

```yaml
jobs:
  test:
    uses: ./.github/workflows/test.yml
    with:
      coverage-threshold: 85
    secrets:
      CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}
```

### 6. Custom Actions

**JavaScript Action** `.github/actions/hello/action.yml`:

```yaml
name: 'Hello World'
description: 'Greet someone'
inputs:
  who-to-greet:
    description: 'Who to greet'
    required: true
    default: 'World'
outputs:
  time:
    description: 'The time'
    value: ${{ steps.hello.outputs.time }}
runs:
  using: 'node20'
  main: 'dist/index.js'
```

`.github/actions/hello/index.js`:

```javascript
const core = require('@actions/core');
const github = require('@actions/github');

try {
  const nameToGreet = core.getInput('who-to-greet');
  console.log(`Hello ${nameToGreet}!`);

  const time = new Date().toTimeString();
  core.setOutput('time', time);
} catch (error) {
  core.setFailed(error.message);
}
```

**Composite Action** `.github/actions/setup-tools/action.yml`:

```yaml
name: 'Setup Tools'
description: 'Setup build tools'
runs:
  using: 'composite'
  steps:
    - run: echo "Installing tools..."
      shell: bash
    - run: npm install -g eslint prettier
      shell: bash
```

### 7. Conditional Execution

```yaml
steps:
  - if: github.event_name == 'push'
    run: echo "Push event"

  - if: success()
    run: echo "Previous step succeeded"

  - if: failure()
    run: echo "Previous step failed"

  - if: startsWith(github.ref, 'refs/tags/')
    run: echo "Tag push"

  - if: contains(github.event.head_commit.message, '[skip ci]')
    run: echo "Skipping CI"
```

### 8. Context and Expressions

```yaml
steps:
  - run: |
      echo "Actor: ${{ github.actor }}"
      echo "Repository: ${{ github.repository }}"
      echo "Branch: ${{ github.ref_name }}"
      echo "Commit: ${{ github.sha }}"
      echo "Event: ${{ github.event_name }}"

  - if: github.event_name == 'pull_request'
    run: |
      echo "PR Number: ${{ github.event.pull_request.number }}"
      echo "PR Title: ${{ github.event.pull_request.title }}"
```

---

## Configuration

### Basic Workflow Template

`.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    needs: lint
    strategy:
      matrix:
        node: ['18', '20', '22']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
          cache: 'npm'

      - run: npm ci
      - run: npm test -- --coverage

      - uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
```

### Docker Build and Push

`.github/workflows/docker.yml`:

```yaml
name: Docker Build

on:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4

      - uses: docker/setup-buildx-action@v3

      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - uses: docker/metadata-action@v5
        id: meta
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=ref,event=branch
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}

      - uses: docker/build-push-action@v5
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=registry,ref=ghcr.io/${{ github.repository }}:buildcache
          cache-to: type=registry,ref=ghcr.io/${{ github.repository }}:buildcache,mode=max
```

### Deployment Workflow

`.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    tags: ['v*']

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to production
        run: |
          aws s3 sync build/ s3://${{ secrets.AWS_BUCKET }} --delete
          aws cloudfront create-invalidation --distribution-id ${{ secrets.CLOUDFRONT_ID }} --paths "/*"
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_REGION: us-east-1

      - name: Notify Slack
        if: always()
        uses: slackapi/slack-github-action@v1.27
        with:
          webhook-url: ${{ secrets.SLACK_WEBHOOK }}
          payload: |
            {
              "text": "Deployment ${{ job.status }}",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Deployment Status:* ${{ job.status }}\n*Tag:* ${{ github.ref_name }}"
                  }
                }
              ]
            }
```

---

## Examples

### Example 1: Multi-Language Matrix Build

```yaml
name: Multi-Platform Build

on: [push, pull_request]

jobs:
  build:
    runs-on: ${{ matrix.runner }}
    strategy:
      matrix:
        include:
          - runner: ubuntu-latest
            lang: python
            version: '3.11'
          - runner: ubuntu-latest
            lang: node
            version: '20'
          - runner: macos-latest
            lang: rust
            version: stable
          - runner: windows-latest
            lang: java
            version: '21'
    steps:
      - uses: actions/checkout@v4

      - name: Setup ${{ matrix.lang }}
        run: |
          case "${{ matrix.lang }}" in
            python)
              python -m pip install --upgrade pip
              pip install -r requirements.txt
              ;;
            node)
              npm install
              ;;
            rust)
              rustup toolchain install ${{ matrix.version }}
              ;;
            java)
              # Java already installed on runner
              ;;
          esac
        shell: bash

      - name: Build
        run: make build

      - name: Test
        run: make test
```

### Example 2: Conditional Deployment

```yaml
name: Smart Deploy

on:
  push:
    branches: [main, develop]
    tags: ['v*']

jobs:
  determine-environment:
    runs-on: ubuntu-latest
    outputs:
      environment: ${{ steps.env.outputs.name }}
    steps:
      - id: env
        run: |
          if [[ "${{ github.ref }}" == refs/tags/* ]]; then
            echo "name=production" >> $GITHUB_OUTPUT
          elif [[ "${{ github.ref }}" == "refs/heads/main" ]]; then
            echo "name=staging" >> $GITHUB_OUTPUT
          else
            echo "name=development" >> $GITHUB_OUTPUT
          fi

  deploy:
    needs: determine-environment
    runs-on: ubuntu-latest
    environment: ${{ needs.determine-environment.outputs.environment }}
    steps:
      - uses: actions/checkout@v4
      - run: echo "Deploying to ${{ needs.determine-environment.outputs.environment }}"
      - run: bash scripts/deploy.sh ${{ needs.determine-environment.outputs.environment }}
```

### Example 3: Cache and Performance

```yaml
name: Optimized Build

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'
          cache: true

      # Cache Docker layers
      - uses: docker/setup-buildx-action@v3

      - name: Build with caching
        run: npm ci && npm run build

      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build-${{ runner.os }}
          path: dist/
          retention-days: 5

      - name: Download all artifacts
        if: always()
        uses: actions/download-artifact@v4
```

### Example 4: Release Automation

```yaml
name: Release

on:
  push:
    tags: ['v*']

permissions:
  contents: write
  packages: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          registry-url: 'https://registry.npmjs.org'

      - run: npm ci
      - run: npm run build
      - run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}

      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          body_path: CHANGELOG.md
          draft: false
          prerelease: ${{ contains(github.ref, '-alpha') || contains(github.ref, '-beta') }}
          files: dist/**
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Example 5: Code Quality Gates

```yaml
name: Quality Gates

on:
  pull_request:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci

      - name: Lint
        run: npm run lint

      - name: Type Check
        run: npm run typecheck

      - name: Test with Coverage
        run: npm test -- --coverage

      - name: SonarCloud Scan
        uses: SonarSource/sonarcloud-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}

      - name: Check Coverage
        run: |
          coverage=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
          if (( $(echo "$coverage < 80" | bc -l) )); then
            echo "Coverage below threshold: $coverage%"
            exit 1
          fi
```

### Example 6: Scheduled Maintenance

```yaml
name: Scheduled Tasks

on:
  schedule:
    - cron: '0 2 * * MON'  # Monday 2 AM UTC
    - cron: '0 4 1 * *'    # First day of month 4 AM UTC

jobs:
  update-dependencies:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm update
      - run: npm audit fix || true

      - uses: peter-evans/create-pull-request@v6
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: 'chore: update dependencies'
          title: 'chore: update dependencies'
          branch: dependencies/scheduled-update
          delete-branch: true
          labels: dependencies

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Trivy security scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: 'trivy-results.sarif'
```

---

## Best Practices

### 1. Minimize Build Time

```yaml
# Good: Use caching
- uses: actions/setup-node@v4
  with:
    cache: 'npm'

# Good: Use shallow checkout for faster clone
- uses: actions/checkout@v4
  with:
    fetch-depth: 1

# Good: Cancel redundant runs
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

### 2. Secure Secret Management

```yaml
# Good: Use environment-specific secrets
jobs:
  deploy:
    environment: production
    steps:
      - run: deploy.sh
        env:
          API_KEY: ${{ secrets.PROD_API_KEY }}

# Bad: Checking secrets in git
# secrets.env  # Don't commit!

# Good: Rotate secrets regularly
# Store in GitHub Secrets, not in code
```

### 3. Fail Fast and Provide Feedback

```yaml
# Good: Fail fast on critical steps
- name: Type Check
  run: npm run typecheck

# Good: Provide clear error messages
- name: Build
  run: npm run build || { echo "Build failed"; exit 1; }

# Good: Report to channels
- uses: slackapi/slack-github-action@v1
  if: failure()
  with:
    webhook-url: ${{ secrets.SLACK_WEBHOOK }}
```

### 4. Use Permissions Principle of Least Privilege

```yaml
permissions:
  contents: read
  pull-requests: write
  checks: write

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
```

### 5. Document Workflow Intent

```yaml
# Good: Clear names and descriptions
name: CI/CD Pipeline - Test, Build, Deploy
description: Complete CI/CD workflow with quality gates

# Good: Comments explaining complex logic
steps:
  # Use matrix strategy to test across Node versions
  - run: npm test

# Good: Environment documentation
env:
  # Timeout in seconds (default 360)
  NODE_OPTIONS: --max-old-space-size=4096
```

---

## Integration with Other Skills

GitHub Actions Workflows integrates with:

- **git-commit-strategy** - Trigger workflows on conventional commits
- **github-pr-management** - Auto-merge with passing checks
- **git-workflow-strategy** - Enforce branch protection with status checks
- **docker-compose-setup** - Build and push container images
- **kubernetes-yaml-generation** - Deploy to K8s clusters
- **secrets-management** - Store API keys and credentials
- **build-optimization** - Optimize Maven/Gradle/npm builds
- **github-security-scanning** - Run CodeQL and Dependabot

---

## Complete Command Reference

```bash
# Validate workflow syntax
gh workflow view .github/workflows/ci.yml

# List all workflows
gh workflow list

# Run workflow manually
gh workflow run ci.yml

# View recent runs
gh run list

# View run details
gh run view <RUN_ID>

# Download artifacts
gh run download <RUN_ID> --dir ./artifacts

# Cancel run
gh run cancel <RUN_ID>

# View logs
gh run view <RUN_ID> --log

# Create secret
gh secret set SECRET_NAME --body "secret_value"

# List secrets
gh secret list

# View workflow runs with details
gh run list --workflow ci.yml --json status,conclusion,name
```

---

## Troubleshooting

### Problem: Workflow not triggering

**Solution:**
- Check branch is in `on.push.branches` or `on.pull_request.branches`
- Verify workflow file is in `.github/workflows/` with `.yml` extension
- Check branch protection rules aren't blocking
- Review GitHub Actions logs for syntax errors

### Problem: Secret not available in step

**Solution:**
- Verify secret name is correct (case-sensitive)
- Ensure secret is in repository settings
- For environment secrets, job must specify `environment`

### Problem: Matrix build too slow

**Solution:**
- Use `fail-fast: false` only when needed
- Split into separate workflows
- Use `exclude` to skip unnecessary combinations

### Problem: Docker build layer caching not working

**Solution:**
- Use `docker/setup-buildx-action@v3`
- Enable cache with `cache-from` and `cache-to` in build-push-action
- Ensure Dockerfile has efficient layer caching

---

## File Organization

Standard GitHub Actions directory structure:

```
.github/
├── workflows/
│   ├── ci.yml              # Main CI workflow
│   ├── deploy.yml          # Deployment workflow
│   ├── docker.yml          # Docker build
│   ├── release.yml         # Release automation
│   └── scheduled.yml       # Scheduled tasks
├── actions/
│   ├── setup-tools/
│   │   └── action.yml
│   └── custom-build/
│       ├── action.yml
│       └── index.js
└── CODEOWNERS
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
