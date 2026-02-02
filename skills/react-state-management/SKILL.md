---
name: react-state-management
description: Design and implement state management solutions for React applications using Context, Redux, Zustand, or other patterns
---

# React State Management Skill

## When to Use This Skill

- Choosing appropriate state management for your application
- Implementing global state with Context API
- Setting up Redux or Zustand stores
- Managing complex application state
- Coordinating state between distant components
- Implementing real-time data synchronization
- Managing form state across multiple components
- Handling authentication and user state

## Quick Start

```
/react-state-management <application_requirements>
```

**Example**:
```
/react-state-management E-commerce app with shopping cart, user auth, and wishlist
```

## How It Works

The skill covers state management patterns and solutions:

### 1. State Management Options
- **useState**: Simple component state (recommended for local state)
- **Context API**: Shared state without library (good for theme, auth)
- **Redux**: Predictable state container with middleware support
- **Zustand**: Lightweight alternative to Redux
- **Recoil**: Atomic state management (experimental)
- **TanStack Query**: Server state management

### 2. When to Use Each
- **Component State (useState)**: Form input, UI toggles, animation states
- **Context API**: Theme, auth, user preferences
- **Redux**: Complex app with many state mutations
- **Zustand**: Simple global state, lightweight alternative
- **TanStack Query**: Server data caching and synchronization

### 3. State Patterns
- **Action Creators**: Functions that create actions
- **Reducers**: Pure functions transforming state
- **Selectors**: Functions extracting data from state
- **Middleware**: Intercept and process actions
- **Sagas/Thunks**: Handle side effects

### 4. Best Practices
- Keep state as local as possible
- Normalize complex state shapes
- Use selectors for derived state
- Avoid prop drilling with Context
- Handle async operations properly

## Configuration

**Context API Setup**:
```typescript
interface AuthContextType {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [user, setUser] = useState<User | null>(null);

  const login = async (email: string, password: string) => {
    const response = await fetch("/api/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    });
    const data = await response.json();
    setUser(data.user);
  };

  const logout = () => setUser(null);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be inside AuthProvider");
  return context;
};
```

**Zustand Setup**:
```typescript
import { create } from "zustand";

interface AuthStore {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

export const useAuthStore = create<AuthStore>((set) => ({
  user: null,
  login: async (email, password) => {
    const response = await fetch("/api/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    });
    const { user } = await response.json();
    set({ user });
  },
  logout: () => set({ user: null }),
}));
```

## Examples

### Example 1: Context API for Theme

```typescript
type Theme = "light" | "dark";

interface ThemeContextType {
  theme: Theme;
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType | null>(null);

export const ThemeProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [theme, setTheme] = useState<Theme>(() => {
    const stored = localStorage.getItem("theme");
    return (stored as Theme) || "light";
  });

  const toggleTheme = useCallback(() => {
    setTheme((prev) => {
      const newTheme = prev === "light" ? "dark" : "light";
      localStorage.setItem("theme", newTheme);
      return newTheme;
    });
  }, []);

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) throw new Error("useTheme must be inside ThemeProvider");
  return context;
};
```

### Example 2: Zustand Shopping Cart

```typescript
interface CartItem {
  id: string;
  name: string;
  price: number;
  quantity: number;
}

interface CartStore {
  items: CartItem[];
  addItem: (item: CartItem) => void;
  removeItem: (id: string) => void;
  updateQuantity: (id: string, quantity: number) => void;
  total: number;
}

export const useCartStore = create<CartStore>((set, get) => ({
  items: [],

  addItem: (item) =>
    set((state) => {
      const existing = state.items.find((i) => i.id === item.id);
      if (existing) {
        return {
          items: state.items.map((i) =>
            i.id === item.id
              ? { ...i, quantity: i.quantity + item.quantity }
              : i
          ),
        };
      }
      return { items: [...state.items, item] };
    }),

  removeItem: (id) =>
    set((state) => ({
      items: state.items.filter((i) => i.id !== id),
    })),

  updateQuantity: (id, quantity) =>
    set((state) => ({
      items: state.items.map((i) =>
        i.id === id ? { ...i, quantity } : i
      ),
    })),

  get total() {
    return get().items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  },
}));

// Usage:
const ShoppingCart = () => {
  const { items, removeItem, total } = useCartStore();

  return (
    <div>
      {items.map((item) => (
        <div key={item.id}>
          {item.name} - ${item.price} x {item.quantity}
          <button onClick={() => removeItem(item.id)}>Remove</button>
        </div>
      ))}
      <div>Total: ${total}</div>
    </div>
  );
};
```

### Example 3: Redux Pattern with useReducer

