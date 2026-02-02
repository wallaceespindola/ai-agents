---
name: python-type-checking
description: Add comprehensive type hints to Python code and configure mypy for static type checking
---

# Python Type Checking Skill

## When to Use This Skill

- Adding type hints to existing Python codebases
- Setting up mypy for static type checking
- Converting untyped functions to properly typed ones
- Integrating type checking into CI/CD pipelines
- Catching type errors before runtime
- Improving IDE autocompletion and documentation
- Migrating to Python 3.10+ type syntax
- Handling complex typing scenarios (generics, protocols, unions)

## Quick Start

```
/python-type-checking <module_or_file>
```

**Example**:
```
/python-type-checking User service with complex data models
```

## How It Works

The skill provides comprehensive type hints and mypy configuration:

### 1. Type Hint Basics
- **Function Signatures**: Input and return types
- **Variables**: Type annotations for better clarity
- **Collections**: List[T], Dict[K, V], Set[T], Tuple[T, ...]
- **Optional Types**: Optional[T] for nullable values
- **Union Types**: Union[T1, T2] or T1 | T2 (Python 3.10+)

### 2. Advanced Typing
- **Generics**: TypeVar for generic functions and classes
- **Protocols**: Structural subtyping for duck typing
- **Literal**: Specific string or numeric values
- **Type Aliases**: Named types for complex definitions

### 3. Mypy Configuration
- **Strictness Levels**: From basic to very strict checking
- **Per-Module Configuration**: Override globally
- **Type Stubs**: .pyi files for untyped libraries
- **Plugin System**: Custom type checking rules

### 4. Common Type Patterns
- **Class Methods**: cls parameter typing
- **Static Methods**: No self/cls
- **Decorators**: Callable type annotations
- **Context Managers**: __enter__ and __exit__ typing

### 5. Type Checking Workflow
- **Static Analysis**: mypy without running code
- **Type Inference**: mypy infers types when possible
- **Error Reporting**: Clear error messages with locations
- **Integration**: Pre-commit hooks and CI/CD

### 6. Migration Strategy
- **Gradual Typing**: Start with important modules
- **Type Stubs**: Use .pyi for external libraries
- **Allowlist Untyped**: Mark modules as untyped initially
- **Iterative Improvement**: Increase strictness over time

### 7. Runtime Type Checking
- **Type Guards**: Custom type narrowing
- **Pydantic**: Runtime validation with types
- **dataclasses**: Type-aware data containers
- **TypedDict**: Typed dictionaries

## Configuration

**pyproject.toml**:
```toml
[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_calls = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
strict_equality = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
disallow_untyped_calls = false

[[tool.mypy.overrides]]
module = "external_library"
ignore_missing_imports = true
```

**requirements-dev.txt**:
```
mypy==1.7.1
types-requests==2.31.0.10
types-redis==4.6.0.11
types-pyyaml==6.0.12.12
pydantic==2.5.0
```

**Makefile**:
```makefile
type-check:
	mypy src/

type-check-strict:
	mypy src/ --strict

type-check-report:
	mypy src/ --html mypy-report
```

## Examples

### Example 1: Basic Type Hints

```python
# ❌ NO TYPE HINTS
def add_numbers(a, b):
    return a + b

def process_users(users):
    result = []
    for user in users:
        result.append({"name": user["name"], "age": user["age"]})
    return result


# ✅ WITH TYPE HINTS
def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the sum."""
    return a + b


def process_users(users: list[dict[str, str | int]]) -> list[dict[str, str | int]]:
    """Process list of users and return filtered users."""
    result: list[dict[str, str | int]] = []
    for user in users:
        result.append({"name": user["name"], "age": user["age"]})
    return result
```

### Example 2: Complex Type Annotations

