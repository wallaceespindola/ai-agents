---
name: react-hooks-advanced
description: Master custom React hooks, hook patterns, and advanced hook composition for complex logic
---

# React Hooks Advanced Skill

## When to Use This Skill

- Creating custom hooks for reusable logic
- Building complex state management with hooks
- Optimizing performance with hook memoization
- Managing side effects and subscriptions
- Integrating with external libraries via hooks
- Testing custom hooks
- Building hook composition and chaining
- Handling async operations in hooks

## Quick Start

```
/react-hooks-advanced <hook_use_case_or_logic>
```

**Example**:
```
/react-hooks-advanced Custom hook for form state with validation and API submission
```

## How It Works

The skill covers advanced React hook patterns and creation:

### 1. Custom Hook Creation
- **Rules of Hooks**: Call hooks at top level, only from components
- **Hook Naming**: Custom hooks start with "use"
- **Logic Extraction**: Move state and effects into custom hooks
- **Composable Hooks**: Hooks that combine other hooks
- **Hook Dependencies**: Understanding exhaustive-deps

### 2. State Management Hooks
- **useState**: Basic state management
- **useReducer**: Complex state with multiple actions
- **useCallback**: Memoize function references
- **useMemo**: Memoize computed values
- **useRef**: Persist values across renders
- **useLayoutEffect**: Synchronous effects
- **useContext**: Access context values

### 3. Advanced Patterns
- **Hook Composition**: Multiple hooks working together
- **Conditional Hook Effects**: Setup/cleanup patterns
- **Infinite Loops Prevention**: Proper dependency arrays
- **Custom Middleware**: Hook patterns for middleware-like behavior
- **Event Emitter Hooks**: Publish/subscribe via hooks

### 4. Testing Hooks
- **renderHook from @testing-library/react**: Test custom hooks
- **act() utility**: Handle state updates in tests
- **Mock External Dependencies**: Mock API calls, events
- **Cleanup**: Proper cleanup between tests

## Configuration

**Custom Hook Template**:
```typescript
interface UseAsyncState<T> {
  data: T | null;
  loading: boolean;
  error: Error | null;
}

export const useAsync = <T,>(
  fn: () => Promise<T>,
  dependencies: React.DependencyList = []
): UseAsyncState<T> => {
  const [state, setState] = useState<UseAsyncState<T>>({
    data: null,
    loading: true,
    error: null,
  });

  useEffect(() => {
    let isMounted = true;

    (async () => {
      try {
        const data = await fn();
        if (isMounted) {
          setState({ data, loading: false, error: null });
        }
      } catch (error) {
        if (isMounted) {
          setState({
            data: null,
            loading: false,
            error: error as Error,
          });
        }
      }
    })();

    return () => {
      isMounted = false;
    };
  }, dependencies);

  return state;
};
```

## Examples

### Example 1: useAsync Hook

```typescript
// Custom hook for async operations
export const useAsync = <T, E = string>(
  asyncFunction: () => Promise<T>,
  immediate = true
) => {
  const [status, setStatus] = useState<
    "idle" | "pending" | "success" | "error"
  >("idle");
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<E | null>(null);

  const execute = useCallback(
    async () => {
      setStatus("pending");
      setData(null);
      setError(null);

      try {
        const response = await asyncFunction();
        setData(response);
        setStatus("success");
        return response;
      } catch (error) {
        setError(error as E);
        setStatus("error");
      }
    },
    [asyncFunction]
  );

  useEffect(() => {
    if (immediate) {
      execute();
    }
  }, [execute, immediate]);

  return { execute, status, data, error };
};

// Usage:
const UserProfile = ({ userId }: { userId: string }) => {
  const { data: user, status, error } = useAsync(
    () => fetch(`/api/users/${userId}`).then((r) => r.json()),
    true // Execute immediately
  );

  if (status === "pending") return <div>Loading...</div>;
  if (status === "error") return <div>Error: {error}</div>;
  return <div>{user?.name}</div>;
};
```

### Example 2: usePrevious Hook

```typescript
export const usePrevious = <T,>(value: T): T | undefined => {
  const ref = useRef<T>();

  useEffect(() => {
    ref.current = value;
  }, [value]);

  return ref.current;
};

// Usage: Track when value changes
const Component = ({ count }: { count: number }) => {
  const prevCount = usePrevious(count);

  return (
    <div>
      Now: {count}, before: {prevCount}
    </div>
  );
};
```

### Example 3: useLocalStorage Hook

