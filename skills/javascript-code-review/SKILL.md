---
name: javascript-code-review
description: Review JavaScript and TypeScript code for best practices, performance, and security
---

# JavaScript Code Review Skill

## When to Use This Skill

- Reviewing pull requests for code quality
- Identifying JavaScript/TypeScript anti-patterns
- Enforcing coding standards and best practices
- Checking for performance issues and memory leaks
- Verifying security best practices
- Assessing accessibility and browser compatibility
- Reviewing API design and error handling
- Evaluating code maintainability and readability

## Quick Start

```
/javascript-code-review <file_or_module_name>
```

**Example**:
```
/javascript-code-review React component for user authentication
```

## How It Works

The skill performs comprehensive code review with multiple dimensions:

### 1. Code Quality Dimensions
- **Readability**: Clear variable names, function organization
- **Maintainability**: Low coupling, high cohesion
- **Consistency**: Follows project conventions
- **Complexity**: Functions under 20 lines, cyclomatic complexity
- **Testing**: Adequate test coverage

### 2. JavaScript Best Practices
- **Modern Syntax**: ES6+, destructuring, arrow functions
- **Error Handling**: Try-catch, proper error propagation
- **Async Patterns**: Promise chains vs async/await
- **Object/Array Handling**: Immutability, spread operator
- **Function Design**: Single responsibility, DRY principle

### 3. TypeScript Specific
- **Type Safety**: No any types, proper generics
- **Inference**: Leverage type inference
- **Assertions**: Avoid unnecessary type assertions
- **Strict Mode**: Enable strict compiler options
- **Declaration Files**: Proper .d.ts for modules

### 4. Performance Review
- **Bundle Size**: Tree-shaking, code splitting
- **Runtime Performance**: Unnecessary re-renders, loops
- **Memory Management**: Circular references, event listener cleanup
- **Network**: API call optimization, caching
- **Rendering**: React hooks optimization, memo usage

### 5. Security Review
- **Input Validation**: Sanitize user input
- **XSS Prevention**: Proper escaping, dangerouslySetInnerHTML
- **CSRF Protection**: Token validation
- **Authentication**: Secure token storage
- **Dependencies**: Check for vulnerable packages

### 6. React Specific
- **Hooks**: Proper dependency arrays, custom hooks
- **Components**: Pure components, prop drilling
- **State Management**: Redux, Context API usage
- **Rendering**: Unnecessary renders, memoization
- **Effects**: Cleanup, dependencies

### 7. Testing & Documentation
- **Test Coverage**: Adequate unit and integration tests
- **Comments**: When and what to document
- **JSDoc**: Proper type documentation
- **Examples**: Usage examples for complex code
- **TODOs**: Tracked and addressed

## Configuration

**.eslintrc.json**:
```json
{
  "extends": ["eslint:recommended", "next"],
  "rules": {
    "no-console": ["warn", { "allow": ["warn", "error"] }],
    "no-debugger": "error",
    "prefer-const": "error",
    "no-var": "error",
    "eqeqeq": ["error", "always"],
    "no-implicit-coercion": "error",
    "complexity": ["warn", 10]
  }
}
```

**tsconfig.json**:
```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  }
}
```

## Examples

### Example 1: Code Quality Issues

```typescript
// ❌ PROBLEMATIC CODE
export const UserComponent = (props: any) => {
  const [loading, setLoading] = React.useState(false);

  const handleClick = () => {
    fetch(`/api/users/${props.userId}`)
      .then(res => res.json())
      .then(data => {
        if (data) {
          console.log('Success:', data);
          setLoading(false);
        }
      });
  };

  return (
    <div>
      <button onClick={handleClick}>
        {loading ? 'Loading...' : 'Load User'}
      </button>
    </div>
  );
};

// Issues:
// - No error handling
// - No cleanup for race conditions
// - any type used
// - No loading state management
// - Missing dependencies


// ✅ IMPROVED CODE
interface UserComponentProps {
  userId: string;
}

export const UserComponent: React.FC<UserComponentProps> = ({ userId }) => {
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);

  const handleClick = React.useCallback(async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(`/api/users/${userId}`);

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log('User loaded:', data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error');
    } finally {
      setLoading(false);
    }
  }, [userId]);

  return (
    <div>
      <button onClick={handleClick} disabled={loading}>
        {loading ? 'Loading...' : 'Load User'}
      </button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};
```

