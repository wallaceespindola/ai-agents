# Pre-Commit Hooks Setup Skill

**Master pre-commit framework, hook chaining, custom hooks, linting integration, and automated code quality checks.**

## Overview

Pre-commit hooks automate code quality checks before committing. This skill covers framework setup, hook configuration, and integration.

**What it does:**
- Configures pre-commit framework
- Chains multiple linting tools
- Implements custom hooks
- Enforces code standards locally
- Prevents common mistakes
- Integrates with CI/CD
- Manages hook updates
- Documents team standards

**Perfect for:**
- Enforcing code quality
- Preventing bad commits
- Automating formatting
- Testing before commit
- Team standardization

---

## When to Use This Skill

Use Pre-Commit Hooks when you need to:

- **Prevent bad code** from being committed
- **Enforce formatting** standards
- **Run tests** before commit
- **Detect secrets** in code
- **Validate YAML/JSON** files
- **Lint code** automatically
- **Format code** before commit
- **Block commits** that don't meet standards

---

## Quick Start (10 Minutes)

### 1. Install pre-commit

```bash
# macOS
brew install pre-commit

# Linux/Windows
pip install pre-commit

# Verify
pre-commit --version
```

### 2. Create Configuration

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.13
    hooks:
      - id: ruff
```

### 3. Install Hooks

```bash
pre-commit install
# Creates .git/hooks/pre-commit
```

### 4. Run Manually

```bash
# Test on all files
pre-commit run --all-files

# Test on staged files
pre-commit run
```

### 5. Bypass if Needed

```bash
git commit --no-verify  # Skip hooks (use carefully)
```

---

## How It Works

### 1. Pre-Commit Framework

**Hook Execution:**

```
1. You run: git commit
2. Pre-commit framework runs
3. Each hook processes files
4. If any fail, commit is blocked
5. Fix issues and retry
6. Commit succeeds
```

**File Processing:**

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace  # Remove trailing whitespace
      - id: end-of-file-fixer    # Add newline at EOF
      - id: check-yaml           # Validate YAML syntax
      - id: detect-private-key   # Detect private keys
```

### 2. Configuration Structure

**Full Configuration:**

```yaml
# .pre-commit-config.yaml

default_language_version:
  python: python3.11
  ruby: '3.2'
  node: '20'

default_stages: [commit, push, manual]

repos:
  # External repository with hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
        stages: [commit]
      - id: check-yaml
        args: ['--unsafe']
      - id: check-json

  # Python linting
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        language_version: python3.11

  # Node.js linting
  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v8.56.0
    hooks:
      - id: eslint
        files: \.(js|ts|jsx|tsx)$
        types: [javascript]

  # Custom local hook
  - repo: local
    hooks:
      - id: custom-check
        name: Custom Check
        entry: bash scripts/check.sh
        language: script
        stages: [commit]
```

### 3. Hook Types

**Language-Specific Hooks:**

```yaml
# Python
- repo: https://github.com/psf/black
  hooks:
    - id: black

# JavaScript/TypeScript
- repo: https://github.com/pre-commit/mirrors-eslint
  hooks:
    - id: eslint

# Go
- repo: https://github.com/pre-commit/mirrors-gofmt
  hooks:
    - id: gofmt
```

**Utility Hooks:**

```yaml
# File operations
- id: trailing-whitespace
- id: end-of-file-fixer
- id: mixed-line-ending

# Syntax validation
- id: check-yaml
- id: check-json
- id: check-xml
- id: check-toml

# Security
- id: detect-private-key
- id: detect-aws-credentials

# Git
- id: check-merge-conflict
- id: check-case-conflict
```

### 4. Custom Hooks

**Local Hook Script:**

```bash
#!/bin/bash
# scripts/check-secrets.sh

# Custom hook to detect secrets
if grep -r "password\|secret\|api.key" . --exclude-dir=.git; then
  echo "Possible secrets detected!"
  exit 1
fi
```

**Configure Local Hook:**

```yaml
repos:
  - repo: local
    hooks:
      - id: check-secrets
        name: Check for Secrets
        entry: bash scripts/check-secrets.sh
        language: script
        stages: [commit]
        files: ''  # Run on all files

      - id: mypy
        name: Type Check
        entry: mypy
        language: system
        types: [python]
        require_serial: true

      - id: pytest
        name: Run Tests
        entry: pytest
        language: system
        types: [python]
        stages: [push]  # Only on push
        pass_filenames: false
```

### 5. Stages

**Hook Stages:**

```yaml
stages:
  - commit    # Default, runs on git commit
  - push      # Runs before git push
  - merge-commit
  - manual    # Must run explicitly
```

**Configured Per Hook:**

```yaml
hooks:
  - id: black
    stages: [commit]    # Run on commit

  - id: pytest
    stages: [push]      # Run on push only

  - id: custom-check
    stages: [manual]    # Run with: pre-commit run --hook-stage=manual
```

### 6. Configuration Options

**Hook-Level Options:**

