---
name: javascript-documentation
description: Create JSDoc documentation and component documentation for JavaScript and React applications
---

# JavaScript Documentation Skill

## When to Use This Skill

- Adding JSDoc comments to JavaScript functions
- Documenting React component props and usage
- Creating component storybook documentation
- Generating API documentation from code comments
- Writing TypeScript parameter documentation
- Creating component examples and recipes
- Documenting complex algorithms and business logic
- Setting up documentation websites

## Quick Start

```
/javascript-documentation <module_or_component_type>
```

**Example**:
```
/javascript-documentation React form components with validation
```

## How It Works

The skill provides comprehensive JavaScript documentation strategies:

### 1. JSDoc Standards
- **Function Documentation**: Parameters, returns, examples
- **Type Definitions**: @param, @returns, @typedef
- **Examples**: Usage examples in comments
- **Deprecation**: @deprecated for old APIs
- **See Also**: @see for related items

### 2. React Component Documentation
- **Props Documentation**: @component with props
- **Children**: Component children documentation
- **Examples**: Component usage patterns
- **Accessibility**: ARIA attributes and keyboard support
- **Styling**: CSS classes and customization

### 3. Documentation Tools
- **Storybook**: Interactive component documentation
- **Docusaurus**: Documentation website generator
- **Typedoc**: TypeScript API documentation
- **JSDoc**: Inline source documentation
- **Markdown**: Written documentation

### 4. Type Documentation
- **@typedef**: Custom type definitions
- **@callback**: Callback function signatures
- **@async**: Async function documentation
- **@template**: Generic type parameters
- **@union**: Union type documentation

### 5. Example Documentation
- **Basic Usage**: Simple examples
- **Advanced Patterns**: Complex scenarios
- **Error Handling**: Error cases
- **Edge Cases**: Special situations
- **Integration**: Cross-component usage

### 6. API Documentation
- **Endpoints**: API route documentation
- **Request/Response**: Schema documentation
- **Errors**: Error code documentation
- **Authentication**: Auth requirement documentation
- **Rate Limiting**: API limits

### 7. Documentation Generation
- **Auto-documentation**: Generate from comments
- **HTML Output**: Static documentation sites
- **Versioning**: Multiple documentation versions
- **Search**: Full-text search support
- **Mobile**: Responsive documentation

## Configuration

**jsdoc.json**:
```json
{
  "source": {
    "include": ["src"],
    "includePattern": ".+\\.js(doc|x)?$",
    "excludePattern": "(^|\\/|\\\\)_"
  },
  "opts": {
    "destination": "./docs",
    "recurse": true,
    "readme": "./README.md"
  },
  "templates": {
    "cleverLinks": false,
    "monospaceLinks": false
  }
}
```

**.storybook/main.ts**:
```typescript
import type { StorybookConfig } from '@storybook/react-vite';

const config: StorybookConfig = {
  stories: ['../src/**/*.stories.ts'],
  addons: [
    '@storybook/addon-links',
    '@storybook/addon-essentials',
    '@storybook/addon-interactions',
  ],
  framework: {
    name: '@storybook/react-vite',
    options: {},
  },
};

export default config;
```

## Examples

### Example 1: Function JSDoc

```javascript
/**
 * Calculates the total price including tax and shipping.
 *
 * @param {number} subtotal - The subtotal before tax and shipping
 * @param {number} taxRate - Tax rate as decimal (0.1 for 10% tax)
 * @param {number} shippingCost - Fixed shipping cost
 * @returns {number} Total price rounded to 2 decimal places
 *
 * @throws {Error} If subtotal is negative
 * @throws {Error} If tax rate is not between 0 and 1
 *
 * @example
 * const total = calculateTotal(100, 0.1, 10);
 * console.log(total); // 121
 *
 * @example
 * // With destructured parameters
 * const total = calculateTotal(500, 0.08, 15);
 * console.log(total); // 557
 */
function calculateTotal(subtotal, taxRate, shippingCost) {
  if (subtotal < 0) {
    throw new Error('Subtotal cannot be negative');
  }

  if (taxRate < 0 || taxRate > 1) {
    throw new Error('Tax rate must be between 0 and 1');
  }

  const tax = subtotal * taxRate;
  const total = subtotal + tax + shippingCost;
  return Math.round(total * 100) / 100;
}
```

