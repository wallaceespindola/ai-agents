---
name: java-documentation
description: Create comprehensive JavaDoc and technical documentation for Java applications
---

# Java Documentation Skill

## When to Use This Skill

- Writing JavaDoc for public APIs
- Creating architectural documentation
- Documenting API endpoints and request/response contracts
- Writing setup and installation guides
- Creating troubleshooting guides
- Documenting configuration options
- Creating developer onboarding guides
- Generating API documentation (Swagger/OpenAPI)

## Quick Start

```
/java-documentation <class_or_module> <documentation_type>
```

**Example**:
```
/java-documentation OrderService class for JavaDoc and API documentation
```

## How It Works

The skill creates comprehensive documentation:

### 1. JavaDoc Standards
- **Public API**: Document all public classes, methods, and fields
- **Parameters**: @param for all method parameters
- **Returns**: @return describing return value
- **Exceptions**: @throws for checked exceptions
- **Examples**: Code examples in documentation
- **Deprecation**: @deprecated with replacement information
- **Links**: Cross-references using @see and {@link}

### 2. Architecture Documentation
- **System Overview**: High-level architecture diagram
- **Component Descriptions**: Purpose and responsibilities
- **Data Flow**: How data flows through components
- **Design Decisions**: Why certain patterns were chosen
- **Trade-offs**: Pros and cons of architectural choices

### 3. API Documentation
- **Endpoint Descriptions**: What each endpoint does
- **HTTP Methods**: GET, POST, PUT, DELETE usage
- **Request/Response**: Example JSON payloads
- **Error Codes**: Possible error responses
- **Authentication**: How to authenticate requests
- **Rate Limiting**: Throttling policies if applicable

### 4. Configuration Documentation
- **Environment Variables**: Required and optional env vars
- **Property Files**: Configuration properties
- **Secret Management**: How to provide secrets
- **Profiles**: Different configurations for dev/test/prod
- **Examples**: Sample configuration files

### 5. Setup & Installation
- **Prerequisites**: Required software and versions
- **Installation Steps**: Step-by-step setup
- **Configuration**: How to configure the application
- **Running**: How to start the application
- **Testing**: How to verify installation

## Configuration

**Swagger/OpenAPI Dependencies (pom.xml)**:
```xml
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.0.0</version>
</dependency>
```

**Maven JavaDoc Plugin**:
```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-javadoc-plugin</artifactId>
    <version>3.5.0</version>
    <configuration>
        <source>17</source>
        <doclet>com.github.javaparser.JavaParser</doclet>
        <additionalOptions>
            <additionalOption>-author</additionalOption>
            <additionalOption>-version</additionalOption>
        </additionalOptions>
    </configuration>
</plugin>
```

## Examples

### Example 1: Comprehensive JavaDoc

```java
/**
 * Manages user operations including creation, retrieval, and deletion.
 *
 * <p>This service handles all business logic related to user management,
 * including validation, persistence, and event publishing.
 *
 * <p>Example usage:
 * <pre>{@code
 * UserDTO user = userService.createUser(createRequest);
 * UserDTO updated = userService.updateUser(user.getId(), updateRequest);
 * userService.deleteUser(user.getId());
 * }</pre>
 *
 * @author John Doe
 * @version 2.0
 * @since 1.0
 * @see UserRepository
 * @see UserValidator
 */
@Service
@RequiredArgsConstructor
@Slf4j
public class UserService {

    /**
     * Creates a new user with the provided information.
     *
     * <p>Validates input, checks for duplicates, and publishes user creation event.
     *
     * @param request contains user email, name, and initial password.
     *                Cannot be null.
     * @return the created user with assigned ID
     * @throws UserAlreadyExistsException if user with email already exists
     * @throws InvalidUserDataException if request data is invalid
     * @since 1.0
     *
     * @see UserValidator#validate(CreateUserRequest)
     * @see UserRepository#save(User)
     */
    public UserDTO createUser(@Valid @NotNull CreateUserRequest request) {
        // implementation
    }

    /**
     * Finds a user by their unique email address.
     *
     * @param email the user's email address. Must be a valid email format.
     * @return an Optional containing the user if found, empty otherwise
     * @throws IllegalArgumentException if email is null or blank
     * @since 1.0
     */
    public Optional<UserDTO> findByEmail(@NotBlank String email) {
        // implementation
    }

    /**
     * Retrieves a paginated list of all users.
     *
     * @param pageable pagination information (page number, size, sort)
     * @return a page of users
     * @throws IllegalArgumentException if pageable is null
     * @since 2.0
     */
    public Page<UserDTO> listUsers(@NotNull Pageable pageable) {
        // implementation
    }

    /**
     * Deletes a user by ID.
     *
     * @param id the user's unique identifier
     * @throws UserNotFoundException if user with ID not found
     * @throws UserDeletionException if deletion fails
     * @since 1.0
     */
    public void deleteUser(@NotNull Long id) {
        // implementation
    }
}
```

