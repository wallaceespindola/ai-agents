# Build Optimization Skill

**Optimize Maven, Gradle, and npm builds. Master caching, dependency resolution, incremental builds, and custom build tasks.**

## Overview

Build optimization reduces CI/CD time and improves developer productivity. This skill covers build system optimization across languages.

**What it does:**
- Optimizes Maven and Gradle builds
- Implements dependency caching
- Enables incremental compilation
- Creates custom build tasks
- Parallelizes build processes
- Reduces build artifact sizes
- Implements build time tracking
- Optimizes test execution

**Perfect for:**
- Faster CI/CD pipelines
- Improved developer experience
- Reduced resource consumption
- Faster feedback loops
- Cost reduction

---

## When to Use This Skill

Use Build Optimization when you need to:

- **Speed up Maven/Gradle builds**
- **Implement caching strategies**
- **Parallelize build processes**
- **Reduce build artifact size**
- **Enable incremental builds**
- **Optimize test execution**
- **Track build performance**
- **Create custom tasks**

---

## Quick Start (10 Minutes)

### 1. Maven Build Optimization

```xml
<!-- pom.xml -->
<properties>
  <maven.compiler.source>21</maven.compiler.source>
  <maven.compiler.target>21</maven.compiler.target>
  <!-- Parallel compilation -->
  <maven.compiler.parallel>true</maven.compiler.parallel>
  <maven.compiler.parallelCount>4</maven.compiler.parallelCount>
  <!-- Skip tests in build -->
  <skipTests>false</skipTests>
</properties>

<build>
  <plugins>
    <!-- Use incremental compiler -->
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-compiler-plugin</artifactId>
      <version>3.11.0</version>
      <configuration>
        <useIncrementalCompilation>true</useIncrementalCompilation>
      </configuration>
    </plugin>
  </plugins>
</build>
```

### 2. Gradle Build Optimization

```gradle
// build.gradle
gradle.buildCacheDir = new File(rootDir, '.gradle-build-cache')

plugins {
  id 'build-cache'
}

tasks.withType(JavaCompile) {
  options.incremental = true
  options.fork = true
}
```

### 3. npm Cache Setup

```bash
# Use npm ci instead of install
npm ci  # Faster, respects package-lock.json

# Enable offline caching
npm ci --prefer-offline --no-audit
```

### 4. GitHub Actions Caching

```yaml
- uses: actions/cache@v3
  with:
    path: ~/.m2/repository
    key: ${{ runner.os }}-maven-${{ hashFiles('**/pom.xml') }}

- uses: actions/cache@v3
  with:
    path: ~/.gradle/caches
    key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle.lock') }}

- uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

---

## How It Works

### 1. Maven Optimization

**Parallel Building:**

```bash
mvn -T 4 clean install  # 4 threads
mvn -T 0.5C clean install  # 0.5 CPU cores each
```

**Skip Tests in Build:**

```bash
mvn clean install -DskipTests
mvn test  # Run tests separately
```

**Incremental Compilation:**

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <incremental>true</incremental>
  </configuration>
</plugin>
```

**Build Cache (Maven 3.9+):**

```bash
export MAVEN_BUILD_CACHE=true
mvn clean install  # Caches build outputs
```

**Profile-Based Builds:**

```xml
<profiles>
  <profile>
    <id>fast-build</id>
    <properties>
      <skipTests>true</skipTests>
      <maven.javadoc.skip>true</maven.javadoc.skip>
    </properties>
  </profile>
</profiles>
```

Use: `mvn clean install -Pfast-build`

### 2. Gradle Optimization

**Build Cache:**

```gradle
tasks {
  withType(AbstractCompile) {
    outputs.cacheIf { true }
  }
}
```

**Parallel Building:**

```gradle
org.gradle.parallel=true
org.gradle.workers.max=4
```

**Incremental Compilation:**

```gradle
tasks.withType(JavaCompile) {
  options.incremental = true
}
```

**Daemon Mode (faster reuse):**

```bash
gradle --daemon build  # Use daemon for fast rebuilds
gradle --stop          # Stop daemon
```

