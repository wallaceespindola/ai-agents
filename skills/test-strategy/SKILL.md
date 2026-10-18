---
name: test-strategy
description: Develop comprehensive testing strategies for software projects. Use when planning test coverage, choosing testing tools, or improving test quality.
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash(pytest *), Bash(npm test *), Bash(make test *)
---

# Test Strategy Framework

Comprehensive guide for developing and implementing effective testing strategies.

## Testing Pyramid

```
        /\
       /  \  E2E Tests (Few)
      /    \  - UI tests, integration tests
     /______\
    /        \  Integration Tests (Some)
   /          \  - API tests, database tests
  /____________\
 /              \  Unit Tests (Many)
/________________\  - Function tests, class tests
```

**Principle**: More unit tests, fewer integration tests, even fewer E2E tests.

**Why?**
- Unit tests: Fast, cheap, easy to maintain
- Integration tests: Slower, test component interactions
- E2E tests: Slowest, most brittle, test full workflows

## Testing Levels

### 1. Unit Tests

**What**: Test individual functions/methods in isolation

**Characteristics**:
- Fast execution (< 1ms per test)
- No external dependencies (mock DB, APIs, etc.)
- Test one thing per test
- High code coverage (aim for 80%+)

**Example (Python/pytest)**:
```python
def test_calculate_distance():
    """Test haversine distance calculation"""
    # Arrange
    lat1, lon1 = 50.8503, 4.3517  # Brussels
    lat2, lon2 = 50.8466, 4.3528  # Nearby point

    # Act
    distance = calculate_distance(lat1, lon1, lat2, lon2)

    # Assert
    assert 0.3 < distance < 0.5  # ~0.4 km
```

**Example (TypeScript/Jest)**:
```typescript
describe('calculateDistance', () => {
  it('should calculate distance between two points', () => {
    const distance = calculateDistance(
      50.8503, 4.3517,
      50.8466, 4.3528
    );
    expect(distance).toBeCloseTo(0.4, 1);
  });
});
```

### 2. Integration Tests

**What**: Test interactions between components

**Characteristics**:
- Test with real database (test DB)
- Test API endpoints with real requests
- Test external service integrations (use mocks/stubs)
- Slower than unit tests

**Example (FastAPI integration test)**:
```python
@pytest.mark.asyncio
async def test_create_reservation_endpoint():
    """Test reservation creation via API"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Authenticate
        auth_response = await client.post("/auth/login", json={
            "email": "test@example.com"
        })
        token = auth_response.json()["access_token"]

        # Create reservation
        response = await client.post(
            "/reservations",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "offer_id": "123",
                "bar_id": "456"
            }
        )

        assert response.status_code == 201
        assert response.json()["status"] == "active"
```

### 3. End-to-End (E2E) Tests

**What**: Test complete user workflows through the UI

**Characteristics**:
- Test real user scenarios
- Use real browser (Playwright, Selenium)
- Test critical paths only
- Slowest, most expensive

**Example (Playwright)**:
```typescript
test('user can reserve a beer and redeem it', async ({ page }) => {
  // Login
  await page.goto('/login');
  await page.fill('[name="email"]', 'test@example.com');
  await page.click('button:text("Send Code")');

  // Reserve beer
  await page.goto('/nearby');
  await page.click('.offer-card:first-child');
  await page.click('button:text("Reserve")');

  // Verify reservation
  await expect(page.locator('.reservation-status')).toHaveText('Active');

  // Generate QR code
  await page.click('button:text("Show QR Code")');
  await expect(page.locator('.qr-code')).toBeVisible();
});
```

### 4. Performance Tests

**What**: Test system performance under load

**Types**:
- **Load testing**: Normal expected load
- **Stress testing**: Beyond normal load
- **Spike testing**: Sudden traffic spikes
- **Endurance testing**: Sustained load over time

**Tools**:
- k6, Locust, JMeter, Artillery

**Example (k6)**:
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 100, // 100 virtual users
  duration: '30s',
};

