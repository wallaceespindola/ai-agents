---
name: python-coder
description: Generate complete production-ready Python projects with full source code, tests, and documentation. Create linked repositories where articles in /docs reference code in src and tests in test folders. Perfect for tutorials, patterns, and real-world examples.
---

# Python Coder Skill

Generate production-ready Python projects that complement technical articles. This skill creates complete, runnable code with proper project structure, dependency management, tests, and documentation.

## When to Use This Skill

Use this skill when:
- Writing a Python tutorial and want readers to access complete working code
- Demonstrating a design pattern with a full implementation
- Building a case study with actual running code
- Creating a reference implementation for an architecture pattern
- Writing about FastAPI, async/await, or Django and need functional examples
- Showing concurrent/async patterns with working code
- Teaching Python best practices through example projects

## Quick Start

### Create a Python Project

When you have an article about Python, request code generation:

```
Create a Python project for my article "FastAPI Async Patterns"
Include:
- FastAPI application with async endpoints
- Service layer with business logic
- Database models with SQLAlchemy
- Unit tests with pytest
- Integration tests with httpx test client
- README with setup instructions
- Link to article in /docs/ARTICLE.md
```

### Project Structure

Standard Python project layout:

```
project-name/
├── pyproject.toml                   # Project metadata and dependencies
├── README.md                        # Quick start guide
├── docs/
│   ├── ARTICLE.md                   # Your article (or link to it)
│   └── SETUP.md                     # Development setup guide
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── main.py                  # Application entry point
│       ├── api/                     # API routes/controllers
│       │   ├── __init__.py
│       │   ├── endpoints.py
│       │   └── models.py            # Pydantic models (DTOs)
│       ├── service/                 # Business logic
│       │   ├── __init__.py
│       │   └── service.py
│       ├── repository/              # Data access
│       │   ├── __init__.py
│       │   └── repository.py
│       ├── model/                   # Domain models
│       │   ├── __init__.py
│       │   └── domain.py
│       ├── util/                    # Utilities
│       │   ├── __init__.py
│       │   └── helpers.py
│       └── config.py                # Configuration
├── tests/
│   ├── __init__.py
│   ├── conftest.py                  # pytest fixtures
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_service.py
│   │   └── test_repository.py
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_api.py
│   └── fixtures/
│       ├── __init__.py
│       └── test_data.py             # Test data builders
├── .gitignore                       # Python-specific exclusions
└── .env.example                     # Environment variables template
```

## Core Concepts

### 1. Project Configuration

**pyproject.toml Setup:**
- Project metadata (name, version, description)
- Python version specification (3.9+)
- Dependencies with version constraints
- Development dependencies (testing, linting)
- Tool configurations (pytest, mypy, ruff)

**Example pyproject.toml structure:**
```toml
[project]
name = "project-name"
version = "1.0.0"
description = "Description"
requires-python = ">=3.9"
dependencies = [
    "fastapi>=0.100",
    "sqlalchemy>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "mypy>=1.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.mypy]
python_version = "3.9"
strict = true
```

**Alternative uv setup:**
```
uv init --python 3.9 project-name
uv add fastapi sqlalchemy
uv add --dev pytest pytest-cov mypy
```

### 2. Code Organization

**API Layer (FastAPI):**
- Routes with clear endpoints
- Async/await patterns
- Request/response models with Pydantic
- Dependency injection
- Error handling with HTTPException

**Service Layer:**
- Business logic separation
- Dependency injection
- Transaction management
- Error handling and logging

**Repository Layer:**
- Database access abstraction
- SQLAlchemy ORM usage
- Query optimization
- Consistent naming conventions

**Model Layer:**
- SQLAlchemy ORM models
- Pydantic models for API (DTOs)
- Validation using Pydantic validators
- Type hints throughout

### 3. Testing Strategy

**Unit Tests:**
- Service layer with mocks
- Repository with test database
- Utility functions

**Integration Tests:**
- API endpoints with test client
- Full async flow
- Database transactions
- Real-world scenarios

**Test Organization:**
```
tests/
├── unit/
│   ├── test_service.py
│   └── test_repository.py
├── integration/
│   └── test_api.py
└── fixtures/
    ├── conftest.py              # Shared pytest fixtures
    └── test_data.py             # Test data builders
```

