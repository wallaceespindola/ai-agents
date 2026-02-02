# GitHub Actions YAML Skill

**Master GitHub Actions YAML syntax, custom actions, reusable workflows, expressions, and advanced configuration.**

## Overview

GitHub Actions YAML syntax defines workflow automation. This skill covers syntax, expressions, custom actions, and advanced patterns.

**What it does:**
- Implements GitHub Actions YAML syntax
- Creates custom composite actions
- Develops reusable workflows
- Manages workflow expressions and context
- Handles matrix strategies
- Implements conditional execution
- Manages job dependencies
- Creates comprehensive CI/CD workflows

**Perfect for:**
- CI/CD pipeline automation
- Custom workflow actions
- Reusable workflow libraries
- Complex automation logic
- Enterprise workflows

---

## When to Use This Skill

Use GitHub Actions YAML when you need to:

- **Define CI/CD workflows** in YAML
- **Create custom actions** for automation
- **Build reusable workflows** for your organization
- **Implement complex logic** in workflows
- **Share actions** across repositories
- **Manage workflow triggers** and conditions
- **Implement matrix builds** for testing
- **Reference secrets and variables** securely

---

## Quick Start (10 Minutes)

### 1. Create Workflow File

Create `.github/workflows/build.yml`:

```yaml
name: Build and Test

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm install
      - run: npm run build
      - run: npm test
```

### 2. Use Expressions

```yaml
env:
  BRANCH: ${{ github.ref_name }}
  SHA: ${{ github.sha }}
  ACTOR: ${{ github.actor }}

steps:
  - run: echo "Running on $BRANCH"
```

### 3. Matrix Strategy

```yaml
strategy:
  matrix:
    node: ['18', '20', '22']
    os: [ubuntu-latest, macos-latest]

steps:
  - uses: actions/setup-node@v4
    with:
      node-version: ${{ matrix.node }}
```

### 4. Create Custom Action

Create `.github/actions/my-action/action.yml`:

```yaml
name: My Custom Action
inputs:
  parameter:
    description: Input parameter
    required: true
outputs:
  result:
    description: Output result
    value: ${{ steps.step.outputs.value }}
runs:
  using: composite
  steps:
    - id: step
      run: echo "result"
      shell: bash
```

---

## How It Works

### 1. Workflow Syntax

**Basic Structure:**

```yaml
name: Workflow Name

on: [push, pull_request]  # Trigger events

env:
  GLOBAL_VAR: value

jobs:
  job_id:
    runs-on: ubuntu-latest
    outputs:
      output_id: ${{ steps.step_id.outputs.var }}
    steps:
      - id: step_id
        uses: action/name@v1
        with:
          parameter: value
        env:
          JOB_VAR: value
      - run: command
```

### 2. Trigger Events

**Event Types:**

```yaml
on:
  push:
    branches: [main, develop]
    paths: ['src/**', 'Dockerfile']
    tags: ['v*']

  pull_request:
    branches: [main]
    types: [opened, synchronize, reopened]

  schedule:
    - cron: '0 2 * * *'

  workflow_dispatch:
    inputs:
      environment:
        description: Environment
        required: true
        type: choice
        options: [dev, prod]

  workflow_run:
    workflows: [ci.yml]
    types: [completed]
    branches: [main]

  release:
    types: [published]

  repository_dispatch:
    types: [custom-event]
```

### 3. Expressions and Context

**GitHub Context Variables:**

```yaml
github:
  repository: owner/repo
  ref: refs/heads/main
  ref_name: main
  sha: abc123def456
  event_name: push
  actor: username
  event: {}              # Full event payload
  workflow: build.yml
  job: build
  action: run
  event_path: /github/workflow/event.json
  server_url: https://github.com
  api_url: https://api.github.com
```

**Expression Functions:**

