# Spring Boot Microservices Skill

**Master Spring Cloud, service discovery, API Gateway, circuit breakers, distributed transactions, and microservices patterns.**

## Overview

Microservices architecture requires sophisticated patterns and tools. This skill covers Spring Cloud patterns and distributed system design.

**What it does:**
- Configures Spring Cloud services
- Implements service discovery (Eureka, Consul)
- Sets up API Gateway (Spring Cloud Gateway)
- Implements circuit breakers (Hystrix, Resilience4j)
- Handles distributed transactions (Saga pattern)
- Manages distributed configuration
- Implements inter-service communication
- Handles service-to-service authentication

**Perfect for:**
- Scaling applications
- Building resilient systems
- Managing multiple services
- Enterprise microservices
- Cloud-native applications

---

## When to Use This Skill

Use Spring Boot Microservices when you need to:

- **Scale independent services** horizontally
- **Manage service discovery** dynamically
- **Handle service failures** gracefully
- **Implement distributed transactions**
- **Route traffic** through API Gateway
- **Implement circuit breaker** pattern
- **Manage distributed configuration**
- **Handle inter-service communication**

---

## Quick Start (15 Minutes)

### 1. Service Discovery (Eureka)

Add dependency:

```xml
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
</dependency>
```

Enable server:

```java
@SpringBootApplication
@EnableEurekaServer
public class EurekaServerApplication {
  public static void main(String[] args) {
    SpringApplication.run(EurekaServerApplication.class, args);
  }
}
```

### 2. Service Registration

Add client dependency:

```xml
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>
```

Configure application.yml:

```yaml
spring:
  application:
    name: user-service

eureka:
  client:
    serviceUrl:
      defaultZone: http://localhost:8761/eureka/
```

### 3. API Gateway

Add dependency:

```xml
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-starter-gateway</artifactId>
</dependency>
```

