---
name: python-code-review
description: Review Python code for best practices, Pythonic patterns, performance, and PEP compliance
---

# Python Code Review Skill

## When to Use This Skill

- Reviewing pull requests for Python/FastAPI applications
- Assessing code quality and PEP 8 compliance
- Identifying performance issues and bottlenecks
- Catching security vulnerabilities in Python code
- Ensuring type hints and type safety
- Validating async/await patterns
- Checking for proper error handling
- Enforcing project coding standards

## Quick Start

```
/python-code-review <file_path_or_module>
```

**Example**:
```
/python-code-review src/services/user_service.py
```

## How It Works

The skill performs comprehensive Python code analysis:

### 1. PEP Compliance
- **PEP 8**: Code style and naming conventions
- **PEP 257**: Docstring conventions
- **PEP 3107**: Function annotations
- **PEP 484**: Type hints and type checking

### 2. Code Quality
- **Readability**: Clear variable names, function length, cyclomatic complexity
- **Maintainability**: DRY principle, code duplication, SOLID principles
- **Pythonic Style**: Idiomatic Python patterns and conventions
- **Import Organization**: Proper grouping with isort

### 3. Performance Analysis
- **Algorithmic Complexity**: O(n) vs O(n²) analysis
- **Memory Usage**: Unnecessary list copies, generators vs lists
- **Async Patterns**: Proper use of async/await, event loop
- **Database Queries**: N+1 problems, query optimization (SQLAlchemy)

### 4. Security Review
- **Input Validation**: Proper validation of user input
- **SQL Injection**: Safe SQL query construction
- **Secrets Management**: No hardcoded credentials or API keys
- **Dependency Vulnerabilities**: Known CVEs in dependencies
- **OWASP**: Common security vulnerabilities

### 5. Type Safety
- **Type Hints**: Complete and accurate type annotations
- **Optional Usage**: Proper handling of None values
- **Generics**: Correct use of generic types
- **Mypy Compliance**: Passes mypy type checking

## Configuration

**Code Quality Tools**:
```bash
# Black: Code formatter
black --line-length 88 src/

# isort: Import organizer
isort src/

# flake8: Code linter
flake8 src/ --max-line-length=88

# mypy: Type checker
mypy src/ --strict

# bandit: Security scanner
bandit -r src/
```

**pyproject.toml Configuration**:
```toml
[tool.black]
line-length = 88
target-version = ['py310']

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.10"
strict = true
warn_unused_configs = true

[tool.pylint]
max-line-length = 88
```

## Examples

### Example 1: Type Hints and None Handling

```python
# ❌ ISSUE: No type hints, unclear None handling
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user_to_dict(user)
    return None

# ✅ FIXED: Complete type hints
from typing import Optional
from models import User
from schemas import UserDTO

def get_user(user_id: int) -> Optional[UserDTO]:
    """Retrieve a user by ID.

    Args:
        user_id: The user's unique identifier.

    Returns:
        User data if found, None otherwise.

    Raises:
        ValueError: If user_id is negative.
    """
    if user_id < 0:
        raise ValueError("user_id must be non-negative")

    user = User.query.get(user_id)
    return UserDTO.from_orm(user) if user else None
```

### Example 2: Async/Await Patterns

```python
# ❌ ISSUE: Blocking I/O in async function
async def fetch_users():
    users = []
    for user_id in range(1, 100):
        response = requests.get(f"/api/users/{user_id}")  # Blocks!
        users.append(response.json())
    return users

# ✅ FIXED: Proper async/await
import aiohttp
from typing import List

async def fetch_users() -> List[UserDTO]:
    """Fetch multiple users concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_user_async(session, user_id)
            for user_id in range(1, 100)
        ]
        users = await asyncio.gather(*tasks)
    return users

async def fetch_user_async(
    session: aiohttp.ClientSession,
    user_id: int
) -> UserDTO:
    """Fetch a single user."""
    async with session.get(f"/api/users/{user_id}") as resp:
        data = await resp.json()
        return UserDTO(**data)
```

### Example 3: Proper Error Handling

