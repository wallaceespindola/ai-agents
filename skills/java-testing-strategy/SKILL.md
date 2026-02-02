---
name: java-testing-strategy
description: Design comprehensive test strategies for Java applications using JUnit, Mockito, and TestContainers
---

# Java Testing Strategy Skill

## When to Use This Skill

- Designing test strategy for new Java/Spring Boot applications
- Improving test coverage and test quality
- Setting up test automation frameworks
- Planning unit, integration, and E2E tests
- Configuring test isolation and mocking strategies
- Establishing testing best practices for teams
- Migrating from legacy testing approaches

## Quick Start

```
/java-testing-strategy <component_or_service>
```

**Example**:
```
/java-testing-strategy UserService class for payment processing
```

## How It Works

The skill develops a multi-layered testing strategy:

### 1. Test Pyramid Analysis
- **Unit Tests (70%)**: Fast, isolated, mocked dependencies
- **Integration Tests (20%)**: Database, external services with TestContainers
- **E2E Tests (10%)**: Full application flow, critical user journeys

### 2. Coverage Planning
- **Code Coverage Target**: 80% minimum (70% for legacy code)
- **Coverage Gap Analysis**: Identify untested paths
- **Branch Coverage**: Ensure all conditional paths tested
- **Critical Paths**: 100% coverage for security/payment logic

### 3. Test Framework Selection
- **JUnit 5**: Modern testing framework with parameterized tests
- **Mockito**: Mocking and stubbing dependencies
- **TestContainers**: Docker-based test databases and services
- **AssertJ**: Fluent assertions for readable tests
- **Awaitility**: Async and parallel test execution

### 4. Test Organization
- **Naming Convention**: Test class = `{ClassName}Test`
- **Method Naming**: `should{Expected}When{Condition}`
- **Package Structure**: Mirror production package structure
- **Test Fixtures**: Setup/teardown, shared test data

### 5. Mock Strategy
- **Constructor Injection**: Inject mocks for testability
- **Mock vs Stub**: When to use each approach
- **Partial Mocking**: Spy on real objects when needed
- **Test Doubles**: Fakes, mocks, stubs, spies explained

## Configuration

**Dependencies (pom.xml)**:
```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.9.0</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-core</artifactId>
    <version>5.0.0</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.17.0</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.assertj</groupId>
    <artifactId>assertj-core</artifactId>
    <version>3.22.0</version>
    <scope>test</scope>
</dependency>
```

## Examples

### Example 1: Unit Test with Mockito

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private EmailService emailService;

    @InjectMocks
    private UserService userService;

    @Test
    void shouldCreateUserAndSendEmail() {
        // Arrange
        CreateUserRequest request = new CreateUserRequest("john@example.com");
        User expectedUser = new User(1L, "john@example.com");

        when(userRepository.save(any(User.class)))
            .thenReturn(expectedUser);

        // Act
        User createdUser = userService.createUser(request);

        // Assert
        assertThat(createdUser)
            .isNotNull()
            .extracting("email")
            .isEqualTo("john@example.com");

        verify(emailService).sendWelcomeEmail("john@example.com");
    }

    @Test
    void shouldThrowExceptionWhenEmailAlreadyExists() {
        // Arrange
        CreateUserRequest request = new CreateUserRequest("john@example.com");
        when(userRepository.save(any(User.class)))
            .thenThrow(new DataIntegrityViolationException("Email exists"));

        // Act & Assert
        assertThatThrownBy(() -> userService.createUser(request))
            .isInstanceOf(UserAlreadyExistsException.class)
            .hasMessage("User with email already exists");
    }
}
```

### Example 2: Integration Test with TestContainers

```java
@SpringBootTest
@Testcontainers
class UserRepositoryIntegrationTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(
        DockerImageName.parse("postgres:14-alpine")
    ).withDatabaseName("testdb");

    @Autowired
    private UserRepository userRepository;

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Test
    void shouldFindUserByEmail() {
        // Arrange
        User user = new User(null, "john@example.com", "John Doe");
        userRepository.save(user);

        // Act
        Optional<User> foundUser = userRepository.findByEmail("john@example.com");

        // Assert
        assertThat(foundUser)
            .isPresent()
            .get()
            .extracting("email")
            .isEqualTo("john@example.com");
    }
}
```

### Example 3: Parameterized Test

```java
@ParameterizedTest
@CsvSource({
    "john@example.com, true",
    "invalid.email, false",
    "admin@company.com, true",
    "user @example.com, false"
})
void shouldValidateEmailFormat(String email, boolean expected) {
    assertThat(userService.isValidEmail(email))
        .isEqualTo(expected);
}
```

### Example 4: Testing Async Code

```java
@Test
void shouldCompleteAsyncOperation() {
    // Arrange
    CompletableFuture<User> future = userService.fetchUserAsync(1L);

    // Act & Assert
    assertThat(future)
        .succeedsWithin(Duration.ofSeconds(2))
        .extracting("email")
        .isEqualTo("john@example.com");
}

