---
name: quarkus-framework
description: Set up and configure Quarkus cloud-native applications with REST, persistence, messaging, and observability.
---

# Quarkus Framework Skill

**Set up and configure Quarkus cloud-native applications with REST, persistence, messaging, and observability.**

## Overview

Quarkus is a Kubernetes-native Java framework built for GraalVM and HotSpot, offering supersonic startup time and low memory footprint — ideal for containers and serverless.

**What it does:**
- Scaffolds Quarkus projects with Maven or Gradle
- Configures REST endpoints with RESTEasy Reactive
- Sets up Panache ORM/Repository for persistence
- Integrates Kafka with SmallRye Reactive Messaging
- Configures OpenAPI/Swagger and health checks
- Sets up CDI dependency injection
- Enables dev mode with live reload
- Prepares applications for container and native compilation

**Perfect for:**
- Microservices with fast startup requirements
- Serverless and FaaS deployments
- Container-first applications
- Teams migrating from Spring Boot to cloud-native Java
- High-density Kubernetes workloads

---

## When to Use This Skill

Use Quarkus Framework when you need to:

- **Build cloud-native microservices** with minimal footprint
- **Achieve sub-second startup times** for containerized apps
- **Reduce memory consumption** significantly vs Spring Boot
- **Implement reactive REST APIs** with RESTEasy Reactive
- **Use Panache** for simplified JPA/MongoDB persistence
- **Integrate Kafka** via SmallRye Reactive Messaging
- **Enable native compilation** as a next step (see `quarkus-graalvm-native`)
- **Develop with live reload** via Quarkus Dev Mode

---

## Quick Start (10 Minutes)

### 1. Create a New Project

```bash
mvn io.quarkus.platform:quarkus-maven-plugin:3.8.0:create \
  -DprojectGroupId=com.example \
  -DprojectArtifactId=my-service \
  -DclassName="com.example.GreetingResource" \
  -Dpath="/hello" \
  -Dextensions="resteasy-reactive-jackson,hibernate-orm-panache,postgresql,smallrye-health,smallrye-openapi"

cd my-service
```

### 2. Start Dev Mode

```bash
./mvnw quarkus:dev
# Hot reload enabled at http://localhost:8080
# Dev UI at http://localhost:8080/q/dev
```

### 3. Run a REST Request

```bash
curl http://localhost:8080/hello
# Output: Hello from Quarkus REST
```

---

## How It Works

### 1. Project Structure

```
my-service/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/com/example/
│   │   │   ├── resource/       # JAX-RS endpoints
│   │   │   ├── service/        # Business logic
│   │   │   ├── repository/     # Panache repositories
│   │   │   ├── entity/         # JPA entities
│   │   │   └── dto/            # Data Transfer Objects
│   │   └── resources/
│   │       ├── application.properties
│   │       └── import.sql      # Dev mode seed data
│   └── test/
│       └── java/com/example/
├── Dockerfile.jvm
├── Dockerfile.native
└── docker-compose.yml
```

### 2. REST Endpoints with RESTEasy Reactive

```java
@Path("/api/products")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class ProductResource {

    @Inject
    ProductService productService;

    @GET
    public List<ProductDTO> getAll() {
        return productService.listAll();
    }

    @GET
    @Path("/{id}")
    public Response getById(@PathParam("id") Long id) {
        return productService.findById(id)
            .map(p -> Response.ok(p).build())
            .orElse(Response.status(Status.NOT_FOUND).build());
    }

    @POST
    @ResponseStatus(201)
    public ProductDTO create(@Valid ProductDTO dto) {
        return productService.create(dto);
    }

    @PUT
    @Path("/{id}")
    public ProductDTO update(@PathParam("id") Long id, @Valid ProductDTO dto) {
        return productService.update(id, dto);
    }

    @DELETE
    @Path("/{id}")
    @ResponseStatus(204)
    public void delete(@PathParam("id") Long id) {
        productService.delete(id);
    }
}
```

### 3. Panache ORM (Active Record Pattern)

```java
@Entity
@Table(name = "products")
public class Product extends PanacheEntity {

    @NotBlank
    public String name;

    @DecimalMin("0.0")
    public BigDecimal price;

    @Enumerated(EnumType.STRING)
    public ProductStatus status;

    public Instant createdAt;

    @PrePersist
    void prePersist() {
        createdAt = Instant.now();
    }

    // Static finder methods
    public static List<Product> findByStatus(ProductStatus status) {
        return list("status", status);
    }

    public static Optional<Product> findByName(String name) {
        return find("name", name).firstResultOptional();
    }
}
```

### 4. Panache Repository Pattern

```java
@ApplicationScoped
public class ProductRepository implements PanacheRepository<Product> {

    public List<Product> findActive() {
        return list("status = ?1", ProductStatus.ACTIVE);
    }

    public Page<Product> findPaged(int page, int size) {
        return find("status = 'ACTIVE' ORDER BY name")
            .page(Page.of(page, size));
    }
}
```

