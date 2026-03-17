---
name: quarkus-extensions
description: Manage, configure, and develop Quarkus extensions to add capabilities and integrate with third-party libraries.
---

# Quarkus Extensions Skill

**Manage, configure, and develop Quarkus extensions to add capabilities and integrate with third-party libraries.**

## Overview

Quarkus extensions are the primary way to add functionality to a Quarkus application. Each extension integrates a library (Hibernate, Kafka, Redis, etc.) with Quarkus's build-time processing engine, ensuring native image compatibility and optimal performance.

**What it does:**
- Discovers and adds extensions via the Quarkus CLI or Maven
- Configures existing extensions with `application.properties`
- Resolves extension compatibility with native image
- Creates custom extensions for internal libraries
- Manages extension versioning via the Quarkus BOM
- Troubleshoots extension conflicts and missing registrations
- Integrates extensions from the Quarkus ecosystem and community

**Perfect for:**
- Adding capabilities to existing Quarkus applications
- Integrating internal frameworks with Quarkus build-time processing
- Ensuring third-party libraries work with native compilation
- Creating reusable extension packages across microservices

---

## When to Use This Skill

Use Quarkus Extensions when you need to:

- **Add a new capability** (REST, security, caching, messaging) to a Quarkus app
- **Integrate a third-party library** and ensure native image compatibility
- **Create a custom extension** for an internal framework
- **Resolve `ClassNotFoundException`** or reflection errors in native builds
- **Audit extension compatibility** before enabling native compilation
- **Manage extension versions** via the Quarkus BOM

---

## Quick Start (5 Minutes)

### 1. List Available Extensions

```bash
# Via Quarkus CLI
quarkus extension list

# Search for a specific extension
quarkus extension list --search redis

# Via Maven
./mvnw quarkus:list-extensions
```

### 2. Add an Extension

```bash
# Via Quarkus CLI (recommended)
quarkus extension add smallrye-jwt
quarkus extension add redis-client
quarkus extension add hibernate-search-orm-elasticsearch

# Via Maven
./mvnw quarkus:add-extension -Dextensions="smallrye-jwt,redis-client"

# Manual: add to pom.xml then run dependency:resolve
```

### 3. Remove an Extension

```bash
quarkus extension remove redis-client
```

### 4. Check Extension Info

```bash
quarkus extension info smallrye-jwt
# Shows: description, version, native support status, guides
```

---

## How It Works

### 1. Extension Anatomy

A Quarkus extension has two Maven modules:

```
my-extension/
├── deployment/              # Build-time processing
│   ├── pom.xml
│   └── src/main/java/
│       └── MyExtensionProcessor.java   # @BuildStep methods
└── runtime/                 # Runtime code
    ├── pom.xml
    └── src/main/java/
        └── MyExtensionRecorder.java    # @Recorder methods
```

- **Deployment module**: Runs at build time. Processes annotations, generates bytecode, wires CDI beans.
- **Runtime module**: What ships in the final application. Called by the recorder at startup or at static init.

### 2. Key Extension Categories

| Category | Popular Extensions |
|----------|--------------------|
| REST | `resteasy-reactive-jackson`, `rest-client-reactive` |
| Persistence | `hibernate-orm-panache`, `mongodb-panache`, `jdbc-postgresql` |
| Security | `oidc`, `smallrye-jwt`, `elytron-security` |
| Messaging | `smallrye-reactive-messaging-kafka`, `amqp` |
| Caching | `cache`, `redis-client`, `infinispan-client` |
| Observability | `smallrye-health`, `micrometer-registry-prometheus`, `opentelemetry` |
| Config | `config-yaml`, `vault`, `kubernetes-config` |
| Testing | `junit5`, `test-h2` |

### 3. Common Extension Configurations

**OIDC (OAuth2 / Keycloak):**

```properties
quarkus.oidc.auth-server-url=https://keycloak.example.com/realms/myrealm
quarkus.oidc.client-id=my-service
quarkus.oidc.credentials.secret=${OIDC_SECRET}
quarkus.http.auth.permission.authenticated.paths=/*
quarkus.http.auth.permission.authenticated.policy=authenticated
```

**Redis Client:**

```properties
quarkus.redis.hosts=redis://${REDIS_HOST:localhost}:6379
quarkus.redis.password=${REDIS_PASSWORD:}
quarkus.redis.timeout=5s
```

