# Maven Gradle Optimization Skill

**Master Maven profiles, Gradle optimization, dependency management, and custom build tasks.**

## Overview

Build system optimization improves development and CI/CD performance. This skill covers advanced Maven and Gradle patterns.

**What it does:**
- Configures Maven profiles for different builds
- Optimizes Gradle build performance
- Manages complex dependencies
- Creates custom build tasks
- Implements build caching
- Handles multi-module projects
- Optimizes artifact creation
- Tracks build metrics

**Perfect for:**
- Complex build requirements
- Multi-module projects
- Profile-based deployments
- Dependency conflict resolution
- Custom build logic

---

## When to Use This Skill

Use Maven Gradle Optimization when you need to:

- **Optimize build times** for large projects
- **Manage complex dependencies** across modules
- **Create build profiles** for different environments
- **Implement custom build tasks** and logic
- **Cache build artifacts** effectively
- **Handle multi-module projects** efficiently
- **Generate custom reports** and artifacts
- **Parallelize builds** across modules

---

## Quick Start (10 Minutes)

### 1. Maven Profiles

```xml
<profiles>
  <profile>
    <id>dev</id>
    <activation>
      <activeByDefault>true</activeByDefault>
    </activation>
    <properties>
      <environment>development</environment>
      <skipTests>false</skipTests>
    </properties>
  </profile>

  <profile>
    <id>prod</id>
    <properties>
      <environment>production</environment>
      <skipTests>true</skipTests>
    </properties>
  </profile>
</profiles>
```

Use: `mvn clean install -Pprod`

### 2. Gradle Tasks

```gradle
task buildDev {
  dependsOn clean, build
  doLast {
    println 'Build complete for development'
  }
}

task buildProd {
  dependsOn clean, build
  doLast {
    println 'Build complete for production'
  }
}
```

Use: `./gradlew buildProd`

### 3. Multi-Module Maven

```xml
<modules>
  <module>common</module>
  <module>api</module>
  <module>web</module>
</modules>
```

```bash
mvn clean install -pl common -am  # Build common and dependents
mvn clean install -pl api         # Build only api
```

### 4. Gradle Multi-Project

```gradle
subprojects {
  apply plugin: 'java'
  sourceCompatibility = '21'

  dependencies {
    testImplementation 'junit:junit:4.13'
  }
}

project(':api') {
  dependencies {
    implementation project(':common')
  }
}
```

---

## How It Works

### 1. Maven Profiles

**Profile Activation:**

```xml
<profiles>
  <!-- Activated by property -->
  <profile>
    <id>mysql</id>
    <activation>
      <property>
        <name>db</name>
        <value>mysql</value>
      </property>
    </activation>
  </profile>

  <!-- Activated by file -->
  <profile>
    <id>unix</id>
    <activation>
      <file>
        <exists>/etc/os-release</exists>
      </file>
    </activation>
  </profile>

  <!-- Activated by OS -->
  <profile>
    <id>windows</id>
    <activation>
      <os>
        <family>Windows</family>
      </os>
    </activation>
  </profile>
</profiles>
```

Use: `mvn clean install -Ddb=mysql`

**Profile Configuration:**

```xml
<profile>
  <id>production</id>
  <properties>
    <env>production</env>
    <maven.compiler.source>21</maven.compiler.source>
    <maven.compiler.target>21</maven.compiler.target>
  </properties>
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-shade-plugin</artifactId>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>shade</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</profile>
```

### 2. Gradle Optimization

**Build Cache:**

```gradle
plugins {
  id 'build-cache'
}

tasks {
  withType(JavaCompile) {
    outputs.cacheIf { true }
  }
}
```

**Parallel Builds:**

```gradle
// gradle.properties
org.gradle.parallel=true
org.gradle.workers.max=4

// Or command line
./gradlew build -x test --parallel
```

**Lazy Task Configuration:**

```gradle
tasks.register('myTask') {
  doLast {
    println 'Task executed'
  }
}

// Not evaluated until needed
```

### 3. Dependency Management

**Maven BOM (Bill of Materials):**

```xml
<!-- common-dependencies/pom.xml -->
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

<!-- In consuming project -->
<parent>
  <groupId>com.example</groupId>
  <artifactId>parent-pom</artifactId>
  <version>1.0.0</version>
</parent>
```

**Gradle Dependency Constraints:**

```gradle
dependencies {
  constraints {
    implementation 'org.springframework.boot:spring-boot-bom:3.2.0'
  }
}

// Or Platform
dependencies {
  implementation platform('org.springframework.cloud:spring-cloud-dependencies:2023.0.0')
  implementation 'org.springframework.cloud:spring-cloud-starter-config'
}
```

### 4. Custom Build Tasks

**Maven Plugin:**

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-antrun-plugin</artifactId>
  <executions>
    <execution>
      <phase>generate-sources</phase>
      <goals>
        <goal>run</goal>
      </goals>
      <configuration>
        <target>
          <echo message="Custom build task"/>
          <exec executable="bash">
            <arg value="scripts/generate-code.sh"/>
          </exec>
        </target>
      </configuration>
    </execution>
  </executions>