export default function () {
  const res = http.get('http://localhost:8004/api/v1/bars/nearby');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
  sleep(1);
}
```

### 5. Security Tests

**What**: Test for security vulnerabilities

**Areas**:
- Input validation (SQL injection, XSS)
- Authentication/authorization
- Rate limiting
- Secrets management
- Dependencies (known vulnerabilities)

**Tools**:
- bandit (Python security linting)
- npm audit (Node.js vulnerabilities)
- OWASP ZAP (web app security)
- Snyk (dependency scanning)

## Test Organization

### Arrange-Act-Assert (AAA) Pattern

```python
def test_user_registration():
    # Arrange: Set up test data
    user_data = {
        "email": "test@example.com",
        "name": "Test User"
    }

    # Act: Execute the operation
    result = register_user(user_data)

    # Assert: Verify the outcome
    assert result.email == "test@example.com"
    assert result.is_verified == False
```

### Given-When-Then (BDD Style)

```python
def test_reservation_expiry():
    # Given: A reservation that expired 10 minutes ago
    reservation = create_reservation(
        created_at=datetime.now() - timedelta(minutes=55)
    )

    # When: The expiry check runs
    check_reservation_expiry(reservation)

    # Then: The reservation status is 'expired'
    assert reservation.status == "expired"
```

## Testing Best Practices

### ✅ DO

1. **Write tests first (TDD)** or immediately after code
2. **Test one thing per test** (single assertion when possible)
3. **Use descriptive test names** (`test_user_cannot_reserve_twice_same_day`)
4. **Mock external dependencies** (APIs, databases in unit tests)
5. **Use fixtures/factories** for test data
6. **Run tests in CI/CD** (fail build if tests fail)
7. **Measure coverage** (aim for 80%+ critical paths)
8. **Test edge cases** (empty input, null, max values)
9. **Test error handling** (what happens when things fail?)
10. **Keep tests fast** (parallel execution, test DB, in-memory cache)

### ❌ DON'T

1. **Don't test framework code** (trust FastAPI, React, etc.)
2. **Don't test third-party libraries** (they have their own tests)
3. **Don't write flaky tests** (tests that randomly fail)
4. **Don't skip tests** (fix or delete them)
5. **Don't test implementation details** (test behavior, not internals)
6. **Don't share state between tests** (each test independent)
7. **Don't ignore failing tests** (fix immediately or delete)
8. **Don't write slow unit tests** (mock dependencies)

## Test Data Management

### Fixtures (pytest)

```python
@pytest.fixture
async def test_user():
    """Create a test user"""
    user = await User(
        email="test@example.com",
        name="Test User"
    ).save()
    yield user
    await user.delete()  # Cleanup

@pytest.fixture
async def authenticated_client(test_user):
    """Create authenticated API client"""
    token = create_access_token(test_user.id)
    async with AsyncClient(app=app, base_url="http://test") as client:
        client.headers["Authorization"] = f"Bearer {token}"
        yield client
```

### Factories (Factory Boy)

```python
import factory

class UserFactory(factory.Factory):
    class Meta:
        model = User

    email = factory.Faker('email')
    name = factory.Faker('name')
    phone = factory.Faker('phone_number')

# Usage
user = UserFactory.create()
users = UserFactory.create_batch(10)
```

## Mocking Strategies

### Mock External APIs

```python
from unittest.mock import patch, AsyncMock

@pytest.mark.asyncio
@patch('app.providers.brevo.send_email')
async def test_send_otp(mock_send_email):
    """Test OTP sending without actually calling Brevo"""
    mock_send_email.return_value = AsyncMock(return_value=True)

    result = await send_otp_email("test@example.com", "123456")

    assert result is True
    mock_send_email.assert_called_once()
```

### Mock Database Queries

```python
@pytest.mark.asyncio
@patch('app.models.user.User.find_one')
async def test_get_user(mock_find_one):
    """Test user retrieval"""
    mock_find_one.return_value = User(
        id="123",
        email="test@example.com"
    )

    user = await get_user("123")

    assert user.email == "test@example.com"