```python
from typing import TypeVar, Generic, Optional, Union, Callable
from dataclasses import dataclass


# ✅ GENERIC CLASS
T = TypeVar('T')

class Container(Generic[T]):
    """Generic container that holds a value of type T"""

    def __init__(self, value: T) -> None:
        self.value = value

    def get_value(self) -> T:
        return self.value

    def map(self, func: Callable[[T], T]) -> 'Container[T]':
        return Container(func(self.value))


# ✅ UNION AND OPTIONAL TYPES
def process_data(data: Union[str, int, float]) -> str:
    """Process data that could be multiple types"""
    return str(data)


def find_user(user_id: Optional[int] = None) -> Optional[dict]:
    """Find user by ID, returns None if not found"""
    if user_id is None:
        return None
    # Lookup logic...
    return {"id": user_id}


# ✅ TYPE ALIASES for complex types
UserId = int
UserData = dict[str, Union[str, int, float]]
UserCallback = Callable[[UserId], Optional[UserData]]


def register_callback(user_id: UserId, callback: UserCallback) -> None:
    """Register callback for user events"""
    pass


# ✅ DATACLASS WITH TYPES
@dataclass
class User:
    id: int
    name: str
    email: str
    age: Optional[int] = None

    def display(self) -> str:
        return f"{self.name} ({self.email})"
```

### Example 3: Mypy Configuration and Strict Mode

```python
# src/user_service.py
# mypy: disallow_untyped_defs = True

from typing import Optional, Any
from .models import User


class UserService:
    """Service for managing users"""

    def __init__(self, repository: Any) -> None:
        self.repository = repository

    def create_user(
        self,
        name: str,
        email: str,
        age: Optional[int] = None
    ) -> User:
        """Create a new user"""
        user = User(name=name, email=email, age=age)
        return self.repository.save(user)

    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID, returns None if not found"""
        return self.repository.find_by_id(user_id)

    def update_user(self, user_id: int, **kwargs: Any) -> User:
        """Update user with provided fields"""
        user = self.get_user(user_id)
        if user is None:
            raise ValueError(f"User {user_id} not found")

        for key, value in kwargs.items():
            setattr(user, key, value)

        return self.repository.save(user)


# ❌ MYPY ERRORS
class BadUserService:
    def create_user(self, name, email) -> User:  # Missing type hints
        user = User(name=name, email=email)
        return user  # Actually returns User

    def get_user(self, user_id: str) -> User:  # Wrong type
        return self.repository.find_by_id(user_id)  # Maybe None
```

### Example 4: Type Guards and Type Narrowing

```python
from typing import TypeGuard, Union


class Dog:
    def bark(self) -> None:
        print("Woof!")


class Cat:
    def meow(self) -> None:
        print("Meow!")


# ✅ TYPE GUARD FUNCTION
def is_dog(animal: Union[Dog, Cat]) -> TypeGuard[Dog]:
    """Type guard to check if animal is a Dog"""
    return isinstance(animal, Dog)


def is_cat(animal: Union[Dog, Cat]) -> TypeGuard[Cat]:
    """Type guard to check if animal is a Cat"""
    return isinstance(animal, Cat)


def make_sound(animal: Union[Dog, Cat]) -> None:
    """Make sound based on animal type"""
    if is_dog(animal):
        animal.bark()  # mypy knows animal is Dog
    elif is_cat(animal):
        animal.meow()  # mypy knows animal is Cat


# ✅ LITERAL TYPES
from typing import Literal

def process_event(event_type: Literal["create", "update", "delete"]) -> None:
    """Process events of specific types"""
    if event_type == "create":
        print("Creating...")
    elif event_type == "update":
        print("Updating...")
    elif event_type == "delete":
        print("Deleting...")
    # mypy catches invalid event types
```

### Example 5: Protocol for Structural Typing