```java
@ApplicationScoped
public class CacheService {

    @Inject
    RedisDataSource redisDataSource;

    public void set(String key, String value, Duration ttl) {
        redisDataSource.value(String.class).set(key, value);
        redisDataSource.key().expire(key, ttl);
    }

    public Optional<String> get(String key) {
        return Optional.ofNullable(redisDataSource.value(String.class).get(key));
    }
}
```

**SmallRye JWT:**

```properties
mp.jwt.verify.publickey.location=META-INF/resources/publicKey.pem
mp.jwt.verify.issuer=https://auth.example.com

# Or use JWKS endpoint
mp.jwt.verify.publickey.location=https://auth.example.com/.well-known/jwks.json
```

```java
@Path("/protected")
@Authenticated
public class ProtectedResource {

    @Inject
    JsonWebToken jwt;

    @GET
    public Response profile() {
        return Response.ok(Map.of(
            "subject", jwt.getSubject(),
            "name", jwt.getClaim("name"),
            "roles", jwt.getGroups()
        )).build();
    }
}
```

**Hibernate Search (Elasticsearch):**

```properties
quarkus.hibernate-search-orm.elasticsearch.version=8
quarkus.hibernate-search-orm.elasticsearch.hosts=localhost:9200
quarkus.hibernate-search-orm.schema-management.strategy=create-or-update
```

```java
@Entity
@Indexed
public class Product extends PanacheEntity {

    @FullTextField(analyzer = "english")
    public String name;

    @KeywordField
    public String category;

    public static List<Product> search(String query) {
        return Search.session(Panache.getEntityManager())
            .search(Product.class)
            .where(f -> f.match()
                .fields("name")
                .matching(query))
            .fetchAllHits();
    }
}
```

**OpenTelemetry:**

```properties
quarkus.otel.exporter.otlp.traces.endpoint=http://jaeger:4317
quarkus.otel.resource.attributes=service.name=my-service,service.version=1.0.0
quarkus.otel.traces.sampler=parentbased_traceidratio
quarkus.otel.traces.sampler.arg=0.1
```

### 4. Creating a Custom Extension

```bash
# Scaffold a new extension
mvn io.quarkus.platform:quarkus-maven-plugin:3.8.0:create-extension \
  -DgroupId=com.example \
  -DextensionId=my-extension \
  -DwithoutTests=false
```

**Deployment module — BuildStep:**

```java
@BuildSteps(onlyIf = IsNormal.class)
public class MyExtensionProcessor {

    @BuildStep
    FeatureBuildItem feature() {
        return new FeatureBuildItem("my-extension");
    }

    @BuildStep
    @Record(ExecutionTime.RUNTIME_INIT)
    void initialize(
        MyExtensionRecorder recorder,
        MyExtensionConfig config,
        BuildProducer<SyntheticBeanBuildItem> syntheticBeans) {

        RuntimeValue<MyExtensionClient> client = recorder.createClient(config);

        syntheticBeans.produce(SyntheticBeanBuildItem
            .configure(MyExtensionClient.class)
            .scope(ApplicationScoped.class)
            .runtimeValue(client)
            .done());
    }

    @BuildStep
    void registerForReflection(
        BuildProducer<ReflectiveClassBuildItem> reflectiveClasses) {

        reflectiveClasses.produce(ReflectiveClassBuildItem
            .builder(MyInternalDTO.class)
            .constructors()
            .fields()
            .methods()
            .build());
    }
}
```

**Runtime module — Recorder:**

```java
@Recorder
public class MyExtensionRecorder {

    public RuntimeValue<MyExtensionClient> createClient(MyExtensionConfig config) {
        return new RuntimeValue<>(new MyExtensionClient(
            config.host(),
            config.port(),
            config.timeout()
        ));
    }
}
```

**Configuration:**

```java
@ConfigRoot(phase = ConfigPhase.RUN_TIME)
@ConfigMapping(prefix = "my-extension")
public interface MyExtensionConfig {

    String host();

    int port();

    @WithDefault("5s")
    Duration timeout();

    @WithDefault("true")
    boolean enabled();
}
```

---

## Configuration

### Extension Version Management via BOM

```xml
<!-- Always use the Quarkus BOM — never specify extension versions manually -->
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.quarkus.platform</groupId>
            <artifactId>quarkus-bom</artifactId>
            <version>3.8.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <!-- No version needed — managed by BOM -->
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-smallrye-jwt</artifactId>
    </dependency>
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-redis-client</artifactId>
    </dependency>
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-hibernate-search-orm-elasticsearch</artifactId>
    </dependency>
</dependencies>
```