```yaml
hooks:
  - id: eslint
    args: ['--max-warnings=0']           # Additional arguments
    exclude: ^(src/vendor|dist/)         # Exclude files
    exclude_types: [json]                # Exclude file types
    files: \.(js|ts)$                    # Only these files
    types: [javascript]                  # File types
    additional_dependencies: [prettier]  # Extra packages
    stages: [commit]                     # Execution stage
    pass_filenames: true                 # Pass files as args
    always_run: false                    # Run even if no files match
    language_version: node20             # Version
    require_serial: false                # Don't parallelize
```

### 7. Updating Hooks

**Check for Updates:**

```bash
pre-commit autoupdate
# Updates .pre-commit-config.yaml with latest versions
```

**Run Specific Hook:**

```bash
pre-commit run black --all-files
pre-commit run --hook-stage manual
```

### 8. Team Enforcement

**Install in CI/CD:**

```yaml
# .github/workflows/pre-commit.yml
name: Pre-Commit

on: [push, pull_request]

jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
      - uses: pre-commit/action@v3.0.0
```

**Skip in CI (if needed):**

```bash
# Only run on push, not on CI
SKIP=tests,long-running-check pre-commit run --all-files
```

---

## Configuration

### Complete Pre-Commit Setup

`.pre-commit-config.yaml`:

```yaml
default_language_version:
  python: python3.11
  node: '20'

default_stages: [commit]

repos:
  # File fixes
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-merge-conflict
      - id: detect-private-key

  # Python formatting
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        language_version: python3.11

  # Python linting
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.13
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  # Python type checking
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--strict]

  # JavaScript/TypeScript
  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v8.56.0
    hooks:
      - id: eslint
        files: \.(js|ts|jsx|tsx)$
        types: [javascript]
        additional_dependencies: [eslint, prettier, eslint-config-prettier]

  # YAML validation
  - repo: https://github.com/adrienverge/yamllint
    rev: v1.33.0
    hooks:
      - id: yamllint
        args: [-c, .yamllint]

  # Secrets detection
  - repo: https://github.com/zricethezav/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
        stages: [commit]

  # Local custom hooks
  - repo: local
    hooks:
      - id: tests
        name: Run Tests
        entry: pytest
        language: system
        types: [python]
        stages: [push]
        pass_filenames: false
```

---

## Examples

### Example 1: Basic Setup

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
```

### Example 2: JavaScript Project

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-json

  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v8.56.0
    hooks:
      - id: eslint
        args: [--fix]
        types: [javascript]

  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.1.1
    hooks:
      - id: prettier
        types_or: [javascript, json, yaml]
```

### Example 3: Python Project

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: check-yaml
      - id: detect-private-key

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.13
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
```

### Example 4: Custom Hooks

```yaml
repos:
  - repo: local
    hooks:
      - id: format-code
        name: Format Code
        entry: prettier --write
        language: node
        types: [javascript, json]
        stages: [commit]

      - id: lint-commit-msg
        name: Lint Commit Message
        entry: bash scripts/validate-commit-msg.sh
        language: script
        stages: [commit-msg]

      - id: unit-tests
        name: Unit Tests
        entry: npm test
        language: system
        pass_filenames: false
        stages: [push]
```

### Example 5: Staged Rollout

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
        stages: [commit]

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        stages: [commit]

  - repo: local
    hooks:
      - id: tests
        name: Unit Tests
        entry: pytest
        language: system
        stages: [push]
        pass_filenames: false
        always_run: true
```

---

## Best Practices

### 1. Keep Hooks Fast

```yaml
# Bad: Long-running tests
- id: all-tests
  entry: pytest
  stages: [commit]

# Good: Fast linting on commit, tests on push
- id: lint
  entry: black
  stages: [commit]

- id: tests
  entry: pytest
  stages: [push]
```

### 2. Exclude Generated Files

```yaml
hooks:
  - id: black
    exclude: ^(migrations|generated|vendor)
```

### 3. Version Hooks

```yaml
# Good: Specific version
rev: v4.5.0

# Bad: Floating (unpredictable)
rev: main
```

### 4. Allow Bypass for Hotfixes

```bash
# When necessary (use sparingly)
git commit --no-verify
```

### 5. Update Regularly

```bash
# Check for updates
pre-commit autoupdate

# Commit updated config
git add .pre-commit-config.yaml
git commit -m "chore: update pre-commit hooks"
```

---

## Integration with Other Skills

Pre-Commit Hooks integrates with:

- **github-actions-workflows** - Run in CI/CD
- **git-commit-strategy** - Validate commit messages
- **build-optimization** - Run fast checks before slow builds
- **yaml-validation-config** - Validate YAML files
- **secrets-management** - Detect secret leaks

---

## Complete Command Reference

```bash
# Installation
pre-commit install
pre-commit install --hook-type pre-push
pre-commit uninstall

# Running
pre-commit run                    # Staged files
pre-commit run --all-files        # All files
pre-commit run black --all-files  # Specific hook
pre-commit run --hook-stage push  # Push stage

# Maintenance
pre-commit autoupdate             # Update versions
pre-commit clean                  # Clean cache
pre-commit validate-config        # Validate config
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