### Example 2: React Component JSDoc

```typescript
/**
 * Button component for user interactions.
 *
 * @component
 * @example
 * const onClick = () => alert('Button clicked!');
 * return <Button onClick={onClick}>Click me</Button>
 *
 * @param {Object} props - Component props
 * @param {() => void} props.onClick - Click handler function
 * @param {string} [props.variant='primary'] - Button variant (primary, secondary, danger)
 * @param {boolean} [props.disabled=false] - Whether button is disabled
 * @param {React.ReactNode} props.children - Button label or content
 * @returns {React.ReactElement} Button element
 */
export const Button = ({ onClick, variant = 'primary', disabled = false, children }) => (
  <button
    onClick={onClick}
    className={`btn btn-${variant}`}
    disabled={disabled}
  >
    {children}
  </button>
);
```

### Example 3: TypeScript Component Documentation

```typescript
/**
 * User profile form component.
 *
 * @component
 * @template T - The form data type
 *
 * @example
 * interface UserFormData {
 *   name: string;
 *   email: string;
 *   age: number;
 * }
 *
 * return (
 *   <Form<UserFormData>
 *     onSubmit={(data) => console.log(data)}
 *   >
 *     {/* form fields */}
 *   </Form>
 * )
 *
 * @param {Object} props - Component props
 * @param {(data: T) => Promise<void>} props.onSubmit - Form submission handler
 * @param {React.ReactNode} props.children - Form fields
 * @param {boolean} [props.loading=false] - Loading state
 * @returns {React.ReactElement} Form element
 */
export function Form<T>({
  onSubmit,
  children,
  loading = false
}: FormProps<T>): React.ReactElement {
  // Implementation
}
```

### Example 4: Storybook Story Documentation

```typescript
// Button.stories.ts
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta = {
  title: 'Components/Button',
  component: Button,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

/**
 * The primary button variant for main actions.
 */
export const Primary: Story = {
  args: {
    children: 'Click me',
    variant: 'primary',
  },
};

/**
 * The secondary button variant for secondary actions.
 */
export const Secondary: Story = {
  args: {
    children: 'Cancel',
    variant: 'secondary',
  },
};

/**
 * The danger button variant for destructive actions.
 */
export const Danger: Story = {
  args: {
    children: 'Delete',
    variant: 'danger',
  },
};

/**
 * Disabled button state.
 */
export const Disabled: Story = {
  args: {
    children: 'Disabled',
    disabled: true,
  },
};

/**
 * Loading state with spinner.
 */
export const Loading: Story = {
  args: {
    children: 'Loading...',
    loading: true,
    disabled: true,
  },
};
```

### Example 5: Complex Function Documentation

```typescript
/**
 * Fetches user data with error handling and retry logic.
 *
 * Implements exponential backoff retry strategy for handling
 * temporary network failures.
 *
 * @async
 * @function fetchUserData
 *
 * @param {string} userId - The ID of the user to fetch
 * @param {Object} [options] - Optional configuration
 * @param {number} [options.maxRetries=3] - Maximum retry attempts
 * @param {number} [options.initialDelay=1000] - Initial delay in ms
 * @param {number} [options.backoff=2] - Exponential backoff multiplier
 *
 * @returns {Promise<User>} User object if successful
 *
 * @throws {NetworkError} If all retry attempts fail
 * @throws {NotFoundError} If user doesn't exist
 * @throws {UnauthorizedError} If API key is invalid
 *
 * @example
 * try {
 *   const user = await fetchUserData('user-123', {
 *     maxRetries: 5,
 *     initialDelay: 500,
 *   });
 *   console.log(user);
 * } catch (error) {
 *   if (error instanceof NotFoundError) {
 *     console.log('User not found');
 *   }
 * }
 *
 * @see {@link updateUserData} for updating user information
 * @see {@link deleteUserData} for deleting users
 */
async function fetchUserData(
  userId: string,
  options: FetchOptions = {}
): Promise<User> {
  // Implementation with retry logic
}
```

