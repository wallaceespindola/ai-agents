---
name: java-code-review
description: Review Java code for best practices, design patterns, performance, and security issues
---

# Java Code Review Skill

## When to Use This Skill

- Reviewing pull requests for Java/Spring Boot applications
- Assessing code quality before merging to main branches
- Identifying design pattern opportunities and anti-patterns
- Catching performance issues and memory leaks
- Ensuring OWASP compliance and security best practices
- Mentoring junior developers on Java standards
- Enforcing coding standards across teams

## Quick Start

```
/java-code-review <file_path_or_diff>
```

**Example**:
```
/java-code-review src/main/java/com/example/UserService.java
```

## How It Works

The skill performs multi-level code analysis:

### 1. Code Quality Analysis
- **Readability**: Variable naming, method length, complexity (cyclomatic complexity)
- **Maintainability**: DRY principle, code duplication, cohesion
- **Standards**: Google Java Style Guide compliance, PEP conventions
- **Imports**: Unused imports, proper organization with `import java.util.*` detection

### 2. Design Pattern Review
- **Structural Patterns**: Singleton, Factory, Builder, Decorator usage
- **Behavioral Patterns**: Observer, Strategy, State pattern identification
- **SOLID Principles**: SRP, OCP, LSP, ISP, DIP compliance
- **Anti-patterns**: Detection of common mistakes (God Objects, Feature Envy)

### 3. Performance Analysis
- **Memory Usage**: Object creation frequency, garbage collection impact
- **Concurrency**: Thread safety, synchronization issues, deadlock potential
- **Database Queries**: N+1 problems, inefficient queries, missing indexes
- **Caching**: Missed optimization opportunities

### 4. Security Review
- **OWASP Top 10**: SQL injection, XSS, authentication/authorization
- **Credential Management**: No hardcoded secrets, proper vault usage
- **Validation**: Input validation, null checks, bounds checking
- **Encryption**: Proper use of cryptography, secure random generation
- **Dependencies**: Known vulnerabilities in third-party libraries

### 5. Spring Boot Specific
- **Best Practices**: Proper bean management, lifecycle handling
- **Configuration**: Application properties, profiles, externalized config
- **Exception Handling**: Global exception handlers, proper logging
- **Testing**: MockMvc usage, test isolation, mock management

## Configuration

No special configuration required. The skill uses:
- Java language syntax analysis
- Spring Boot framework conventions
- OWASP security guidelines
- Google Java Style Guide

**Optional Environment Variables**:
```
CHECKSTYLE_CONFIG=path/to/checkstyle.xml  # Custom style rules
SONARQUBE_URL=http://sonarqube:9000       # For SonarQube integration
```

## Examples

### Example 1: Identifying Memory Leak

```java
// ❌ ISSUE: Static collection grows indefinitely
public class Cache {
    private static final List<String> cache = new ArrayList<>();

    public void add(String value) {
        cache.add(value);  // Never cleared!
    }
}

// ✅ FIXED: Use bounded cache with eviction
public class Cache {
    private final LinkedHashMap<String, String> cache =
        new LinkedHashMap<String, String>(16, 0.75f, true) {
            protected boolean removeEldestEntry(Map.Entry eldest) {
                return size() > 1000;  // Max 1000 entries
            }
        };
}
```

### Example 2: Thread Safety Issue

```java
// ❌ ISSUE: Non-thread-safe lazy initialization
public class Singleton {
    private static Singleton instance;

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();  // Race condition!
        }
        return instance;
    }
}

// ✅ FIXED: Thread-safe eager initialization
public class Singleton {
    private static final Singleton instance = new Singleton();

    public static Singleton getInstance() {
        return instance;
    }

    private Singleton() {}
}
```

### Example 3: N+1 Query Problem