```python
# ❌ ISSUE: Bare except, swallowing exceptions
def process_data(data):
    try:
        return parse_json(data)
    except:
        return None

# ✅ FIXED: Specific exception handling
import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def process_data(data: str) -> Optional[dict[str, Any]]:
    """Parse JSON data with proper error handling.

    Args:
        data: JSON string to parse.

    Returns:
        Parsed data if valid, None if parsing fails.
    """
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON: {e}")
        return None
    except Exception as e:
        logger.exception(f"Unexpected error parsing data: {e}")
        raise DataProcessingError("Failed to process data") from e
```

### Example 4: SQLAlchemy N+1 Query

```python
# ❌ ISSUE: N+1 queries
@app.get("/users")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()  # 1 query
    return [
        {
            "user": user,
            "posts": db.query(Post).filter_by(user_id=user.id).all()  # N queries!
        }
        for user in users
    ]

# ✅ FIXED: Use joinedload
from sqlalchemy.orm import joinedload

@app.get("/users")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).options(
        joinedload(User.posts)  # 1 query with JOIN
    ).all()
    return [UserWithPostsDTO.from_orm(user) for user in users]
```

### Example 5: Generator for Memory Efficiency

```python
# ❌ ISSUE: Loads entire dataset into memory
def process_large_file(filepath: str) -> list[str]:
    """Process a large file."""
    lines = []
    with open(filepath) as f:
        for line in f:
            lines.append(process_line(line))
    return lines

# ✅ FIXED: Use generator for lazy evaluation
from typing import Generator

def process_large_file(filepath: str) -> Generator[str, None, None]:
    """Process a large file with lazy evaluation.

    Yields:
        Processed lines one at a time.
    """
    with open(filepath) as f:
        for line in f:
            yield process_line(line)

# Usage:
for processed_line in process_large_file("huge_file.txt"):
    save_to_db(processed_line)  # Memory constant, not O(n)
```

## Best Practices

### 1. Docstring Convention (Google Style)

```python
def calculate_discount(
    total: float,
    customer_type: str,
    items_count: int = 1
) -> float:
    """Calculate discount based on customer type and purchase amount.

    Args:
        total: Total purchase amount in dollars.
        customer_type: One of 'gold', 'silver', or 'standard'.
        items_count: Number of items purchased. Defaults to 1.

    Returns:
        Discount amount to apply.

    Raises:
        ValueError: If total is negative or customer_type is invalid.

    Examples:
        >>> calculate_discount(100.0, 'gold')
        20.0
        >>> calculate_discount(50.0, 'silver', items_count=2)
        5.0
    """
    if total < 0:
        raise ValueError("total must be non-negative")

    discounts = {'gold': 0.20, 'silver': 0.10, 'standard': 0.05}
    if customer_type not in discounts:
        raise ValueError(f"Invalid customer_type: {customer_type}")

    return total * discounts[customer_type]
```

### 2. Context Managers

```python
# Use context managers for resource cleanup
from contextlib import contextmanager

@contextmanager
def database_session():
    """Database session context manager."""
    session = create_session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# Usage:
with database_session() as db:
    user = db.query(User).get(1)
    user.name = "Updated"
```

### 3. Dataclasses and TypedDict

```python
from dataclasses import dataclass
from typing import TypedDict

# For simple data classes
@dataclass
class User:
    id: int
    name: str
    email: str
    is_active: bool = True

# For typed dictionaries
class UserDict(TypedDict):
    id: int
    name: str
    email: str
    is_active: bool
```

### 4. List Comprehensions

```python
# Use list comprehensions for clarity
numbers = [1, 2, 3, 4, 5]

# ❌ Not Pythonic
squares = []
for n in numbers:
    squares.append(n ** 2)

# ✅ Pythonic
squares = [n ** 2 for n in numbers]

# With filtering
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
```

## Integration with Other Skills

- **`python-testing-strategy`**: Ensure code is testable
- **`python-performance-tuning`**: Optimize performance issues found
- **`python-type-checking`**: Validate type hints with mypy
- **`fastapi-setup`**: Review adherence to project structure

## Review Checklist

- [ ] PEP 8 compliance (use black/flake8)
- [ ] Complete type hints (mypy --strict)
- [ ] Docstrings for all public functions
- [ ] No hardcoded credentials or secrets
- [ ] Proper error handling (specific exceptions)
- [ ] No bare except clauses
- [ ] Async/await used correctly
- [ ] Database queries optimized (no N+1)
- [ ] Security checks (bandit)
- [ ] Code coverage >= 80%
- [ ] No unnecessary imports
- [ ] Functions under 20 lines (preferably)
