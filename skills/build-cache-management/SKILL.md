# Build Cache Management Skill

**Master Maven/Gradle caching, Docker layer caching, npm/yarn caching, and cache invalidation strategies.**

## Overview

Effective caching dramatically reduces build times. This skill covers caching strategies across all major build systems.

**What it does:**
- Configures Maven dependency cache
- Optimizes Gradle build cache
- Implements Docker layer caching
- Manages npm/yarn package cache
- Handles cache invalidation
- Monitors cache effectiveness
- Implements distributed caching
- Troubleshoots cache issues

**Perfect for:**
- Reducing CI/CD build times
- Improving developer experience
- Reducing bandwidth and costs
- Large-scale builds
- Parallel builds

---

## When to Use This Skill

Use Build Cache Management when you need to:

- **Speed up builds** with caching
- **Reduce bandwidth** and costs
- **Improve CI/CD performance** significantly
- **Cache dependencies** effectively
- **Cache build artifacts** across jobs
- **Implement distributed caching**
- **Monitor cache hit rates**
- **Debug cache issues**

---

## Quick Start (10 Minutes)

### 1. Maven Cache

```bash
# Maven uses ~/.m2/repository by default
mvn clean install
# Caches dependencies in ~/.m2/

# Custom cache location
mvn clean install -Dmaven.repo.local=/custom/cache

# Clear cache if corrupted
rm -rf ~/.m2/repository
mvn clean install
```

### 2. Gradle Cache

```gradle
// Enable build cache
org.gradle.caching=true

// Or command line
./gradlew build --build-cache

// View cache info
./gradlew build --build-cache -i | grep cache
```

### 3. Docker Layer Caching

```dockerfile
# Bad: Loses cache on any change
FROM node:20
COPY . .
RUN npm install
RUN npm run build

# Good: Cache layers separately
FROM node:20
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
```

### 4. npm/yarn Cache

```bash
# npm uses ~/.npm by default
npm install

# ci is faster for CI/CD (uses lock file)
npm ci

# Offline mode
npm ci --offline

# Yarn cache
yarn cache clean
yarn install --prefer-offline
```

---

## How It Works

### 1. Maven Caching Strategy

**Local Repository Structure:**

```
~/.m2/repository/
├── org/
│   └── springframework/
│       └── boot/
│           └── spring-boot-starter/
│               └── 3.2.0/
│                   ├── spring-boot-starter-3.2.0.jar
│                   ├── spring-boot-starter-3.2.0.pom
│                   └── spring-boot-starter-3.2.0.jar.lastUpdated
```

**Cache Configuration:**

```xml
<!-- .m2/settings.xml -->
<settings>
  <localRepository>/path/to/custom/cache</localRepository>

  <repositories>
    <repository>
      <id>central</id>
      <url>https://repo.maven.apache.org/maven2</url>
      <!-- Cache remote artifacts -->
    </repository>
  </repositories>
</settings>
```

**Remote Repository Caching:**

```bash
# Add remote cache proxy (Nexus, Artifactory)
# Reduces external dependency downloads
```

### 2. Gradle Build Cache

**Configuration:**

```gradle
// gradle.properties
org.gradle.caching=true
org.gradle.cache.debug=true

// Or in code
buildCache {
  local {
    directory = file('/custom/gradle/cache')
    removeUnusedEntriesAfterDays = 7
  }
}
```

**Task Caching:**

```gradle
tasks.register('processResources', Copy) {
  from('src/main/resources')
  into('build/resources/main')

  // Enable caching
  outputs.cacheIf { true }
}

// Or conditional
tasks.register('deploy') {
  outputs.cacheIf { gradle.startParameter.taskNames == ['build'] }
}
```

**Build Scan:**

```bash
./gradlew build --scan
# Provides detailed cache analysis
# Shows what was cached and what wasn't
```

### 3. Docker Layer Caching

**Dockerfile Optimization:**

```dockerfile
# ❌ Bad - Loses cache on any source change
FROM node:20
COPY . /app
WORKDIR /app
RUN npm install
RUN npm run build

# ✅ Good - Caches npm install separately
FROM node:20
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# ✅ Better - Even more granular
FROM node:20 as builder
WORKDIR /app

# Cache this layer
COPY package*.json ./
RUN npm ci --production

# Cache this layer
COPY package*.json ./
RUN npm ci

# Application code changes don't invalidate npm install
COPY src ./src
RUN npm run build

# Final layer
FROM node:20
COPY --from=builder /app/dist /app/dist
COPY --from=builder /app/node_modules /app/node_modules
CMD ["node", "dist/index.js"]
```

**BuildKit Advanced Caching:**

```dockerfile
# syntax=docker/dockerfile:1.4

FROM node:20
WORKDIR /app

# Cache mounting - preserves cache across builds
RUN --mount=type=cache,target=/root/.npm \
  npm ci

COPY . .
RUN npm run build
```

**GitHub Actions Docker Caching:**

```yaml
- uses: docker/build-push-action@v4
  with:
    context: .
    push: true
    tags: myapp:latest
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

### 4. npm/yarn Cache

**npm Cache:**

```bash
# View cache location
npm cache dir
# ~/.npm on Linux/macOS
# %AppData%\npm-cache on Windows

# Clean cache
npm cache clean --force

# Verify cache
npm cache verify

# Configure cache
npm config set cache ~/.npm
```

**npm ci (CI-optimized):**

```bash
# Better than npm install for CI/CD
npm ci --prefer-offline --no-audit

# Uses lock file for exact versions
# Fails if lock file missing (safer)
# Much faster in CI
```

**Yarn Offline Mode:**

```bash
# Create offline cache
yarn install --prefer-offline

