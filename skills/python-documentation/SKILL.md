---
name: python-documentation
description: Create comprehensive docstrings and technical documentation for Python projects
---

# Python Documentation Skill

## When to Use This Skill

- Adding docstrings to Python modules, functions, and classes
- Creating technical documentation for APIs and libraries
- Generating documentation from docstrings with Sphinx
- Writing README files and setup guides
- Creating architecture documentation
- Documenting configuration options
- Writing examples and tutorials
- Setting up API reference documentation

## Quick Start

```
/python-documentation <module_or_project_name>
```

**Example**:
```
/python-documentation FastAPI user service with complex models
```

## How It Works

The skill creates comprehensive documentation with multiple formats:

### 1. Docstring Styles
- **Google Style**: Popular, readable format
- **NumPy Style**: Scientific computing convention
- **reStructuredText**: Sphinx-compatible format
- **Epydoc**: Tool-friendly markup

### 2. Documentation Levels
- **Module**: Overview and purpose
- **Class**: Purpose, attributes, methods
- **Function**: Parameters, return value, exceptions
- **Attributes**: Type and description

### 3. Tools and Frameworks
- **Sphinx**: Documentation generator
- **Google docstring parser**: Parses Google-style docstrings
- **Autodoc**: Auto-generate API docs from code
- **Read the Docs**: Hosting for project documentation

### 4. Documentation Structure
- **Overview**: Project purpose and features
- **Installation**: How to install
- **Quick Start**: Basic usage example
- **API Reference**: Complete API documentation
- **Examples**: Detailed usage examples
- **Contributing**: How to contribute

### 5. API Documentation Generation
- **Auto-discovery**: Find all modules and classes
- **Signature extraction**: Parse function signatures
- **Type hints as documentation**: Use types for clarity
- **HTML generation**: Styled API docs

### 6. Example Documentation
- **Code examples**: Runnable examples
- **Use cases**: Real-world scenarios
- **Common patterns**: Best practices
- **Troubleshooting**: Known issues and solutions

### 7. Deployment
- **Read the Docs**: Cloud hosting
- **GitHub Pages**: Static site hosting
- **Local hosting**: Self-hosted documentation
- **Version management**: Multiple documentation versions

## Configuration

**sphinx/conf.py**:
```python
project = 'My Project'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
```

**requirements-docs.txt**:
```
sphinx==7.2.6
sphinx-rtd-theme==2.0.0
sphinx-autodoc-typehints==1.25.3
myst-parser==2.0.0
```

**Makefile**:
```makefile
docs-build:
	cd docs && make html

docs-serve:
	cd docs && python -m http.server 8000

docs-clean:
	cd docs && make clean
```

## Examples

### Example 1: Function Documentation

```python
# ❌ NO DOCUMENTATION
def calculate_total(items, tax_rate):
    result = 0
    for item in items:
        result += item['price'] * item['quantity']
    return result * (1 + tax_rate)


# ✅ GOOGLE STYLE DOCSTRING
def calculate_total(items: list[dict], tax_rate: float) -> float:
    """Calculate total price including tax for a list of items.

    This function computes the sum of all item prices (quantity * price)
    and applies the given tax rate.

    Args:
        items: List of item dictionaries with 'price' and 'quantity' keys.
        tax_rate: Tax rate as decimal (0.1 for 10% tax).

    Returns:
        Total price including tax, rounded to 2 decimal places.

    Raises:
        ValueError: If tax_rate is negative or items is empty.
        KeyError: If items don't contain 'price' or 'quantity' keys.

    Example:
        >>> items = [
        ...     {"price": 100.0, "quantity": 2},
        ...     {"price": 50.0, "quantity": 1}
        ... ]
        >>> calculate_total(items, 0.1)
        275.0

    Note:
        Tax rate should be between 0 and 1 (e.g., 0.1 for 10%).
    """
    if not items:
        raise ValueError("Items list cannot be empty")

    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")

    total = sum(item['price'] * item['quantity'] for item in items)
    return round(total * (1 + tax_rate), 2)


# ✅ NUMPY STYLE DOCSTRING
def calculate_total(items: list[dict], tax_rate: float) -> float:
    """Calculate total price including tax for a list of items.

    Parameters
    ----------
    items : list[dict]
        List of item dictionaries with 'price' and 'quantity' keys.
    tax_rate : float
        Tax rate as decimal (0.1 for 10% tax).

    Returns
    -------
    float
        Total price including tax, rounded to 2 decimal places.

    Raises
    ------
    ValueError
        If tax_rate is negative or items is empty.
    KeyError
        If items don't contain 'price' or 'quantity' keys.

    Examples
    --------
    >>> items = [
    ...     {"price": 100.0, "quantity": 2},
    ...     {"price": 50.0, "quantity": 1}
    ... ]
    >>> calculate_total(items, 0.1)
    275.0

    Notes
    -----
    Tax rate should be between 0 and 1 (e.g., 0.1 for 10%).
    """
    pass
```