### Example 2: REST Controller with Swagger Annotations

```java
/**
 * User API endpoints for managing users.
 */
@RestController
@RequestMapping("/api/v1/users")
@RequiredArgsConstructor
@Slf4j
@Tag(
    name = "Users",
    description = "Endpoints for user management"
)
public class UserController {

    private final UserService userService;

    /**
     * Create a new user.
     *
     * @param request user creation request with email and password
     * @return the created user with ID
     * @response 201 Created user successfully
     * @response 400 Invalid user data
     * @response 409 User already exists
     */
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    @Operation(
        summary = "Create a new user",
        description = "Creates a new user with the provided email and password"
    )
    @ApiResponse(
        responseCode = "201",
        description = "User created successfully"
    )
    @ApiResponse(
        responseCode = "400",
        description = "Invalid input data"
    )
    public UserDTO createUser(@Valid @RequestBody CreateUserRequest request) {
        return userService.createUser(request);
    }

    /**
     * Retrieve a user by ID.
     *
     * @param id the user's unique identifier
     * @return the user details
     * @response 200 User found
     * @response 404 User not found
     */
    @GetMapping("/{id}")
    @Operation(summary = "Get user by ID")
    public UserDTO getUser(
            @PathVariable
            @Parameter(description = "User's unique identifier")
            Long id) {
        return userService.findById(id);
    }

    /**
     * List all users with pagination and filtering.
     *
     * @param page page number (0-indexed)
     * @param size number of items per page
     * @param sort sort criteria (format: field,asc|desc)
     * @return paginated list of users
     */
    @GetMapping
    @Operation(summary = "List users")
    public Page<UserDTO> listUsers(
            @RequestParam(defaultValue = "0")
            @Parameter(description = "Page number")
            int page,
            @RequestParam(defaultValue = "10")
            @Parameter(description = "Page size")
            int size) {
        Pageable pageable = PageRequest.of(page, size);
        return userService.listUsers(pageable);
    }
}
```

### Example 3: Architecture Documentation (Markdown)

```markdown
# Order Service Architecture

## Overview

The Order Service is a microservice responsible for managing customer orders,
including creation, fulfillment, and tracking.

## Components

### Controller Layer (UserFacing)
- `OrderController`: REST API endpoints for order operations
- Input validation and HTTP error handling

### Service Layer (BusinessLogic)
- `OrderService`: Core business logic for order processing
- `OrderValidationService`: Validates orders before creation
- `OrderEventPublisher`: Publishes domain events

### Persistence Layer (DataAccess)
- `OrderRepository`: Spring Data JPA repository
- `OrderHistoryRepository`: Tracks order status changes

### External Integrations
- Payment Service API (via REST client)
- Notification Service (via message queue)
- Analytics Service (via event stream)

## Data Flow

```
1. Client sends POST /orders
2. OrderController receives request
3. OrderValidationService validates input
4. OrderService creates order
5. OrderRepository persists to database
6. OrderEventPublisher sends events
7. Response returned to client
```

## Technology Stack

- Language: Java 17
- Framework: Spring Boot 3.x
- Database: PostgreSQL 14
- Message Queue: RabbitMQ
- Monitoring: Prometheus + Grafana

## Configuration

See [Configuration Guide](./CONFIG.md)

## API Documentation

See [API Documentation](./API.md) or visit `/swagger-ui.html` when running locally
```