**Profile-Based Tasks:**

```gradle
task fastBuild {
  dependsOn 'clean', 'compileJava'
  // Skip tests, docs, etc
}
```

### 3. npm Optimization

**npm ci vs npm install:**

```bash
npm ci    # Faster, exact versions (CI/CD)
npm install  # Flexible versions (development)
```

**Offline Mode:**

```bash
npm ci --prefer-offline  # Use local cache first

# Create offline bundle
npm ci --offline --cache=./npm-cache
```

**Parallel Installation:**

```bash
npm config set max-sockets 50
```

**Workspaces (monorepo):**

```json
{
  "workspaces": [
    "packages/*"
  ]
}
```

```bash
npm install  # Installs all workspaces
npm run build -w package-name  # Run in workspace
```

### 4. Docker Build Caching

**Layer Caching Strategy:**

```dockerfile
# Bad: Dependencies change frequently
FROM node:20
COPY . .
RUN npm install

# Good: Dependencies cached separately
FROM node:20
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
```

**BuildKit Advanced Caching:**

```dockerfile
# syntax=docker/dockerfile:1.4

FROM node:20 as build
RUN --mount=type=cache,target=/root/.npm \
  npm ci
COPY . .
RUN npm run build

FROM node:20
COPY --from=build /app/dist /app/dist
```

**Docker Compose Caching:**

```yaml
services:
  app:
    build:
      context: .
      cache_from:
        - app:latest
      cache_to:
        - type=registry,ref=myregistry/app:buildcache,mode=max
```

### 5. CI/CD Caching

**Maven Cache:**

```yaml
- uses: actions/cache@v3
  with:
    path: ~/.m2/repository
    key: maven-${{ hashFiles('**/pom.xml') }}
    restore-keys: maven-
```

**Gradle Cache:**

```yaml
- uses: actions/cache@v3
  with:
    path: ~/.gradle/caches
    key: gradle-${{ hashFiles('**/*.gradle.lock') }}
```

**Docker Layer Caching:**

```yaml
- uses: docker/build-push-action@v4
  with:
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

### 6. Test Optimization

**Parallel Testing (Maven):**

```bash
mvn test -T 4  # 4 threads
```

**Parallel Testing (Gradle):**

```gradle
test {
  maxParallelForks = Runtime.runtime.availableProcessors().intdiv(2)
}
```

**Selective Testing:**

```bash
mvn test -Dtest=UserTest,PaymentTest
mvn verify -DskipUnitTests
```

**Test Categorization:**

```java
@Category(UnitTest.class)
public class FastTest { }

@Category(IntegrationTest.class)
public class SlowTest { }
```

```bash
mvn test -Dgroups=UnitTest  # Run only unit tests
```

---

## Configuration

### Maven Optimization POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project>
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.example</groupId>
  <artifactId>my-app</artifactId>
  <version>1.0.0</version>

  <properties>
    <maven.compiler.source>21</maven.compiler.source>
    <maven.compiler.target>21</maven.compiler.target>

    <!-- Parallel compilation -->
    <maven.compiler.parallel>true</maven.compiler.parallel>
    <maven.compiler.parallelCount>4</maven.compiler.parallelCount>

    <!-- Skip tests by default -->
    <skipTests>false</skipTests>
  </properties>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.11.0</version>
        <configuration>
          <useIncrementalCompilation>true</useIncrementalCompilation>
          <parameters>true</parameters>
        </configuration>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.0.0</version>
        <configuration>
          <parallel>methods</parallel>
          <threadCount>4</threadCount>
        </configuration>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-shade-plugin</artifactId>
        <version>3.5.0</version>
        <configuration>
          <minimizeJar>true</minimizeJar>
          <transformers>
            <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
              <mainClass>com.example.App</mainClass>
            </transformer>
          </transformers>
        </configuration>
      </plugin>
    </plugins>
  </build>

  <profiles>
    <profile>
      <id>fast</id>
      <properties>
        <skipTests>true</skipTests>
        <maven.javadoc.skip>true</maven.javadoc.skip>
        <maven.source.skip>true</maven.source.skip>
      </properties>
    </profile>

    <profile>
      <id>native</id>
      <properties>
        <quarkus.package.type>native</quarkus.package.type>
      </properties>
    </profile>
  </profiles>
</project>
```

