---
name: test-quality
description: Testing, linting, and code quality standards for all projects. Use when running tests, fixing linting errors, or ensuring code quality before commits.
user-invocable: true
allowed-tools: Bash(make *), Bash(pytest *), Bash(npm *), Bash(mvn *), Read, Grep
---

# Testing & Code Quality Standards

Run tests and verify code quality before commits.

## Quick Reference by Project

| Project | Test Command | Coverage | Lint | Format |
|---------|-------------|----------|------|--------|
| **hiddenbeer** | `make test` | `make test-cov` | `make lint` | `make format` |
| **skipy** | `make test` | `make test-api` | `make lint` | Prettier |
| **fake-data-springboot** | `make test` | Maven | Maven | - |
| **flashcards-app** | `pytest` | `pytest --cov` | `flake8` | `black` |
| **PythonRuns** | `make test` | `make test-coverage` | pytest | `black`/`isort` |

## Python Projects (hiddenbeer, skipy, flashcards-app, PythonRuns)

### Testing with pytest
```bash
# Run all tests
make test                    # or pytest

# Run specific test file
pytest tests/test_auth.py

# Run with coverage
make test-cov                # or pytest --cov

# Run verbose
pytest -v

# Run only failed tests
pytest --lf
```

### Code Quality Tools

1. **black** - Code formatter (opinionated, no config needed)
   ```bash
   black .                   # Format all Python files
   black --check .           # Check without modifying
   ```

2. **isort** - Import sorting
   ```bash
   isort .                   # Sort imports
   isort --check-only .      # Check without modifying
   ```

3. **flake8** - Linting (PEP 8 compliance)
   ```bash
   flake8 .                  # Lint all files
   flake8 --max-line-length=100 .
   ```

4. **mypy** - Type checking
   ```bash
   mypy app/                 # Type check specific directory
   mypy --strict .           # Strict mode
   ```

5. **bandit** - Security linting
   ```bash
   bandit -r app/            # Scan for security issues
   ```

### Pre-commit Hooks
All Python projects have `.pre-commit-config.yaml`:
```bash
pre-commit run --all-files    # Run all hooks
pre-commit install            # Install git hooks
```

## JavaScript/TypeScript Projects (Next.js frontends, skipy monorepo)

### Testing
```bash
# hiddenbeer frontend
npm test                      # Run Jest tests
npm run test:watch            # Watch mode

# skipy (pnpm workspace)
pnpm test                     # All workspaces
pnpm --filter @skipy/client test    # Specific workspace
```

### Code Quality Tools

1. **ESLint** - Linting
   ```bash
   npm run lint              # Run ESLint
   npm run lint:fix          # Auto-fix issues
   ```

2. **Prettier** - Code formatter
   ```bash
   npm run format            # Format all files
   npm run format:check      # Check without modifying
   ```

3. **TypeScript** - Type checking
   ```bash
   npm run type-check        # tsc --noEmit
   ```

### Configuration
- **ESLint**: `.eslintrc.json` or `eslint.config.js`
- **Prettier**: `.prettierrc`
- **TypeScript**: `tsconfig.json` (strict mode enabled)

## Java Projects (fake-data-springboot)

### Testing with Maven
```bash
make test                     # mvn -B test
mvn test -Dtest=UserControllerTest    # Single test class
mvn verify                    # Integration tests + unit tests
```

### Code Quality
- **Lombok** - Reduces boilerplate (@Data, @Builder, etc.)
- **Maven** - Build and dependency management
- **Spring Boot Test** - Testing framework

### Test Structure
```
src/test/java/
├── com/example/
│   ├── controller/     # Controller tests (Spring integration)
│   ├── service/        # Service tests (Spring + mocks)
│   └── unit/           # Fast unit tests (no Spring)
```

## Quality Standards

### Before Every Commit
```bash
# Run this in project root
make lint && make format && make test
```

### Coverage Goals
- **Python backend**: Aim for 80%+ coverage
- **Spring Boot**: Aim for 70%+ coverage
- **Frontend**: Focus on critical paths (auth, payments, etc.)

### Common Issues

1. **Import order errors** (Python):
   ```bash
   isort .                   # Fix automatically
   ```

2. **Line too long** (flake8):
   - Break into multiple lines
   - Use black formatter (handles most cases)

3. **TypeScript errors**:
   ```bash
   npm run type-check        # See all type errors
   ```

4. **Test failures**:
   ```bash
   pytest -vv --tb=short     # Verbose output, short traceback
   ```

## CI/CD Integration

All projects run quality checks in GitHub Actions:
- Linting must pass
- Tests must pass
- Type checking must pass (TS projects)
- Coverage thresholds enforced (some projects)

Check `.github/workflows/` for CI configuration.

## Tips

1. **Run tests frequently**: After every feature or bug fix
2. **Fix linting before committing**: Don't bypass with `--no-verify`
3. **Write tests for bug fixes**: Prevent regressions
4. **Use coverage reports**: Identify untested code paths
5. **Keep test data small**: Fast tests = run more often
6. **Mock external services**: Tests should work offline

## Pre-commit Hook Setup

If pre-commit hooks fail:
```bash
# Check what failed
git commit -m "message"      # See the failure output

# Run hooks manually
pre-commit run --all-files

# Fix issues
make format                  # Auto-fix formatting
make lint                    # Check remaining issues

# Commit again
git commit -m "message"
```

Never use `git commit --no-verify` unless absolutely necessary (bypasses quality checks).