### Example 4: Configuration Documentation

```markdown
# Configuration Guide

## Environment Variables

### Required
- `DB_HOST`: Database hostname (default: localhost)
- `DB_PORT`: Database port (default: 5432)
- `DB_NAME`: Database name (default: orders_db)
- `DB_USER`: Database username
- `DB_PASSWORD`: Database password

### Optional
- `SERVER_PORT`: Application port (default: 8080)
- `LOG_LEVEL`: Logging level (default: INFO)
- `CACHE_TTL`: Cache time-to-live in seconds (default: 600)
- `RABBITMQ_HOST`: RabbitMQ hostname (default: localhost)

## Application Properties

Create `application.properties` or `application.yml`:

```yaml
spring:
  datasource:
    url: jdbc:postgresql://${DB_HOST}:${DB_PORT}/${DB_NAME}
    username: ${DB_USER}
    password: ${DB_PASSWORD}

  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false

logging:
  level:
    com.example: INFO
    org.springframework: WARN

server:
  port: ${SERVER_PORT:8080}
```

## Running the Application

```bash
# With environment variables
export DB_HOST=localhost
export DB_PORT=5432
export DB_USER=admin
export DB_PASSWORD=secret
mvn spring-boot:run

# Or with properties
mvn spring-boot:run -Dspring-boot.run.arguments=\
  --spring.datasource.url=jdbc:postgresql://localhost:5432/orders_db
```
```

## Best Practices

### 1. Keep JavaDoc Current
- Update JavaDoc when code changes
- Use IDE hints to identify missing documentation
- Generate JavaDoc regularly to check for inconsistencies

### 2. Use Code Examples
- Include realistic usage examples
- Show both happy path and error cases
- Keep examples compilable and correct

### 3. Document "Why" Not Just "What"
```java
// ❌ Poor: Just repeats the method name
/**
 * Creates a user.
 */
public User createUser(CreateUserRequest request) { }

// ✅ Good: Explains business logic
/**
 * Creates a new user and sends welcome email.
 *
 * This method validates the email format to prevent duplicate entries,
 * generates a secure password hash, and publishes a UserCreated event
 * that triggers the welcome email workflow.
 */
public User createUser(CreateUserRequest request) { }
```

### 4. Link Related Classes
```java
/**
 * {@link UserService} for creating users
 * {@link UserValidator} for validation rules
 * @see UserRepository
 */
```

### 5. Document Exceptions
```java
/**
 * @throws UserAlreadyExistsException if email is already registered
 * @throws InvalidEmailException if email format is invalid
 * @throws DatabaseException if persistence fails
 */
public User createUser(String email) throws UserAlreadyExistsException {
}
```

## Integration with Other Skills

- **`java-code-review`**: Verify code is properly documented
- **`technical-writer`**: Publish generated documentation to user guides
- **`spring-boot-setup`**: Document generated project structure

## Documentation Checklist

- [ ] All public classes have JavaDoc
- [ ] All public methods have parameter descriptions
- [ ] All public methods have return value documentation
- [ ] All exceptions are documented
- [ ] Usage examples provided for complex APIs
- [ ] Deprecated items marked with @deprecated
- [ ] Related classes linked with @see
- [ ] Architecture documentation written
- [ ] API endpoints documented with Swagger
- [ ] Configuration options documented
- [ ] Setup guide provided
- [ ] README includes quick start