**Example pytest usage:**
```python
# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    yield SessionLocal(bind=engine)

@pytest.fixture
def client(db):
    app.dependency_overrides[get_db] = lambda: db
    return TestClient(app)
```

### 4. Documentation

**README.md should include:**
- Project description and purpose
- Prerequisites (Python version, uv/pip)
- Setup instructions (git clone, dependencies)
- Running the application
- Running tests
- Project structure overview
- Key features and endpoints (for APIs)
- Article reference

**SETUP.md should include:**
- Development environment setup
- IDE configuration (VS Code, PyCharm, etc.)
- Database setup (if using SQLite, PostgreSQL)
- Pre-commit hooks setup
- Troubleshooting common issues

**Inline code documentation:**
- Module docstrings explaining purpose
- Function docstrings with parameter/return docs
- Complex algorithm explanations
- Type hints for all parameters and returns
- Links to related article sections

### 5. Linking to Articles

**In article (/docs/ARTICLE.md):**
```markdown
## Running the Example

This article includes a complete working example. Clone the repository:

```bash
git clone <repo-url>
cd project-name
uv sync  # or pip install -r requirements.txt
```

Then follow the instructions in README.md to run the code.

Key files:
- `src/project_name/api/endpoints.py` - API endpoint implementation
- `tests/integration/test_api.py` - Tests demonstrating usage
```

**In code (README.md):**
```markdown
## Associated Article

This code example supports the article:
[Article Title](./docs/ARTICLE.md)

For detailed explanation of design decisions and patterns, see the article.
```

## Common Patterns

### FastAPI REST API Project

**Files to generate:**
- main.py - FastAPI application setup
- api/endpoints.py - Route handlers
- api/models.py - Pydantic models for requests/responses
- service/ - Business logic layer
- repository/ - Database access layer
- model/domain.py - SQLAlchemy models
- config.py - Configuration management
- Integration tests with httpx TestClient

**Key features:**
- Async/await throughout
- Pydantic for request/response validation
- SQLAlchemy ORM for database
- Type hints for everything
- Error handling with HTTPException
- OpenAPI/Swagger documentation (automatic)

### Design Pattern Implementation

**Example: Observer Pattern**
```
Files:
- observer.py (Observer and Subject abstractions)
- concrete_observer.py (implementations)
- main.py (usage example)
- test_observer.py (comprehensive tests)
- README.md explaining the pattern
```

**Example: Factory Pattern**
```
Files:
- factory.py (Factory implementation)
- product.py (Product abstractions)
- concrete_products.py (implementations)
- test_factory.py (tests)
```

### Async/Await Pattern Example

**Files to generate:**
- Async function examples
- AsyncIO patterns (gather, create_task)
- Context managers and async context managers
- Concurrent execution examples
- Error handling in async code
- Testing async functions (pytest-asyncio)

**Key features:**
- Modern async/await syntax
- Structured concurrency patterns
- Proper exception handling
- Performance considerations
- Real-world async examples

### Data Processing Pipeline

**Files to generate:**
- Data loading (CSV, JSON, APIs)
- Transformation logic
- Validation
- Output formatting
- Error handling and logging
- Unit and integration tests

**Key features:**
- Pandas or Polars for data
- Pydantic for validation
- Type hints throughout
- Logging for debugging
- Test data fixtures

## Article Integration Workflow

### Step 1: Write Article in /docs/ARTICLE.md

Create your article explaining the concept, design, or pattern.

### Step 2: Request Code Generation

```
Generate Python code for my article about [topic].
Article file: docs/ARTICLE.md

Requirements:
- FastAPI / Django / AsyncIO (choose framework)
- [specific implementation details]
- [design patterns to demonstrate]
- [technologies to use]
- [test coverage expectations]
```

### Step 3: Generated Project Includes

- Complete source code in `src/project_name/`
- Comprehensive tests in `tests/`
- README.md with setup instructions
- pyproject.toml with all dependencies
- Links to article in documentation

### Step 4: Integrate in Repository

```
my-repo/
├── docs/
│   └── articles/
│       └── article-name/
│           ├── ARTICLE.md             # Your article
│           ├── README.md              # Project guide
│           └── code/                  # Code folder (optional)
│
└── projects/
    └── article-name-example/
        ├── pyproject.toml
        ├── README.md                  # Links to article
        ├── src/project_name/...
        └── tests/...
```

