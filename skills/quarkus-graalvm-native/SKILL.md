---
name: quarkus-graalvm-native
description: Compile Quarkus applications to GraalVM native images for sub-millisecond startup and minimal memory footprint.
---

# Quarkus GraalVM Native Skill

**Compile Quarkus applications to GraalVM native images for sub-millisecond startup and minimal memory footprint.**

## Overview

GraalVM native compilation transforms JVM applications into standalone native executables — no JVM required at runtime. Combined with Quarkus build-time processing, the result is containers that start in milliseconds and use a fraction of the memory of a standard JVM deployment.

**What it does:**
- Configures Quarkus for native image compilation
- Handles reflection and serialization configuration
- Sets up multi-stage Docker builds for native binaries
- Optimizes for container and serverless targets
- Manages native image build profiles and flags
- Validates native-compatibility of dependencies
- Configures native testing with `@NativeImageTest`
- Produces minimal container images (~50–100 MB)

**Perfect for:**
- Serverless functions (AWS Lambda, Azure Functions, Knative)
- High-density Kubernetes deployments
- Edge computing and constrained environments
- Applications with strict cold-start SLAs
- Microservices where JVM overhead is not acceptable

---

## When to Use This Skill

Use Quarkus GraalVM Native when you need to:

- **Eliminate JVM startup time** — achieve <50ms startup vs. 2–5s JVM
- **Reduce memory usage** dramatically (typically 10–50 MB RSS vs. 200–500 MB)
- **Deploy to serverless** platforms where cold starts matter
- **Minimize container image size** for faster pulls and lower storage costs
- **Meet strict resource quotas** in Kubernetes with many replicas
- **Build self-contained executables** without a JRE dependency

---

## Quick Start (15 Minutes)

### 1. Add Native Profile to pom.xml

```xml
<profiles>
    <profile>
        <id>native</id>
        <activation>
            <property>
                <name>native</name>
            </property>
        </activation>
        <properties>
            <skipITs>false</skipITs>
            <quarkus.native.enabled>true</quarkus.native.enabled>
        </properties>
    </profile>
</profiles>
```

### 2. Build Native (In-Container, No Local GraalVM Required)

```bash
# Uses a build container — no GraalVM installation needed locally
./mvnw package -Pnative -Dquarkus.native.container-build=true

# Output: target/my-service-1.0.0-runner
```

### 3. Build and Run the Native Container Image

```bash
docker build -f src/main/docker/Dockerfile.native -t my-service:native .
docker run -i --rm -p 8080:8080 my-service:native
# Startup time: ~20ms
```

### 4. Run Native Integration Tests

```bash
./mvnw verify -Pnative -Dquarkus.native.container-build=true
```

---

## How It Works

### 1. Native Build Process

```
Maven build
    │
    ▼
Quarkus build-time processing
(annotation scanning, CDI wiring,
 config resolution — all at build time)
    │
    ▼
native-image compiler (GraalVM)
(static analysis, AOT compilation,
 dead code elimination)
    │
    ▼
Native executable
(no JVM, no classloading, instant start)
```

### 2. Dockerfile for Native

```dockerfile
# src/main/docker/Dockerfile.native
FROM quay.io/quarkus/ubi-quarkus-mandrel-builder-image:23.1-java21 AS build
USER quarkus
WORKDIR /code
COPY --chown=quarkus:quarkus mvnw /code/mvnw
COPY --chown=quarkus:quarkus .mvn /code/.mvn
COPY --chown=quarkus:quarkus pom.xml /code/
RUN ./mvnw -B dependency:resolve-plugins dependency:resolve
COPY --chown=quarkus:quarkus src /code/src
RUN ./mvnw package -Pnative -Dquarkus.native.container-build=true

FROM quay.io/quarkus/quarkus-micro-image:2.0
WORKDIR /work/
RUN chown 1001 /work \
    && chmod "g+rwX" /work \
    && chown 1001:root /work
COPY --from=build --chown=1001:root /code/target/*-runner /work/application

EXPOSE 8080
USER 1001

CMD ["./application", "-Dquarkus.http.host=0.0.0.0"]
```

