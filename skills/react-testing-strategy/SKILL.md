---
name: react-testing-strategy
description: Design comprehensive test strategies for React applications using Jest, React Testing Library, and best practices
---

# React Testing Strategy Skill

## When to Use This Skill

- Designing test architecture for React applications
- Creating unit, integration, and E2E test strategies
- Setting up Jest and React Testing Library
- Writing component, hook, and integration tests
- Implementing test coverage reporting
- Testing React Context, Redux, and async operations
- Accessibility and visual regression testing
- CI/CD test automation

## Quick Start

```
/react-testing-strategy <component_or_application_type>
```

**Example**:
```
/react-testing-strategy React form component with validation and API calls
```

## How It Works

The skill provides comprehensive React testing strategies:

### 1. Test Pyramid for React
- **Unit Tests** (70%): Components, hooks, utilities in isolation
- **Integration Tests** (20%): Components working together
- **E2E Tests** (10%): Complete user workflows

### 2. React Testing Library Principles
- Test user behavior, not implementation
- Query by accessible elements (label, role, text)
- Avoid testing implementation details
- Simulate real user interactions

### 3. Jest Configuration
- Test file discovery and execution
- Mocking modules and external dependencies
- Snapshot testing for UI components
- Coverage reporting and thresholds

### 4. Testing Patterns
- Component rendering and props
- User interactions (click, type, submit)
- Async operations and API calls
- Error boundaries and error states
- Context and Redux state management

### 5. Hooks Testing
- Custom hooks with renderHook
- Hook state and side effects
- Hook composition and dependencies
- Hook cleanup and memory leaks

### 6. Accessibility Testing
- ARIA roles and attributes
- Keyboard navigation
- Screen reader compatibility
- Semantic HTML verification

### 7. Performance Testing
- Component render count
- Unnecessary re-renders
- Memory leaks
- Animation performance

## Configuration

**jest.config.js**:
```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.ts'],
  collectCoverageFrom: [
    'src/**/*.{ts,tsx}',
    '!src/**/*.d.ts',
    '!src/index.tsx'
  ],
  coverageThreshold: {
    global: {
      statements: 80,
      branches: 80,
      functions: 80,
      lines: 80
    }
  }
};
```

**requirements**:
```
jest@29.7.0
@testing-library/react@14.1.2
@testing-library/jest-dom@6.1.5
@testing-library/user-event@14.5.1
@types/jest@29.5.8
jest-mock-extended@3.0.5
```

## Examples

### Example 1: Component Testing

```typescript
// src/components/Button.tsx
import React from 'react';

interface ButtonProps {
  onClick: () => void;
  disabled?: boolean;
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  onClick,
  disabled = false,
  children
}) => (
  <button onClick={onClick} disabled={disabled}>
    {children}
  </button>
);


// src/components/__tests__/Button.test.tsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Button } from '../Button';

describe('Button Component', () => {
  test('renders button with text', () => {
    render(<Button onClick={jest.fn()}>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  test('calls onClick handler when clicked', async () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);

    const button = screen.getByText('Click me');
    await userEvent.click(button);

    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  test('is disabled when disabled prop is true', () => {
    render(
      <Button onClick={jest.fn()} disabled>
        Click me
      </Button>
    );

    expect(screen.getByText('Click me')).toBeDisabled();
  });

  test('is not disabled by default', () => {
    render(<Button onClick={jest.fn()}>Click me</Button>);
    expect(screen.getByText('Click me')).not.toBeDisabled();
  });
});
```

### Example 2: Testing Async Operations

