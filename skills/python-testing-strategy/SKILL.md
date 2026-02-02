---
name: python-testing-strategy
description: Design comprehensive test strategies for Python projects using pytest and best practices
---

# Python Testing Strategy Skill

## When to Use This Skill

- Designing test architecture for new Python projects
- Creating unit, integration, and E2E test strategies
- Setting up pytest fixtures and test organization
- Implementing test coverage and CI/CD integration
- Refactoring legacy code with tests
- Defining testing standards for development teams
- Planning performance and load testing strategies
- Setting up test data management and mocking

## Quick Start

```
/python-testing-strategy <project_type_or_component>
```

**Example**:
```
/python-testing-strategy FastAPI REST API with database interactions
```

## How It Works

The skill creates a complete testing strategy with multiple testing levels:

### 1. Test Pyramid Design
- **Unit Tests** (70%): Test individual functions and classes in isolation
- **Integration Tests** (20%): Test components working together
- **E2E Tests** (10%): Test complete user workflows

### 2. Pytest Framework Setup
- **Fixtures**: Reusable test components and setup/teardown
- **Parametrization**: Data-driven testing for multiple inputs
- **Marks**: Test organization and filtering (unit, integration, slow)
- **Plugins**: Coverage, xdist for parallel execution, faker for test data

### 3. Unit Testing Patterns
- **Arrange-Act-Assert (AAA)**: Test structure pattern
- **Mocking**: Isolate units with mock objects
- **Stubbing**: Return predetermined values
- **Spying**: Track function calls and arguments

### 4. Integration Testing
- **Database Testing**: SQLAlchemy test sessions, fixtures
- **API Testing**: Mock HTTP requests with responses library
- **Service Integration**: Test component interactions
- **Transaction Rollback**: Clean state between tests

### 5. Test Coverage Strategy
- **Line Coverage**: Percentage of code executed
- **Branch Coverage**: Both true and false code paths
- **Coverage Goals**: Minimum thresholds (typically 80%)
- **Coverage Reports**: HTML reports and CI integration

### 6. Test Data Management
- **Factories**: pytest-factory for generating objects
- **Fixtures**: Shared test data and state
- **Seeds**: Reproducible test data
- **Cleanup**: Proper teardown and resource management

### 7. Mocking Strategy
- **Mock External APIs**: Prevent external dependencies
- **Mock Time**: Control datetime for temporal tests
- **Mock Databases**: In-memory SQLite for testing
- **Mock File System**: pyfakefs for file operations

## Configuration

**pytest.ini**:
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --strict-markers --tb=short --cov=src --cov-report=html
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    slow: Slow running tests
    database: Tests requiring database
```

**requirements-dev.txt**:
```
pytest==7.4.3
pytest-cov==4.1.0
pytest-xdist==3.5.0
pytest-asyncio==0.21.1
pytest-mock==3.12.0
faker==20.1.0
factory-boy==3.3.0
responses==0.24.1
pyfakefs==4.7.2
```

**Makefile**:
```makefile
test:
	pytest tests/

test-unit:
	pytest tests/ -m unit

test-integration:
	pytest tests/ -m integration

test-cov:
	pytest tests/ --cov=src --cov-report=html --cov-report=term

test-watch:
	pytest-watch tests/

test-parallel:
	pytest tests/ -n auto
```

## Examples

### Example 1: Unit Test with Fixtures

```python
# tests/test_user_service.py
import pytest
from unittest.mock import Mock
from src.services.user_service import UserService
from src.models import User


@pytest.fixture
def mock_repository():
    """Fixture providing a mock user repository"""
    return Mock()


@pytest.fixture
def user_service(mock_repository):
    """Fixture providing UserService with mocked dependencies"""
    return UserService(repository=mock_repository)


