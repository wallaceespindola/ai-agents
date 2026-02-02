---
name: typescript-migration
description: Migrate JavaScript projects to TypeScript with incremental adoption strategies and best practices
---

# TypeScript Migration Skill

## When to Use This Skill

- Converting JavaScript projects to TypeScript
- Incrementally adopting TypeScript in existing projects
- Setting up TypeScript configuration and tooling
- Migrating JavaScript components to typed versions
- Establishing TypeScript best practices
- Handling third-party library types
- Setting up type checking in CI/CD
- Training teams on TypeScript fundamentals

## Quick Start

```
/typescript-migration <project_type_and_scale>
```

**Example**:
```
/typescript-migration Medium-sized React app with 50+ components
```

## How It Works

The skill provides comprehensive TypeScript migration strategies:

### 1. Migration Planning
- **Assessment**: Evaluate codebase complexity
- **Phasing**: Incremental adoption approach
- **Tooling**: Set up TypeScript infrastructure
- **Training**: Team onboarding and knowledge
- **Timeline**: Realistic project estimation

### 2. Incremental Adoption
- **allowJs**: Mix TypeScript and JavaScript
- **Gradual**: Convert files incrementally
- **Testing**: Maintain test coverage during migration
- **Rollback**: Easy revert if needed
- **Parallel**: Run both during transition

### 3. Configuration Setup
- **tsconfig.json**: Starter configuration
- **Strict Mode**: Progressive strictness increase
- **Build Integration**: Webpack, Vite, Next.js
- **IDE Integration**: VS Code support
- **Pre-commit Hooks**: Type checking automation