```typescript
// src/components/UserLoader.tsx
interface User {
  id: number;
  name: string;
}

export const UserLoader = ({ userId }: { userId: number }) => {
  const [user, setUser] = React.useState<User | null>(null);
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);

  React.useEffect(() => {
    const fetchUser = async () => {
      setLoading(true);
      try {
        const response = await fetch(`/api/users/${userId}`);
        const data = await response.json();
        setUser(data);
      } catch (err) {
        setError('Failed to load user');
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;
  if (!user) return <div>No user found</div>;

  return <div>{user.name}</div>;
};


// src/components/__tests__/UserLoader.test.tsx
import { render, screen, waitFor } from '@testing-library/react';
import { UserLoader } from '../UserLoader';

describe('UserLoader Component', () => {
  beforeEach(() => {
    global.fetch = jest.fn();
  });

  afterEach(() => {
    jest.restoreAllMocks();
  });

  test('displays loading state initially', () => {
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      json: async () => ({ id: 1, name: 'John' })
    });

    render(<UserLoader userId={1} />);
    expect(screen.getByText('Loading...')).toBeInTheDocument();
  });

  test('displays user data after loading', async () => {
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      json: async () => ({ id: 1, name: 'John Doe' })
    });

    render(<UserLoader userId={1} />);

    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
    });
  });

  test('displays error message on failure', async () => {
    (global.fetch as jest.Mock).mockRejectedValueOnce(new Error('Network error'));

    render(<UserLoader userId={1} />);

    await waitFor(() => {
      expect(screen.getByText('Failed to load user')).toBeInTheDocument();
    });
  });

  test('refetches when userId prop changes', async () => {
    const { rerender } = render(<UserLoader userId={1} />);

    expect(global.fetch).toHaveBeenCalledWith('/api/users/1');

    rerender(<UserLoader userId={2} />);

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith('/api/users/2');
    });
  });
});
```

### Example 3: Custom Hooks Testing

```typescript
// src/hooks/useCounter.ts
import { useState, useCallback } from 'react';

export const useCounter = (initialValue = 0) => {
  const [count, setCount] = useState(initialValue);

  const increment = useCallback(() => setCount(c => c + 1), []);
  const decrement = useCallback(() => setCount(c => c - 1), []);
  const reset = useCallback(() => setCount(initialValue), [initialValue]);

  return { count, increment, decrement, reset };
};


// src/hooks/__tests__/useCounter.test.ts
import { renderHook, act } from '@testing-library/react';
import { useCounter } from '../useCounter';

describe('useCounter Hook', () => {
  test('initializes with default value', () => {
    const { result } = renderHook(() => useCounter());
    expect(result.current.count).toBe(0);
  });

  test('initializes with custom value', () => {
    const { result } = renderHook(() => useCounter(10));
    expect(result.current.count).toBe(10);
  });

  test('increment increases count', () => {
    const { result } = renderHook(() => useCounter());

    act(() => {
      result.current.increment();
    });

    expect(result.current.count).toBe(1);
  });

  test('decrement decreases count', () => {
    const { result } = renderHook(() => useCounter(10));

    act(() => {
      result.current.decrement();
    });

    expect(result.current.count).toBe(9);
  });

  test('reset returns to initial value', () => {
    const { result, rerender } = renderHook(() => useCounter(5));

    act(() => {
      result.current.increment();
      result.current.increment();
    });

    expect(result.current.count).toBe(7);

    act(() => {
      result.current.reset();
    });

    expect(result.current.count).toBe(5);
  });
});
```

### Example 4: Form Testing