### 5. CDI Dependency Injection

```java
@ApplicationScoped
public class ProductService {

    @Inject
    ProductRepository productRepository;

    @Inject
    EventBus eventBus;

    @Transactional
    public ProductDTO create(ProductDTO dto) {
        Product product = ProductMapper.toEntity(dto);
        productRepository.persist(product);
        eventBus.publish("product.created", product.id);
        return ProductMapper.toDTO(product);
    }

    public Optional<ProductDTO> findById(Long id) {
        return productRepository.findByIdOptional(id)
            .map(ProductMapper::toDTO);
    }

    @Transactional
    public void delete(Long id) {
        productRepository.deleteById(id);
    }
}
```

### 6. Reactive Messaging with Kafka

```java
@ApplicationScoped
public class ProductEventProcessor {

    @Incoming("product-events-in")
    @Outgoing("product-events-out")
    public ProductEvent process(ProductEvent event) {
        // Transform or enrich the event
        event.setProcessedAt(Instant.now());
        return event;
    }

    @Incoming("product-events-dead-letter")
    public void handleFailure(ProductEvent event) {
        Log.warnf("Failed to process event: %s", event.getId());
    }
}
```

### 7. Health Checks

```java
@Liveness
@ApplicationScoped
public class DatabaseHealthCheck implements HealthCheck {

    @Inject
    DataSource dataSource;

    @Override
    public HealthCheckResponse call() {
        try (Connection c = dataSource.getConnection()) {
            return HealthCheckResponse.up("database");
        } catch (SQLException e) {
            return HealthCheckResponse.down("database");
        }
    }
}
```

---

## Configuration

### pom.xml

```xml
<properties>
    <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>
    <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>
    <quarkus.platform.version>3.8.0</quarkus.platform.version>
    <java.version>21</java.version>
</properties>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>${quarkus.platform.group-id}</groupId>
            <artifactId>${quarkus.platform.artifact-id}</artifactId>
            <version>${quarkus.platform.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <!-- REST -->
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-resteasy-reactive-jackson</artifactId>
    </dependency>
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-hibernate-validator</artifactId>
    </dependency>

    <!-- Persistence -->
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-hibernate-orm-panache</artifactId>
    </dependency>
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-jdbc-postgresql</artifactId>
    </dependency>

    <!-- Messaging -->
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-smallrye-reactive-messaging-kafka</artifactId>
    </dependency>

    <!-- Observability -->
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-smallrye-health</artifactId>
    </dependency>
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-micrometer-registry-prometheus</artifactId>
    </dependency>
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-smallrye-openapi</artifactId>
    </dependency>

    <!-- Testing -->
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-junit5</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>io.rest-assured</groupId>
        <artifactId>rest-assured</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

### application.properties

```properties
# Application
quarkus.application.name=my-service
quarkus.application.version=1.0.0

# HTTP
quarkus.http.port=8080
quarkus.http.cors=true
quarkus.http.cors.origins=*

# Database
quarkus.datasource.db-kind=postgresql
quarkus.datasource.username=${DB_USER:postgres}
quarkus.datasource.password=${DB_PASSWORD:secret}
quarkus.datasource.jdbc.url=jdbc:postgresql://${DB_HOST:localhost}:5432/${DB_NAME:mydb}
quarkus.datasource.jdbc.max-size=20
quarkus.hibernate-orm.database.generation=validate
quarkus.hibernate-orm.log.sql=false

# Dev mode overrides
%dev.quarkus.hibernate-orm.database.generation=drop-and-create
%dev.quarkus.hibernate-orm.log.sql=true
%dev.quarkus.datasource.jdbc.url=jdbc:postgresql://localhost:5432/mydb_dev

# Kafka
kafka.bootstrap.servers=${KAFKA_BROKERS:localhost:9092}
mp.messaging.outgoing.product-events-out.connector=smallrye-kafka
mp.messaging.outgoing.product-events-out.topic=product-events
mp.messaging.incoming.product-events-in.connector=smallrye-kafka
mp.messaging.incoming.product-events-in.topic=product-events

# OpenAPI
quarkus.smallrye-openapi.path=/q/openapi
quarkus.swagger-ui.always-include=true
quarkus.swagger-ui.path=/q/swagger-ui

# Health
quarkus.smallrye-health.root-path=/q/health

