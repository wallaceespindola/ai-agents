---
name: code-examples-generator
description: Generate production-ready code examples for technical articles including setup, complete implementations, testing code, and runnable demonstrations. Use when creating code examples for tutorials, blog posts, and documentation that readers can immediately use and learn from.
---

# Code Examples Generation for Technical Content

## When to Use This Skill

Use this skill when:
- Creating runnable code examples for articles
- Building sample projects demonstrating patterns
- Generating before/after code comparisons
- Writing complete, production-grade examples
- Creating code repositories for tutorial series
- Generating test examples and test data
- Producing code snippets for multiple platforms

## Principles for Technical Article Code

### Code Quality Standards

#### Readability Over Cleverness
```java
// ❌ Avoid: Clever but hard to understand
return items.parallelStream()
    .filter(i -> i.getStatus() == Status.ACTIVE)
    .map(Item::getValue)
    .reduce(0, Integer::sum);

// ✅ Good: Clear intent
long totalValue = items.stream()
    .filter(item -> item.getStatus() == Status.ACTIVE)
    .map(Item::getValue)
    .reduce(0, Integer::sum);
```

#### Proper Formatting & Structure
- **Consistent indentation**: 4 spaces or 2 spaces, be consistent
- **Line length**: 80-100 characters max
- **Whitespace**: Blank lines between logical sections
- **Naming**: Clear, descriptive variable/method names
- **Comments**: Explain "why," not "what"

#### Error Handling
```python
# ❌ Avoid: Ignoring errors
try:
    user = fetch_user(user_id)
except:
    pass  # Silent failure

# ✅ Good: Proper error handling
try:
    user = fetch_user(user_id)
except UserNotFoundError as e:
    logger.warning(f"User {user_id} not found: {e}")
    return None
except NetworkError as e:
    logger.error(f"Network error fetching user: {e}")
    raise
```

### Complete vs. Snippet Code

#### When to Show Complete Code
- **New concepts**: Full context helps understanding
- **Best practices**: Show proper setup and teardown
- **Production concerns**: Include error handling, logging
- **Standalone examples**: Readers can copy and run
- **Key implementations**: Core algorithm/pattern

**Complete code characteristics:**
- Includes all imports/dependencies
- Has a main() or entry point
- Shows configuration setup
- Includes error handling
- Ready to run with minimal changes

#### When to Show Snippets
- **Demonstrating specific pattern**: Show only relevant part
- **Within larger explanation**: Snippet of larger file
- **Comparing approaches**: Before/after snippets
- **Simple operations**: Self-contained operations
- **Building on previous example**: Show additions only

**Snippet code characteristics:**
- Focused on specific concept
- Labeled with surrounding context
- Often prefaced with explanation
- Readers understand how to integrate

### Example Organization

#### Single Concept Example
```typescript
// Show the specific feature being taught
async function fetchUserWithRetry(
  userId: number,
  maxRetries: number = 3
): Promise<User> {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await fetch(`/api/users/${userId}`).then(r => r.json());
    } catch (error) {
      if (attempt === maxRetries) throw error;
      await sleep(Math.pow(2, attempt) * 100); // Exponential backoff
    }
  }
}

// Usage example
const user = await fetchUserWithRetry(42);
```

#### Complete Working Project Example
```python
"""
complete_example.py
A working example of the pattern discussed in this article.
Run with: python complete_example.py
"""

import asyncio
import logging
from typing import TypedDict
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class User:
    id: int
    name: str
    email: str

class UserService:
    """Production-ready user service implementation."""

    def __init__(self, db_connection):
        self.db = db_connection

    async def get_user(self, user_id: int) -> User:
        """Fetch user with error handling."""
        try:
            user = await self.db.query(
                "SELECT * FROM users WHERE id = ?",
                (user_id,)
            )
            if not user:
                raise ValueError(f"User {user_id} not found")
            return User(**user)
        except Exception as e:
            logger.error(f"Error fetching user {user_id}: {e}")
            raise

async def main():
    # Example usage
    service = UserService(db_connection)
    user = await service.get_user(1)
    print(f"User: {user.name} ({user.email})")

if __name__ == "__main__":
    asyncio.run(main())
```

## Code Generation By Language

