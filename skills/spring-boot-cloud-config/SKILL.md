# Spring Boot Cloud Config Skill

**Master Spring Cloud Config server, distributed configuration management, feature flags, and config patterns.**

## Overview

Distributed configuration management enables dynamic configuration updates without redeployment. This skill covers Spring Cloud Config patterns.

**What it does:**
- Configures Spring Cloud Config server
- Manages centralized configuration
- Implements configuration inheritance
- Handles environment-specific configs
- Implements feature flags
- Manages configuration updates
- Secures sensitive configuration
- Implements config validation

**Perfect for:**
- Managing configuration across environments
- Dynamic feature toggling
- Multi-tenant applications
- Cloud-native deployments
- Configuration as code

---

## Quick Start (10 Minutes)

### 1. Config Server Setup

Add dependency:

```xml
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-config-server</artifactId>
</dependency>
```

Enable server:

```java
@SpringBootApplication
@EnableConfigServer
public class ConfigServerApplication {
  public static void main(String[] args) {
    SpringApplication.run(ConfigServerApplication.class, args);
  }
}
```

### 2. Configure Git Backend

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

### 3. Client Configuration

```yaml
spring:
  cloud:
    config:
      uri: http://config-server:8888
      name: user-service
      profile: production
      label: main
```

### 4. Access Configuration

```java
@RestController
public class ConfigController {

  @Value("${app.name}")
  private String appName;

  @Value("${database.url}")
  private String dbUrl;

  @GetMapping("/config")
  public Map<String, String> getConfig() {
    return Map.of(
      "app.name", appName,
      "database.url", dbUrl
    );
  }
}
```

---

## How It Works

### 1. Config Server Architecture

**Repository Structure:**

```
config-repo/
├── application.yml                    # Shared config
├── application-prod.yml              # Production
├── application-dev.yml               # Development
├── user-service.yml                  # Service-specific
├── user-service-prod.yml
├── order-service.yml
└── order-service-prod.yml
```

**Configuration Files:**

```yaml
# application.yml (shared)
server:
  port: 8080
  servlet:
    context-path: /api

logging:
  level:
    root: INFO
    com.example: DEBUG

security:
  jwt:
    secret: ${JWT_SECRET}
    expiration: 86400
```

```yaml
# application-prod.yml (production)
server:
  port: 8080

logging:
  level:
    root: WARN
    com.example: INFO

database:
  host: prod-db.example.com
  ssl: true
```

### 2. Configuration Loading Order

```
1. application.yml                 (shared defaults)
2. application-{profile}.yml       (profile-specific)
3. {service-name}.yml              (service defaults)
4. {service-name}-{profile}.yml    (service + profile)
5. Environment variables override all
```

### 3. Refresh Mechanism

**Manual Refresh:**

```java
@RestController
@RequestMapping("/config")
public class ConfigRefreshController {

  @Autowired
  private ConfigurableApplicationContext context;

  @PostMapping("/refresh")
  public ResponseEntity<?> refresh() {
    // Get current configuration values
    String before = context.getEnvironment().getProperty("app.version");

    // Trigger refresh from config server
    context.getEnvironment().setProperty("app.version", "new-value");

    return ResponseEntity.ok("Refreshed");
  }
}
```

**Automatic Refresh with @RefreshScope:**

```java
@RestController
@RefreshScope  // Auto-refresh when config updates
public class FeatureController {

  @Value("${feature.new-dashboard.enabled:false}")
  private boolean newDashboardEnabled;

  @GetMapping("/features")
  public Map<String, Boolean> getFeatures() {
    return Map.of("new-dashboard", newDashboardEnabled);
  }
}
```

### 4. Feature Flags

**Configuration:**

```yaml
# application.yml
features:
  authentication:
    oauth2: true
    saml: false
    mfa-required: false
  ui:
    new-dashboard: false
    dark-mode: true
  api:
    v2-endpoints: true
    rate-limiting: true
    cache-responses: false
```

**Implementation:**

```java
@Service
public class FeatureService {

  @Value("${features.authentication.oauth2:false}")
  private boolean oauth2Enabled;

  @Value("${features.ui.new-dashboard:false}")
  private boolean newDashboardEnabled;

  public boolean isFeatureEnabled(String feature) {
    switch (feature) {
      case "oauth2":
        return oauth2Enabled;
      case "new-dashboard":
        return newDashboardEnabled;
      default:
        return false;
    }
  }
}

@RestController
public class DashboardController {

  @Autowired
  private FeatureService featureService;

  @GetMapping("/dashboard")
  public Dashboard getDashboard() {
    if (featureService.isFeatureEnabled("new-dashboard")) {
      return new NewDashboard();
    }
    return new LegacyDashboard();
  }
}
```

### 5. Environment-Specific Config

**Dev Configuration:**

```yaml
# user-service-dev.yml
server:
  port: 8081

database:
  url: postgresql://localhost:5432/userdb_dev
  username: postgres
  password: postgres

logging:
  level:
    root: DEBUG

security:
  cors:
    allowed-origins: "http://localhost:3000"
```

