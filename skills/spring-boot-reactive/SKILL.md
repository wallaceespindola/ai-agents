# Spring Boot Reactive Skill

**Master Project Reactor, WebFlux, reactive streams, backpressure, non-blocking DB operations.**

## Overview

Reactive programming enables high-performance, non-blocking applications. This skill covers Project Reactor and Spring WebFlux patterns.

**What it does:**
- Implements reactive streams with Project Reactor
- Uses Spring WebFlux for non-blocking web applications
- Handles backpressure correctly
- Implements non-blocking database operations
- Manages reactive transformations
- Implements error handling in reactive chains
- Performs reactive testing
- Optimizes reactive applications

**Perfect for:**
- High-throughput applications
- Real-time data processing
- Non-blocking I/O operations
- Resource-constrained environments
- Highly concurrent systems

---

## Quick Start (15 Minutes)

### 1. WebFlux Setup

Add dependency:

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-webflux</artifactId>
</dependency>
```

### 2. Reactive Controller

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

  @Autowired
  private UserService userService;

  @GetMapping("/{id}")
  public Mono<User> getUser(@PathVariable String id) {
    return userService.getUserById(id);
  }

  @GetMapping
  public Flux<User> getAllUsers() {
    return userService.getAllUsers();
  }

  @PostMapping
  public Mono<User> createUser(@RequestBody Mono<CreateUserRequest> request) {
    return request.flatMap(userService::createUser);
  }
}
```

### 3. Reactive Service

```java
@Service
public class UserService {

  @Autowired
  private UserRepository repository;

  public Mono<User> getUserById(String id) {
    return Mono.fromCallable(() -> repository.findById(id))
      .flatMap(Mono::fromOptional)
      .onErrorResume(e -> Mono.empty());
  }

  public Flux<User> getAllUsers() {
    return Flux.fromIterable(repository.findAll())
      .parallel(10)
      .runOn(Schedulers.parallel())
      .sequential();
  }
}
```

### 4. WebClient (Reactive HTTP)

```java
@Service
public class ApiClient {

  @Autowired
  private WebClient webClient;

  public Mono<UserData> getUser(String id) {
    return webClient.get()
      .uri("/users/{id}", id)
      .retrieve()
      .bodyToMono(UserData.class);
  }

  public Flux<Post> getPosts(String userId) {
    return webClient.get()
      .uri("/posts?userId={id}", userId)
      .retrieve()
      .bodyToFlux(Post.class);
  }
}
```

---

## How It Works

### 1. Project Reactor Basics

**Mono (0-1 element):**

```java
// Create Mono
Mono<String> mono = Mono.just("Hello");
Mono<String> empty = Mono.empty();
Mono<String> error = Mono.error(new Exception("Error"));

// Subscribe
mono.subscribe(
  value -> System.out.println(value),
  error -> System.err.println(error),
  () -> System.out.println("Complete")
);

// Transform
Mono<Integer> length = mono.map(String::length);
Mono<String> upper = mono.map(String::toUpperCase);

// Chain
Mono<String> chained = mono
  .map(String::toUpperCase)
  .flatMap(s -> Mono.just(s + " WORLD"))
  .filter(s -> s.length() > 5);
```

**Flux (0-N elements):**

```java
// Create Flux
Flux<Integer> numbers = Flux.range(1, 5);
Flux<String> items = Flux.just("a", "b", "c");
Flux<String> empty = Flux.empty();

// Subscribe
items.subscribe(
  item -> System.out.println(item),
  error -> System.err.println(error),
  () -> System.out.println("Complete")
);

// Transform
Flux<Integer> mapped = numbers
  .map(n -> n * 2)
  .filter(n -> n > 5)
  .take(3);

// Combine
Flux<String> combined = Flux.concat(
  Flux.just("Hello"),
  Flux.just("World")
);
```

### 2. Backpressure Handling