# Use offline
yarn install --offline
```

**GitHub Actions npm Caching:**

```yaml
- uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: ${{ runner.os }}-npm-

- run: npm ci
```

### 5. Multi-Stage Build Caching

**Efficient Multi-Stage:**

```dockerfile
# Stage 1: Build
FROM node:20 as builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Dependencies
FROM node:20 as deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --production

# Stage 3: Runtime
FROM node:20
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY package.json .
CMD ["node", "dist/index.js"]
```

### 6. Distributed Caching

**Artifactory/Nexus Cache:**

```xml
<!-- settings.xml -->
<settings>
  <mirrors>
    <mirror>
      <id>central</id>
      <name>Artifactory Mirror</name>
      <url>https://artifactory.example.com/artifactory/libs-release</url>
      <mirrorOf>*</mirrorOf>
    </mirror>
  </mirrors>
</settings>
```

**S3 Cache (AWS):**

```gradle
build {
  cache {
    remote {
      class = com.example.S3Cache
      push = true
    }
  }
}
```

---

## Configuration

### Complete Cache Setup

`pom.xml` (Maven):

```xml
<!-- Maven settings -->
<properties>
  <maven.compiler.source>21</maven.compiler.source>
  <maven.repo.local>${project.basedir}/.m2/repository</maven.repo.local>
</properties>

<build>
  <plugins>
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

`gradle.properties` (Gradle):

```properties
org.gradle.caching=true
org.gradle.parallel=true
org.gradle.workers.max=4

# Remote caching
org.gradle.caching.debug=false
```

`.github/workflows/build.yml` (GitHub Actions):

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Maven cache
      - uses: actions/cache@v3
        with:
          path: ~/.m2/repository
          key: maven-${{ hashFiles('**/pom.xml') }}
          restore-keys: maven-

      # Gradle cache
      - uses: gradle/gradle-build-action@v2
        with:
          gradle-version: wrapper

      # npm cache
      - uses: actions/cache@v3
        with:
          path: ~/.npm
          key: npm-${{ hashFiles('**/package-lock.json') }}

      - run: npm ci
      - run: npm run build
```

---

## Examples

### Example 1: Optimized Dockerfile

```dockerfile
FROM node:20 as builder

# Install dependencies
WORKDIR /build
COPY package*.json ./
RUN npm ci

# Copy and build
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine

# Install production dependencies only
WORKDIR /app
COPY package*.json ./
RUN npm ci --production

# Copy built application
COPY --from=builder /build/dist ./dist

# Health check
HEALTHCHECK --interval=30s CMD node -e "require('http').get('http://localhost:3000', (r) => {if (r.statusCode !== 200) throw new Error(r.statusCode)})"

CMD ["node", "dist/index.js"]
```

### Example 2: GitHub Actions Caching

```yaml
name: Build and Test

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Maven cache
      - uses: actions/cache@v3
        id: maven-cache
        with:
          path: ~/.m2/repository
          key: ${{ runner.os }}-maven-${{ hashFiles('**/pom.xml') }}
          restore-keys: ${{ runner.os }}-maven-

      # npm cache
      - uses: actions/cache@v3
        with:
          path: ~/.npm
          key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
          restore-keys: ${{ runner.os }}-npm-

      - name: Build
        run: |
          mvn clean install -DskipTests
          npm ci
          npm run build
```

### Example 3: Gradle Cache Configuration

```gradle
buildCache {
  local {
    // Custom cache directory
    directory = file(System.env.GRADLE_CACHE_DIR ?: "$rootDir/.gradle/cache")
    removeUnusedEntriesAfterDays = 7
  }

  remote(HttpBuildCache) {
    url = 'https://cache.example.com/'
    push = System.env.GRADLE_CACHE_PUSH == 'true'
    enabled = System.env.GRADLE_CACHE_ENABLED != 'false'
  }
}

// Cache specific tasks
tasks.withType(JavaCompile) {
  outputs.cacheIf { true }
}
```

### Example 4: Cache Hit Analysis

```bash
# Maven
mvn clean install -X | grep -i cache

# Gradle
./gradlew build --build-cache -i | grep cache
./gradlew build --scan  # Detailed analysis

# Docker
docker build --progress=plain . 2>&1 | grep -i cache
```

---

## Best Practices

### 1. Layer Order Matters

```dockerfile
# Bad: Source changes invalidate npm install cache
COPY . .
RUN npm install

# Good: npm install cache preserved across source changes
COPY package*.json ./
RUN npm install
COPY . .
```

### 2. Use Cache Busting Wisely

```dockerfile
# Bust cache intentionally when needed
ARG CACHE_BUST=1
RUN CACHE_BUST=$CACHE_BUST && npm install

# Don't cache everything
RUN npm install  # Cache this
RUN npm run build  # Cache this too
```

### 3. Monitor Cache Effectiveness

```bash
# Build with detailed logging
./gradlew build --build-cache -i

# Check cache hit rate
# Look for "From cache" messages
```

### 4. Size and Performance

```bash
# Gradle cache size
du -sh ~/.gradle/caches

# npm cache size
du -sh ~/.npm

# Cleanup if needed
npm cache clean --force
```

### 5. CI/CD Specific

```yaml
# Restore and save cache on CI
- uses: actions/cache@v3
  with:
    path: ~/.m2/repository
    key: maven-${{ hashFiles('**/pom.xml') }}
    restore-keys: maven-
```

---

## Integration with Other Skills

Build Cache Management integrates with:

- **build-optimization** - Combined caching and optimization
- **github-actions-workflows** - Cache in CI/CD
- **docker-compose-setup** - Image caching
- **maven-gradle-optimization** - Build system caching

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