# Logging
quarkus.log.level=INFO
quarkus.log.category."com.example".level=DEBUG
quarkus.log.console.format=%d{HH:mm:ss} %-5p [%c{2.}] (%t) %s%e%n
```

### docker-compose.yml

```yaml
version: '3.8'
services:
  app:
    image: ${IMAGE_NAME:-my-service}:${IMAGE_TAG:-latest}
    ports:
      - "8080:8080"
    environment:
      DB_HOST: postgres
      DB_USER: myuser
      DB_PASSWORD: secret
      DB_NAME: mydb
      KAFKA_BROKERS: kafka:9092
    depends_on:
      postgres:
        condition: service_healthy
      kafka:
        condition: service_started

  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: mydb
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myuser"]
      interval: 5s
      retries: 5

  kafka:
    image: confluentinc/cp-kafka:7.6.0
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092
    depends_on:
      - zookeeper

  zookeeper:
    image: confluentinc/cp-zookeeper:7.6.0
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
```

---

## Examples

### Example 1: Integration Test with REST-Assured

```java
@QuarkusTest
class ProductResourceTest {

    @Test
    void testListProducts() {
        given()
            .when().get("/api/products")
            .then()
                .statusCode(200)
                .body("$.size()", greaterThan(0));
    }

    @Test
    void testCreateProduct() {
        given()
            .contentType(ContentType.JSON)
            .body("""
                {"name": "Widget", "price": 9.99, "status": "ACTIVE"}
                """)
            .when().post("/api/products")
            .then()
                .statusCode(201)
                .body("name", equalTo("Widget"))
                .body("price", equalTo(9.99f));
    }

    @Test
    void testGetNotFound() {
        given()
            .when().get("/api/products/99999")
            .then()
                .statusCode(404);
    }
}
```

### Example 2: Panache Query with Pagination

```java
@GET
@Path("/search")
public Response search(
    @QueryParam("q") String query,
    @QueryParam("page") @DefaultValue("0") int page,
    @QueryParam("size") @DefaultValue("20") int size) {

    PanacheQuery<Product> results = Product.find(
        "LOWER(name) LIKE LOWER(?1) OR LOWER(description) LIKE LOWER(?1)",
        "%" + query + "%"
    );

    long total = results.count();
    List<ProductDTO> items = results
        .page(Page.of(page, size))
        .list()
        .stream()
        .map(ProductMapper::toDTO)
        .toList();

    return Response.ok(new PageResponse<>(items, total, page, size)).build();
}
```

### Example 3: Exception Mapper

```java
@Provider
public class ValidationExceptionMapper
    implements ExceptionMapper<ConstraintViolationException> {

    @Override
    public Response toResponse(ConstraintViolationException e) {
        Map<String, String> errors = e.getConstraintViolations().stream()
            .collect(Collectors.toMap(
                v -> v.getPropertyPath().toString(),
                ConstraintViolation::getMessage
            ));

        return Response.status(Status.BAD_REQUEST)
            .entity(Map.of(
                "errors", errors,
                "timestamp", Instant.now().toString()
            ))
            .build();
    }
}
```

---

## Best Practices

### 1. Prefer Reactive Endpoints for I/O-Heavy Paths

```java
// Blocking (acceptable for CRUD)
@GET
public List<ProductDTO> getAll() {
    return Product.listAll().stream().map(ProductMapper::toDTO).toList();
}

// Non-blocking (preferred for high-concurrency)
@GET
@Path("/async")
public Uni<List<ProductDTO>> getAllAsync() {
    return Product.<Product>listAll()
        .map(list -> list.stream().map(ProductMapper::toDTO).toList());
}
```

### 2. Use @Transactional Consistently

```java
@Transactional
public ProductDTO create(ProductDTO dto) {
    Product product = ProductMapper.toEntity(dto);
    product.persist();
    return ProductMapper.toDTO(product);
}

// Read-only transactions are faster
@Transactional(readOnly = true)
public List<ProductDTO> listAll() {
    return Product.<Product>listAll()
        .stream().map(ProductMapper::toDTO).toList();
}
```

### 3. Leverage Dev Services for Zero-Config Local Dev

```properties
# No config needed — Quarkus Dev Services auto-starts containers
# quarkus.datasource.jdbc.url is auto-set in dev/test mode
# kafka.bootstrap.servers is auto-set in dev/test mode
```

### 4. Profile-Specific Configuration

```properties
# Shared
quarkus.datasource.db-kind=postgresql

# Dev only
%dev.quarkus.hibernate-orm.database.generation=drop-and-create

# Test only
%test.quarkus.hibernate-orm.database.generation=drop-and-create

# Prod only
%prod.quarkus.datasource.jdbc.url=jdbc:postgresql://prod-host:5432/proddb
```

---

## Integration with Other Skills

- **`quarkus-graalvm-native`** - Compile this application to a native binary
- **`quarkus-extensions`** - Add and manage Quarkus extensions
- **`java-testing-strategy`** - Comprehensive test strategy with `@QuarkusTest`
- **`docker-compose-setup`** - Full local stack with dependencies
- **`kubernetes-setup`** - Deploy to Kubernetes with minimal memory footprint
- **`java-security-audit`** - Secure the REST API and data layer

---

*Last Updated: 2026-03-17*
*Part of: AI Agents & Skills Repository*