### Gradle Optimization Build

```gradle
plugins {
  id 'java'
}

java {
  toolchain {
    languageVersion = JavaLanguageVersion.of(21)
  }
}

tasks.withType(JavaCompile) {
  options.incremental = true
  options.fork = true
  options.forkOptions.jvmArgs += ['-XX:TieredStopAtLevel=1']
}

test {
  maxParallelForks = Runtime.runtime.availableProcessors().intdiv(2) ?: 1
  testLogging {
    events = ["passed", "failed", "skipped"]
  }
}

jar {
  minimize()
}

gradle.projectsEvaluated {
  tasks.withType(Test) {
    shouldRunAfter tasks.withType(Assemble)
  }
}
```

---

## Examples

### Example 1: Maven Fast Build Profile

```bash
mvn clean install -Pfast -DskipTests
# Skips tests, documentation, slow plugins
```

### Example 2: Gradle Incremental Build

```bash
./gradlew build --build-cache  # Use cache
./gradlew build --dry-run       # See what would run
./gradlew build -x test         # Skip tests
```

### Example 3: npm Workspace Optimization

```bash
npm ci --workspace-root        # Install root only
npm ci -w package-a -w package-b  # Specific packages
npm run build -w '*'           # Run in all workspaces
```

### Example 4: GitHub Actions Caching

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/cache@v3
        with:
          path: ~/.m2/repository
          key: ${{ runner.os }}-maven-${{ hashFiles('**/pom.xml') }}
          restore-keys: ${{ runner.os }}-maven-

      - run: mvn clean verify -T 4 -DskipTests

      - uses: actions/cache@v3
        with:
          path: |
            ~/.m2/repository
            target/
          key: maven-${{ github.run_id }}
```

### Example 5: Build Time Tracking

```bash
# Maven build time
mvn clean install -DskipTests | grep -E "^\[INFO\] BUILD|Total time"

# Gradle build time
./gradlew build --build-cache | grep -E "^BUILD|^Execution time"

# Track over time
./gradlew build --scan  # Generates build scan for analysis
```

---

## Best Practices

### 1. Use Appropriate Tool

```bash
# Development: use install/build for flexibility
npm install
./gradlew build

# CI/CD: use ci for speed and reproducibility
npm ci
./gradlew build --build-cache
```

### 2. Cache Aggressively

```yaml
- uses: actions/cache@v3
  with:
    path: ~/.m2/repository
    key: maven-${{ hashFiles('**/pom.xml') }}
    restore-keys: maven-  # Fallback to any maven cache
```

### 3. Parallelize Everything

```gradle
tasks.withType(JavaCompile) {
  options.incremental = true
}

test {
  maxParallelForks = 4
}
```

### 4. Separate Build and Test

```bash
# Build in parallel
mvn clean verify -T 4 -DskipTests

# Test separately (can be parallelized differently)
mvn test -T 1
```

### 5. Monitor Build Time

Track and alert on:
- Total build time
- Cache hit/miss rates
- Longest task times
- Artifact sizes

---

## Integration with Other Skills

Build Optimization integrates with:

- **github-actions-workflows** - CI/CD pipeline optimization
- **docker-compose-setup** - Container build caching
- **kubernetes-yaml-generation** - Build artifact sizing
- **build-cache-management** - Advanced caching strategies

---

## Complete Command Reference

```bash
# Maven
mvn clean install          # Standard build
mvn -T 4 clean install    # Parallel build
mvn -Pfast clean install  # Fast profile
mvn clean verify -DskipTests -T 4

# Gradle
./gradlew build           # Standard build
./gradlew build --build-cache
./gradlew build -x test   # Skip tests
./gradlew clean build --parallel

# npm
npm install               # Development
npm ci                    # CI/CD
npm ci --prefer-offline   # Cached
npm run build --workspace # Workspace
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