```java
// ❌ ISSUE: N+1 database queries
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;
    @Autowired
    private AddressRepository addressRepository;

    public List<UserDTO> getUsers() {
        List<User> users = userRepository.findAll();  // 1 query
        return users.stream()
            .map(user -> new UserDTO(
                user,
                addressRepository.findByUser(user)  // N more queries!
            ))
            .collect(toList());
    }
}

// ✅ FIXED: Eager load with JOIN
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    public List<UserDTO> getUsers() {
        List<User> users = userRepository.findAllWithAddresses();  // 1 query with JOIN
        return users.stream()
            .map(UserDTO::new)
            .collect(toList());
    }
}

// In UserRepository:
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    @Query("SELECT u FROM User u LEFT JOIN FETCH u.addresses")
    List<User> findAllWithAddresses();
}
```

### Example 4: Security - Hardcoded Credentials

```java
// ❌ ISSUE: Hardcoded database password
public class DatabaseConfig {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/mydb";
    private static final String DB_USER = "root";
    private static final String DB_PASSWORD = "password123";  // SECURITY ISSUE!
}

// ✅ FIXED: Use environment variables or config server
@Configuration
public class DatabaseConfig {
    @Value("${db.url}")
    private String dbUrl;

    @Value("${db.user}")
    private String dbUser;

    @Value("${db.password}")
    private String dbPassword;

    // Use these values from application.properties or external vault
}
```

### Example 5: Proper Exception Handling

```java
// ❌ ISSUE: Swallowing exceptions, bare throws
public class OrderService {
    public void processOrder(Order order) throws Exception {
        try {
            // process order
        } catch (SQLException e) {
            e.printStackTrace();  // Bad: printed to console
            throw new Exception("Error");  // Bad: generic exception
        }
    }
}

// ✅ FIXED: Specific exceptions, proper logging
public class OrderService {
    private static final Logger logger = LoggerFactory.getLogger(OrderService.class);

    public void processOrder(Order order) throws OrderProcessingException {
        try {
            // process order
        } catch (SQLException e) {
            logger.error("Failed to process order {}: {}", order.getId(), e.getMessage(), e);
            throw new OrderProcessingException("Failed to process order", e);
        }
    }
}
```

## Best Practices

### 1. Method Length
- **Target**: Methods should be 20-30 lines maximum
- **Benefit**: Easier to test, understand, and maintain
- **Refactor**: Extract smaller methods with clear responsibility

### 2. Class Cohesion
- **Target**: All methods should use most fields of the class
- **Benefit**: Clear responsibility, easier to test
- **Refactor**: Split into smaller, focused classes

### 3. Dependency Injection
- **Practice**: Inject dependencies via constructor, not instantiate
- **Benefit**: Easier to test, swap implementations
- **Spring**: Use `@Autowired` with constructor injection (not field injection)

### 4. Null Safety
- **Practice**: Use Optional or null checks, avoid NullPointerException
- **Tools**: Use `@NonNull`, `@Nullable` annotations
- **Alternative**: Use `Objects.requireNonNull()` for defensive programming

### 5. Constants and Magic Numbers
- **Practice**: Extract magic numbers to named constants
- **Example**: `if (age > 18)` → `if (age > ADULT_AGE)` where `ADULT_AGE = 18`

### 6. Immutability
- **Practice**: Prefer immutable objects when possible
- **Benefit**: Thread-safe, predictable behavior
- **Java Records**: Use Java 16+ records for simple immutable classes

### 7. Exception Handling
- **Practice**: Catch specific exceptions, not generic `Exception`
- **Logging**: Use SLF4J with proper log levels
- **Hierarchy**: Create custom exception types for domain-specific errors

## Integration with Other Skills

- **`java-testing-strategy`**: Use code review findings to design comprehensive tests
- **`java-performance-tuning`**: Address performance issues identified in review
- **`java-security-audit`**: Deep dive into security findings from code review
- **`spring-boot-setup`**: Review alignment with project templates and conventions

## Common Issues Found

| Issue | Impact | Solution |
|-------|--------|----------|
| Mutable static fields | Thread safety | Use `final` or encapsulation |
| Exception swallowing | Debugging difficulty | Log and re-throw |
| N+1 queries | Performance | Use JOIN FETCH or batch loading |
| Hardcoded secrets | Security | Use environment variables |
| God objects | Maintainability | Split into smaller classes |
| No null checks | Runtime errors | Use Optional or assertions |
| Synchronization on `this` | Concurrency | Use dedicated locks or ConcurrentHashMap |
