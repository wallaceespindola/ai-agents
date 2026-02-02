---
name: fastapi-setup
description: Generate FastAPI project structures with best practices, authentication, and documentation
---

# FastAPI Setup Skill

## When to Use This Skill

- Creating new FastAPI project structures
- Setting up API project with proper layering
- Implementing authentication and authorization
- Configuring database connections and ORM setup
- Generating API documentation and OpenAPI schemas
- Setting up dependency injection patterns
- Implementing middleware and error handling
- Configuring CORS, request validation, and logging

## Quick Start

```
/fastapi-setup <project_name_and_requirements>
```

**Example**:
```
/fastapi-setup User management API with JWT auth and MongoDB
```

## How It Works

The skill generates production-ready FastAPI projects with complete structure:

### 1. Project Structure
- **main.py**: Application entry point
- **config.py**: Configuration management
- **routes/**: API endpoint modules
- **models/**: Database models and schemas
- **services/**: Business logic layer
- **dependencies.py**: Dependency injection
- **middleware/**: Custom middleware
- **utils/**: Helper functions

### 2. API Layer Design
- **Router-based organization**: Group endpoints by resource
- **Request/Response Models**: Pydantic for validation
- **Status codes**: Proper HTTP status responses
- **Error handling**: Comprehensive exception handling
- **Documentation**: Automatic OpenAPI generation

### 3. Authentication & Security
- **JWT Tokens**: Token-based authentication
- **OAuth2**: OAuth2 password flow
- **Scopes**: Fine-grained permission control
- **CORS**: Cross-origin resource sharing
- **HTTPS**: Secure communication
- **Password hashing**: Bcrypt password management

### 4. Database Integration
- **SQLAlchemy ORM**: Database abstraction
- **Alembic**: Database migrations
- **Connection pooling**: Efficient database access
- **Async support**: Async database queries
- **Session management**: Transaction handling

### 5. Dependency Injection
- **FastAPI Depends**: Built-in dependency system
- **Scopes**: Request, app, global scopes
- **Caching**: Dependency result caching
- **Composition**: Complex dependency chains

### 6. Middleware & Error Handling
- **Request logging**: Track all requests
- **Error handlers**: Global exception handling
- **CORS middleware**: Handle cross-origin requests
- **Response middleware**: Transform responses
- **Timing middleware**: Request duration tracking

### 7. Testing & Documentation
- **OpenAPI documentation**: Auto-generated API docs
- **Swagger UI**: Interactive API explorer
- **ReDoc**: Alternative documentation
- **Test client**: FastAPI test utilities

## Configuration

**pyproject.toml**:
```toml
[project]
name = "api-service"
version = "0.1.0"

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.109.0"
uvicorn = "^0.27.0"
sqlalchemy = "^2.0.23"
alembic = "^1.13.1"
pydantic = "^2.5.0"
pydantic-settings = "^2.1.0"
python-jose = "^3.3.0"
python-multipart = "^0.0.6"
bcrypt = "^4.1.1"
passlib = "^1.7.4"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.3"
pytest-asyncio = "^0.21.1"
httpx = "^0.25.2"
```

**requirements.txt**:
```
fastapi==0.109.0
uvicorn[standard]==0.27.0
sqlalchemy==2.0.23
alembic==1.13.1
pydantic==2.5.0
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
python-multipart==0.0.6
bcrypt==4.1.1
passlib[bcrypt]==1.7.4
```

**Makefile**:
```makefile
setup:
	uv sync

dev:
	uv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

test:
	uv run pytest tests/

test-cov:
	uv run pytest tests/ --cov=src

lint:
	uv run ruff check src/

format:
	uv run ruff format src/
```

## Examples

### Example 1: Project Structure and Main Application

```python
# src/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.routes import users, items, auth
from src.middleware import request_logging

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    description="User and Item Management API"
)

# Add middleware
app.add_middleware(request_logging.RequestLoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(items.router, prefix="/api/items", tags=["items"])


@app.get("/health")
async def health_check() -> dict:
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )


# src/config.py
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application configuration"""

    # Project
    PROJECT_NAME: str = "API Service"
    VERSION: str = "0.1.0"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str
    DATABASE_ECHO: bool = DEBUG

    # Authentication
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"


settings = Settings()
```

### Example 2: Models and Schemas

```python
# src/models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="items")


# src/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True
```

### Example 3: Authentication with JWT

```python
# src/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from src.config import settings
from src.schemas import User, UserCreate
from src.services.user_service import UserService

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hash(password: str) -> str:
    """Hash password using bcrypt"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Create JWT access token"""
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Verify JWT token and return current user"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user_service = UserService()
    user = await user_service.get_by_email(email)

    if user is None:
        raise credentials_exception

    return user


@router.post("/register")
async def register(user_create: UserCreate) -> dict:
    """Register new user"""
    user_service = UserService()

    existing = await user_service.get_by_email(user_create.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = get_password_hash(user_create.password)
    user = await user_service.create(
        email=user_create.email,
        username=user_create.username,
        hashed_password=hashed_password
    )

    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> dict:
    """Login with email and password"""
    user_service = UserService()
    user = await user_service.get_by_email(form_data.username)

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
```

### Example 4: Resource Routes

```python
# src/routes/users.py
from fastapi import APIRouter, HTTPException, status, Depends
from src.schemas import User, UserCreate, UserUpdate
from src.services.user_service import UserService
from src.routes.auth import get_current_user

router = APIRouter()


@router.get("/me", response_model=User)
async def get_current_user_profile(
    current_user: User = Depends(get_current_user)
) -> User:
    """Get current user profile"""
    return current_user


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int) -> User:
    """Get user by ID"""
    service = UserService()
    user = await service.get_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


@router.put("/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user)
) -> User:
    """Update user"""
    # Check authorization
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized"
        )

    service = UserService()
    updated_user = await service.update(user_id, user_update.dict(exclude_unset=True))

    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return updated_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    current_user: User = Depends(get_current_user)
) -> None:
    """Delete user"""
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized"
        )

    service = UserService()
    success = await service.delete(user_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
```

### Example 5: Dependency Injection

```python
# src/dependencies.py
from sqlalchemy.orm import Session
from fastapi import Depends
from src.database import SessionLocal


def get_db() -> Session:
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# src/services/user_service.py
from sqlalchemy.orm import Session
from fastapi import Depends
from src.models import User
from src.dependencies import get_db


class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    async def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    async def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    async def create(self, **kwargs) -> User:
        user = User(**kwargs)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    async def update(self, user_id: int, data: dict) -> User | None:
        user = await self.get_by_id(user_id)
        if not user:
            return None

        for key, value in data.items():
            setattr(user, key, value)

        self.db.commit()
        self.db.refresh(user)
        return user

    async def delete(self, user_id: int) -> bool:
        user = await self.get_by_id(user_id)
        if not user:
            return False

        self.db.delete(user)
        self.db.commit()
        return True
```

## Best Practices

### 1. Project Organization
- Keep routes, models, services, and schemas separated
- Use routers for logical grouping of endpoints
- Implement consistent naming conventions
- Keep dependencies at the top level (main.py)

### 2. Error Handling
```python
from fastapi import HTTPException, status

# Use appropriate status codes
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Resource not found"
)
```

### 3. Request Validation
- Use Pydantic models for all request bodies
- Leverage Pydantic validators for complex validation
- Return appropriate status codes

### 4. Documentation
- FastAPI auto-generates OpenAPI schema
- Add descriptions to endpoints
- Document request/response models
- Visit `/docs` for interactive Swagger UI

## Integration with Other Skills

- **`python-testing-strategy`**: Unit and integration tests for endpoints
- **`cicd-pipeline-setup`**: Automated API testing and deployment
- **`api-design`**: RESTful API design principles
- **`database-schema-design`**: Optimal database schema for FastAPI