### Java Code Examples

#### Setup Pattern
```java
// What to import
import java.util.*;
import java.util.concurrent.*;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
```

#### Best Practices
- Always show proper package declaration
- Include necessary imports
- Use modern Java features (records, var, pattern matching)
- Include JavaDoc for public methods
- Show exception handling

#### Framework Integration
```java
@SpringBootApplication
public class Application {

    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }

    @RestController
    @RequestMapping("/api/users")
    public class UserController {

        @GetMapping("/{id}")
        public ResponseEntity<User> getUser(@PathVariable Long id) {
            User user = userService.findById(id);
            return ResponseEntity.ok(user);
        }
    }

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

### Python Code Examples

#### Setup Pattern
```python
"""Module docstring explaining purpose."""

from typing import Optional, List
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)
```

#### Best Practices
- Use type hints (Python 3.9+)
- Include docstrings
- Use dataclasses for simple data structures
- Show async/await when relevant
- Include error handling with specific exceptions

#### FastAPI Framework
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users/{user_id}")
async def get_user(user_id: int) -> User:
    """Get user by ID."""
    user = await db.query(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

### JavaScript/TypeScript Code Examples

#### Setup Pattern
```typescript
/**
 * Module description and exports.
 */

import { Request, Response } from 'express';
import { Logger } from './utils/logger';

const logger = new Logger(__filename);
```

#### Best Practices
- Always use TypeScript (even for JavaScript articles)
- Include type definitions
- Use async/await for promises
- Show proper error handling
- Include JSDoc comments

#### Express Framework
```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