### Example 2: TypeScript Type Safety

```typescript
// ❌ PROBLEMATIC: Using any
const processUser = (user: any): any => {
  return {
    name: user.name,
    email: user.email,
    age: user.age
  };
};


// ✅ IMPROVED: Proper types
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

interface ProcessedUser {
  name: string;
  email: string;
  age: number;
}

const processUser = (user: User): ProcessedUser => {
  return {
    name: user.name,
    email: user.email,
    age: user.age
  };
};

// Even better with Pick:
type ProcessedUser = Pick<User, 'name' | 'email' | 'age'>;

const processUser = (user: User): ProcessedUser => {
  const { name, email, age } = user;
  return { name, email, age };
};
```

### Example 3: React Hooks Anti-patterns

```typescript
// ❌ ANTI-PATTERNS
export const DataFetcher = ({ url }: { url: string }) => {
  const [data, setData] = React.useState(null);

  // Missing dependency array - fetches on every render
  React.useEffect(() => {
    fetch(url).then(res => res.json()).then(setData);
  });

  // Stale closure - url might be from old render
  const refetch = () => {
    fetch(url).then(res => res.json()).then(setData);
  };

  return <div onClick={refetch}>{data}</div>;
};


// ✅ IMPROVED
export const DataFetcher = ({ url }: { url: string }) => {
  const [data, setData] = React.useState<any>(null);
  const [error, setError] = React.useState<Error | null>(null);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    let isMounted = true;

    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        const result = await response.json();

        if (isMounted) {
          setData(result);
          setError(null);
        }
      } catch (err) {
        if (isMounted) {
          setError(err instanceof Error ? err : new Error('Unknown error'));
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    };

    fetchData();

    // Cleanup function
    return () => {
      isMounted = false;
    };
  }, [url]); // Proper dependency array

  const refetch = React.useCallback(async () => {
    setLoading(true);
    try {
      const response = await fetch(url);
      const result = await response.json();
      setData(result);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err : new Error('Unknown error'));
    } finally {
      setLoading(false);
    }
  }, [url]);

  return (
    <div>
      {loading && <p>Loading...</p>}
      {error && <p>Error: {error.message}</p>}
      {data && <div>{JSON.stringify(data)}</div>}
      <button onClick={refetch}>Refetch</button>
    </div>
  );
};
```

### Example 4: Error Handling

```typescript
// ❌ POOR ERROR HANDLING
export const submitForm = async (data: any) => {
  const response = await fetch('/api/submit', {
    method: 'POST',
    body: JSON.stringify(data)
  });
  return response.json();
};


// ✅ COMPREHENSIVE ERROR HANDLING
interface ApiError {
  status: number;
  message: string;
  details?: Record<string, any>;
}

export class ApiErrorHandler extends Error {
  constructor(
    public status: number,
    message: string,
    public details?: Record<string, any>
  ) {
    super(message);
    this.name = 'ApiErrorHandler';
  }
}

export const submitForm = async (data: Record<string, any>): Promise<any> => {
  try {
    const response = await fetch('/api/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new ApiErrorHandler(
        response.status,
        errorData.message || 'Request failed',
        errorData.details
      );
    }

    return await response.json();
  } catch (error) {
    if (error instanceof ApiErrorHandler) {
      throw error;
    }

    if (error instanceof TypeError) {
      throw new ApiErrorHandler(0, 'Network error', { originalError: error.message });
    }

    throw new ApiErrorHandler(500, 'Unknown error occurred');
  }
};

// Usage in component
try {
  const result = await submitForm(formData);
} catch (error) {
  if (error instanceof ApiErrorHandler) {
    console.error(`API Error [${error.status}]: ${error.message}`);
  }
}
```