</plugin>
```

**Gradle Custom Task:**

```gradle
task generateCode {
  doLast {
    exec {
      commandLine 'bash', 'scripts/generate-code.sh'
    }
  }
}

task buildAll {
  dependsOn generateCode, build
  doLast {
    println 'Full build complete'
  }
}
```

### 5. Multi-Module Projects

**Maven Parent POM:**

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>parent</artifactId>
  <version>1.0.0</version>
  <packaging>pom</packaging>

  <modules>
    <module>common</module>
    <module>api</module>
    <module>web</module>
  </modules>

  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.13</version>
        <scope>test</scope>
      </dependency>
    </dependencies>
  </dependencyManagement>

  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-compiler-plugin</artifactId>
          <version>3.11.0</version>
          <configuration>
            <source>21</source>
            <target>21</target>
          </configuration>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>
</project>
```

**Gradle Multi-Project:**

```gradle
// settings.gradle
rootProject.name = 'myapp'

include 'common'
include 'api'
include 'web'

// root build.gradle
allprojects {
  group = 'com.example'
  version = '1.0.0'
}

subprojects {
  apply plugin: 'java'

  java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
  }

  repositories {
    mavenCentral()
  }

  dependencies {
    testImplementation 'junit:junit:4.13'
  }
}

project(':api') {
  dependencies {
    implementation project(':common')
  }
}

project(':web') {
  dependencies {
    implementation project(':common')
    implementation project(':api')
  }
}
```

---

## Examples

### Example 1: Maven Profiles

```xml
<profiles>
  <profile>
    <id>dev</id>
    <activation>
      <activeByDefault>true</activeByDefault>
    </activation>
    <properties>
      <env>development</env>
      <skipTests>false</skipTests>
    </properties>
  </profile>

  <profile>
    <id>staging</id>
    <properties>
      <env>staging</env>
      <skipTests>true</skipTests>
    </properties>
  </profile>

  <profile>
    <id>prod</id>
    <properties>
      <env>production</env>
      <skipTests>true</skipTests>
    </properties>
    <build>
      <plugins>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-shade-plugin</artifactId>
          <version>3.5.0</version>
          <executions>
            <execution>
              <phase>package</phase>
              <goals>
                <goal>shade</goal>
              </goals>
            </execution>
          </executions>
        </plugin>
      </plugins>
    </build>
  </profile>
</profiles>
```

Use: `mvn clean install -Pprod`

### Example 2: Gradle Build Variants

```gradle
ext {
  versions = [
    spring: '3.2.0',
    postgres: '42.7.1'
  ]
}

// Development variant
task devBuild {
  dependsOn clean, test, build
  doLast {
    println "Development build complete"
  }
}

// Production variant
task prodBuild {
  dependsOn clean, build
  doLast {
    println "Production build complete"
  }
}

// Custom task
task generateBuildInfo {
  doLast {
    file("build/resources/main/build-info.properties").text = """
version=${project.version}
build.time=${new Date()}
java.version=${System.getProperty('java.version')}
"""
  }
}
```

### Example 3: Multi-Module Build

```bash
# Build entire project
mvn clean install

# Build specific module
mvn clean install -pl api

# Build module and dependencies
mvn clean install -pl web -am

# Skip tests
mvn clean install -DskipTests

# Parallel build
mvn clean install -T 4
```

### Example 4: Dependency Management

```xml
<!-- parent-pom.xml -->
<dependencyManagement>
  <dependencies>
    <!-- Spring Cloud BOM -->
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-dependencies</artifactId>
      <version>2023.0.0</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>

    <!-- Internal modules -->
    <dependency>
      <groupId>${project.groupId}</groupId>
      <artifactId>common</artifactId>
      <version>${project.version}</version>
    </dependency>
  </dependencies>
</dependencyManagement>

<!-- Consuming project just declares without version -->
<dependencies>
  <dependency>
    <groupId>${project.groupId}</groupId>
    <artifactId>common</artifactId>
  </dependency>
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter</artifactId>
  </dependency>
</dependencies>
```

---

## Best Practices

### 1. Use Profiles Consistently

```bash
mvn clean install -Pdev   # Development
mvn clean install -Pstaging  # Staging
mvn clean install -Pprod  # Production
```

### 2. Parallel Builds

```bash
mvn clean install -T 4    # 4 threads
mvn clean install -T 1.5C # 1.5 CPU cores
```

### 3. Manage Transitive Dependencies

```xml
<dependency>
  <groupId>old-lib</groupId>
  <artifactId>legacy</artifactId>
  <version>1.0</version>
  <exclusions>
    <exclusion>
      <groupId>conflicting-group</groupId>
      <artifactId>conflicting-lib</artifactId>
    </exclusion>
  </exclusions>
</dependency>
```

### 4. Version Consistency

```xml
<properties>
  <spring.version>3.2.0</spring.version>
  <postgres.version>42.7.1</postgres.version>
</properties>

<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter</artifactId>
  <version>${spring.version}</version>
</dependency>
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
