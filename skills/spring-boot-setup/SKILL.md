---
name: spring-boot-setup
description: Generate and configure Spring Boot project structures with best practices and patterns
---

# Spring Boot Setup Skill

## When to Use This Skill

- Creating new Spring Boot microservices
- Setting up Spring Boot REST APIs
- Configuring Spring Data JPA for databases
- Setting up authentication and authorization
- Creating Spring Boot multi-module projects
- Configuring externalized configuration
- Setting up actuator and monitoring
- Initializing Cloud-ready Spring Boot applications

## Quick Start

```
/spring-boot-setup <project_name> <features>
```

**Example**:
```
/spring-boot-setup order-service with web, data-jpa, security, cloud-config
```

## How It Works

The skill generates complete Spring Boot project structures:

### 1. Project Structure
```
my-service/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/com/example/
│   │   │   ├── Application.java
│   │   │   ├── config/
│   │   │   ├── controller/
│   │   │   ├── service/
│   │   │   ├── repository/
│   │   │   ├── domain/
│   │   │   └── exception/
│   │   └── resources/
│   │       ├── application.yml
│   │       ├── application-dev.yml
│   │       ├── application-prod.yml
│   │       └── db/migration/ (Flyway)
│   └── test/
│       ├── java/com/example/
│       └── resources/
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── README.md
```

### 2. Key Components
- **Main Application Class**: Spring Boot entry point
- **Configuration Classes**: Database, security, cache, logging
- **Controllers**: REST endpoints with proper exception handling
- **Services**: Business logic layer with transactions
- **Repositories**: Data access layer with Spring Data JPA
- **DTOs**: Data transfer objects for API contracts
- **Exceptions**: Custom exception hierarchy
- **Tests**: Unit and integration tests

### 3. Dependencies Management
- Spring Boot Starters (web, data-jpa, security)
- Logging (SLF4J, Logback)
- Database (H2, PostgreSQL drivers)
- Testing (JUnit 5, Mockito, TestContainers)
- Utilities (Lombok, Jackson)

### 4. Configuration
- **application.yml**: Base configuration
- **Profiles**: dev, test, prod configurations
- **Externalization**: Environment-based property override
- **Secrets**: Vault integration for sensitive data

## Configuration

**Essential Dependencies (pom.xml)**:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.2.0</version>
</parent>

<dependencies>
    <!-- Web -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <!-- Data -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
    </dependency>

    <!-- Security -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-security</artifactId>
    </dependency>

    <!-- Testing -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>testcontainers</artifactId>
        <version>1.17.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

## Examples

### Example 1: Generated Application Class

```java
@SpringBootApplication
@EnableScheduling
@EnableAsync
public class OrderServiceApplication {

    public static void main(String[] args) {
        SpringApplication.run(OrderServiceApplication.class, args);
    }

    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
```

### Example 2: REST Controller

```java
@RestController
@RequestMapping("/api/v1/orders")
@RequiredArgsConstructor
@Slf4j
public class OrderController {

    private final OrderService orderService;
    private final OrderMapper orderMapper;

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public OrderDTO createOrder(@Valid @RequestBody CreateOrderRequest request) {
        log.info("Creating order: {}", request);
        Order order = orderService.create(request);
        return orderMapper.toDTO(order);
    }

    @GetMapping("/{id}")
    public OrderDTO getOrder(@PathVariable Long id) {
        return orderService.findById(id)
            .map(orderMapper::toDTO)
            .orElseThrow(() -> new OrderNotFoundException(id));
    }

    @GetMapping
    public Page<OrderDTO> listOrders(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size) {
        Pageable pageable = PageRequest.of(page, size);
        return orderService.findAll(pageable)
            .map(orderMapper::toDTO);
    }
}
```

### Example 3: Service Layer

```java
@Service
@RequiredArgsConstructor
@Slf4j
@Transactional
public class OrderService {

    private final OrderRepository orderRepository;
    private final OrderValidationService validationService;
    private final OrderEventPublisher eventPublisher;

    public Order create(CreateOrderRequest request) {
        validationService.validate(request);

        Order order = Order.builder()
            .customerId(request.getCustomerId())
            .status(OrderStatus.PENDING)
            .createdAt(LocalDateTime.now())
            .build();

        Order saved = orderRepository.save(order);
        eventPublisher.publishOrderCreated(saved);

        log.info("Order created: {}", saved.getId());
        return saved;
    }

    @Transactional(readOnly = true)
    public Optional<Order> findById(Long id) {
        return orderRepository.findById(id);
    }

    @Transactional(readOnly = true)
    public Page<Order> findAll(Pageable pageable) {
        return orderRepository.findAll(pageable);
    }
}
```