class TestUserService:
    """Test suite for UserService"""

    def test_create_user_success(self, user_service, mock_repository):
        """Test successful user creation"""
        # Arrange
        email = "test@example.com"
        mock_repository.save.return_value = User(id=1, email=email)

        # Act
        result = user_service.create_user(email=email, name="Test User")

        # Assert
        assert result.id == 1
        assert result.email == email
        mock_repository.save.assert_called_once()

    def test_create_user_invalid_email(self, user_service):
        """Test user creation with invalid email"""
        # Arrange & Act & Assert
        with pytest.raises(ValueError, match="Invalid email"):
            user_service.create_user(email="invalid", name="Test")

    @pytest.mark.parametrize("email,valid", [
        ("user@example.com", True),
        ("invalid.email", False),
        ("@example.com", False),
        ("user@example", True),  # Common domain
    ])
    def test_email_validation(self, user_service, email, valid):
        """Parametrized test for email validation"""
        result = user_service.is_valid_email(email)
        assert result == valid
```

### Example 2: Integration Test with Database

```python
# tests/integration/test_user_repository.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, User
from src.repositories import UserRepository


@pytest.fixture(scope="function")
def db_session():
    """Fixture providing a test database session"""
    # Create in-memory SQLite database
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()


@pytest.fixture
def user_repository(db_session):
    """Fixture providing UserRepository"""
    return UserRepository(session=db_session)


@pytest.mark.integration
class TestUserRepository:
    """Integration tests for UserRepository"""

    def test_save_and_retrieve_user(self, user_repository, db_session):
        """Test saving and retrieving a user"""
        # Arrange
        user = User(email="test@example.com", name="Test User")

        # Act
        user_repository.save(user)
        retrieved = user_repository.find_by_email("test@example.com")

        # Assert
        assert retrieved is not None
        assert retrieved.email == "test@example.com"
        assert retrieved.name == "Test User"

    def test_find_user_not_found(self, user_repository):
        """Test finding non-existent user"""
        result = user_repository.find_by_email("nonexistent@example.com")
        assert result is None

    def test_update_user(self, user_repository):
        """Test updating user"""
        # Arrange
        user = User(email="test@example.com", name="Original Name")
        user_repository.save(user)

        # Act
        user.name = "Updated Name"
        user_repository.save(user)
        retrieved = user_repository.find_by_email("test@example.com")

        # Assert
        assert retrieved.name == "Updated Name"
```

### Example 3: Async Test with pytest-asyncio

```python
# tests/test_async_service.py
import pytest
from unittest.mock import AsyncMock
from src.services.async_service import AsyncUserService


@pytest.fixture
def async_mock_api():
    """Fixture providing mock async API"""
    return AsyncMock()


@pytest.mark.asyncio
class TestAsyncUserService:
    """Test suite for async services"""

    async def test_fetch_user_async(self, async_mock_api):
        """Test asynchronous user fetching"""
        # Arrange
        async_mock_api.get_user.return_value = {
            "id": 1,
            "email": "test@example.com"
        }
        service = AsyncUserService(api=async_mock_api)

        # Act
        result = await service.fetch_user(1)

        # Assert
        assert result["email"] == "test@example.com"
        async_mock_api.get_user.assert_called_once_with(1)

    @pytest.mark.parametrize("user_id,expected", [
        (1, {"id": 1, "email": "user1@example.com"}),
        (2, {"id": 2, "email": "user2@example.com"}),
    ])
    async def test_fetch_users_parametrized(self, async_mock_api, user_id, expected):
        """Parametrized async test"""
        async_mock_api.get_user.return_value = expected
        service = AsyncUserService(api=async_mock_api)

        result = await service.fetch_user(user_id)
        assert result == expected
```

### Example 4: Mocking External APIs

```python
# tests/test_external_integration.py
import pytest
import responses
import requests
from src.services.payment_service import PaymentService


@pytest.fixture
def payment_service():
    """Fixture providing PaymentService"""
    return PaymentService(api_url="https://api.payment.com")


@responses.activate
def test_process_payment_success(payment_service):
    """Test payment processing with mocked API"""
    # Arrange
    responses.add(
        responses.POST,
        "https://api.payment.com/charge",
        json={"transaction_id": "txn_123", "status": "success"},
        status=200
    )

    # Act
    result = payment_service.process_payment(amount=100.0, card_token="tok_visa")

    # Assert
    assert result["transaction_id"] == "txn_123"
    assert result["status"] == "success"
    assert len(responses.calls) == 1


