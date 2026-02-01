---
name: javascript-content
description: Write engaging JavaScript and TypeScript content covering modern frameworks, async patterns, performance, tooling, and best practices. Use when creating articles about React, Node.js, TypeScript, Vue, web performance, or JavaScript ecosystem tools for developer audiences.
---

# JavaScript Content Generation

## When to Use This Skill

Use this skill when:
- Writing tutorials on JavaScript features or frameworks
- Explaining TypeScript, async patterns, or ES6+ syntax
- Creating articles about React, Vue, Svelte, or Next.js
- Covering Node.js patterns and backend JavaScript
- Discussing web performance and optimization
- Explaining JavaScript tooling (webpack, Vite, esbuild, turbopack)
- Writing about async/promises, event loops, or concurrency

## Quick Start: Article Structure

### For Tutorials
1. **Hook** (2-3 sentences): Problem the reader faces
2. **Why It Matters** (1 paragraph): Use cases and benefits
3. **Prerequisites** (bullet points): Knowledge and setup needed
4. **Step-by-Step Implementation** (5-8 steps): Clear walkthrough
5. **Complete Code Example** (full, runnable code)
6. **Key Takeaways** (3-5 bullet points)
7. **Common Mistakes** (pitfalls to avoid)
8. **Next Steps** (related topics)

### For Best Practices Articles
1. **Problem Statement**: What developers commonly do wrong
2. **Why It Matters**: Performance/maintainability/UX implications
3. **The Right Pattern**: Recommended approach with explanation
4. **Code Comparison** (Before/After):
   - Before: Anti-pattern or naive approach
   - After: Best practice solution
   - Explanation: Why this is better
5. **Real-world Example**: From popular libraries or production code
6. **Edge Cases**: When NOT to use this pattern
7. **Further Reading**: Related concepts

## JavaScript Core Concepts to Cover

### Modern JavaScript (ES2020+)
- Optional chaining: `obj?.nested?.property`
- Nullish coalescing: `value ?? defaultValue`
- BigInt: Large integer support
- Dynamic imports: `import(modulePath)`
- Promise.all variants: Promise.allSettled, Promise.any
- WeakMap/WeakSet for memory efficiency

### TypeScript Mastery
- Advanced types: Discriminated unions, generics, conditional types
- Utility types: Partial, Pick, Omit, Record
- Type guards and assertion functions
- Decorators and metadata
- Module declaration and augmentation
- Strict mode best practices

### React Patterns (17+)
- Hooks: useState, useEffect, useContext, useReducer
- Custom hooks and composition
- Suspense and error boundaries
- Concurrent features and transitions
- Performance: React.memo, useMemo, useCallback
- State management patterns (zustand, Jotai)
- Testing with React Testing Library

### Node.js & Backend
- Express vs Fastify vs Hono: Architecture differences
- Middleware patterns and error handling
- Stream processing for large data
- Worker threads for CPU-intensive tasks
- Database patterns (ORMs vs query builders)
- Testing Node.js (Jest, Vitest)

### Web Performance
- Core Web Vitals: LCP, FID, CLS
- Code splitting and lazy loading
- Image optimization (WebP, AVIF)
- Bundle analysis and tree-shaking
- Caching strategies
- Service workers and PWAs

### Async Patterns
- Callbacks (legacy)
- Promises: Then/catch chains vs error handling
- Async/await best practices
- Concurrent requests with Promise.all
- Error handling in async contexts
- Race conditions and cancellation

### Modern Tooling
- **Build tools**: Vite, webpack, esbuild, turbopack
- **Package managers**: npm, yarn, pnpm (why pnpm is better)
- **Testing**: Vitest, Jest, Playwright
- **Linting**: ESLint, Prettier, TypeScript
- **Development**: hot module replacement (HMR), source maps

## Code Example Template

```typescript
/**
 * Module purpose and exports.
 */

interface UserData {
  id: number;
  name: string;
  email: string;
}

/**
 * Fetches user data from API.
 * @param userId - The user ID to fetch
 * @returns Promise with user data
 */
async function fetchUser(userId: number): Promise<UserData> {
  const response = await fetch(`/api/users/${userId}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch user: ${response.statusText}`);
  }
  return response.json();
}

// Example usage
async function main(): Promise<void> {
  try {
    const user = await fetchUser(1);
    console.log(`User: ${user.name}`);
  } catch (error) {
    console.error("Error:", error);
  }
}

main();
```