@Test
void shouldHandleAsyncError() {
    // Arrange
    when(userRepository.findByIdAsync(999L))
        .thenReturn(CompletableFuture.failedFuture(
            new UserNotFoundException("User not found")
        ));

    // Act & Assert
    assertThat(userService.fetchUserAsync(999L))
        .failsWithin(Duration.ofSeconds(2))
        .withThrowableOfType(CompletionException.class)
        .withCauseInstanceOf(UserNotFoundException.class);
}
```

## Best Practices

### 1. Test Naming Convention
```java
@Test
void should{Action}When{Condition}And{AnotherCondition}() {
    // Clear what should happen and under what conditions
}

// Examples:
// shouldThrowExceptionWhenUserNotFound
// shouldReturnUserWhenIdExists
// shouldUpdateEmailAndSendNotificationWhenEmailChanges
```

### 2. Arrange-Act-Assert Pattern
```java
@Test
void shouldCalculateDiscount() {
    // ARRANGE: Setup test data
    Order order = new Order();
    order.setTotal(100.0);
    order.addItem(new Item(50.0));

    // ACT: Execute the operation
    double discount = pricingService.calculateDiscount(order);

    // ASSERT: Verify results
    assertThat(discount).isEqualTo(10.0);
}
```

### 3. Test Data Builders
```java
@Test
void shouldProcessOrder() {
    Order order = new OrderBuilder()
        .withCustomer("John")
        .withItems(new Item("Product1"), new Item("Product2"))
        .withPaymentMethod("CREDIT_CARD")
        .build();

    assertThat(orderService.process(order)).isSuccessful();
}
```

### 4. Avoid Test Interdependence
```java
// ❌ BAD: Tests depend on execution order
@Test
void shouldCreateUser() { /* ... */ }

@Test
void shouldFindUser() {  // Depends on shouldCreateUser running first
    // ...
}

// ✅ GOOD: Each test is independent
@Test
void shouldFindUser() {
    User user = userRepository.save(new User("john@example.com"));
    // Test can run in any order
}
```

### 5. Mock External Dependencies
```java
@Test
void shouldRetryOnFailure() {
    // Mock external API that might be slow/unavailable
    when(externalApi.call()).thenThrow(new TimeoutException())
        .thenReturn("success");

    String result = service.callWithRetry();
    assertThat(result).isEqualTo("success");
}
```

### 6. Use Test Fixtures
```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    private UserService userService;

    @BeforeEach
    void setUp() {
        userService = new UserService(userRepository, emailService);
    }

    @Test
    void shouldCreateUser() { /* ... */ }
}
```

## Integration with Other Skills

- **`java-code-review`**: Ensure code is testable before writing tests
- **`java-performance-tuning`**: Test performance improvements
- **`java-security-audit`**: Test security fixes and validation logic
- **`spring-boot-setup`**: Follow test structure in project templates

## Test Strategy Template

```
1. Unit Tests (70%)
   - Service layer business logic
   - Utility and helper functions
   - Edge cases and error conditions
   - Mocked external dependencies

2. Integration Tests (20%)
   - Database operations (with TestContainers)
   - API endpoints (MockMvc)
   - Message queue integration
   - Cache behavior

3. E2E Tests (10%)
   - Critical user journeys
   - Payment processing flows
   - User registration to purchase
   - Admin operations

4. Coverage Goals
   - Overall: 80% line coverage
   - Security code: 95% coverage
   - Payment code: 95% coverage
   - Legacy code: 50% coverage

5. Performance
   - Unit tests: < 1 second per 100 tests
   - Integration tests: < 5 seconds per test
   - E2E tests: < 30 seconds per test
```