```java
// Producer that emits values faster than consumer
Flux<Integer> producer = Flux.range(1, 1000000);

// Consumer with limited capacity
producer
  .onBackpressureBuffer(100)  // Buffer up to 100
  .delayElements(Duration.ofMillis(10))
  .subscribe(System.out::println);

// Or drop values
producer
  .onBackpressureDrop()  // Drop if consumer can't keep up
  .subscribe(System.out::println);

// Or latest only
producer
  .onBackpressureLatest()  // Keep only latest
  .subscribe(System.out::println);
```

### 3. Error Handling

```java
Mono<String> operation = Mono.fromCallable(() -> {
  throw new RuntimeException("Error!");
})
  // Option 1: Provide fallback
  .onErrorReturn("Default value")
  // Option 2: Try different path
  .onErrorResume(e -> Mono.just("Recovery"))
  // Option 3: Transform error
  .onErrorMap(e -> new CustomException(e))
  // Option 4: Retry
  .retry(3)
  // Option 5: Timeout
  .timeout(Duration.ofSeconds(5));
```

### 4. Reactive Streams Composition

```java
@Service
public class CompositeService {

  @Autowired
  private UserService userService;

  @Autowired
  private OrderService orderService;

  // Sequential
  public Mono<UserWithOrders> getUserWithOrders(String userId) {
    return userService.getUser(userId)
      .flatMap(user ->
        orderService.getOrders(userId)
          .collectList()
          .map(orders -> new UserWithOrders(user, orders))
      );
  }

  // Parallel
  public Mono<UserProfile> getUserProfile(String userId) {
    return Mono.zip(
      userService.getUser(userId),
      orderService.getOrders(userId).collectList(),
      addressService.getAddresses(userId).collectList()
    ).map(tuple -> new UserProfile(
      tuple.getT1(),  // User
      tuple.getT2(),  // Orders
      tuple.getT3()   // Addresses
    ));
  }

  // Combine multiple Flux
  public Flux<Event> getEvents() {
    return Flux.merge(
      userService.getUserEvents(),
      orderService.getOrderEvents(),
      notificationService.getNotifications()
    );
  }
}
```

### 5. Database Operations

**R2DBC (Reactive Database Connectivity):**

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-data-r2dbc</artifactId>
</dependency>

<dependency>
  <groupId>org.postgresql</groupId>
  <artifactId>r2dbc-postgresql</artifactId>
</dependency>
```

**Reactive Repository:**

```java
@Repository
public interface UserRepository extends ReactiveCrudRepository<User, String> {

  Mono<User> findByEmail(String email);

  Flux<User> findByStatus(String status);

  Mono<Long> countByCreatedAfter(LocalDateTime date);
}

@Service
public class UserService {

  @Autowired
  private UserRepository repository;

  public Mono<User> getUserById(String id) {
    return repository.findById(id);
  }

  public Flux<User> getAllUsers() {
    return repository.findAll();
  }

  public Mono<User> createUser(User user) {
    return repository.save(user);
  }

  public Mono<Void> deleteUser(String id) {
    return repository.deleteById(id);
  }
}
```

### 6. WebClient (Reactive HTTP Client)

```java
@Configuration
public class WebClientConfig {

  @Bean
  public WebClient webClient(WebClient.Builder builder) {
    return builder
      .baseUrl("https://api.example.com")
      .defaultHeader("User-Agent", "MyApp/1.0")
      .build();
  }
}

@Service
public class ExternalApiClient {

  @Autowired
  private WebClient webClient;

  public Mono<UserData> getUser(String id) {
    return webClient.get()
      .uri("/users/{id}", id)
      .retrieve()
      .bodyToMono(UserData.class)
      .timeout(Duration.ofSeconds(5));
  }

  public Flux<Post> getPosts(String userId) {
    return webClient.get()
      .uri("/posts?userId={id}", userId)
      .retrieve()
      .bodyToFlux(Post.class);
  }