Configure routes:

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://user-service
          predicates:
            - Path=/users/**
```

### 4. Circuit Breaker

Add dependency:

```xml
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-starter-circuitbreaker-resilience4j</artifactId>
</dependency>
```

Use in service:

```java
@Service
public class PaymentService {
  @CircuitBreaker(name = "paymentService", fallbackMethod = "fallback")
  public Payment processPayment(Order order) {
    // Call external service
  }

  public Payment fallback(Order order, Exception ex) {
    return new Payment(0, "Service unavailable");
  }
}
```

---

## How It Works

### 1. Service Discovery

**Eureka Server:**

```java
@SpringBootApplication
@EnableEurekaServer
public class EurekaServer {
  public static void main(String[] args) {
    SpringApplication.run(EurekaServer.class, args);
  }
}
```

**Eureka Client:**

```yaml
eureka:
  client:
    serviceUrl:
      defaultZone: http://eureka-server:8761/eureka/
  instance:
    hostname: user-service
    prefer-ip-address: true
    health-check-url: http://${eureka.instance.hostname}:${server.port}/health
```

**Service Discovery:**

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
  @Autowired
  private RestTemplate restTemplate;

  @GetMapping("/{id}/orders")
  public List<Order> getUserOrders(@PathVariable String id) {
    // Service discovery automatically finds order-service
    String url = "http://order-service/api/orders?userId=" + id;
    return restTemplate.getForObject(url, List.class);
  }
}
```

### 2. API Gateway

**Route Configuration:**

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://user-service
          predicates:
            - Path=/api/users/**
          filters:
            - StripPrefix=2

        - id: order-service
          uri: lb://order-service
          predicates:
            - Path=/api/orders/**
          filters:
            - AddRequestHeader=X-Request-ID, 1234

        - id: product-service
          uri: lb://product-service
          predicates:
            - Path=/api/products/**
            - Method=GET,POST
```

**Custom Filters:**

```java
@Component
public class LoggingGatewayFilterFactory extends AbstractGatewayFilterFactory<LoggingGatewayFilterFactory.Config> {

  @Override
  public GatewayFilter apply(Config config) {
    return (exchange, chain) -> {
      ServerHttpRequest request = exchange.getRequest();
      LOG.info("Incoming request: {} {}", request.getMethod(), request.getPath());

      return chain.filter(exchange).then(Mono.fromRunnable(() -> {
        ServerHttpResponse response = exchange.getResponse();
        LOG.info("Response status: {}", response.getStatusCode());
      }));
    };
  }

  public static class Config {
  }
}
```

### 3. Circuit Breaker Patterns

**Resilience4j Configuration:**

```yaml
resilience4j:
  circuitbreaker:
    configs:
      default:
        registerHealthIndicator: true
        slidingWindowSize: 10
        minimumNumberOfCalls: 5
        permittedNumberOfCallsInHalfOpenState: 3
        automaticTransitionFromOpenToHalfOpenEnabled: true
        waitDurationInOpenState: 5s
        failureRateThreshold: 50
        slowCallRateThreshold: 50
        slowCallDurationThreshold: 2s
    instances:
      paymentService:
        baseConfig: default
        waitDurationInOpenState: 10s
```

**Circuit Breaker Annotation:**

```java
@Service
public class PaymentService {

  @CircuitBreaker(name = "paymentService", fallbackMethod = "paymentFallback")
  @Retry(name = "paymentService")
  @Timeout(name = "paymentService")
  public Payment processPayment(Order order) {
    // May fail
    return paymentGateway.charge(order);
  }

  public Payment paymentFallback(Order order, Exception ex) {
    LOG.warn("Payment service failed, returning pending", ex);
    return new Payment(0, "PENDING", "Service temporarily unavailable");
  }
}
```

### 4. Inter-Service Communication

**Synchronous (REST):**

```java
@Service
public class OrderService {
  @Autowired
  private RestTemplate restTemplate;

  @Autowired
  private WebClient webClient;

  // Using RestTemplate
  public User getUser(String userId) {
    return restTemplate.getForObject("http://user-service/users/" + userId, User.class);
  }

  // Using WebClient (reactive)
  public Mono<User> getUserAsync(String userId) {
    return webClient.get()
      .uri("http://user-service/users/{id}", userId)
      .retrieve()
      .bodyToMono(User.class);
  }
}
```

**Asynchronous (Messages):**

```java
@Service
public class OrderService {
  @Autowired
  private RabbitTemplate rabbitTemplate;

  public void createOrder(Order order) {
    order.setId(UUID.randomUUID().toString());
    // Send event to message broker
    rabbitTemplate.convertAndSend("order.exchange", "order.created", order);
  }
}

@Service
public class NotificationService {
  @RabbitListener(queues = "order.created.queue")
  public void handleOrderCreated(Order order) {
    sendEmailNotification(order.getCustomerId());
  }
}
```

### 5. Distributed Transactions (Saga Pattern)

**Choreography (Event-Driven):**

```java
// Order Service
@Service
public class OrderService {
  @Autowired
  private RabbitTemplate rabbit;

  public void createOrder(Order order) {
    order.setStatus("PENDING");
    orderRepository.save(order);

    rabbit.convertAndSend("order.exchange", "order.created", order);
  }

  @RabbitListener(queues = "payment.confirmed.queue")
  public void handlePaymentConfirmed(Payment payment) {
    Order order = orderRepository.findById(payment.getOrderId());
    order.setStatus("CONFIRMED");
    orderRepository.save(order);

    rabbit.convertAndSend("order.exchange", "order.confirmed", order);
  }
}

// Payment Service
@Service
public class PaymentService {
  @RabbitListener(queues = "order.created.queue")
  public void handleOrderCreated(Order order) {
    try {
      Payment payment = processPayment(order);
      payment.setStatus("CONFIRMED");
      paymentRepository.save(payment);

      rabbit.convertAndSend("payment.exchange", "payment.confirmed", payment);
    } catch (Exception ex) {
      rabbit.convertAndSend("order.exchange", "order.cancelled", order);
    }
  }
}
```

**Orchestration (Saga Orchestrator):**

```java
@Service
public class OrderSagaOrchestrator {

  @Transactional
  public void executeOrderSaga(Order order) {
    try {
      // Step 1: Create order
      order.setStatus("PENDING");
      orderService.create(order);

      // Step 2: Process payment
      Payment payment = paymentService.process(order.getId());
      if (!payment.isSuccessful()) {
        throw new PaymentFailedException();
      }

      // Step 3: Reserve inventory
      inventoryService.reserve(order.getId());

      // Step 4: Confirm order
      order.setStatus("CONFIRMED");
      orderService.update(order);

    } catch (Exception ex) {
      // Compensate
      paymentService.refund(order.getId());
      inventoryService.release(order.getId());
      order.setStatus("CANCELLED");
      orderService.update(order);
    }
  }
}
```

### 6. Distributed Configuration

**Spring Cloud Config Server:**

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/myorg/config-repo
          username: ${GIT_USER}
          password: ${GIT_PASSWORD}
          search-paths: config
```

**Client Configuration:**

```yaml
spring:
  cloud:
    config:
      uri: http://config-server:8888
      name: user-service
      profile: prod
```

---

## Configuration

### Complete Microservices Setup

`pom.xml`:

```xml
<parent>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-parent</artifactId>
  <version>3.2.0</version>
</parent>

<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-dependencies</artifactId>
      <version>2023.0.0</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>

<dependencies>
  <!-- Service Discovery -->
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
  </dependency>

  <!-- Circuit Breaker -->
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-circuitbreaker-resilience4j</artifactId>
  </dependency>

  <!-- API Gateway -->
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-gateway</artifactId>
  </dependency>

  <!-- Distributed Config -->
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-config</artifactId>
  </dependency>

  <!-- Messaging -->
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-amqp</artifactId>
  </dependency>

  <!-- Reactive -->
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-webflux</artifactId>
  </dependency>

  <!-- Monitoring -->
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
  </dependency>
</dependencies>
```

---

## Examples

### Example 1: Complete Service

```java
@SpringBootApplication
@EnableEurekaClient
@EnableCircuitBreaker
public class UserServiceApplication {
  public static void main(String[] args) {
    SpringApplication.run(UserServiceApplication.class, args);
  }
}

@RestController
@RequestMapping("/api/users")
public class UserController {
  @Autowired
  private UserService service;

  @GetMapping("/{id}")
  public User getUser(@PathVariable String id) {
    return service.getUserById(id);
  }
}

@Service
public class UserService {
  @Autowired
  private UserRepository repository;

  @CircuitBreaker(name = "userService")
  public User getUserById(String id) {
    return repository.findById(id)
      .orElseThrow(() -> new UserNotFoundException());
  }
}
```

### Example 2: API Gateway Configuration

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://user-service
          predicates:
            - Path=/api/users/**
          filters:
            - StripPrefix=2
            - AddRequestHeader=X-Service-Id, user-service

        - id: order-service
          uri: lb://order-service
          predicates:
            - Path=/api/orders/**
          filters:
            - StripPrefix=2
```

### Example 3: Saga Pattern

```java
@Service
public class OrderSaga {

  public void execute(Order order) {
    // Step 1
    orderService.create(order);

    // Step 2
    try {
      paymentService.charge(order);
    } catch (Exception ex) {
      // Compensate
      orderService.cancel(order);
      throw ex;
    }
  }
}
```

---

## Best Practices

### 1. Use Circuit Breakers

```java
@CircuitBreaker(name = "externalService", fallbackMethod = "fallback")
public Data callExternalService() {
  return externalService.getData();
}

public Data fallback(Exception ex) {
  return getCachedData();
}
```

### 2. Implement Timeouts

```yaml
resilience4j:
  timelimiter:
    configs:
      default:
        cancelRunningFuture: true
        timeoutDuration: 2s
```

### 3. Log Distributed Calls

```java
@Aspect
@Component
public class LoggingAspect {
  @Around("execution(* com.example.service.*.*(..))")
  public Object logServiceCall(ProceedingJoinPoint pjp) throws Throwable {
    String serviceName = pjp.getTarget().getClass().getSimpleName();
    LOG.info("Calling: {}", serviceName);

    long start = System.currentTimeMillis();
    Object result = pjp.proceed();

    LOG.info("Completed: {} in {}ms", serviceName, System.currentTimeMillis() - start);
    return result;
  }
}
```

### 4. Monitor Services

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,metrics,env,configprops
  metrics:
    export:
      prometheus:
        enabled: true
```

---

## Integration with Other Skills

Spring Boot Microservices integrates with:

- **kubernetes-yaml-generation** - Deploy microservices to K8s
- **docker-compose-setup** - Local development environment
- **build-optimization** - Fast builds for multiple services
- **secrets-management** - Manage service credentials

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