```yaml
steps:
  - run: echo ${{ contains('hello', 'ell') }}     # true
  - run: echo ${{ startsWith('hello', 'he') }}    # true
  - run: echo ${{ endsWith('hello', 'lo') }}      # true
  - run: echo ${{ format('{0} {1}', 'Hello', 'World') }}
  - run: echo ${{ toJson(matrix) }}               # JSON stringify
  - run: echo ${{ fromJson('{"key":"value"}') }}  # Parse JSON
  - run: echo ${{ hashFiles('**/package-lock.json') }}
  - run: echo ${{ success() }}                    # Job status
  - run: echo ${{ failure() }}
  - run: echo ${{ always() }}
```

**Conditionals:**

```yaml
if: github.event_name == 'push'
if: startsWith(github.ref, 'refs/tags/')
if: contains(github.event.head_commit.message, '[skip ci]')
if: github.actor != 'dependabot[bot]'
if: success()
if: failure()
if: always()
if: cancelled()
```

### 4. Variables and Secrets

**Environment Variables:**

```yaml
env:
  GLOBAL_VAR: global_value

jobs:
  job:
    env:
      JOB_VAR: job_value
    steps:
      - env:
          STEP_VAR: step_value
        run: echo $GLOBAL_VAR $JOB_VAR $STEP_VAR
```

**Secrets:**

```yaml
steps:
  - run: npm publish
    env:
      NPM_TOKEN: ${{ secrets.NPM_TOKEN }}

# Set in GitHub UI: Settings → Secrets and variables → Actions
# Or via GitHub CLI:
# gh secret set NPM_TOKEN --body "token_value"
```

**GitHub Token:**

```yaml
- uses: actions/checkout@v4
  with:
    token: ${{ secrets.GITHUB_TOKEN }}

# Or environment variable
env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 5. Matrix Strategy

**Basic Matrix:**

```yaml
strategy:
  matrix:
    node: ['16', '18', '20']
    os: [ubuntu-latest, macos-latest, windows-latest]
```

**Include/Exclude:**

```yaml
strategy:
  matrix:
    node: ['16', '18', '20']
    os: [ubuntu-latest, macos-latest]
    exclude:
      - os: macos-latest
        node: '16'
    include:
      - os: ubuntu-latest
        node: '20'
        experimental: true
```

**Dynamic Matrix:**

```yaml
strategy:
  matrix:
    include:
      - name: Build Linux
        os: ubuntu-latest
        artifact: app-linux
      - name: Build macOS
        os: macos-latest
        artifact: app-macos
      - name: Build Windows
        os: windows-latest
        artifact: app.exe
```

### 6. Custom Composite Action

**Composite Action (`action.yml`):**

```yaml
name: Build Application
description: Build and test application
inputs:
  node-version:
    description: Node version
    required: true
    default: '20'
  cache-key:
    description: Cache key
    required: false
outputs:
  test-results:
    description: Test results path
    value: ${{ steps.test.outputs.results }}
runs:
  using: composite
  steps:
    - uses: actions/checkout@v4

    - uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.node-version }}
        cache: 'npm'

    - id: build
      run: npm run build
      shell: bash

    - id: test
      run: |
        npm test
        echo "results=coverage/index.html" >> $GITHUB_OUTPUT
      shell: bash

    - if: failure()
      run: echo "Build failed"
      shell: bash
```

**Use Custom Action:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: ./.github/actions/build-application
        with:
          node-version: '20'
          cache-key: 'npm-cache'

      - uses: actions/upload-artifact@v4
        with:
          path: ${{ steps.build.outputs.test-results }}
```

### 7. Reusable Workflows

**Define Reusable Workflow:**

```yaml
# .github/workflows/test-reusable.yml
name: Reusable Test Workflow

on:
  workflow_call:
    inputs:
      node-version:
        description: Node version
        type: string
        required: true
        default: '20'
    outputs:
      coverage:
        description: Test coverage percentage
        value: ${{ jobs.test.outputs.coverage }}
    secrets:
      npm-token:
        required: false

jobs:
  test:
    runs-on: ubuntu-latest
    outputs:
      coverage: ${{ steps.coverage.outputs.percent }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
      - run: npm test -- --coverage
      - id: coverage
        run: echo "percent=$(cat coverage.txt)" >> $GITHUB_OUTPUT
```