@responses.activate
def test_process_payment_failure(payment_service):
    """Test payment processing failure"""
    # Arrange
    responses.add(
        responses.POST,
        "https://api.payment.com/charge",
        json={"error": "Insufficient funds"},
        status=402
    )

    # Act & Assert
    with pytest.raises(Exception, match="Payment failed"):
        payment_service.process_payment(amount=100.0, card_token="tok_visa")
```

### Example 5: Test with Faker and Factories

```python
# tests/factories.py
from faker import Faker
from factory import Factory
from src.models import User, Order

fake = Faker()


class UserFactory(Factory):
    """Factory for generating test User objects"""
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    email = factory.LazyFunction(lambda: fake.email())
    name = factory.LazyFunction(lambda: fake.name())
    created_at = factory.LazyFunction(lambda: fake.date_time())


class OrderFactory(Factory):
    """Factory for generating test Order objects"""
    class Meta:
        model = Order

    id = factory.Sequence(lambda n: n)
    user = factory.SubFactory(UserFactory)
    total = factory.LazyFunction(lambda: fake.pydecimal(left_digits=5, right_digits=2))


# tests/test_with_factories.py
@pytest.mark.unit
class TestOrders:
    def test_order_total_calculation(self):
        """Test with factory-generated data"""
        # Arrange
        user = UserFactory(email="test@example.com")
        order = OrderFactory(user=user, total=100.50)

        # Act
        discount = order.calculate_discount(0.10)

        # Assert
        assert discount == 10.05
        assert order.total - discount == 90.45
```

### Example 6: Fixture Scope Management

```python
# tests/conftest.py
import pytest
from src.database import Database, SessionLocal


@pytest.fixture(scope="session")
def test_db():
    """Session-scoped fixture for test database setup"""
    db = Database(url="sqlite:///:memory:")
    db.init()
    yield db
    db.cleanup()


@pytest.fixture(scope="function")
def db_session(test_db):
    """Function-scoped fixture for transaction rollback"""
    session = SessionLocal()

    # Begin transaction
    transaction = session.begin_nested()

    yield session

    # Rollback after test
    transaction.rollback()
    session.close()


@pytest.fixture(scope="module")
def test_client(test_db):
    """Module-scoped fixture for FastAPI test client"""
    from fastapi.testclient import TestClient
    from src.main import app

    return TestClient(app)
```

## Best Practices

### 1. Test Organization
```
tests/
├── conftest.py              # Shared fixtures
├── test_*.py                # Unit tests
├── unit/
│   ├── test_models.py
│   └── test_services.py
├── integration/
│   ├── test_repositories.py
│   └── test_api.py
├── e2e/
│   └── test_user_workflows.py
└── factories.py             # Test data factories
```

### 2. Fixture Best Practices
- Use function scope by default for isolation
- Use session scope for expensive resources (database)
- Name fixtures descriptively
- Avoid shared mutable state

### 3. Test Naming
- Describe what is being tested: `test_create_user_with_valid_email`
- Include expected outcome: `test_save_returns_user_with_id`
- Use parametrize for similar tests

### 4. Assertion Best Practices
```python
# Good: Specific assertions
assert user.email == "test@example.com"
assert len(users) == 3
assert "error" not in response

# Avoid: Generic assertions
assert user is not None
assert response  # Too vague
```

### 5. Mock Best Practices
- Mock external dependencies, not business logic
- Use `unittest.mock.patch` for replacing
- Verify mock was called with correct arguments
- Consider using `pytest-mock` for safer mocking

### 6. Coverage Goals
```python
# Run with coverage reporting
pytest --cov=src --cov-report=html --cov-report=term-missing

# Focus on untested lines
coverage report --show-missing
```

## Integration with Other Skills

- **`python-code-review`**: Code review includes test coverage assessment
- **`python-performance-tuning`**: Benchmark tests for performance-critical code
- **`cicd-pipeline-setup`**: Automated test execution in CI/CD
- **`test-strategy-doc`**: Create comprehensive testing documentation
- **`python-documentation`**: Test examples in docstrings

