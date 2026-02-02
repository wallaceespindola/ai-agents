---
name: test-automation-setup
description: Set up test automation frameworks for unit, integration, and E2E testing
---

# Test Automation Setup Skill

## When to Use This Skill

- Selecting test automation tools and frameworks
- Setting up testing infrastructure
- Configuring CI/CD test pipelines
- Establishing test best practices
- Implementing page object models
- Setting up parallel test execution
- Configuring test reporting and dashboards

## Quick Start

```
/test-automation-setup <technology_stack_and_test_type>
```

**Example**:
```
/test-automation-setup React application with E2E and unit testing
```

## Test Frameworks by Technology

### Python
- **pytest**: Simplest, most flexible
- **unittest**: Built-in framework
- **nose2**: pytest-like with plugins

### JavaScript/TypeScript
- **Jest**: Most popular, all-in-one
- **Vitest**: Vite-native, fast
- **Cypress**: E2E testing specialist
- **Playwright**: Cross-browser E2E

### Java
- **JUnit 5**: Industry standard
- **TestNG**: Advanced features
- **Mockito**: Mocking framework

### Configuration Example

**pytest.ini**:
```ini
[pytest]
testpaths = tests
python_files = test_*.py
addopts = -v --cov=src --tb=short
```

**jest.config.js**:
```javascript
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/setupTests.ts'],
  collectCoverageFrom: ['src/**/*.{ts,tsx}'],
  coverageThreshold: {
    global: { statements: 80, branches: 80, functions: 80, lines: 80 }
  }
};
```

## Examples

### Example: E2E Test with Playwright

```typescript
import { test, expect } from '@playwright/test';

test.describe('Checkout Flow', () => {
  test('should complete purchase', async ({ page }) => {
    // Navigate
    await page.goto('https://example.com');

    // Add to cart
    await page.click('[data-testid="product-add"]');
    await expect(page.locator('.cart-badge')).toContainText('1');

    // Checkout
    await page.click('[data-testid="checkout"]');
    await page.fill('#card-number', '4111111111111111');
    await page.click('button:has-text("Pay")');

    // Verify
    await expect(page).toHaveURL('/order-confirmation');
  });
});
```

### Example: API Test

```javascript
describe('User API', () => {
  test('should create user', async () => {
    const response = await fetch('/api/users', {
      method: 'POST',
      body: JSON.stringify({ email: 'test@example.com' })
    });

    expect(response.status).toBe(201);
    const user = await response.json();
    expect(user.id).toBeDefined();
  });
});
```

## CI/CD Integration

```yaml
# GitHub Actions
name: Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: npm install
      - name: Unit tests
        run: npm run test:unit
      - name: E2E tests
        run: npm run test:e2e
      - name: Upload coverage
        run: npm run coverage:upload
```

## Best Practices

1. **Test Organization**: Group by feature/functionality
2. **Naming**: Descriptive test names
3. **Setup/Teardown**: Clean state between tests
4. **Assertions**: Clear, specific assertions
5. **Avoid Flakiness**: No timing-dependent tests
6. **Parallel Execution**: Run tests in parallel
7. **Reporting**: Clear pass/fail reports

## Integration with Other Skills

- **`test-strategy-doc`**: Test planning
- **`cicd-pipeline-setup`**: CI/CD integration
- **`test-case-generator`**: Test case creation
- **`api-testing-setup`**: API testing

