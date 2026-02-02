---
name: api-testing-setup
description: Set up API testing frameworks for REST and GraphQL endpoints
---

# API Testing Setup Skill

## When to Use This Skill

- Setting up API test automation
- Testing REST and GraphQL APIs
- Mocking API responses
- Performance testing APIs
- Contract testing
- Load testing endpoints

## Quick Start

```
/api-testing-setup <api_type_and_endpoints>
```

## Popular API Testing Tools

- **Postman**: UI-based, easy to use
- **REST Assured**: Java testing framework
- **pytest + requests**: Python HTTP testing
- **Jest + supertest**: Node.js API testing
- **Apollo Client Testing**: GraphQL testing

## Example: API Tests with Jest

```javascript
describe('User API', () => {
  test('GET /users should return list', async () => {
    const response = await fetch('/api/users');
    expect(response.status).toBe(200);
    const users = await response.json();
    expect(Array.isArray(users)).toBe(true);
  });

  test('POST /users should create user', async () => {
    const response = await fetch('/api/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: 'John', email: 'john@example.com' })
    });
    expect(response.status).toBe(201);
    const user = await response.json();
    expect(user.id).toBeDefined();
  });

  test('GET /users/:id should return specific user', async () => {
    const response = await fetch('/api/users/1');
    expect(response.status).toBe(200);
    const user = await response.json();
    expect(user.id).toBe(1);
  });

  test('DELETE /users/:id should delete user', async () => {
    const response = await fetch('/api/users/1', { method: 'DELETE' });
    expect(response.status).toBe(204);
  });
});
```

## GraphQL Testing Example

```javascript
test('GraphQL query should fetch user', async () => {
  const response = await fetch('/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query: `
        query {
          user(id: 1) {
            id
            name
            email
          }
        }
      `
    })
  });

  const result = await response.json();
  expect(result.data.user.id).toBe(1);
});
```

## Best Practices

1. **Test all HTTP methods**: GET, POST, PUT, DELETE, PATCH
2. **Verify status codes**: 200, 201, 400, 401, 404, 500
3. **Validate response structure**: Check schema
4. **Test error scenarios**: Invalid input, auth failure
5. **Mock external APIs**: Avoid external dependencies
6. **Performance**: Test response time < threshold

## Integration with Other Skills

- **`api-design`**: API specification
- **`test-automation-setup`**: Test framework setup
- **`cicd-pipeline-setup`**: API tests in CI/CD