```

## Coverage Goals

### Backend (FastAPI, Flask, Spring Boot)

- **Overall**: 80%+ coverage
- **Critical paths**: 100% (auth, payments, data integrity)
- **Models**: 90%+ (business logic)
- **Routes**: 80%+ (endpoint testing)
- **Utils**: 90%+ (pure functions)

### Frontend (Next.js, React)

- **Critical user flows**: 80%+ (authentication, checkout)
- **Utility functions**: 90%+
- **Components**: 70%+ (focus on logic, not UI)
- **API clients**: 80%+

### Coverage Tools

- **Python**: `pytest --cov=app --cov-report=html`
- **JavaScript**: `jest --coverage`
- **Java**: JaCoCo

## Test Environments

### Local Development

```bash
# Separate test database
MONGO_URI=mongodb://localhost:27017/test_db

# In-memory cache
REDIS_URL=redis://localhost:6379/1

# Mock external services
USE_MOCK_EMAIL=true
USE_MOCK_SMS=true
```

### CI/CD

```yaml
# GitHub Actions example
test:
  runs-on: ubuntu-latest
  services:
    mongodb:
      image: mongo:8.0
      ports:
        - 27017:27017
    redis:
      image: redis:7
      ports:
        - 6379:6379
  steps:
    - run: pytest --cov=app --cov-report=xml
    - run: npm test -- --coverage
```

## Test Strategy Template

### For New Features

1. **Unit tests**: Test business logic in isolation
2. **Integration tests**: Test API endpoints with test DB
3. **E2E test**: Test one critical happy path
4. **Manual testing**: Verify in browser/app

### For Bug Fixes

1. **Write failing test** that reproduces the bug
2. **Fix the bug** until test passes
3. **Verify** related tests still pass
4. **Add edge case tests** if bug was subtle

### For Refactoring

1. **Ensure good test coverage** before refactoring
2. **Run tests frequently** during refactoring
3. **Verify all tests pass** after refactoring
4. **No new functionality** = no new tests needed

## Testing Anti-Patterns

❌ **Testing Implementation**: Don't test private methods
❌ **Brittle Tests**: Tests break on minor UI changes
❌ **Slow Tests**: Test suite takes > 5 minutes
❌ **Flaky Tests**: Tests randomly fail (timing issues)
❌ **Incomplete Mocking**: Calling real APIs in unit tests
❌ **No Assertions**: Test runs but doesn't verify anything
❌ **Testing Everything**: 100% coverage of trivial code

## Test Metrics

Track these over time:

- **Coverage %**: Is it increasing or decreasing?
- **Test count**: Growing with codebase?
- **Test execution time**: Staying fast?
- **Flaky test rate**: < 1% flaky tests
- **Build failure rate**: Tests catching bugs?

## Tools by Language/Framework

### Python (FastAPI, Flask)
- **pytest**: Test runner
- **pytest-asyncio**: Async test support
- **pytest-cov**: Coverage reporting
- **httpx**: Async HTTP client for API tests
- **factory-boy**: Test data factories
- **faker**: Generate fake data
- **freezegun**: Mock datetime

### JavaScript/TypeScript (Next.js, React)
- **Jest**: Test runner
- **React Testing Library**: Component testing
- **Playwright**: E2E testing
- **MSW**: Mock Service Worker (API mocking)
- **faker-js**: Generate fake data

### Java (Spring Boot)
- **JUnit 5**: Test runner
- **Mockito**: Mocking framework
- **Spring Boot Test**: Integration testing
- **TestContainers**: Docker containers for tests
- **RestAssured**: REST API testing

## Quick Start Template

### pytest.ini (Python)
```ini
[pytest]
asyncio_mode = auto
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    -v
    --cov=app
    --cov-report=html
    --cov-report=term-missing
    --cov-fail-under=80
```

### jest.config.js (JavaScript)
```javascript
module.exports = {
  testEnvironment: 'jsdom',
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts',
  ],
  coverageThreshold: {
    global: {
      branches: 70,
      functions: 70,
      lines: 70,
      statements: 70,
    },
  },
};
```

## Remember

> "Tests are not about achieving 100% coverage. They're about confidence that your code works and will continue to work."

Good tests:
- **Give you confidence** to refactor
- **Catch bugs** before production
- **Document behavior** (tests as specs)
- **Run fast** (feedback loop)
- **Are maintainable** (easy to update)