  public Mono<UserData> createUser(CreateUserRequest request) {
    return webClient.post()
      .uri("/users")
      .body(Mono.just(request), CreateUserRequest.class)
      .retrieve()
      .bodyToMono(UserData.class);
  }
}
```

---

## Examples

### Example 1: Complete Reactive Controller

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

  @Autowired
  private UserService userService;

  @GetMapping("/{id}")
  public Mono<ResponseEntity<User>> getUser(@PathVariable String id) {
    return userService.getUserById(id)
      .map(ResponseEntity::ok)
      .onErrorResume(e -> Mono.just(ResponseEntity.notFound().build()));
  }

  @GetMapping
  public Flux<User> getAllUsers(
    @RequestParam(defaultValue = "0") int page,
    @RequestParam(defaultValue = "10") int size) {
    return userService.getAllUsers(page, size);
  }

  @PostMapping
  public Mono<ResponseEntity<User>> createUser(
    @RequestBody Mono<CreateUserRequest> request) {
    return request
      .flatMap(userService::createUser)
      .map(user -> ResponseEntity.status(201).body(user))
      .onErrorResume(e -> Mono.just(ResponseEntity.badRequest().build()));
  }

  @GetMapping("/{id}/posts")
  public Flux<Post> getUserPosts(@PathVariable String id) {
    return userService.getUserPosts(id);
  }
}
```

### Example 2: Reactive Service with Composition

```java
@Service
public class UserService {

  @Autowired
  private UserRepository userRepository;

  @Autowired
  private PostRepository postRepository;

  public Mono<UserProfile> getUserProfile(String userId) {
    return Mono.zip(
      userRepository.findById(userId),
      postRepository.findByUserId(userId).collectList(),
      userRepository.countFollowers(userId)
    ).map(tuple -> new UserProfile(
      tuple.getT1(),  // User
      tuple.getT2(),  // Posts
      tuple.getT3()   // Follower count
    ));
  }

  public Flux<User> searchUsers(String query) {
    return userRepository.findAll()
      .filter(user -> user.getName().contains(query) ||
                      user.getEmail().contains(query))
      .parallel(4)
      .runOn(Schedulers.parallel())
      .sequential();
  }
}
```

### Example 3: Backpressure Management

```java
@Service
public class DataStreamService {

  public Flux<Data> getDataStream() {
    return Flux.generate((Synchronous.Generator<Integer>) sink -> {
      for (int i = 0; i < 1000000; i++) {
        sink.next(i);
      }
      sink.complete();
    })
      .map(this::processData)
      .onBackpressureBuffer(1000)  // Buffer up to 1000
      .delayElements(Duration.ofMillis(1));
  }

  private Data processData(Integer value) {
    return new Data(value);
  }
}
```

### Example 4: Error Handling in Reactive Chain

```java
@Service
public class ResilientService {

  public Mono<Result> executeOperation() {
    return Mono.fromCallable(this::callExternalService)
      .retryWhen(Retry.backoff(3, Duration.ofSeconds(1)))
      .timeout(Duration.ofSeconds(10))
      .onErrorReturn(new Result("default"))
      .doOnError(e -> LOG.error("Operation failed", e));
  }

  private Result callExternalService() {
    // May fail
    return new Result("success");
  }
}
```

---

## Best Practices

### 1. Use Correct Scheduler

```java
// CPU-bound operations
.subscribeOn(Schedulers.parallel())

// I/O operations
.subscribeOn(Schedulers.boundedElastic())

// Blocking operations (minimize)
.subscribeOn(Schedulers.boundedElastic())

// Event loop (never block)
.subscribeOn(Schedulers.immediate())
```

### 2. Handle Backpressure

```java
flux
  .onBackpressureBuffer(1000)   // Explicit backpressure
  .delayElements(Duration.ofMillis(10))
  .subscribe();
```

### 3. Proper Error Handling

```java
mono
  .onErrorResume(e -> Mono.empty())
  .onErrorReturn(defaultValue)
  .doOnError(e -> LOG.error("Error", e))
  .retry(3);
```

### 4. Use Structured Concurrency

```java
Mono.zip(
  operation1(),
  operation2(),
  operation3()
).subscribe();
```

---

## Integration with Other Skills

Spring Boot Reactive integrates with:

- **spring-boot-microservices** - Reactive microservices
- **docker-compose-setup** - Async application deployment
- **kubernetes-yaml-generation** - K8s reactive apps
- **build-optimization** - Optimize reactive builds

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
