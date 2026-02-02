---
name: javascript-coder
description: Generate complete production-ready JavaScript/TypeScript projects with full source code, tests, and documentation. Create linked repositories where articles in /docs reference code in src and tests folders. Perfect for tutorials, patterns, and real-world examples.
---

# JavaScript/TypeScript Coder Skill

Generate production-ready JavaScript and TypeScript projects that complement technical articles. This skill creates complete, runnable code with proper project structure, dependency management, tests, and documentation.

## When to Use This Skill

Use this skill when:
- Writing a JavaScript/TypeScript tutorial and want readers to access complete working code
- Demonstrating a design pattern with a full implementation
- Building a case study with actual running code
- Creating a reference implementation for an architecture pattern
- Writing about React, Node.js, or async patterns and need functional examples
- Showing advanced JavaScript/TypeScript features with working code
- Teaching best practices through example projects

## Quick Start

### Create a JavaScript Project

When you have an article about JavaScript, request code generation:

```
Create a TypeScript/React project for my article "React Hooks Deep Dive"
Include:
- React components with custom hooks
- TypeScript strict mode
- Jest unit tests
- React Testing Library integration tests
- README with setup instructions
- Link to article in /docs/ARTICLE.md
```

### Project Structure

Standard Node.js/React project layout:

```
project-name/
├── package.json                     # Project metadata and dependencies
├── tsconfig.json                    # TypeScript configuration
├── jest.config.js                   # Jest test configuration
├── .eslintrc.json                   # ESLint configuration
├── .prettierrc                       # Code formatting
├── README.md                        # Quick start guide
├── docs/
│   ├── ARTICLE.md                   # Your article (or link to it)
│   └── SETUP.md                     # Development setup guide
├── src/
│   ├── index.ts                     # Entry point
│   ├── main.ts                      # Application bootstrap
│   ├── components/                  # React components
│   │   ├── Component.tsx
│   │   └── Component.test.tsx
│   ├── hooks/                       # Custom React hooks
│   │   ├── useHook.ts
│   │   └── useHook.test.ts
│   ├── services/                    # Business logic
│   │   ├── service.ts
│   │   └── service.test.ts
│   ├── types/                       # TypeScript types
│   │   └── index.ts
│   ├── utils/                       # Utility functions
│   │   ├── helper.ts
│   │   └── helper.test.ts
│   └── styles/                      # CSS/styling (optional)
├── tests/
│   ├── setup.ts                     # Test setup
│   ├── fixtures.ts                  # Test data
│   └── integration/
│       └── integration.test.ts
├── node_modules/                    # Dependencies
├── dist/                            # Build output
└── .gitignore
```

## Core Concepts

### 1. Project Configuration

**package.json Setup:**
- Project metadata (name, version, description)
- Scripts for dev, build, test
- Dependencies with versions
- Development dependencies
- TypeScript configuration
- Testing configuration

**Example package.json:**
```json
{
  "name": "project-name",
  "version": "1.0.0",
  "description": "Description",
  "type": "module",
  "main": "dist/index.js",
  "scripts": {
    "dev": "tsx watch src/main.ts",
    "build": "tsc",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "lint": "eslint src",
    "format": "prettier --write src"
  },
  "dependencies": {
    "react": "^18.0.0"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "jest": "^29.0.0"
  }
}
```

**TypeScript Configuration:**
- Strict mode enabled
- Modern target (ES2020+)
- Module resolution
- Declaration files

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM"],
    "jsx": "react-jsx",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

### 2. Code Organization

**Components (React):**
- Functional components with hooks
- TypeScript interfaces for props
- Clear component responsibilities
- Custom hooks for logic
- Proper error boundaries

**Services/Business Logic:**
- Separation from components
- Pure functions
- Type-safe implementations
- Error handling

**Utilities:**
- Helper functions
- Constants
- Configuration

**Types:**
- Centralized type definitions
- Interface definitions
- Type guards
- Utility types

### 3. Testing Strategy