### Checking Native Compatibility

```bash
# List all extensions and their native support status
quarkus extension list --installable | grep -i native

# Or check quarkus.io/extensions directly
# Green badge = native supported
# Yellow badge = preview/partial native support
# Red badge = not yet native compatible
```

### Conditional Extension Activation

```java
// Only active in production profile
@BuildSteps(onlyIfNot = IsDevelopment.class)
public class ProductionOnlySteps { ... }

// Only active in native builds
@BuildSteps(onlyIf = NativeBuild.class)
public class NativeOnlySteps { ... }
```

---

## Examples

### Example 1: Adding Security to an Existing App

```bash
# Add OIDC extension
quarkus extension add oidc

# Configure Keycloak integration
cat >> src/main/resources/application.properties << EOF
quarkus.oidc.auth-server-url=https://keycloak.example.com/realms/myrealm
quarkus.oidc.client-id=my-service
quarkus.oidc.credentials.secret=\${OIDC_CLIENT_SECRET}
quarkus.http.auth.permission.public.paths=/q/health/**,/q/metrics
quarkus.http.auth.permission.public.policy=permit
quarkus.http.auth.permission.authenticated.paths=/*
quarkus.http.auth.permission.authenticated.policy=authenticated
EOF
```

### Example 2: Audit Extensions for Native Compatibility

```bash
# Run native build in verbose mode to see extension issues
./mvnw package -Pnative \
  -Dquarkus.native.additional-build-args=--report-unsupported-elements-at-runtime \
  2>&1 | grep -i "unsupported\|warning\|error"
```

### Example 3: Using the Quarkus Extension Registry

```bash
# Search the Quarkus extension registry
quarkus extension list --search "graphql" --installable

# Add from the Quarkiverse (community extensions)
quarkus extension add io.quarkiverse.langchain4j:quarkus-langchain4j-openai
```

### Example 4: Dev UI Extension Exploration

```bash
# Start dev mode
./mvnw quarkus:dev

# Open Dev UI in browser
open http://localhost:8080/q/dev

# Dev UI shows:
# - All active extensions
# - Configuration explorer
# - CDI bean browser
# - Hibernate entity browser
# - Kafka topics (if using Kafka extension)
```

---

## Best Practices

### 1. Always Use the Quarkus BOM

```xml
<!-- Never set versions directly — the BOM ensures compatibility -->
<dependency>
    <groupId>io.quarkus</groupId>
    <artifactId>quarkus-resteasy-reactive-jackson</artifactId>
    <!-- No <version> here -->
</dependency>
```

### 2. Prefer First-Party Extensions Over Third-Party JARs

```xml
<!-- Avoid: Raw Kafka client (not native-optimized) -->
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-clients</artifactId>
    <version>3.6.0</version>
</dependency>

<!-- Prefer: Quarkus extension (native-ready, CDI-integrated) -->
<dependency>
    <groupId>io.quarkus</groupId>
    <artifactId>quarkus-smallrye-reactive-messaging-kafka</artifactId>
</dependency>
```

### 3. Test Extension Interactions in Dev Mode

```bash
# Dev mode hot-reload lets you test extension behavior instantly
./mvnw quarkus:dev

# Check the Dev UI for extension-specific tooling
# (Kafka UI, Hibernate schema browser, config explorer)
```

### 4. Register Third-Party Classes for Reflection Explicitly

```java
// When using a third-party library that isn't wrapped by an extension
@RegisterForReflection(targets = {
    com.thirdparty.SomeDTO.class,
    com.thirdparty.AnotherClass.class
})
public class ThirdPartyReflectionConfig {
}
```

### 5. Upgrade Extensions Atomically via BOM

```bash
# Upgrade all extensions at once by bumping the BOM version
# Then run: ./mvnw versions:update-properties -DgenerateBackupPoms=false
```

---

## Integration with Other Skills

- **`quarkus-framework`** - Foundation skill for setting up the Quarkus application
- **`quarkus-graalvm-native`** - Ensure extensions are native-compatible before compiling
- **`java-security-audit`** - Audit security extension configuration (OIDC, JWT, mTLS)
- **`java-testing-strategy`** - Test extensions with `@QuarkusTest` and `@QuarkusIntegrationTest`
- **`docker-compose-setup`** - Spin up extension dependencies (Kafka, Redis, Keycloak) locally
- **`build-cache-management`** - Cache extension artifacts in Maven local repository

---

*Last Updated: 2026-03-17*
*Part of: AI Agents & Skills Repository*