**Call Reusable Workflow:**

```yaml
# .github/workflows/ci.yml
on: [push, pull_request]

jobs:
  test:
    uses: ./.github/workflows/test-reusable.yml
    with:
      node-version: '20'
    secrets:
      npm-token: ${{ secrets.NPM_TOKEN }}
```

### 8. Job Dependencies

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      artifact: ${{ steps.build.outputs.name }}

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "Artifact: ${{ needs.build.outputs.artifact }}"

  deploy:
    needs: [build, test]  # Depends on both
    runs-on: ubuntu-latest
    if: success()
```

### 9. Permissions

```yaml
permissions:
  contents: read
  pull-requests: write
  checks: write
  statuses: write
  packages: write

jobs:
  job:
    permissions:
      contents: write  # Override job permission
    steps:
      - run: git config --global user.email "bot@example.com"
```

### 10. Timeout and Concurrency

```yaml
jobs:
  job:
    runs-on: ubuntu-latest
    timeout-minutes: 30

    steps:
      - run: ./long-running-task.sh
        timeout-minutes: 10

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

---

## Configuration

### Complete CI/CD Workflow

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

permissions:
  contents: read
  packages: write

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm install
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: ['18', '20', '22']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
          cache: 'npm'
      - run: npm install
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v3

  build:
    needs: [lint, test]
    runs-on: ubuntu-latest
    permissions:
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v2
      - uses: docker/login-action@v2
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v4
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
```

---

## Examples

### Example 1: Matrix Build

```yaml
jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python: ['3.9', '3.10', '3.11']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python }}
      - run: python -m pytest
```

### Example 2: Conditional Steps

```yaml
steps:
  - if: github.event_name == 'push'
    run: echo "Push event"

  - if: github.event_name == 'pull_request'
    run: echo "PR event"

  - if: success()
    run: echo "Previous step succeeded"

  - if: failure()
    run: echo "Previous step failed"

  - if: always()
    run: echo "Always run"
```

### Example 3: Artifact Handling

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: build
          path: dist/

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build
      - run: npm test
```

### Example 4: Release Workflow

```yaml
name: Release

on:
  push:
    tags: ['v*']

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4

      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          body_path: CHANGELOG.md
          files: dist/**

      - run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

### Example 5: Dynamic Variables

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - id: vars
        run: |
          echo "branch=${GITHUB_REF#refs/heads/}" >> $GITHUB_OUTPUT
          echo "sha_short=$(git rev-parse --short HEAD)" >> $GITHUB_OUTPUT
          echo "version=$(cat VERSION)" >> $GITHUB_OUTPUT

      - run: echo "Branch: ${{ steps.vars.outputs.branch }}"
      - run: echo "SHA: ${{ steps.vars.outputs.sha_short }}"
      - run: echo "Version: ${{ steps.vars.outputs.version }}"
```

---

## Best Practices

### 1. Pin Action Versions

```yaml
# Good: Use specific commit
uses: actions/setup-node@abc123def456

# Also good: Use release tag
uses: actions/setup-node@v4

# Bad: Use floating version
uses: actions/setup-node@v4.0  # Insecure
```

### 2. Use Cache

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'

# Or manual
- uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-
```

### 3. Set Concurrency Limits

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

### 4. Handle Secrets Securely

```yaml
# Good: Use secrets
env:
  TOKEN: ${{ secrets.TOKEN }}

# Never hardcode
# env:
#   TOKEN: abc123
```

### 5. Use Permissions Principle

```yaml
permissions:
  contents: read
  packages: write
  # Explicitly grant needed permissions
```

---

## Integration with Other Skills

GitHub Actions YAML integrates with:

- **github-actions-workflows** - Complete workflow design
- **github-pr-management** - PR-related actions
- **git-workflow-strategy** - Branch protection integration
- **yaml-validation-config** - Validate workflow syntax

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