### 3. Reflection Configuration

GraalVM requires explicit registration of classes accessed via reflection. Quarkus handles most of this automatically, but custom code may need manual registration:

```java
// Option 1: Annotation-based (preferred)
@RegisterForReflection
public class MyDTO {
    public String name;
    public int value;
}

// Option 2: Register via application class
@RegisterForReflection(targets = {MyDTO.class, AnotherClass.class})
public class ReflectionConfig {
}

// Option 3: JSON config file
// src/main/resources/reflection-config.json
```

```json
[
  {
    "name": "com.example.dto.MyDTO",
    "allDeclaredConstructors": true,
    "allDeclaredFields": true,
    "allDeclaredMethods": true
  }
]
```

```properties
# application.properties
quarkus.native.additional-build-args=-H:ReflectionConfigurationFiles=reflection-config.json
```

### 4. Resource Registration

```java
@RegisterForReflection(
    targets = {MyDTO.class},
    registerFullHierarchy = true
)
public class NativeConfig implements NativeImageFeature {

    @Override
    public void beforeAnalysis(BeforeAnalysisAccess access) {
        // Register resources for inclusion in native image
    }
}
```

```properties
# Include resource files in the native image
quarkus.native.resources.includes=templates/**,static/**,*.json
```

### 5. Native Integration Tests

```java
@NativeImageTest
@QuarkusIntegrationTest
class ProductResourceIT extends ProductResourceTest {
    // Inherits all tests from ProductResourceTest
    // Runs against the native executable
}
```

### 6. Environment Detection at Runtime

```java
@ApplicationScoped
public class RuntimeInfo {

    @Inject
    io.quarkus.runtime.configuration.ProfileManager profileManager;

    public boolean isNative() {
        return io.quarkus.runtime.LaunchMode.current() != io.quarkus.runtime.LaunchMode.DEVELOPMENT;
    }
}
```

---

## Configuration

### Native Build Properties

```properties
# application.properties

# Enable native compilation (usually set via Maven profile, not here)
# quarkus.native.enabled=true

# Use container build (no local GraalVM needed)
quarkus.native.container-build=true
quarkus.native.builder-image=quay.io/quarkus/ubi-quarkus-mandrel-builder-image:23.1-java21

# Memory for the native image builder (increase for large apps)
quarkus.native.native-image-xmx=6g

# Speed up builds during development (less optimization)
%dev.quarkus.native.additional-build-args=-O0

# Production: optimize for size
%prod.quarkus.native.additional-build-args=-Os

# Include debugging symbols (useful for profiling, increases binary size)
# quarkus.native.debug.enabled=true

# Additional build arguments
quarkus.native.additional-build-args=\
  --initialize-at-build-time=org.slf4j.LoggerFactory,\
  --report-unsupported-elements-at-runtime

# Resources to bundle in the native image
quarkus.native.resources.includes=db/migration/**
```

### pom.xml Native Profile (Complete)

```xml
<profiles>
    <profile>
        <id>native</id>
        <activation>
            <property>
                <name>native</name>
            </property>
        </activation>
        <properties>
            <skipITs>false</skipITs>
            <quarkus.native.enabled>true</quarkus.native.enabled>
            <quarkus.native.container-build>true</quarkus.native.container-build>
            <quarkus.native.native-image-xmx>6g</quarkus.native.native-image-xmx>
        </properties>
        <build>
            <plugins>
                <plugin>
                    <groupId>io.quarkus.platform</groupId>
                    <artifactId>quarkus-maven-plugin</artifactId>
                    <executions>
                        <execution>
                            <goals>
                                <goal>build</goal>
                            </goals>
                        </execution>
                    </executions>
                </plugin>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-failsafe-plugin</artifactId>
                    <executions>
                        <execution>
                            <goals>
                                <goal>integration-test</goal>
                                <goal>verify</goal>
                            </goals>
                            <configuration>
                                <systemPropertyVariables>
                                    <native.image.path>
                                        ${project.build.directory}/${project.build.finalName}-runner
                                    </native.image.path>
                                    <java.util.logging.manager>
                                        org.jboss.logmanager.LogManager
                                    </java.util.logging.manager>
                                    <maven.home>${maven.home}</maven.home>
                                </systemPropertyVariables>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
```

