---
name: react-component-patterns
description: Design React components using best patterns, composition, rendering strategies, and component architecture
---

# React Component Patterns Skill

## When to Use This Skill

- Designing component architecture for React applications
- Building reusable, composable components
- Implementing component composition patterns
- Designing prop interfaces and component APIs
- Handling component state and side effects
- Optimizing component performance (memo, useMemo, useCallback)
- Creating compound components and context-aware patterns
- Building accessible, semantic components

## Quick Start

```
/react-component-patterns <component_type_or_use_case>
```

**Example**:
```
/react-component-patterns Form component with validation, error handling, and auto-save
```

## How It Works

The skill covers comprehensive React component design patterns:

### 1. Component Composition Patterns
- **Presentational Components**: UI-focused, receive props, no state
- **Container Components**: Logic and state management
- **Compound Components**: Parent and child work together (Dialog, Tabs, Form)
- **Higher-Order Components (HOC)**: Function wrapping component
- **Render Props**: Sharing code via prop callbacks
- **Custom Hooks**: Logic extraction and reuse

### 2. Props Architecture
- **Single Responsibility**: Each prop has one purpose
- **Prop Types**: TypeScript interfaces for type safety
- **Default Props**: Sensible defaults for optional props
- **Spread Props**: Flexible prop forwarding
- **Controlled vs Uncontrolled**: Component control strategy

### 3. State Management Patterns
- **useState**: Simple component state
- **useReducer**: Complex state with multiple transitions
- **useContext**: Shared state across components
- **State Colocation**: Keep state close to where it's used
- **Lifting State**: Shared state between siblings

### 4. Performance Optimization
- **React.memo**: Skip re-renders when props don't change
- **useMemo**: Memoize expensive calculations
- **useCallback**: Memoize function references
- **Code Splitting**: Lazy load components
- **Virtual Lists**: Render only visible items

### 5. Accessibility (a11y)
- **Semantic HTML**: Proper element selection
- **ARIA Attributes**: Accessibility tree annotations
- **Keyboard Navigation**: Full keyboard support
- **Focus Management**: Proper focus handling
- **Screen Reader Testing**: Tested with assistive tech

## Configuration

**TypeScript Component Template**:
```typescript
interface ComponentProps {
  // Define all props with types
  title: string;
  isOpen?: boolean;
  onClose?: () => void;
}

export const Component: React.FC<ComponentProps> = ({
  title,
  isOpen = false,
  onClose,
}) => {
  // Component implementation
};
```

**ESLint Rules for Components**:
```json
{
  "rules": {
    "react/prop-types": "warn",
    "react/jsx-no-useless-fragment": "warn",
    "react-hooks/rules-of-hooks": "error",
    "react-hooks/exhaustive-deps": "warn"
  }
}
```

## Examples

### Example 1: Compound Component Pattern

```typescript
// Dialog compound component
interface DialogProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

const DialogContext = React.createContext<{
  isOpen: boolean;
  onClose: () => void;
} | null>(null);

export const Dialog: React.FC<DialogProps> = ({
  isOpen,
  onClose,
  children,
}) => {
  if (!isOpen) return null;

  return (
    <DialogContext.Provider value={{ isOpen, onClose }}>
      <div className="dialog-overlay" onClick={onClose}>
        {children}
      </div>
    </DialogContext.Provider>
  );
};

Dialog.Header = ({ children }: { children: React.ReactNode }) => (
  <div className="dialog-header">{children}</div>
);

Dialog.Body = ({ children }: { children: React.ReactNode }) => (
  <div className="dialog-body">{children}</div>
);

Dialog.Footer = ({ children }: { children: React.ReactNode }) => (
  <div className="dialog-footer">{children}</div>
);

Dialog.CloseButton = () => {
  const context = React.useContext(DialogContext);
  if (!context) throw new Error("CloseButton must be inside Dialog");
  return <button onClick={context.onClose}>Close</button>;
};

// Usage:
<Dialog isOpen={true} onClose={() => {}}>
  <Dialog.Header>Confirm Action</Dialog.Header>
  <Dialog.Body>Are you sure?</Dialog.Body>
  <Dialog.Footer>
    <Dialog.CloseButton />
  </Dialog.Footer>
</Dialog>
```

### Example 2: Controlled Component Pattern

```typescript
interface InputProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  isError?: boolean;
}

export const ControlledInput: React.FC<InputProps> = ({
  value,
  onChange,
  placeholder,
  isError,
}) => {
  return (
    <input
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
      className={isError ? "input-error" : ""}
      aria-invalid={isError}
    />
  );
};

// Usage - parent controls state
const Form = () => {
  const [email, setEmail] = useState("");

  return (
    <ControlledInput
      value={email}
      onChange={setEmail}
      isError={!email.includes("@")}
    />
  );
};
```

### Example 3: Performance-Optimized Component