```python
from typing import Protocol, runtime_checkable


# ✅ PROTOCOL: Define interface without inheritance
@runtime_checkable
class Drawable(Protocol):
    """Anything with a draw method"""

    def draw(self) -> str:
        ...


class Circle:
    def draw(self) -> str:
        return "●"


class Square:
    def draw(self) -> str:
        return "■"


def render(shape: Drawable) -> None:
    """Render any object that has a draw method"""
    print(shape.draw())  # Works with Circle, Square, any Drawable


# Usage
circle = Circle()
render(circle)  # Valid - Circle has draw() method

square = Square()
render(square)  # Valid - Square has draw() method


# ✅ PROTOCOL WITH ATTRIBUTES
@runtime_checkable
class Sized(Protocol):
    """Anything with a length"""

    def __len__(self) -> int:
        ...


def get_size(obj: Sized) -> int:
    """Get size of any object with __len__"""
    return len(obj)


get_size([1, 2, 3])  # list has __len__
get_size("hello")    # str has __len__
get_size({1: 2})     # dict has __len__
```

### Example 6: Pydantic for Runtime Type Validation

```python
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from datetime import datetime


class UserModel(BaseModel):
    """User model with runtime type validation"""

    id: int
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, le=150)
    created_at: datetime = Field(default_factory=datetime.now)

    @validator('name')
    def name_must_not_be_numeric(cls, v):
        if v.isnumeric():
            raise ValueError('Name cannot be numeric')
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe",
                "email": "john@example.com",
                "age": 30
            }
        }


# Runtime validation
try:
    user = UserModel(
        id=1,
        name="John Doe",
        email="john@example.com",
        age=30
    )
    print(user)
except ValueError as e:
    print(f"Validation error: {e}")


# Invalid data raises ValueError
try:
    bad_user = UserModel(
        id=1,
        name="John",
        email="invalid-email",
        age=30
    )
except ValueError as e:
    print(f"Validation error: {e}")
```

### Example 7: Migration from Untyped Code

```python
# STEP 1: Original untyped code
def calculate_total(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total


# STEP 2: Add basic types
def calculate_total(items: list[dict]) -> float:
    total: float = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total


# STEP 3: Use typed data structures
from typing import TypedDict

class Item(TypedDict):
    price: float
    quantity: int


def calculate_total(items: list[Item]) -> float:
    total: float = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total


# STEP 4: Use dataclass for better clarity
from dataclasses import dataclass

@dataclass
class ItemData:
    price: float
    quantity: int


def calculate_total(items: list[ItemData]) -> float:
    return sum(item.price * item.quantity for item in items)
```

## Best Practices

### 1. Type Checking Strategy
- Start with function signatures
- Add types to critical data structures
- Use strict mode for new code
- Gradually migrate existing code

### 2. Dealing with Untyped Libraries
```python
# Use type stubs (.pyi files) or ignore missing imports
# In myproject/py.typed file (marker for PEP 561)

# In myproject/__init__.pyi
from external_lib import function

declare function: Callable[[int], str]
```

### 3. Common Type Patterns
```python
# Optional values
user: Optional[User] = get_user(1)

# Functions as parameters
callback: Callable[[int, str], bool] = process_event

# Variable length arguments
def process(*args: int, **kwargs: str) -> None:
    pass

# Class types
def instantiate(cls: type[T]) -> T:
    return cls()
```

### 4. Performance Considerations
- Type hints have zero runtime overhead in Python
- mypy analysis can be slow on large codebases
- Use incremental mode for faster checks
- Consider type checking in CI/CD, not every save

### 5. Documentation via Types
```python
def fetch_users(
    skip: int = 0,
    limit: int = 10,
    filter_active: bool = True
) -> list[User]:
    """Fetch users with pagination and filtering"""
    pass
```

## Integration with Other Skills

- **`python-code-review`**: Type checking as part of code review
- **`python-testing-strategy`**: Type-safe test fixtures
- **`python-documentation`**: Types as inline documentation
- **`cicd-pipeline-setup`**: Type checking in CI/CD pipeline