### Example 5: Performance Optimization

```typescript
// ❌ PERFORMANCE ISSUES
export const UserList = ({ users }: { users: User[] }) => {
  const [filter, setFilter] = React.useState('');

  // Filtering runs on every render
  const filtered = users.filter(u => u.name.includes(filter));

  // Re-renders all children even if they don't change
  return (
    <div>
      <input onChange={e => setFilter(e.target.value)} />
      {filtered.map(user => (
        <UserRow key={user.id} user={user} onDelete={() => {}} />
      ))}
    </div>
  );
};


// ✅ OPTIMIZED
interface UserRowProps {
  user: User;
  onDelete: (id: number) => void;
}

const UserRow = React.memo<UserRowProps>(({ user, onDelete }) => {
  return (
    <div>
      {user.name}
      <button onClick={() => onDelete(user.id)}>Delete</button>
    </div>
  );
});

export const UserList = ({ users }: { users: User[] }) => {
  const [filter, setFilter] = React.useState('');

  // Memoize expensive filtering
  const filtered = React.useMemo(
    () => users.filter(u => u.name.includes(filter)),
    [users, filter]
  );

  // Memoize callback to prevent unnecessary child re-renders
  const handleDelete = React.useCallback((id: number) => {
    // Delete logic
  }, []);

  return (
    <div>
      <input
        value={filter}
        onChange={e => setFilter(e.target.value)}
      />
      {filtered.map(user => (
        <UserRow
          key={user.id}
          user={user}
          onDelete={handleDelete}
        />
      ))}
    </div>
  );
};
```

### Example 6: Security Review

```typescript
// ❌ SECURITY ISSUES
export const UserProfile = ({ user }: { user: User }) => {
  // XSS vulnerability
  return (
    <div
      dangerouslySetInnerHTML={{ __html: user.bio }}
    />
  );
};

// Insecure token storage
localStorage.setItem('token', authToken);

// SQL injection risk (if using directly)
const query = `SELECT * FROM users WHERE id = ${userId}`;


// ✅ SECURE
import DOMPurify from 'dompurify';

export const UserProfile = ({ user }: { user: User }) => {
  // Sanitize HTML content
  const sanitizedBio = DOMPurify.sanitize(user.bio, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'p', 'br']
  });

  return <div dangerouslySetInnerHTML={{ __html: sanitizedBio }} />;
};

// Secure token storage (httpOnly cookies)
// Set via server-side Set-Cookie header

// Parameterized queries
const query = 'SELECT * FROM users WHERE id = ?';
db.query(query, [userId]);

// Input validation
const validateEmail = (email: string): boolean => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};
```

## Best Practices

### 1. Code Organization
- Keep files under 300 lines
- One primary export per file
- Related code grouped together
- Clear naming conventions

### 2. Variable Naming
```typescript
// ❌ Bad
const d = new Date();
const u = getUserData(id);
const x = calculateTax(price);

// ✅ Good
const currentDate = new Date();
const userData = getUserData(id);
const taxAmount = calculateTax(price);
```

### 3. Function Design
- Single responsibility principle
- Max 3 parameters (use objects for more)
- Clear return types
- Document complex logic

### 4. Comment Guidelines
```typescript
// ✅ Good comment
// Retry failed requests with exponential backoff
// to handle temporary network issues
const maxRetries = 3;

// ❌ Bad comment
// Set maxRetries to 3
const maxRetries = 3;
```

### 5. Testing Strategy
- Unit tests for business logic
- Integration tests for API calls
- Component tests for UI behavior
- E2E tests for critical flows

## Integration with Other Skills

- **`react-testing-strategy`**: Testing framework and patterns
- **`frontend-performance`**: Performance optimization techniques
- **`typescript-migration`**: TypeScript adoption strategy
- **`javascript-documentation`**: JSDoc and type documentation