### 4. Common Migration Patterns
- **JavaScript to TypeScript**: .js to .ts conversion
- **React Components**: .jsx to .tsx
- **Third-party Types**: @types/* packages
- **Type Inference**: Leverage type inference
- **Generics**: Creating reusable typed code

### 5. Type Definition Sources
- **Bundled Types**: Built-in @types
- **Type Stubs**: .d.ts files
- **Inline Types**: Declare in source
- **DefinitelyTyped**: Community types
- **Custom Types**: Project-specific types

### 6. Testing During Migration
- **Test Updates**: Adapt tests for types
- **Type Tests**: Test type definitions
- **Coverage**: Maintain coverage baseline
- **CI Integration**: Type checking in pipeline
- **Regression**: Catch migration errors

### 7. Library Type Handling
- **DefinitelyTyped**: Most popular libraries
- **Typed Packages**: Built-in @types
- **Custom Declarations**: Fill type gaps
- **any Escape Hatch**: Temporary workaround
- **Type Guards**: Safe type narrowing

## Configuration

**Phase 1: Initial Setup (tsconfig.json)**:
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "declaration": true,
    "allowJs": true,
    "outDir": "./dist",
    "strict": false,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}
```

**Phase 2: Strict Adoption (tsconfig.json)**:
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
    "noFallthroughCasesInSwitch": true,
    "allowJs": false
  }
}
```

## Examples

### Example 1: Migration Plan and Approach

```markdown
## TypeScript Migration Plan

### Phase 1: Foundation (Week 1-2)
- [ ] Install TypeScript and types
- [ ] Configure tsconfig.json
- [ ] Set up build pipeline
- [ ] Add pre-commit hooks
- [ ] Team training session

### Phase 2: Core Utilities (Week 2-3)
- [ ] Migrate utility functions
- [ ] Create type definitions
- [ ] Migrate data models
- [ ] Update tests

### Phase 3: Components (Week 4-6)
- [ ] Convert 10-15 key components
- [ ] Update tests
- [ ] Document patterns
- [ ] Code reviews

### Phase 4: Remaining (Week 7+)
- [ ] Convert remaining components
- [ ] Increase strictness gradually
- [ ] Full strict mode
- [ ] Remove allowJs

### Success Criteria
- 100% TypeScript code
- Strict mode enabled
- CI/CD type checking
- Team proficiency
```

### Example 2: JavaScript to TypeScript Conversion

```javascript
// Before: JavaScript
// user.utils.js
export const formatUser = (user) => {
  return {
    displayName: `${user.firstName} ${user.lastName}`,
    email: user.email
  };
};

export const isAdult = (user) => {
  return user.age >= 18;
};


// After: TypeScript
// user.utils.ts
interface User {
  firstName: string;
  lastName: string;
  email: string;
  age: number;
}

interface FormattedUser {
  displayName: string;
  email: string;
}

export const formatUser = (user: User): FormattedUser => {
  return {
    displayName: `${user.firstName} ${user.lastName}`,
    email: user.email
  };
};

export const isAdult = (user: User): boolean => {
  return user.age >= 18;
};
```

### Example 3: React Component Migration

```typescript
// Before: JavaScript React
// UserProfile.jsx
import React, { useState, useEffect } from 'react';

export const UserProfile = ({ userId }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchUser = async () => {
      setLoading(true);
      const res = await fetch(`/api/users/${userId}`);
      const data = await res.json();
      setUser(data);
      setLoading(false);
    };

    fetchUser();
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (!user) return <div>No user found</div>;

  return <div>{user.name}</div>;
};


// After: TypeScript React
// UserProfile.tsx
import React, { useState, useEffect, FC } from 'react';

interface User {
  id: number;
  name: string;
  email: string;
}

interface UserProfileProps {
  userId: number;
}

export const UserProfile: FC<UserProfileProps> = ({ userId }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUser = async () => {
      setLoading(true);
      try {
        const res = await fetch(`/api/users/${userId}`);
        if (!res.ok) throw new Error('Failed to fetch');
        const data: User = await res.json();
        setUser(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!user) return <div>No user found</div>;

  return <div>{user.name}</div>;
};
```

### Example 4: Type Definition Patterns

```typescript
// Common patterns for type definitions

// 1. Simple Interfaces
interface Config {
  apiUrl: string;
  timeout: number;
  debug?: boolean;
}

// 2. Extending Interfaces
interface User {
  id: number;
  name: string;
}

interface AdminUser extends User {
  adminLevel: 'super' | 'moderate' | 'basic';
}

// 3. Union Types
type Status = 'pending' | 'active' | 'inactive';
type Result<T> = { success: true; data: T } | { success: false; error: string };

// 4. Generics
interface ApiResponse<T> {
  data: T;
  status: number;
  timestamp: Date;
}

// 5. Utility Types
type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};

type Partial<T> = {
  [K in keyof T]?: T[K];
};

type Pick<T, K extends keyof T> = {
  [P in K]: T[P];
};

// 6. Enum Types
enum UserRole {
  Admin = 'admin',
  User = 'user',
  Guest = 'guest'
}

// 7. Function Types
type Validator = (value: string) => boolean;
type AsyncFetcher = <T>(url: string) => Promise<T>;
```

### Example 5: Handling Third-Party Libraries

```typescript
// 1. With Built-in Types
import axios from 'axios'; // @types/axios included

const response = await axios.get<User>('/api/users');

// 2. Install @types Separately
// npm install --save-dev @types/lodash
import { map, filter } from 'lodash';

// 3. Create Type Declaration File
// lodash-extra.d.ts
declare module 'lodash-extra' {
  export function customMap<T, U>(items: T[], fn: (item: T) => U): U[];
}

// 4. Ambient Types
declare global {
  interface Window {
    __DEBUG__: boolean;
  }
}

// 5. Using any as Temporary Escape
import someUntyped from 'untyped-package';
const lib = someUntyped as any;
```

### Example 6: Migration Checklist

```typescript
// Migration Checklist Template

// 1. Setup Phase
// [ ] npm install -D typescript @types/node
// [ ] Create tsconfig.json
// [ ] Configure build tools (webpack, vite, etc.)
// [ ] Set up pre-commit hooks

// 2. Initial Conversion
// [ ] Rename .js files to .ts
// [ ] Rename .jsx files to .tsx
// [ ] Add basic type annotations
// [ ] Run type checker and fix errors

// 3. Type Definitions
// [ ] Create types/ or interfaces/ directory
// [ ] Define main interfaces/types
// [ ] Create .d.ts for globals
// [ ] Document complex types

// 4. Testing
// [ ] Update test files to .ts
// [ ] Fix type errors in tests
// [ ] Ensure test coverage maintained

// 5. Strictness
// [ ] Enable strict mode options
// [ ] Fix strict mode errors
// [ ] Remove any types
// [ ] Enable noImplicitAny

// 6. Documentation
// [ ] Document type conventions
// [ ] Create JSDoc for complex types
// [ ] Update contributing guide
// [ ] Team training

// 7. CI/CD Integration
// [ ] Add tsc to build pipeline
// [ ] Add type checking to pre-commit
// [ ] Configure IDE
// [ ] Document development setup
```

### Example 7: Common Patterns and Solutions

```typescript
// Pattern 1: Generic API Call
async function fetchData<T>(url: string): Promise<T> {
  const response = await fetch(url);
  return response.json() as Promise<T>;
}

// Pattern 2: Component with Generic Props
interface GenericListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
  keyExtractor: (item: T) => string;
}

function GenericList<T>({
  items,
  renderItem,
  keyExtractor
}: GenericListProps<T>) {
  return (
    <ul>
      {items.map(item => (
        <li key={keyExtractor(item)}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}

// Pattern 3: Safe Type Narrowing
function processValue(value: string | number | boolean) {
  if (typeof value === 'string') {
    console.log(value.toUpperCase());
  } else if (typeof value === 'number') {
    console.log(value.toFixed(2));
  } else {
    console.log(value ? 'true' : 'false');
  }
}

// Pattern 4: Error Handling
try {
  const data = await fetchData<User>('/api/user');
} catch (error) {
  const message = error instanceof Error ? error.message : 'Unknown error';
  console.error(message);
}
```

## Best Practices

### 1. Migration Strategy
- Start with strict: false
- Enable one strict option at a time
- Convert utilities and types first
- Then components and features
- End with strict mode enabled

### 2. Type Definitions
- Define interfaces for major entities
- Use Pick, Omit, Partial for variations
- Avoid any types (use unknown if needed)
- Create shared type file for project types

### 3. Testing
- Migrate tests alongside components
- Use type assertions in tests carefully
- Test type safety with TypeScript tests
- Maintain coverage during migration

### 4. Documentation
- Document type naming conventions
- Create type style guide
- Show common patterns
- Maintain onboarding guide

## Integration with Other Skills

- **`javascript-code-review`**: Type safety review
- **`nextjs-setup`**: TypeScript in Next.js
- **`react-testing-strategy`**: Typed test patterns
- **`cicd-pipeline-setup`**: Type checking in CI/CD