### Example 2: Class Documentation

```python
class UserService:
    """Service for managing user operations.

    This service provides methods for creating, updating, retrieving,
    and deleting users from the database. It includes authentication
    and authorization checks.

    Attributes:
        database (DatabaseConnection): Connection to the user database.
        logger (Logger): Logger instance for debugging.
        cache (RedisClient): Cache for frequently accessed users.

    Example:
        >>> service = UserService(db_connection)
        >>> user = service.create_user("john@example.com", "John Doe")
        >>> retrieved = service.get_user(user.id)
        >>> service.update_user(user.id, name="Jane Doe")
        >>> service.delete_user(user.id)
    """

    def __init__(self, database: DatabaseConnection):
        """Initialize UserService with database connection.

        Args:
            database: Active database connection instance.

        Raises:
            ConnectionError: If database connection fails.
        """
        self.database = database
        self.logger = logging.getLogger(__name__)

    def create_user(self, email: str, name: str, password: str) -> User:
        """Create a new user account.

        Args:
            email: User's email address (must be unique).
            name: User's display name.
            password: User's password (will be hashed).

        Returns:
            Created User object with assigned ID.

        Raises:
            ValueError: If email already exists.
            ValueError: If email format is invalid.
            ValueError: If password is too weak.

        Note:
            Password is hashed using bcrypt before storage.
        """
        if not self._is_valid_email(email):
            raise ValueError(f"Invalid email format: {email}")

        if self.database.user_exists(email):
            raise ValueError(f"Email already registered: {email}")

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User(email=email, name=name, hashed_password=hashed_password)

        self.database.save(user)
        self.logger.info(f"Created user: {email}")

        return user

    def get_user(self, user_id: int) -> User | None:
        """Retrieve user by ID.

        Args:
            user_id: The user's ID.

        Returns:
            User object if found, None otherwise.

        Raises:
            ValueError: If user_id is not a positive integer.

        Example:
            >>> user = service.get_user(123)
            >>> if user:
            ...     print(f"Found: {user.name}")
        """
        if user_id <= 0:
            raise ValueError("user_id must be positive")

        return self.database.get_user(user_id)
```

### Example 3: Module Documentation

```python
# src/user_models.py
"""User data models and schemas for the authentication system.

This module contains:
- User model: Database representation of users
- UserSchema: API request/response schema
- UserUpdate: Schema for user updates
- PasswordValidator: Password validation rules

The models use SQLAlchemy for database operations and Pydantic
for API validation.

Example:
    >>> from src.user_models import User, UserSchema
    >>> user = User(email="john@example.com", name="John Doe")
    >>> schema = UserSchema.from_orm(user)
    >>> print(schema.json())

Attributes:
    PASSWORD_MIN_LENGTH (int): Minimum password length (8 chars).
    PASSWORD_SPECIAL_CHARS (str): Required special characters.
"""

from sqlalchemy import Column, String, DateTime
from pydantic import BaseModel, EmailStr
from datetime import datetime

PASSWORD_MIN_LENGTH = 8
PASSWORD_SPECIAL_CHARS = "!@#$%^&*"


class User:
    """Database model for users.

    Stores user credentials and metadata in the database.
    """

    def __init__(self, email: str, name: str):
        self.email = email
        self.name = name
        self.created_at = datetime.now()


class UserSchema(BaseModel):
    """Pydantic schema for user API requests and responses.

    Used for validation and serialization of user data.
    """

    id: int
    email: EmailStr
    name: str

    class Config:
        from_attributes = True
```

### Example 4: Complex Function with Type Hints

