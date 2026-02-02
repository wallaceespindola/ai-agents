---
name: api-design
description: Design RESTful and GraphQL APIs with consistency, scalability, and developer experience
---

# API Design Skill

## When to Use This Skill

- Designing REST APIs
- Designing GraphQL schemas
- Creating API contracts and specifications
- Planning API versioning
- Error handling strategies
- Authentication and authorization design
- Rate limiting and quota management

## Quick Start

```
/api-design <api_type_and_domain>
```

**Example**:
```
/api-design REST API for e-commerce with product search and orders
```

## How It Works

### REST API Design

#### Naming Conventions
```
GET    /api/v1/users                 # List users
GET    /api/v1/users/:id             # Get user
POST   /api/v1/users                 # Create user
PUT    /api/v1/users/:id             # Replace user
PATCH  /api/v1/users/:id             # Partial update
DELETE /api/v1/users/:id             # Delete user

# Nested resources
GET    /api/v1/users/:id/orders      # User's orders
GET    /api/v1/users/:id/orders/:oid # Specific order
```

#### Status Codes
```
200: Success
201: Created
204: No content
400: Bad request
401: Unauthorized
403: Forbidden
404: Not found
409: Conflict
429: Too many requests
500: Server error
503: Service unavailable
```

#### Request/Response Format
```json
{
  "data": {
    "id": 1,
    "name": "John",
    "email": "john@example.com"
  },
  "meta": {
    "timestamp": "2024-02-02T10:00:00Z"
  }
}

// Errors
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

#### Pagination
```
GET /api/v1/users?page=1&limit=20&sort=-created_at

Response:
{
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 1000,
    "pages": 50
  }
}
```

### GraphQL API Design

#### Schema Example
```graphql
type User {
  id: ID!
  name: String!
  email: String!
  orders: [Order!]!
  createdAt: DateTime!
}

type Order {
  id: ID!
  user: User!
  items: [OrderItem!]!
  total: Float!
  status: OrderStatus!
}

enum OrderStatus {
  PENDING
  PROCESSING
  SHIPPED
  DELIVERED
  CANCELLED
}

type Query {
  user(id: ID!): User
  users(first: Int, after: String): UserConnection!
  search(query: String!): [SearchResult!]!
}

type Mutation {
  createUser(input: CreateUserInput!): User!
  updateUser(id: ID!, input: UpdateUserInput!): User!
  deleteUser(id: ID!): Boolean!
}

input CreateUserInput {
  name: String!
  email: String!
  password: String!
}
```

### API Security

#### Authentication Methods
- API Keys: Simple but limited
- OAuth2: Industry standard
- JWT: Stateless tokens
- mTLS: Mutual certificate authentication

#### Authorization
```python
@app.get("/api/v1/users/:id")
def get_user(user_id: str, current_user: User = Depends(get_current_user)):
    # Check permission
    if not has_permission(current_user, "user:read", user_id):
        raise HTTPException(status_code=403, detail="Forbidden")
    return get_user_data(user_id)
```

## Examples

### Example 1: Complete REST API Design

```markdown
# User Management API v1

## Overview
RESTful API for user management with CRUD operations.

## Base URL
`https://api.example.com/v1`

## Authentication
Bearer token in Authorization header:
```
Authorization: Bearer <token>
```

## Endpoints

### List Users
```
GET /users?page=1&limit=20&role=admin&sort=-created_at
```

**Response**:
```json
{
  "data": [
    {
      "id": "usr_123",
      "name": "John Doe",
      "email": "john@example.com",
      "role": "admin",
      "created_at": "2024-01-15T10:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
```

### Create User
```
POST /users
Content-Type: application/json
Authorization: Bearer <token>
```

**Request**:
```json
{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "role": "user"
}
```

**Response** (201 Created):
```json
{
  "data": {
    "id": "usr_456",
    "name": "Jane Smith",
    "email": "jane@example.com",
    "role": "user",
    "created_at": "2024-02-02T10:00:00Z"
  }
}
```

### Update User
```
PATCH /users/:id
Content-Type: application/json
Authorization: Bearer <token>
```

**Request**:
```json
{
  "name": "Jane Doe"
}
```

**Response** (200 OK):
```json
{
  "data": {
    "id": "usr_456",
    "name": "Jane Doe",
    "email": "jane@example.com",
    "role": "user"
  }
}
```

### Delete User
```
DELETE /users/:id
Authorization: Bearer <token>
```

**Response** (204 No Content)

## Error Responses

### 400 Bad Request
```json
{
  "error": {
    "code": "INVALID_INPUT",
    "message": "Validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

### 401 Unauthorized
```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Invalid or missing authentication token"
  }
}
```

### 429 Too Many Requests
```json
{
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many requests",
    "retry_after": 60
  }
}
```

## Rate Limiting

- Authenticated: 1000 requests/hour
- Public: 100 requests/hour
- Batch operations: 50 requests/hour

Limits in response headers:
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1706862000
```

## Versioning

- API versioned in URL: `/v1`, `/v2`
- Deprecation warnings in headers
- Sunset header indicates end of support
```
Deprecation: true
Sunset: Sun, 31 Dec 2025 23:59:59 GMT
```
```

### Example 2: GraphQL Query Examples

```graphql
# Query users with their orders
query {
  users(first: 10) {
    edges {
      node {
        id
        name
        email
        orders {
          id
          total
          status
        }
      }
    }
  }
}

# Search with filters
query {
  search(query: "laptop", filters: {category: "electronics", minPrice: 500}) {
    ... on Product {
      id
      name
      price
    }
    ... on Article {
      id
      title
      content
    }
  }
}

# Mutation with input
mutation {
  createUser(input: {name: "John", email: "john@example.com"}) {
    id
    name
    email
  }
}
```

## Best Practices

1. **Consistency**: Uniform naming and structure
2. **Documentation**: OpenAPI/Swagger spec
3. **Versioning**: Plan for API evolution
4. **Rate Limiting**: Protect from abuse
5. **Monitoring**: Track usage and errors
6. **Security**: Proper auth and validation

## Integration with Other Skills

- **`system-design-doc`**: API design documentation
- **`backend-testing-setup`**: API test automation
- **`monitoring-setup`**: API metrics tracking
- **`security-scanning`**: API security review