```typescript
interface AppState {
  user: User | null;
  todos: Todo[];
  isLoading: boolean;
  error: string | null;
}

type AppAction =
  | { type: "SET_USER"; payload: User }
  | { type: "LOGOUT" }
  | { type: "ADD_TODO"; payload: Todo }
  | { type: "REMOVE_TODO"; payload: string }
  | { type: "SET_LOADING"; payload: boolean }
  | { type: "SET_ERROR"; payload: string | null };

const initialState: AppState = {
  user: null,
  todos: [],
  isLoading: false,
  error: null,
};

function appReducer(state: AppState, action: AppAction): AppState {
  switch (action.type) {
    case "SET_USER":
      return { ...state, user: action.payload };
    case "LOGOUT":
      return { ...state, user: null };
    case "ADD_TODO":
      return { ...state, todos: [...state.todos, action.payload] };
    case "REMOVE_TODO":
      return {
        ...state,
        todos: state.todos.filter((t) => t.id !== action.payload),
      };
    case "SET_LOADING":
      return { ...state, isLoading: action.payload };
    case "SET_ERROR":
      return { ...state, error: action.payload };
    default:
      return state;
  }
}

const AppContext = createContext<{
  state: AppState;
  dispatch: Dispatch<AppAction>;
} | null>(null);

export const AppProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [state, dispatch] = useReducer(appReducer, initialState);

  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
};

export const useAppContext = () => {
  const context = useContext(AppContext);
  if (!context) throw new Error("useAppContext must be inside AppProvider");
  return context;
};
```

### Example 4: TanStack Query for Server State

```typescript
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";

const UserProfile = ({ userId }: { userId: string }) => {
  // Fetch user data with automatic caching
  const { data: user, isLoading, error } = useQuery({
    queryKey: ["users", userId],
    queryFn: () => fetch(`/api/users/${userId}`).then((r) => r.json()),
    staleTime: 5 * 60 * 1000, // 5 minutes
  });

  // Mutation for updating user
  const queryClient = useQueryClient();
  const { mutate: updateUser } = useMutation({
    mutationFn: (updates: Partial<User>) =>
      fetch(`/api/users/${userId}`, {
        method: "PATCH",
        body: JSON.stringify(updates),
      }).then((r) => r.json()),
    onSuccess: (data) => {
      // Invalidate cached query
      queryClient.invalidateQueries({
        queryKey: ["users", userId],
      });
    },
  });

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <button onClick={() => updateUser({ name: "New Name" })}>
        Update Name
      </button>
    </div>
  );
};
```

## State Management Decision Tree

```
Do you need to share state across multiple components?
├─ No → Use useState (local state)
└─ Yes
   ├─ Is it a few values (theme, auth, user)?
   │  └─ Use Context API
   │
   ├─ Is it server data (users, posts, comments)?
   │  └─ Use TanStack Query
   │
   └─ Is it complex application state?
      ├─ Need middleware or time-travel debugging?
      │  └─ Use Redux
      └─ Otherwise?
         └─ Use Zustand (lighter)
```

## Best Practices

### 1. State Shape
```typescript
// ❌ Bad: Nested structure
const state = {
  user: {
    id: 1,
    posts: [
      { id: 1, comments: [{ id: 1, text: "" }] }
    ]
  }
};

// ✅ Good: Normalized
const state = {
  users: { 1: { id: 1 } },
  posts: { 1: { id: 1, userId: 1 } },
  comments: { 1: { id: 1, postId: 1 } }
};
```

### 2. Selectors for Derived State
```typescript
// Use selectors to compute values
const selectUserName = (state: AppState) => state.user?.name;
const selectCartTotal = (state: CartStore) =>
  state.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
```

### 3. Keep Business Logic in Actions
```typescript
// ❌ Bad: Logic in component
const handleSubmit = () => {
  const newState = { ...user, name: "John" };
  setUser(newState);
};

// ✅ Good: Logic in action/dispatcher
const { dispatch } = useAppContext();
const handleSubmit = () => {
  dispatch({ type: "UPDATE_USER", payload: { name: "John" } });
};
```

## Integration with Other Skills

- **`react-component-patterns`**: Provide state via props/context
- **`react-testing-strategy`**: Test state management
- **`typescript-migration`**: Type-safe state management
- **`react-hooks-advanced`**: Custom hooks with state

## Performance Considerations

- Avoid unnecessary re-renders (use selectors)
- Split state by concern
- Use lazy state initialization
- Memoize computed values
- Consider splitting large stores

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Excessive re-renders | Use selectors, split state |
| State not updating | Check reducer logic, action types |
| Memory leaks | Clean up subscriptions, listeners |
| Performance issues | Normalize state, use selectors |