```python
from typing import Optional, Callable, TypeVar, Generic

T = TypeVar('T')


def retry_on_failure(
    func: Callable[..., T],
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple[type[Exception], ...] = (Exception,)
) -> T:
    """Retry a function on failure with exponential backoff.

    Executes the given function with automatic retry logic. If the function
    raises any of the specified exceptions, it will retry up to max_attempts
    times with increasing delay between attempts.

    Args:
        func: Callable to execute and retry on failure.
        max_attempts: Maximum number of execution attempts (default: 3).
        delay: Initial delay in seconds between retries (default: 1.0).
        backoff: Exponential backoff multiplier (default: 2.0).
        exceptions: Tuple of exception types to catch and retry on.

    Returns:
        Result of the function if successful.

    Raises:
        The last exception raised if all attempts fail.

    Example:
        >>> def unstable_api_call():
        ...     # Might fail occasionally
        ...     response = requests.get("https://api.example.com/data")
        ...     response.raise_for_status()
        ...     return response.json()
        ...
        >>> result = retry_on_failure(
        ...     unstable_api_call,
        ...     max_attempts=5,
        ...     delay=0.5
        ... )

    Note:
        The backoff parameter controls how quickly the delay increases:
        - backoff=1.0: No increase (constant delay)
        - backoff=2.0: Delay doubles each attempt (1s, 2s, 4s, ...)
        - backoff=1.5: Delay increases by 50% each attempt

    Warning:
        For network-based functions, consider using delay >0.5 to avoid
        overwhelming the remote service.
    """
    import time

    last_exception = None
    current_delay = delay

    for attempt in range(max_attempts):
        try:
            return func()
        except exceptions as e:
            last_exception = e
            if attempt < max_attempts - 1:
                time.sleep(current_delay)
                current_delay *= backoff

    raise last_exception
```

### Example 5: Sphinx Configuration

```python
# docs/conf.py
"""Sphinx configuration for project documentation."""

import os
import sys

project = 'My API Project'
copyright = '2024, Your Name'
author = 'Your Name'
version = '1.0'
release = '1.0.0'

# Add source directory to path
sys.path.insert(0, os.path.abspath('../src'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Napoleon configuration for Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
```

### Example 6: README Documentation

```markdown
# User Management API

Complete REST API for user management with authentication and authorization.

## Features

- User registration and authentication
- JWT-based authorization
- User profile management
- Role-based access control

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from src.user_service import UserService

# Create service
service = UserService(database_connection)

# Create user
user = service.create_user("john@example.com", "John Doe", "securepass123")

# Retrieve user
retrieved = service.get_user(user.id)
```

## API Documentation

Full API documentation available at `/docs` after starting the server.

### Endpoints

#### POST /api/users/register
Register a new user.

**Request:**
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "name": "John Doe"
}
```
```

### Example 7: Type-Hinted API Documentation

```python
def filter_users(
    users: list['User'],
    filter_func: Callable[['User'], bool],
    sort_key: Callable[['User'], str] | None = None,
    reverse: bool = False
) -> list['User']:
    """Filter and sort users by custom criteria.

    This function allows complex filtering and sorting of user lists
    using callable predicates and key functions.

    Args:
        users: List of User objects to filter.
        filter_func: Callable that returns True for items to keep.
            Example: lambda user: user.is_active
        sort_key: Optional callable to extract sort key from each user.
            Example: lambda user: user.created_at
            If None, results are not sorted.
        reverse: Sort in reverse order if True (default: False).

    Returns:
        Filtered and sorted list of users.

    Raises:
        TypeError: If filter_func or sort_key is not callable.
        ValueError: If users list is empty.

    Example:
        >>> users = [...]
        >>> active_users = filter_users(
        ...     users,
        ...     filter_func=lambda u: u.is_active,
        ...     sort_key=lambda u: u.name,
        ...     reverse=False
        ... )
    """
    if not callable(filter_func):
        raise TypeError("filter_func must be callable")

    if sort_key is not None and not callable(sort_key):
        raise TypeError("sort_key must be callable")

    filtered = [user for user in users if filter_func(user)]

    if sort_key:
        filtered.sort(key=sort_key, reverse=reverse)

    return filtered
```

## Best Practices

### 1. Docstring Standards
- Use consistent style (Google, NumPy, or reStructuredText)
- Document all public functions and classes
- Include parameters, return values, and exceptions
- Provide usage examples for complex functions

### 2. Type Hints + Documentation
```python
# Use type hints for clarity
def process_data(data: list[dict]) -> dict[str, int]:
    """Process data and return summary."""
    pass
```

### 3. Documentation Organization
```
docs/
├── index.rst
├── installation.rst
├── quickstart.rst
├── api/
│   ├── users.rst
│   └── items.rst
└── examples/
    ├── basic_usage.rst
    └── advanced_patterns.rst
```

### 4. Example Quality
- Include imports
- Show realistic use cases
- Explain expected output
- Cover common scenarios

### 5. Maintenance
- Keep documentation in sync with code
- Include docstrings in code reviews
- Use continuous documentation building

## Integration with Other Skills

- **`python-code-review`**: Check for missing documentation
- **`python-type-checking`**: Use type hints in documentation
- **`cicd-pipeline-setup`**: Build and deploy documentation
- **`fastapi-setup`**: Auto-generate API documentation