**Unit Tests:**
- Service/utility function tests
- Hook tests with react-hooks-testing-library
- Pure function testing

**Component Tests:**
- Render testing with React Testing Library
- User interaction testing
- Props validation
- State changes

**Integration Tests:**
- Multiple components working together
- Data flow testing
- User workflows

**Test Organization:**
```
src/
├── hooks/
│   ├── useHook.ts
│   └── useHook.test.ts
├── services/
│   ├── service.ts
│   └── service.test.ts
└── components/
    ├── Component.tsx
    └── Component.test.tsx

tests/
├── setup.ts
├── fixtures.ts
└── integration/
    └── integration.test.tsx
```

### 4. Documentation

**README.md should include:**
- Project description and purpose
- Prerequisites (Node version, npm/pnpm)
- Setup instructions (git clone, npm install)
- Running the application
- Running tests
- Building for production
- Project structure overview
- Key features
- Article reference

**SETUP.md should include:**
- Development environment setup
- IDE configuration (VS Code, WebStorm)
- Debugging setup
- Environment variables
- Troubleshooting

**Inline code documentation:**
- JSDoc comments for functions
- Type definitions are documentation
- Complex logic explanations
- Links to article sections

### 5. Linking to Articles

**In article (/docs/ARTICLE.md):**
```markdown
## Running the Example

This article includes a complete working example. Clone the repository:

```bash
git clone <repo-url>
cd project-name
npm install
npm run dev
```

Then follow the instructions in README.md.

Key files:
- `src/hooks/useHook.ts` - Custom hook implementation
- `src/components/Component.tsx` - Component using the hook
- `src/components/Component.test.tsx` - Tests demonstrating usage
```

**In code (README.md):**
```markdown
## Associated Article

This code example supports the article:
[Article Title](./docs/ARTICLE.md)

For detailed explanation of design decisions, see the article.
```

## Common Patterns

### React Component Project

**Files to generate:**
- Functional components with React hooks
- Custom hooks (useState, useEffect, useContext, etc.)
- Props interfaces with TypeScript
- Component composition
- State management (Context API or simple state)
- Component tests with React Testing Library
- Integration tests

**Key features:**
- TypeScript strict mode
- React 18+ with hooks
- Functional components only
- Proper error boundaries
- Accessible components (ARIA)
- Good testing practices

### Node.js Backend Project

**Files to generate:**
- Express or Fastify application
- Route handlers
- Service/business logic layer
- Database models
- Middleware
- Error handling
- Request validation
- Tests with Jest
- Integration tests

**Key features:**
- Async/await throughout
- Type-safe with TypeScript
- Error handling patterns
- Logging
- Request validation

### Design Pattern Implementation

**Example: Observer Pattern**
```
Files:
- observer.ts (Observer and Subject types)
- concreteObserver.ts (implementations)
- main.ts (usage example)
- observer.test.ts (tests)
```

**Example: Factory Pattern**
```
Files:
- factory.ts (Factory implementation)
- types.ts (type definitions)
- concrete.ts (concrete implementations)
- factory.test.ts (tests)
```

### Async/Promise Patterns

**Files to generate:**
- Promise handling examples
- Async/await patterns
- Error handling in async code
- Concurrent execution
- Race conditions prevention
- Proper cleanup
- Comprehensive tests

**Key features:**
- Modern async/await
- Error handling
- Type-safe promise handling
- Examples of common pitfalls

## Article Integration Workflow

### Step 1: Write Article in /docs/ARTICLE.md

Create your article explaining the concept, design, or pattern.

### Step 2: Request Code Generation

```
Generate TypeScript/JavaScript code for my article about [topic].
Article file: docs/ARTICLE.md

Requirements:
- React / Node.js (choose framework)
- [specific implementation details]
- [design patterns to demonstrate]
- [technologies to use]
- [test coverage expectations]
```

### Step 3: Generated Project Includes

- Complete source code in `src/`
- Comprehensive tests
- README.md with setup instructions
- package.json with all dependencies
- TypeScript configuration
- Links to article in documentation