Or simpler, single project:

```
my-repo/
├── pyproject.toml
├── README.md                          # Main guide
├── docs/
│   └── ARTICLE.md                     # Your article
├── src/project_name/...
└── tests/...
```

## Best Practices

### Code Quality

✅ **Do:**
- Use clear, descriptive variable and function names
- Follow PEP 8 conventions
- Add type hints for all functions
- Use dataclasses or Pydantic for data structures
- Implement proper logging
- Handle exceptions explicitly
- Use modern Python features (f-strings, walrus operator, pattern matching in 3.10+)
- Keep functions focused and testable
- Use context managers for resource management

❌ **Avoid:**
- No type hints
- Long functions doing too much
- Bare except clauses
- Mutable default arguments
- Circular imports
- Logging instead of raising exceptions
- Magic numbers or strings (use constants)
- Mixing abstraction levels in single function

### Testing

✅ **Do:**
- Write unit tests for business logic
- Use mocks for external dependencies
- Write integration tests for APIs
- Name tests clearly: `test_xxx_when_xxx_then_xxx()`
- Use pytest fixtures for setup/teardown
- Test both success and failure paths
- Use pytest-cov for coverage metrics
- Use pytest-asyncio for async tests
- Organize tests by layer (unit, integration)

❌ **Avoid:**
- 100% code coverage as the only goal
- Over-mocking (test behavior, not implementation)
- Slow tests (except integration tests)
- Tests that depend on each other
- Hardcoded test data (use fixtures/factories)
- Ignoring tests without reason

### Async/Await

✅ **Do:**
- Use async/await for I/O operations
- Use FastAPI for async APIs
- Properly handle async context managers
- Use asyncio.gather for concurrent operations
- Close resources properly
- Handle timeouts explicitly

❌ **Avoid:**
- Mixing sync and async without reason
- Long-running CPU-bound tasks in async context
- Not handling async exceptions properly
- Creating too many coroutines without limits

### Documentation

✅ **Do:**
- Explain why, not what
- Include setup and run instructions
- Document all public functions
- Provide quick start examples
- Link to related articles
- Explain design decisions
- Keep docs in sync with code

❌ **Avoid:**
- Obvious docstrings that just repeat code
- Documentation out of sync with implementation
- Missing error documentation
- No examples

## Project Templates

### Template 1: FastAPI REST API

```
Key files:
- main.py (FastAPI app setup)
- api/endpoints.py (routes)
- api/models.py (Pydantic models)
- service/service.py (business logic)
- repository/repository.py (database)
- model/domain.py (SQLAlchemy models)
- Integration and unit tests
```

**Dependencies:**
- fastapi
- sqlalchemy
- pydantic
- pytest
- httpx (for testing)

### Template 2: Design Pattern Showcase

```
Key files:
- Pattern implementations
- Client code showing usage
- Comprehensive unit tests
- Documentation of pattern
```

**Dependencies:**
- pytest
- pytest-cov

### Template 3: Async/Concurrent Programming

```
Key files:
- Async function examples
- AsyncIO patterns
- Concurrent execution examples
- Context managers
- Comprehensive tests
```

**Dependencies:**
- pytest
- pytest-asyncio
- aiohttp or httpx (if making async requests)

### Template 4: Data Processing

```
Key files:
- Data loaders
- Transformation logic
- Validation with Pydantic
- Output formatters
- Logging and error handling
- Unit and integration tests
```

**Dependencies:**
- pandas or polars
- pydantic
- pytest
- pytest-cov

## File Generation Checklist

### Configuration Files
- [ ] pyproject.toml with all dependencies
- [ ] .env.example with environment variables
- [ ] pyproject.toml with pytest, mypy config
- [ ] .gitignore with Python exclusions
- [ ] .pre-commit-config.yaml (optional)

### Source Code
- [ ] src/project_name/__init__.py
- [ ] main.py or equivalent entry point
- [ ] API routes/endpoints
- [ ] Service/business logic layer
- [ ] Repository/data access layer
- [ ] Domain models
- [ ] Pydantic models (DTOs)
- [ ] Configuration management
- [ ] Utility functions
- [ ] Logging setup