### GitHub Actions Native Build

```yaml
name: Native Build

on:
  push:
    branches: [main]

jobs:
  native-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: 'maven'

      - name: Build native image
        run: ./mvnw package -Pnative -Dquarkus.native.container-build=true

      - name: Run native integration tests
        run: ./mvnw verify -Pnative -Dquarkus.native.container-build=true

      - name: Build and push container image
        uses: docker/build-push-action@v5
        with:
          context: .
          file: src/main/docker/Dockerfile.native
          push: true
          tags: ${{ secrets.REGISTRY }}/my-service:native-${{ github.sha }}
```

---

## Examples

### Example 1: Startup Time Comparison

```bash
# JVM mode
docker run my-service:jvm
# io.quarkus ... started in 1.842s

# Native mode
docker run my-service:native
# io.quarkus ... started in 0.021s  ← 87x faster startup
```

### Example 2: Memory Usage Comparison

```bash
# After serving 1000 requests
docker stats my-service:jvm    # ~350 MB RSS
docker stats my-service:native # ~28 MB RSS  ← 12x less memory
```

### Example 3: Custom Build Step for Native

```java
// Runs only during native image build
public class MyNativeBuildStep {

    @BuildStep
    @Record(ExecutionTime.STATIC_INIT)
    void initAtBuildTime(MyRecorder recorder) {
        recorder.precomputeExpensiveData();
    }
}
```

### Example 4: Troubleshooting Missing Reflection

```bash
# If you see: java.lang.ClassNotFoundException at runtime
# Add to application.properties:
quarkus.native.additional-build-args=\
  -H:+PrintAnalysisCallTree,\
  --report-unsupported-elements-at-runtime

# Or add @RegisterForReflection to the missing class
@RegisterForReflection
public class ThirdPartyDTO { }
```

---

## Best Practices

### 1. Test JVM Mode First, Then Native

```bash
# Step 1: Validate on JVM (fast feedback loop)
./mvnw quarkus:dev
./mvnw test

# Step 2: Build native only when JVM tests pass
./mvnw package -Pnative -Dquarkus.native.container-build=true
./mvnw verify -Pnative -Dquarkus.native.container-build=true
```

### 2. Avoid Reflection Where Possible

```java
// Avoid: Dynamic class loading
Class<?> clazz = Class.forName(className);

// Prefer: Compile-time-known types
// Use CDI injection, interfaces, and generics instead
```

### 3. Keep Native Build in CI, Not Dev Machines

```bash
# Native builds take 2–5 minutes and use 4–8 GB RAM
# Run them in CI, not in the inner dev loop
# Use JVM mode for daily development
```

### 4. Use Dev Services to Match Production Database in Tests

```properties
# application.properties (test profile)
%test.quarkus.datasource.db-kind=postgresql
# Quarkus Dev Services auto-starts a PostgreSQL container for tests
# This ensures native tests run against the same database as production
```

### 5. Pin the Builder Image Version

```properties
# Avoid 'latest' — native image output can change across GraalVM versions
quarkus.native.builder-image=quay.io/quarkus/ubi-quarkus-mandrel-builder-image:23.1-java21
```

---

## Integration with Other Skills

- **`quarkus-framework`** - Build and configure the Quarkus application before going native
- **`quarkus-extensions`** - Ensure all extensions are native-compatible
- **`docker-setup`** - Multi-stage Dockerfile for the native binary
- **`kubernetes-setup`** - Deploy the tiny native image to Kubernetes
- **`github-actions-workflows`** - Automate native builds and tests in CI/CD
- **`java-testing-strategy`** - `@NativeImageTest` integration with the test strategy

---

*Last Updated: 2026-03-17*
*Part of: AI Agents & Skills Repository*