### Example 4: Configuration Classes

```java
// Database Configuration
@Configuration
@EnableJpaAuditing
@EnableJpaRepositories(basePackages = "com.example.repository")
public class DataConfig {
    // JPA configuration
}

// Security Configuration
@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .authorizeRequests()
                .antMatchers("/api/public/**").permitAll()
                .antMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            .and()
            .httpBasic();
        return http.build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}

// Async Configuration
@Configuration
@EnableAsync
public class AsyncConfig {

    @Bean(name = "taskExecutor")
    public Executor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(2);
        executor.setMaxPoolSize(5);
        executor.setQueueCapacity(100);
        executor.setThreadNamePrefix("async-");
        executor.initialize();
        return executor;
    }
}
```

### Example 5: Application Configuration (YAML)

```yaml
# application.yml
spring:
  application:
    name: order-service
  jpa:
    hibernate:
      ddl-auto: validate
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
        format_sql: true
        use_sql_comments: true
  datasource:
    url: jdbc:postgresql://localhost:5432/orders_db
    username: ${DB_USER}
    password: ${DB_PASSWORD}
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
  cache:
    type: redis
    redis:
      time-to-live: 600000

server:
  port: 8080
  servlet:
    context-path: /api
  error:
    include-message: always
    include-binding-errors: always

logging:
  level:
    com.example: DEBUG
    org.springframework.web: INFO
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss} - %logger{36} - %msg%n"
    file: "%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"
  file:
    name: logs/application.log
    max-size: 10MB
    max-history: 10

management:
  endpoints:
    web:
      exposure:
        include: health,metrics,prometheus
  endpoint:
    health:
      show-details: when-authorized
```

## Best Practices

### 1. Layered Architecture
```
controller → service → repository → database
   ↓           ↓         ↓
 DTOs      business   database
          logic       access
```

### 2. Exception Handling
```java
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {

    @ExceptionHandler(OrderNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleOrderNotFound(
            OrderNotFoundException ex) {
        return ResponseEntity
            .status(HttpStatus.NOT_FOUND)
            .body(ErrorResponse.builder()
                .error("ORDER_NOT_FOUND")
                .message(ex.getMessage())
                .timestamp(LocalDateTime.now())
                .build());
    }
}
```

### 3. Validation
```java
@Data
public class CreateOrderRequest {
    @NotNull(message = "Customer ID is required")
    private Long customerId;

    @NotEmpty(message = "Items cannot be empty")
    @Size(min = 1, max = 100, message = "Must have 1-100 items")
    private List<OrderItem> items;
}
```

### 4. Logging
```java
@Slf4j
@Service
public class OrderService {
    public Order create(CreateOrderRequest request) {
        log.info("Creating order for customer {}", request.getCustomerId());
        try {
            Order order = orderRepository.save(/* ... */);
            log.info("Order created successfully: {}", order.getId());
            return order;
        } catch (Exception e) {
            log.error("Error creating order", e);
            throw e;
        }
    }
}
```

## Integration with Other Skills

- **`java-code-review`**: Review generated code for best practices
- **`java-testing-strategy`**: Test the generated services and controllers
- **`java-security-audit`**: Secure the generated security configuration
- **`docker-setup`**: Containerize the generated application

## Generated Project Checklist

- [ ] Application class with Spring Boot annotations
- [ ] Controller with REST endpoints
- [ ] Service with business logic
- [ ] Repository with Spring Data JPA
- [ ] Domain entities with proper annotations
- [ ] DTOs for API contracts
- [ ] Exception handling and global exception handler
- [ ] Logging configured with SLF4J
- [ ] Security configuration (if selected)
- [ ] Database configuration
- [ ] Test structure with unit and integration tests
- [ ] Dockerfile for containerization
- [ ] docker-compose for local development
- [ ] Makefile with build/test/run commands
- [ ] README with setup instructions