### Tests
- [ ] tests/conftest.py with fixtures
- [ ] Unit tests for services
- [ ] Unit tests for repositories
- [ ] Integration tests for APIs
- [ ] Test data builders/factories
- [ ] Test configuration

### Documentation
- [ ] README.md with full setup
- [ ] SETUP.md with development guide
- [ ] Module docstrings
- [ ] Function docstrings
- [ ] Type hints throughout
- [ ] Links to article

### Quality
- [ ] All tests pass
- [ ] No mypy errors
- [ ] Code passes linting (ruff, black)
- [ ] No hardcoded values
- [ ] Proper logging at appropriate levels
- [ ] Exception handling coverage

## Build and Run Commands

**Commands to document:**

```bash
# Setup with uv (recommended)
uv sync
uv run python src/project_name/main.py

# Setup with pip
pip install -r requirements.txt
python src/project_name/main.py

# Run tests
pytest
pytest --cov=src

# Run specific test
pytest tests/integration/test_api.py::test_xxx

# Type checking
mypy src/

# Linting
ruff check src/
black --check src/

# Fix formatting
black src/
ruff check --fix src/

# Run FastAPI app with auto-reload
fastapi dev src/project_name/main.py

# Run with environment
PYTHONENV=development python src/project_name/main.py
```

## Dependency Management

**Using pyproject.toml + uv (modern approach):**
```toml
[project]
dependencies = [
    "fastapi>=0.100",
    "sqlalchemy>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "mypy>=1.0",
    "ruff>=0.1",
]
```

**Using requirements.txt (traditional):**
```
fastapi==0.100.0
sqlalchemy==2.0.0
pydantic==2.0.0
pytest==7.0.0
pytest-cov==4.0.0
```

## Type Hints & Validation

**Use type hints everywhere:**
```python
from typing import Optional, List
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

async def create_user(user: UserCreate) -> User:
    # Implementation
    pass

def process_items(items: List[str]) -> Dict[str, int]:
    # Implementation
    pass
```

**Type checking with mypy:**
```bash
mypy src/
mypy --strict src/  # strictest mode
```

## Logging Configuration

**Structured logging:**
```python
import logging

logger = logging.getLogger(__name__)

def create_user(user_data):
    logger.info("Creating user", extra={"email": user_data.email})
    try:
        # Implementation
    except Exception as e:
        logger.error("Failed to create user", exc_info=True)
        raise
```

## Integration with Article Workflow

1. **Write article** in `/docs/ARTICLE.md`
2. **Request Python code generation** mentioning article file
3. **Receive complete project** with:
   - Source code in `src/project_name/`
   - Tests in `tests/`
   - README.md linking to article
   - Ready to run setup
4. **Link from article** to GitHub repository
5. **Readers can clone** and run the code
6. **Maintain together**: Article and code stay in sync

## Common Scenarios

### Scenario 1: FastAPI Tutorial

Article shows how to build API. Code shows complete working implementation.

Reader can:
- Follow article step by step
- See complete working code
- Run and test locally
- Modify and experiment
- Use as starting point

### Scenario 2: Design Pattern

Article explains pattern. Code shows real, working implementation.

Reader can:
- Learn pattern from article
- See production-ready code
- Run tests to see pattern work
- Use as reference

### Scenario 3: Async/Concurrency

Article explains async patterns. Code shows real examples running.

Reader can:
- Understand async concepts
- See practical implementations
- Run and modify examples
- Experiment safely

## Success Checklist

- [ ] Code runs without errors
- [ ] All tests pass
- [ ] Tests have meaningful assertions
- [ ] README is clear and complete
- [ ] Code follows PEP 8
- [ ] Type hints on all functions
- [ ] Article is linked from README
- [ ] Setup instructions work
- [ ] Code is production-ready
- [ ] Key functions have docstrings
- [ ] Error handling is appropriate
- [ ] Logging is structured and helpful

---

This skill works best combined with:
- **python-content** for Python expertise and guidance
- **code-examples-generator** for snippet generation
- **markdown-formatter** for documentation formatting
- **architecture-design** for pattern explanations
- **image-generator-blog** for architecture diagrams in docs