### Example 6: Custom Type Documentation

```javascript
/**
 * @typedef {Object} User
 * @property {number} id - Unique user identifier
 * @property {string} name - User's full name
 * @property {string} email - User's email address
 * @property {boolean} [isActive=true] - Account active status
 * @property {Date} createdAt - Account creation date
 * @property {'admin'|'user'|'guest'} role - User role
 */

/**
 * @typedef {Object} ApiResponse
 * @template T
 * @property {T} data - Response data
 * @property {number} status - HTTP status code
 * @property {string} [message] - Optional message
 */

/**
 * Processes user data and returns formatted response.
 *
 * @template T
 * @param {User} user - User object to process
 * @param {Object} options - Processing options
 * @returns {ApiResponse<T>} API response
 */
function processUserData(user, options) {
  // Implementation
}
```

### Example 7: API Endpoint Documentation

```typescript
/**
 * @file User API endpoints documentation
 * @module api/users
 */

/**
 * GET /api/users/:id
 *
 * Retrieves a single user by ID.
 *
 * @route GET /api/users/:id
 * @param {string} id - User ID (path parameter)
 * @param {string} [authorization] - Bearer token (header)
 *
 * @returns {Object} 200 - User object
 * @returns {Object} 404 - User not found
 * @returns {Object} 401 - Unauthorized
 *
 * @example
 * GET /api/users/123
 * Authorization: Bearer token123
 *
 * Response:
 * {
 *   "id": "123",
 *   "name": "John Doe",
 *   "email": "john@example.com"
 * }
 */
export async function GET(request: NextRequest, { params }: RouteProps) {
  // Implementation
}

/**
 * POST /api/users
 *
 * Creates a new user account.
 *
 * @route POST /api/users
 * @param {Object} body - Request body
 * @param {string} body.name - User's name
 * @param {string} body.email - User's email
 * @param {string} body.password - User's password
 *
 * @returns {Object} 201 - Created user
 * @returns {Object} 400 - Invalid input
 * @returns {Object} 409 - Email already exists
 *
 * @example
 * POST /api/users
 * Content-Type: application/json
 *
 * {
 *   "name": "John Doe",
 *   "email": "john@example.com",
 *   "password": "securePassword123"
 * }
 *
 * Response: 201 Created
 */
export async function POST(request: NextRequest) {
  // Implementation
}
```

## Best Practices

### 1. Documentation Standards
- Document all public functions and components
- Include parameter types and descriptions
- Provide return value documentation
- Add examples for complex functions
- Document exceptions and error cases

### 2. JSDoc Tags Priority
```javascript
/**
 * Main description here
 *
 * @param {type} name - Description
 * @returns {type} Description
 * @throws {Error} When...
 * @example
 * // Usage example
 * @see {@link relatedFunction}
 * @deprecated Use newFunction instead
 */
```

### 3. Component Documentation
- Props documentation with types
- Children documentation if applicable
- Usage examples with code
- Accessibility notes
- Styling/customization options

### 4. Storybook Organization
```
components/
├── Button.tsx
├── Button.stories.ts
├── Form.tsx
└── Form.stories.ts
```

### 5. Documentation Maintenance
- Review docs during code reviews
- Update docs when code changes
- Keep examples current
- Link related documentation
- Document breaking changes

## Integration with Other Skills

- **`javascript-code-review`**: Doc review during code review
- **`typescript-migration`**: Type hints in documentation
- **`react-testing-strategy`**: Example usage in docs
- **`nextjs-setup`**: API documentation