**Guidelines for code examples:**
- Always use TypeScript (even for JavaScript articles, show TS alternative)
- Include JSDoc comments for public APIs
- Make examples runnable in browser or Node.js
- Keep examples concise (50-100 lines max)
- Use modern syntax (const/let, arrow functions, template literals)
- Show error handling
- Follow Prettier/ESLint conventions
- Comment only non-obvious logic

## Audience-Specific Tips

### For Frontend Developers
- Focus on React, Vue, or framework of choice
- Include CSS/styling considerations
- Discuss browser APIs (fetch, storage, etc.)
- Cover accessibility and semantic HTML

### For Full-Stack Developers
- Balance frontend and backend concerns
- Discuss API design
- Include deployment strategies
- Cover database interactions from JS perspective

### For Backend/Node.js Developers
- Emphasize scalability and performance
- Discuss database ORMs and query patterns
- Cover authentication and authorization
- Include DevOps considerations (logging, monitoring)

### For Performance-Focused Developers
- Include metrics and benchmarks
- Show measurement tools and techniques
- Discuss trade-offs
- Include real-world performance data

## SEO Keywords for JavaScript Content

- JavaScript ES2020, TypeScript
- React, Next.js, Vue.js, Svelte
- Node.js, Express, Fastify
- Async/await, Promises
- Web performance, Core Web Vitals
- Vite, webpack, esbuild
- Jest, Vitest, testing
- Performance optimization
- Hooks, state management
- Web API, browser APIs

## Examples

### Example 1: React Hook Article Hook
"The useEffect hook is one of the hardest concepts in React because it runs at unexpected times. Understanding the dependency array and when effects run can eliminate most bugs in your components."

### Example 2: TypeScript Article
"TypeScript's discriminated unions give you type-safe handling of different data shapes. Instead of checking a type property at runtime, TypeScript tracks which properties are available based on a discriminator. Here's how to use them effectively."

### Example 3: Pattern Article
**Before (❌ Anti-pattern):**
```typescript
// Callback hell
function getData(id: number) {
  fetch(`/api/users/${id}`)
    .then(res => res.json())
    .then(user => {
      fetch(`/api/posts/${user.id}`)
        .then(res => res.json())
        .then(posts => console.log(posts));
    });
}
```

**After (✅ Modern approach):**
```typescript
async function getData(id: number): Promise<void> {
  const user = await fetch(`/api/users/${id}`).then(r => r.json());
  const posts = await fetch(`/api/posts/${user.id}`).then(r => r.json());
  console.log(posts);
}
```

## Common Pitfalls to Mention

1. **Closure issues**: Variables captured unexpectedly
2. **This binding**: Arrow functions vs regular functions
3. **Promise anti-patterns**: Not properly handling rejections
4. **Memory leaks**: Event listeners not removed
5. **N+1 requests**: Fetching in loops instead of parallel
6. **Type safety loss**: Any types defeating TypeScript purpose
7. **Bundle bloat**: Not analyzing dependencies
8. **Inefficient re-renders**: Missing keys, unnecessary state
9. **Race conditions**: Multiple async operations overwriting state
10. **Not using optional chaining**: Defensive programming

## Research & Validation

Before publishing:
- Test all code examples in modern browsers/Node.js
- Check framework version compatibility
- Verify performance claims with benchmarks
- Run examples through TypeScript in strict mode
- Check for security vulnerabilities
- Test on mobile browsers if relevant
- Validate with eslint/prettier configuration

## Modern React Patterns

### Pattern 1: Custom Hook
```typescript
function useFetch<T>(url: string): { data: T | null; loading: boolean; error: Error | null } {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    fetch(url)
      .then(r => r.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [url]);

  return { data, loading, error };
}
```

### Pattern 2: Discriminated Union
```typescript
type Result<T> =
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };

function handleResult<T>(result: Result<T>): void {
  switch (result.status) {
    case 'loading':
      console.log('Loading...');
      break;
    case 'success':
      console.log(result.data); // Type-safe!
      break;
    case 'error':
      console.error(result.error);
  }
}
```

## Content Variations by Platform

- **LinkedIn Pulse**: Career perspectives, industry evolution
- **Medium**: Deep dives with architecture explanations
- **Dev.to**: Quick wins, code snippets, practical tips
- **Substack**: Learning journey, personal development insights
- **JavaPro Equivalent**: Enterprise JavaScript patterns and architecture