app.get('/api/users/:id', async (req: Request, res: Response) => {
  try {
    const user = await db.users.findById(req.params.id);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.json(user);
  } catch (error) {
    logger.error('Error fetching user:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});
```

## Code Example Patterns

### Before/After Comparison

**Structure:**
1. Problem code (what developers commonly do)
2. Explanation of why it's problematic
3. Improved solution
4. Explanation of improvements

```java
// ❌ Before: N+1 Query Problem
public List<User> getUsersWithPosts() {
    List<User> users = userRepository.findAll(); // 1 query
    for (User user : users) {
        user.setPosts(postRepository.findByUserId(user.getId())); // N queries
    }
    return users;
}

// ✅ After: Optimized with Join
@Query("SELECT u FROM User u LEFT JOIN FETCH u.posts")
public List<User> getUsersWithPosts();
```

### Step-by-Step Implementation

**Structure:**
1. Start with basics
2. Add each feature incrementally
3. Show final complete version
4. Explain each addition

```python
# Step 1: Basic function
def calculate_total(items):
    total = 0
    for item in items:
        total += item['price']
    return total

# Step 2: Handle edge cases
def calculate_total(items):
    if not items:
        return 0
    total = 0
    for item in items:
        total += item.get('price', 0)  # Handle missing price
    return total

# Step 3: Use Pythonic approach
def calculate_total(items):
    return sum(item.get('price', 0) for item in items)
```

### Real-World Example

**Structure:**
1. Problem statement
2. Architecture overview
3. Code implementation
4. How it solves the problem
5. Results/metrics

```java
// Problem: Handle spikes in order processing
// Solution: Async event-driven architecture

// Implementation:
public class OrderEventProducer {
    private final KafkaTemplate<String, OrderEvent> kafkaTemplate;

    public void publishOrderCreated(Order order) {
        OrderEvent event = new OrderEvent(
            order.getId(),
            order.getCustomerId(),
            OrderEventType.CREATED
        );
        kafkaTemplate.send("orders", String.valueOf(order.getId()), event);
    }
}

public class OrderEventConsumer {
    @KafkaListener(topics = "orders")
    public void handleOrderCreated(OrderEvent event) {
        // Process order asynchronously
        // Multiple consumers can process in parallel
    }
}
```

## Creating Runnable Examples

### Project Structure
```
example-project/
├── src/
│   └── main/
│       └── java/
│           └── com/example/
│               └── Main.java
├── tests/
│   └── test/
│       └── java/
│           └── com/example/
│               └── MainTest.java
├── pom.xml (or build.gradle)
└── README.md (Instructions to run)
```

### README for Running Examples
```markdown
# Example: [Title]

This example demonstrates [concept].

## Prerequisites
- Java 17+ (or specify version)
- Maven 3.8+ (or gradle 7.0+)

## Running the Example

1. Clone or download this directory
2. Navigate to the directory: `cd example-project`
3. Run: `mvn clean package` (or `gradle build`)
4. Execute: `java -jar target/example.jar`
5. See output in console

## Expected Output
[Show what the successful output looks like]

## Code Explanation
[Brief explanation of what the code does]
```

### Testing Examples
```java
@SpringBootTest
public class UserServiceTest {

    @Autowired
    private UserService userService;

    @MockBean
    private UserRepository userRepository;

    @Test
    public void testGetUserSuccess() {
        // Given
        User expectedUser = new User(1L, "John", "john@example.com");
        when(userRepository.findById(1L)).thenReturn(Optional.of(expectedUser));

        // When
        User result = userService.getUser(1L);

        // Then
        assertNotNull(result);
        assertEquals("John", result.getName());
    }
}
```

## Code Snippets by Concept

### Exception Handling Pattern
```python
try:
    result = perform_operation()
except ValueError as e:
    logger.warning(f"Invalid input: {e}")
    return None
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise  # Re-raise for higher-level handling
```

### Async/Concurrent Pattern
```javascript
// Promise-based
Promise.all([
    fetch('/api/users'),
    fetch('/api/posts'),
    fetch('/api/comments')
])
.then(responses => Promise.all(responses.map(r => r.json())))
.then(([users, posts, comments]) => {
    console.log('All data:', { users, posts, comments });
})
.catch(error => console.error('Error:', error));

// Async/await (modern)
async function loadData() {
    try {
        const [usersRes, postsRes, commentsRes] = await Promise.all([
            fetch('/api/users'),
            fetch('/api/posts'),
            fetch('/api/comments')
        ]);

        const users = await usersRes.json();
        const posts = await postsRes.json();
        const comments = await commentsRes.json();

        return { users, posts, comments };
    } catch (error) {
        console.error('Error loading data:', error);
        throw error;
    }
}
```

## Code Example Checklist

Before including code in article:

- [ ] Code compiles/runs without errors
- [ ] All dependencies shown or explained
- [ ] Example demonstrates stated concept clearly
- [ ] Includes proper error handling
- [ ] Follows language conventions and idioms
- [ ] Line length reasonable (80-100 chars)
- [ ] Variable names are descriptive
- [ ] Comments explain non-obvious logic
- [ ] No credentials or API keys included
- [ ] Security best practices followed
- [ ] Performance considered (if relevant)
- [ ] Testing code included where applicable
- [ ] Can be understood in isolation

## Common Code Mistakes to Avoid

❌ **Overly simplified**: Too simple to be useful in production

❌ **Missing error handling**: Real code needs to handle failures

❌ **Unclear variable names**: `x = foo.bar()` instead of `totalPrice = cart.calculateTotal()`

❌ **No imports shown**: Reader doesn't know dependencies

❌ **Pseudo-code**: "... do something here ..." instead of real code

❌ **Outdated syntax**: Old language features instead of modern

❌ **No comments in complex sections**: Logic is unclear

❌ **Broken code**: Doesn't actually run

❌ **Poor formatting**: Hard to read and follow

❌ **No context**: Code exists in vacuum without explanation

## Platform-Specific Code Formatting

### Medium Code Blocks
- Use markdown backticks with language
- Full code preferred (links not emphasized)
- Keep under 40 lines for readability
- Show output after code

### Dev.to Code Blocks
- Supports many language syntax highlights
- Can create GitHub gists for longer examples
- Code output often shown inline
- Supports runnable embeds (CodePen, JSFiddle)

### LinkedIn Posts
- Keep code snippets minimal (5-10 lines)
- Focus on concept, not full implementation
- Link to full repository
- Screenshot of code sometimes better for mobile

### Substack Code
- Text-based is most reliable
- Code quality depends on email client
- Usually link to GitHub for full examples
- Explain over showing full code

### JavaPro Magazine
- Publication-grade code examples
- Production-ready implementations
- Include supporting files (tests, config)
- Detailed explanation of implementation choices