```typescript
// src/components/LoginForm.tsx
interface LoginFormProps {
  onSubmit: (email: string, password: string) => Promise<void>;
}

export const LoginForm: React.FC<LoginFormProps> = ({ onSubmit }) => {
  const [email, setEmail] = React.useState('');
  const [password, setPassword] = React.useState('');
  const [error, setError] = React.useState('');
  const [loading, setLoading] = React.useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (!email || !password) {
      setError('Email and password are required');
      return;
    }

    setLoading(true);
    try {
      await onSubmit(email, password);
    } catch (err) {
      setError('Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        placeholder="Email"
      />
      <input
        type="password"
        value={password}
        onChange={e => setPassword(e.target.value)}
        placeholder="Password"
      />
      {error && <p role="alert">{error}</p>}
      <button type="submit" disabled={loading}>
        {loading ? 'Logging in...' : 'Login'}
      </button>
    </form>
  );
};


// src/components/__tests__/LoginForm.test.tsx
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { LoginForm } from '../LoginForm';

describe('LoginForm Component', () => {
  test('submits form with email and password', async () => {
    const handleSubmit = jest.fn().mockResolvedValueOnce(undefined);
    render(<LoginForm onSubmit={handleSubmit} />);

    await userEvent.type(screen.getByPlaceholderText('Email'), 'user@example.com');
    await userEvent.type(screen.getByPlaceholderText('Password'), 'password123');
    await userEvent.click(screen.getByText('Login'));

    await waitFor(() => {
      expect(handleSubmit).toHaveBeenCalledWith('user@example.com', 'password123');
    });
  });

  test('displays error when fields are empty', async () => {
    const handleSubmit = jest.fn();
    render(<LoginForm onSubmit={handleSubmit} />);

    await userEvent.click(screen.getByText('Login'));

    expect(screen.getByText('Email and password are required')).toBeInTheDocument();
    expect(handleSubmit).not.toHaveBeenCalled();
  });

  test('displays error on submission failure', async () => {
    const handleSubmit = jest.fn().mockRejectedValueOnce(new Error('API error'));
    render(<LoginForm onSubmit={handleSubmit} />);

    await userEvent.type(screen.getByPlaceholderText('Email'), 'user@example.com');
    await userEvent.type(screen.getByPlaceholderText('Password'), 'password123');
    await userEvent.click(screen.getByText('Login'));

    await waitFor(() => {
      expect(screen.getByText('Login failed')).toBeInTheDocument();
    });
  });

  test('shows loading state during submission', async () => {
    const handleSubmit = jest.fn(
      () => new Promise(resolve => setTimeout(resolve, 100))
    );
    render(<LoginForm onSubmit={handleSubmit} />);

    await userEvent.type(screen.getByPlaceholderText('Email'), 'user@example.com');
    await userEvent.type(screen.getByPlaceholderText('Password'), 'password123');
    await userEvent.click(screen.getByText('Login'));

    expect(screen.getByText('Logging in...')).toBeInTheDocument();

    await waitFor(() => {
      expect(screen.getByText('Login')).toBeInTheDocument();
    });
  });
});
```

### Example 5: Testing with Context

```typescript
// src/context/ThemeContext.tsx
import React from 'react';

type Theme = 'light' | 'dark';

interface ThemeContextType {
  theme: Theme;
  setTheme: (theme: Theme) => void;
}

export const ThemeContext = React.createContext<ThemeContextType | undefined>(undefined);

export const ThemeProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [theme, setTheme] = React.useState<Theme>('light');

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => {
  const context = React.useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
};


// src/components/__tests__/ThemeProvider.test.tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { ThemeProvider, useTheme } from '../../context/ThemeContext';

const ThemeToggle = () => {
  const { theme, setTheme } = useTheme();
  return (
    <div>
      <p>Current theme: {theme}</p>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle
      </button>
    </div>
  );
};

describe('ThemeProvider', () => {
  test('provides theme context', () => {
    render(
      <ThemeProvider>
        <ThemeToggle />
      </ThemeProvider>
    );

    expect(screen.getByText('Current theme: light')).toBeInTheDocument();
  });

  test('toggles theme', async () => {
    render(
      <ThemeProvider>
        <ThemeToggle />
      </ThemeProvider>
    );

    await userEvent.click(screen.getByText('Toggle'));
    expect(screen.getByText('Current theme: dark')).toBeInTheDocument();
  });

  test('throws error when used outside provider', () => {
    const consoleError = jest.spyOn(console, 'error').mockImplementation();

    expect(() => {
      render(<ThemeToggle />);
    }).toThrow('useTheme must be used within ThemeProvider');

    consoleError.mockRestore();
  });
});
```

## Best Practices

### 1. Test Organization
```
src/
├── components/
│   ├── Button.tsx
│   └── __tests__/
│       └── Button.test.tsx
├── hooks/
│   ├── useCounter.ts
│   └── __tests__/
│       └── useCounter.test.ts
└── setupTests.ts
```

### 2. Query Priority (React Testing Library)
1. Accessible queries (getByRole, getByLabelText)
2. Semantic queries (getByText, getByPlaceholderText)
3. Test ID queries (getByTestId)

### 3. Async Testing Pattern
```typescript
await waitFor(() => {
  expect(element).toBeInTheDocument();
});
```

### 4. Mock External Dependencies
```typescript
jest.mock('../api', () => ({
  fetchUser: jest.fn()
}));
```

### 5. Coverage Goals
- Aim for 80% coverage
- Focus on critical paths
- Prioritize user workflows

## Integration with Other Skills

- **`javascript-code-review`**: Code quality in tests
- **`frontend-performance`**: Performance testing patterns
- **`nextjs-setup`**: Testing Next.js applications
- **`cicd-pipeline-setup`**: Test automation in CI/CD