**Production Configuration:**

```yaml
# user-service-prod.yml
server:
  port: 8080

database:
  url: postgresql://prod-db:5432/userdb_prod
  username: ${DB_USER}
  password: ${DB_PASSWORD}
  ssl: true

logging:
  level:
    root: WARN

security:
  cors:
    allowed-origins: "https://example.com"
  ssl: true
```

### 6. Configuration Validation

```java
@Configuration
@ConfigurationProperties(prefix = "app")
@Validated
public class AppProperties {

  @NotBlank
  private String name;

  @Email
  private String contactEmail;

  @Positive
  private int maxConnections;

  @NotNull
  @Valid
  private DatabaseConfig database;

  // Getters and setters
}

@ConfigurationProperties(prefix = "app.database")
public class DatabaseConfig {
  @NotBlank
  private String url;

  @Positive
  private int poolSize;

  @Range(min = 1, max = 300)
  private int connectionTimeout;
}
```

---

## Configuration

### Complete Config Server Setup

`pom.xml`:

```xml
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-config-server</artifactId>
</dependency>

<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-starter-bootstrap</artifactId>
</dependency>
```

`application.yml`:

```yaml
server:
  port: 8888

spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/myorg/config-repo
          username: ${GIT_USER}
          password: ${GIT_TOKEN}
          search-paths: '{application}'
          force-pull: true
          timeout: 4
          basedir: /tmp/config-server

management:
  endpoints:
    web:
      exposure:
        include: health,info,env

logging:
  level:
    org.springframework.cloud: DEBUG
```

---

## Examples

### Example 1: Git-Based Config

```bash
# config-repo/
# ├── application.yml
# ├── user-service.yml
# ├── user-service-prod.yml
# └── order-service.yml

# application.yml
server:
  servlet:
    context-path: /api

# user-service.yml
spring:
  datasource:
    url: jdbc:postgresql://localhost/users

# user-service-prod.yml
spring:
  datasource:
    url: jdbc:postgresql://${DB_HOST}/users
    password: ${DB_PASSWORD}
```

### Example 2: Dynamic Feature Flags

```yaml
# application.yml
features:
  payments:
    stripe: true
    paypal: false
  notifications:
    email: true
    sms: false
    push: false
```

```java
@Service
@RefreshScope
public class PaymentService {

  @Value("${features.payments.stripe:false}")
  private boolean stripeEnabled;

  @Value("${features.payments.paypal:false}")
  private boolean paypalEnabled;

  public Payment processPayment(Order order, String method) {
    if ("stripe".equals(method) && stripeEnabled) {
      return processStripePayment(order);
    }
    if ("paypal".equals(method) && paypalEnabled) {
      return processPaypalPayment(order);
    }
    throw new PaymentMethodNotAvailableException();
  }
}
```

### Example 3: Configuration Validation

```java
@Configuration
@ConfigurationProperties(prefix = "app")
@Validated
public class ApplicationProperties {

  @NotBlank(message = "App name is required")
  private String name;

  @Email(message = "Valid email required")
  private String contactEmail;

  @Positive(message = "Max connections must be positive")
  private int maxConnections = 100;

  @NotNull
  @Valid
  private SecurityProperties security;

  public static class SecurityProperties {
    @NotBlank
    private String jwtSecret;

    @Min(300)
    @Max(86400)
    private int jwtExpiration = 3600;
  }
}
```

### Example 4: Environment Override

```yaml
# bootstrap.yml (client)
spring:
  application:
    name: user-service
  cloud:
    config:
      uri: http://config-server:8888
      profile: ${SPRING_PROFILE:dev}
      label: ${SPRING_LABEL:main}
```

```bash
# Deploy with different profile
java -Dspring.profiles.active=prod \
     -Dspring.cloud.config.profile=prod \
     -jar user-service.jar
```

---

## Best Practices

### 1. Use Git for Version Control

```bash
# Track config changes
git log --oneline application-prod.yml

# Rollback if needed
git revert <commit>
```

### 2. Separate Sensitive Data

```yaml
# application.yml (committed)
app:
  name: MyApp
  version: 1.0.0

# Do NOT commit passwords!
# Use environment variables instead
database:
  password: ${DB_PASSWORD}
```

### 3. Validate Configuration

```java
@Configuration
@ConfigurationProperties(prefix = "app")
@Validated
public class Config {
  @NotNull
  @Email
  private String adminEmail;

  @NotNull
  @Positive
  private Integer maxUsers;
}
```

### 4. Use Profiles Consistently

```
Dev: dev
Staging: staging
Production: prod

application.yml          (all envs)
application-dev.yml     (dev only)
application-prod.yml    (prod only)
```

---

## Integration with Other Skills

Spring Boot Cloud Config integrates with:

- **secrets-management** - Store sensitive config
- **kubernetes-yaml-generation** - K8s ConfigMaps
- **docker-compose-setup** - Local config management
- **spring-boot-microservices** - Centralized service config

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