```typescript
interface ListItemProps {
  item: Item;
  onSelect: (id: string) => void;
}

// Memoized to prevent re-renders when props don't change
export const ListItem = React.memo<ListItemProps>(
  ({ item, onSelect }) => {
    const handleClick = useCallback(() => {
      onSelect(item.id);
    }, [item.id, onSelect]);

    return (
      <button onClick={handleClick} className="list-item">
        {item.name}
      </button>
    );
  },
  (prevProps, nextProps) => {
    // Custom comparison: true if props are equal (skip render)
    return (
      prevProps.item.id === nextProps.item.id &&
      prevProps.onSelect === nextProps.onSelect
    );
  }
);

ListItem.displayName = "ListItem";
```

### Example 4: Custom Hook Pattern

```typescript
interface UseFormState {
  values: Record<string, string>;
  errors: Record<string, string>;
  touched: Record<string, boolean>;
}

interface UseFormReturn extends UseFormState {
  handleChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  handleBlur: (e: React.FocusEvent<HTMLInputElement>) => void;
  handleSubmit: (onSubmit: () => void) => (e: React.FormEvent) => void;
  reset: () => void;
}

export const useForm = (
  initialValues: Record<string, string>,
  onSubmit: (values: Record<string, string>) => void,
  validate?: (values: Record<string, string>) => Record<string, string>
): UseFormReturn => {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [touched, setTouched] = useState<Record<string, boolean>>({});

  const handleChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const { name, value } = e.target;
      setValues((prev) => ({ ...prev, [name]: value }));
    },
    []
  );

  const handleBlur = useCallback(
    (e: React.FocusEvent<HTMLInputElement>) => {
      const { name } = e.target;
      setTouched((prev) => ({ ...prev, [name]: true }));

      if (validate) {
        const newErrors = validate(values);
        setErrors(newErrors);
      }
    },
    [validate, values]
  );

  const handleSubmit = useCallback(
    (onSubmitFn: () => void) => (e: React.FormEvent) => {
      e.preventDefault();
      if (validate) {
        const newErrors = validate(values);
        setErrors(newErrors);
        if (Object.keys(newErrors).length === 0) {
          onSubmitFn();
        }
      } else {
        onSubmitFn();
      }
    },
    [values, validate]
  );

  const reset = useCallback(() => {
    setValues(initialValues);
    setErrors({});
    setTouched({});
  }, [initialValues]);

  return {
    values,
    errors,
    touched,
    handleChange,
    handleBlur,
    handleSubmit,
    reset,
  };
};

// Usage:
const LoginForm = () => {
  const form = useForm(
    { email: "", password: "" },
    (values) => console.log("Submit", values),
    (values) => {
      const errors: Record<string, string> = {};
      if (!values.email.includes("@")) errors.email = "Invalid email";
      if (values.password.length < 8) errors.password = "Min 8 chars";
      return errors;
    }
  );

  return (
    <form onSubmit={form.handleSubmit(() => {})}>
      <input
        name="email"
        value={form.values.email}
        onChange={form.handleChange}
        onBlur={form.handleBlur}
      />
      {form.touched.email && form.errors.email && (
        <span>{form.errors.email}</span>
      )}
    </form>
  );
};
```

## Best Practices

### 1. Component Size
- **Target**: 100-200 lines max
- **Too Large?**: Extract sub-components
- **Example**: Form component → Input, Button, ErrorMessage sub-components

### 2. Prop Drilling Avoidance
```typescript
// ❌ Bad: Props drilled through many levels
<Parent value={value}>
  <Child value={value}>
    <Grandchild value={value} />
  </Child>
</Parent>

// ✅ Good: Use Context
const ValueContext = createContext(null);
<ValueContext.Provider value={value}>
  <Parent>
    <Child>
      <Grandchild /> {/* Access via useContext */}
    </Grandchild>
  </Child>
</ValueContext.Provider>
```

### 3. Render Props vs Hooks
```typescript
// Old Pattern (still valid)
<DataFetcher
  render={(data) => <Component data={data} />}
/>

// Modern Pattern (preferred)
const data = useDataFetcher();
<Component data={data} />
```

### 4. Naming Conventions
- **Components**: PascalCase (Button, UserCard)
- **Hooks**: camelCase starting with "use" (useForm, useLocalStorage)
- **Props**: camelCase (isActive, onSubmit)

## Integration with Other Skills

- **`react-testing-strategy`**: Test component patterns
- **`typescript-migration`**: Ensure strong typing
- **`frontend-performance`**: Optimize with memo/useMemo
- **`nextjs-setup`**: Component structure in Next.js
- **`javascript-code-review`**: Review component implementations

## Component Patterns Checklist

- [ ] Single responsibility principle applied
- [ ] Props clearly documented with TypeScript
- [ ] Accessible (semantic HTML, ARIA)
- [ ] Performance optimized (memo, useMemo, useCallback)
- [ ] Tested (unit and integration)
- [ ] Reusable across application
- [ ] Clear naming and organization
- [ ] Handles error states
- [ ] Handles loading states
- [ ] Works with different viewport sizes