### Step 4: Integrate in Repository

```
my-repo/
├── docs/
│   └── articles/
│       └── article-name/
│           ├── ARTICLE.md
│           └── README.md
│
└── projects/
    └── article-name-example/
        ├── package.json
        ├── tsconfig.json
        ├── README.md              # Links to article
        ├── src/...
        └── tests/...
```

Or simpler, single project:

```
my-repo/
├── package.json
├── README.md
├── docs/
│   └── ARTICLE.md
└── src/...
```

## Best Practices

### Code Quality

✅ **Do:**
- Use TypeScript in strict mode
- Name variables and functions clearly
- Keep functions small and focused
- Use proper types, not `any`
- Handle errors explicitly
- Use const by default, let when needed
- Use early returns to reduce nesting
- Write pure functions
- Use destructuring for cleaner code

❌ **Avoid:**
- Using `any` type
- Long functions doing multiple things
- var (use const/let)
- Mutable global state
- Deep nesting
- Silent error swallowing
- Side effects in pure functions
- Magic numbers or strings (use constants)
- Callback hell (use promises/async-await)

### React Specific

✅ **Do:**
- Use functional components with hooks
- Custom hooks for reusable logic
- Proper dependency arrays in useEffect
- Props interfaces/types
- Error boundaries for error handling
- Proper key in lists
- Accessibility (ARIA labels, semantic HTML)
- Split components into smaller pieces

❌ **Avoid:**
- Class components (unless necessary)
- Missing or wrong dependency arrays
- State in props
- Rendering lists without keys
- Passing too many props (drill)
- Logic inside JSX
- Component inside component definition

### Testing

✅ **Do:**
- Test user behavior, not implementation
- Use React Testing Library patterns
- Test error cases
- Mock external dependencies appropriately
- Use fixtures for test data
- Name tests clearly
- Keep tests DRY with helper functions
- Test accessibility

❌ **Avoid:**
- Over-mocking (mock at boundaries)
- Testing implementation details
- Snapshots as primary assertion
- Slow tests (unit tests should be fast)
- Tests that depend on each other
- Hardcoded test data
- Not testing error cases

### TypeScript

✅ **Do:**
- Use strict mode
- Define types for parameters and returns
- Use interfaces for objects
- Use discriminated unions for variants
- Use utility types (Partial, Pick, etc.)
- Avoid type assertions (let types flow)

❌ **Avoid:**
- Using `any` everywhere
- Loose types (implicit any)
- Over-typing simple things
- Unnecessary type assertions with `as`
- Not using strict mode

## Project Templates

### Template 1: React Component Library

```
Key files:
- Components with proper TypeScript types
- Custom hooks with thorough tests
- Storybook stories (optional)
- Component tests with React Testing Library
- TypeScript strict mode
```

**Dependencies:**
- react
- react-dom
- typescript
- jest
- @testing-library/react
- @testing-library/user-event

### Template 2: Node.js REST API

```
Key files:
- Express/Fastify app setup
- Route handlers
- Service/business logic layer
- Type-safe request/response
- Error handling middleware
- Tests with Jest
- Integration tests
```

**Dependencies:**
- express or fastify
- typescript
- jest
- supertest (for API testing)

### Template 3: Design Pattern Showcase

```
Key files:
- Pattern implementations
- Client code showing usage
- Comprehensive tests
- Documentation of pattern
```

**Dependencies:**
- typescript
- jest

### Template 4: Async/Promise Patterns

```
Key files:
- Promise examples
- Async/await patterns
- Error handling examples
- Concurrent execution examples
- Tests with Jest
```

**Dependencies:**
- typescript
- jest

## File Generation Checklist

### Configuration Files
- [ ] package.json with scripts and dependencies
- [ ] tsconfig.json with strict mode
- [ ] jest.config.js with TypeScript support
- [ ] .eslintrc.json with recommended rules
- [ ] .prettierrc for formatting
- [ ] .gitignore with Node exclusions
- [ ] .env.example with environment variables