```typescript
export const useLocalStorage = <T,>(
  key: string,
  initialValue: T
): [T, (value: T | ((val: T) => T)) => void] => {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(error);
      return initialValue;
    }
  });

  const setValue = useCallback(
    (value: T | ((val: T) => T)) => {
      try {
        const valueToStore =
          value instanceof Function ? value(storedValue) : value;
        setStoredValue(valueToStore);
        window.localStorage.setItem(key, JSON.stringify(valueToStore));
      } catch (error) {
        console.error(error);
      }
    },
    [key, storedValue]
  );

  return [storedValue, setValue];
};

// Usage:
const UserPreferences = () => {
  const [theme, setTheme] = useLocalStorage("theme", "light");

  return (
    <button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
      Toggle Theme (Current: {theme})
    </button>
  );
};
```

### Example 4: useDebounce Hook

```typescript
export const useDebounce = <T,>(value: T, delay: number): T => {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => clearTimeout(handler);
  }, [value, delay]);

  return debouncedValue;
};

// Usage: Debounce search input
const SearchUsers = () => {
  const [query, setQuery] = useState("");
  const debouncedQuery = useDebounce(query, 500);
  const { data: results } = useAsync(
    () => fetch(`/api/search?q=${debouncedQuery}`).then((r) => r.json()),
    true
  );

  return (
    <div>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search users..."
      />
      <ul>
        {results?.map((user) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
};
```

### Example 5: useEventListener Hook

```typescript
export const useEventListener = <K extends keyof WindowEventMap>(
  eventName: K,
  handler: (event: WindowEventMap[K]) => void,
  element?: HTMLElement | Window
) => {
  const savedHandler = useRef(handler);

  useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  useEffect(() => {
    const isSupported = element ? "addEventListener" in element : false;
    if (!isSupported) return;

    const eventListener = (event: Event) =>
      savedHandler.current(event as WindowEventMap[K]);

    (element || window).addEventListener(eventName, eventListener);

    return () => {
      (element || window).removeEventListener(eventName, eventListener);
    };
  }, [eventName, element]);
};

// Usage: Detect click outside
const Dropdown = () => {
  const [isOpen, setIsOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEventListener(
    "click",
    (event) => {
      if (ref.current && !ref.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }
  );

  return (
    <div ref={ref}>
      <button onClick={() => setIsOpen(!isOpen)}>Toggle</button>
      {isOpen && <div>Dropdown Content</div>}
    </div>
  );
};
```

## Best Practices

### 1. Exhaustive Dependencies
```typescript
// ❌ Bad: Missing dependency
useEffect(() => {
  console.log(userId); // Used but not in deps
}, []); // Missing userId

// ✅ Good: All dependencies included
useEffect(() => {
  console.log(userId);
}, [userId]); // userId is a dependency
```

### 2. Avoid Infinite Loops
```typescript
// ❌ Bad: Creates new object every render
useEffect(() => {
  fetchData({ filter: { type: "active" } }); // Object created each render
}, []); // Deps missing

// ✅ Good: Memoize object
const filter = useMemo(() => ({ type: "active" }), []);
useEffect(() => {
  fetchData({ filter });
}, [filter]); // filter is stable
```

### 3. Custom Hook Naming
```typescript
// All custom hooks start with "use"
export const useForm = () => { /* ... */ };
export const useFetch = () => { /* ... */ };
export const useAuth = () => { /* ... */ };
```

### 4. Return Object Memoization
```typescript
// ❌ Bad: Returns new object every render
const useCustom = () => {
  return { value: 1, handler: () => {} }; // New object
};

// ✅ Good: Memoize return value
const useCustom = () => {
  const value = 1;
  const handler = useCallback(() => {}, []);
  return useMemo(() => ({ value, handler }), [value, handler]);
};
```

## Testing Custom Hooks

```typescript
import { renderHook, act } from "@testing-library/react";
import { useForm } from "./useForm";

describe("useForm", () => {
  it("should initialize with default values", () => {
    const { result } = renderHook(() =>
      useForm({ email: "", password: "" })
    );

    expect(result.current.values).toEqual({
      email: "",
      password: "",
    });
  });

  it("should update values on change", () => {
    const { result } = renderHook(() =>
      useForm({ email: "", password: "" })
    );

    act(() => {
      result.current.handleChange({
        target: { name: "email", value: "test@example.com" },
      } as any);
    });

    expect(result.current.values.email).toBe("test@example.com");
  });
});
```

## Integration with Other Skills

- **`react-component-patterns`**: Use hooks in components
- **`react-testing-strategy`**: Test custom hooks
- **`typescript-migration`**: Type-safe hooks
- **`javascript-code-review`**: Review hook implementations

## Common Hook Mistakes to Avoid

- [ ] Calling hooks conditionally or in loops
- [ ] Missing dependencies in exhaustive-deps
- [ ] Creating infinite loops with improper deps
- [ ] Not cleaning up subscriptions in useEffect
- [ ] Mutating ref.current directly
- [ ] Using hooks in custom functions (not components)