### Source Code
- [ ] src/index.ts or main entry point
- [ ] src/types/ with TypeScript definitions
- [ ] src/services/ with business logic
- [ ] src/utils/ with helper functions
- [ ] Components (if React project)
- [ ] Hooks (if React project)
- [ ] Middleware (if Node.js backend)
- [ ] Configuration management

### Tests
- [ ] tests/setup.ts with test configuration
- [ ] tests/fixtures.ts with test data
- [ ] Unit tests for each module
- [ ] Component tests (if React)
- [ ] Integration tests
- [ ] Test configuration and helpers

### Documentation
- [ ] README.md with complete setup
- [ ] SETUP.md with development guide
- [ ] JSDoc comments for public functions
- [ ] Type definitions as documentation
- [ ] Links to article

### Quality
- [ ] All tests pass
- [ ] No TypeScript errors
- [ ] No ESLint errors
- [ ] Code formatted with Prettier
- [ ] No unused imports
- [ ] Proper error handling

## Build and Run Commands

**Commands to document:**

```bash
# Install dependencies
npm install
# or with pnpm (faster)
pnpm install

# Development
npm run dev              # Start dev server/watch mode
npm run build            # Compile TypeScript
npm test                 # Run all tests
npm run test:watch      # Run tests in watch mode
npm run test:coverage   # Tests with coverage report

# Code quality
npm run lint            # Check with ESLint
npm run format          # Format with Prettier
npm run type-check      # TypeScript type checking

# Production
npm run build           # Create production build
npm start               # Run production build
```

## Dependency Management

**Modern approach with package.json:**
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "typescript": "^5.0.0"
  },
  "devDependencies": {
    "jest": "^29.0.0",
    "@testing-library/react": "^14.0.0"
  }
}
```

**Version specifications:**
- `^` - allow minor/patch updates
- `~` - allow patch updates only
- Exact version - no updates

## Code Style & Formatting

**ESLint + Prettier:**
```json
// .eslintrc.json
{
  "extends": ["eslint:recommended", "plugin:@typescript-eslint/recommended"],
  "rules": {
    "no-var": "error",
    "prefer-const": "error"
  }
}

// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 80
}
```

## Integration with Article Workflow

1. **Write article** in `/docs/ARTICLE.md`
2. **Request JavaScript/TypeScript code** mentioning article file
3. **Receive complete project** with:
   - Source code in `src/`
   - Tests set up
   - README.md linking to article
   - Ready to run setup
4. **Link from article** to GitHub repository
5. **Readers can clone** and run the code
6. **Maintain together**: Article and code stay in sync

## Common Scenarios

### Scenario 1: React Tutorial

Article shows how to build component. Code shows complete working implementation.

Reader can:
- Follow article step by step
- See complete working code
- Run and test locally
- Modify and experiment
- Use as starting point

### Scenario 2: Design Pattern

Article explains pattern. Code shows real, working implementation.

Reader can:
- Learn pattern from article
- See production-ready code
- Run tests to see pattern work
- Use as reference

### Scenario 3: Async Patterns

Article explains async concepts. Code shows real examples running.

Reader can:
- Understand async patterns
- See practical implementations
- Run and modify examples
- Experiment safely

## Success Checklist

- [ ] Code compiles without TypeScript errors
- [ ] All tests pass
- [ ] Tests have meaningful assertions
- [ ] README is clear and complete
- [ ] Code passes ESLint
- [ ] Proper TypeScript types throughout
- [ ] Article is linked from README
- [ ] Setup instructions work
- [ ] Code is production-ready
- [ ] Key functions have JSDoc
- [ ] Error handling is appropriate
- [ ] No hardcoded values

---

This skill works best combined with:
- **javascript-content** for JavaScript expertise and guidance
- **code-examples-generator** for snippet generation
- **markdown-formatter** for documentation formatting
- **architecture-design** for pattern explanations
- **image-generator-blog** for architecture diagrams in docs
