---
name: java-coder
description: Generate complete production-ready Java projects with full source code, tests, and documentation. Create linked repositories where articles in /docs reference code in src and test folders. Perfect for tutorials, patterns, and real-world examples.
---

# Java Coder Skill

Generate production-ready Java projects that complement technical articles. This skill creates complete, runnable code with proper project structure, dependency management, tests, and documentation.

## When to Use This Skill

Use this skill when:
- Writing a Java tutorial and want readers to access complete working code
- Demonstrating a design pattern with a full implementation
- Building a case study with actual running code
- Creating a reference implementation for an architecture pattern
- Writing about Spring Boot and need a functional example project
- Showing concurrent programming patterns with working code
- Teaching Java best practices through example projects

## Quick Start

### Create a Java Project

When you have an article about Java, request code generation:

```
Create a Java project for my article "Spring Boot REST API Best Practices"
Include:
- Spring Boot 3.x REST controller
- Service layer with business logic
- JPA entity and repository
- Unit tests with JUnit 5
- Integration tests with TestContainers
- README with setup instructions
- Link to article in /docs/ARTICLE.md
```

### Project Structure

Standard Maven project layout:

```
project-name/
├── pom.xml                          # Maven configuration
├── README.md                        # Quick start guide
├── docs/
│   ├── ARTICLE.md                   # Your article (or link to it)
│   └── SETUP.md                     # Development setup guide
├── src/
│   ├── main/java/com/example/
│   │   ├── controller/              # REST controllers, CLI entry points
│   │   ├── service/                 # Business logic
│   │   ├── repository/              # Data access
│   │   ├── model/                   # Domain entities, DTOs
│   │   ├── util/                    # Utilities and helpers
│   │   └── Application.java         # Main entry point
│   └── resources/
│       ├── application.properties
│       └── logback.xml
├── src/test/java/com/example/
│   ├── controller/
│   ├── service/
│   ├── repository/
│   └── integration/                 # Integration tests
└── target/                          # Build output (ignored in git)
```

## Core Concepts

### 1. Project Configuration

**Maven Setup:**
- Spring Boot parent dependency
- Modern Java version (17, 21)
- Consistent dependency management
- Testing dependencies (JUnit 5, Mockito, TestContainers)
- Build plugins (compiler, surefire, shade)

**Example pom.xml structure:**
```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>project-name</artifactId>
    <version>1.0.0</version>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.0</version>
    </parent>
    <properties>
        <java.version>21</java.version>
    </properties>
    <dependencies>
        <!-- Base dependencies -->
        <!-- Testing dependencies -->
    </dependencies>
</project>
```

### 2. Code Organization

**Controller Layer:**
- REST endpoints with clear routing
- Input validation
- Error handling
- Meaningful HTTP status codes

**Service Layer:**
- Business logic separation
- Dependency injection via constructor
- Transaction management
- Error handling and logging

**Repository Layer:**
- Spring Data JPA interfaces
- Custom queries when needed
- Consistent naming conventions

**Model Layer:**
- JPA entities with proper annotations
- Data Transfer Objects (DTOs)
- Validation annotations
- Proper equals/hashCode/toString

### 3. Testing Strategy

**Unit Tests:**
- Service layer testing with mocks
- Repository testing with @DataJpaTest
- Controller testing with @WebMvcTest

**Integration Tests:**
- Full Spring context with @SpringBootTest
- TestContainers for databases
- Realistic scenarios

**Test Organization:**
```
src/test/java/
├── unit/
│   ├── ServiceTest.java
│   └── RepositoryTest.java
├── integration/
│   └── ControllerIntegrationTest.java
└── common/
    └── TestDataBuilder.java
```

### 4. Documentation

**README.md should include:**
- Project description and purpose
- Prerequisites (Java version, Maven version)
- Setup instructions (git clone, mvn install)
- Running the application
- Running tests
- Project structure overview
- Key features and endpoints (for REST APIs)
- Article reference

**SETUP.md should include:**
- Development environment setup
- IDE configuration (IntelliJ, VS Code, Eclipse)
- Database setup (if using TestContainers or local DB)
- Troubleshooting common issues

**Inline code documentation:**
- Class-level JavaDoc for public classes
- Method JavaDoc for public methods
- Complex algorithm explanations
- Links to related article sections

### 5. Linking to Articles

**In article (/docs/ARTICLE.md):**
```markdown
## Running the Example

This article includes a complete working example. Clone the repository:

```bash
git clone <repo-url>
cd project-name
```

Then follow the instructions in README.md to run the code.

Key files:
- `src/main/java/.../ControllerClass.java` - REST endpoint implementation
- `src/test/java/.../ControllerTest.java` - Tests demonstrating usage
```

**In code (README.md):**
```markdown
## Associated Article

This code example supports the article:
[Article Title](./docs/ARTICLE.md)

For detailed explanation of design decisions and patterns, see the article.
```

## Common Patterns

### REST API Project

**Files to generate:**
- Application.java - Spring Boot main class
- ApplicationProperties.java - Configuration
- Entity classes
- Repository interfaces
- Controller classes with @RestController
- Service classes
- Request/Response DTOs
- Exception handlers
- Integration tests with MockMvc

**Key features:**
- Spring Boot web starter
- Spring Data JPA
- Database support (H2, PostgreSQL, MySQL)
- Input validation with Jakarta Bean Validation
- Error handling with @ControllerAdvice
- Swagger/OpenAPI documentation

### Design Pattern Implementation

**Example: Observer Pattern**
```
Files:
- Observer.java (interface)
- ConcreteObserver.java (implementation)
- Subject.java (interface)
- ConcreteSubject.java (implementation)
- ObserverPatternTest.java (test)
- README.md explaining the pattern
```

**Example: Factory Pattern**
```
Files:
- CreatedObject.java (interface)
- ConcreteCreatedObject.java (implementation)
- ObjectFactory.java (factory)
- FactoryPatternTest.java (test)
```

### Concurrent Programming Example

**Files to generate:**
- Executor service examples
- Thread pool configurations
- Lock and synchronization examples
- Concurrent collections examples
- Virtual threads (Java 21+)
- Structured concurrency examples
- Comprehensive tests

**Key features:**
- Modern Java concurrency (virtual threads if Java 21+)
- Thread-safe implementations
- Deadlock prevention examples
- Performance benchmarking (JMH optional)

### Spring Boot Application

**Files to generate:**
- Application.yml configuration
- Entity classes with JPA annotations
- Repository interfaces
- Service classes with business logic
- Controller classes with REST endpoints
- Request/Response DTOs with validation
- Custom exception classes
- Error handlers
- Integration tests
- Unit tests

## Article Integration Workflow

### Step 1: Write Article in /docs/ARTICLE.md

Create your article explaining the concept, design, or pattern.

### Step 2: Request Code Generation

```
Generate Java code for my article about [topic].
Article file: docs/ARTICLE.md

Requirements:
- [specific implementation details]
- [design patterns to demonstrate]
- [technologies to use]
- [test coverage expectations]
```

### Step 3: Generated Project Includes

- Complete source code in `src/main/java/`
- Comprehensive tests in `src/test/java/`
- README.md with setup instructions
- pom.xml with all dependencies
- Links to article in documentation

### Step 4: Integrate in Repository

```
my-repo/
├── docs/
│   └── articles/
│       └── article-name/
│           ├── ARTICLE.md             # Your article
│           ├── README.md              # Project guide
│           └── code/                  # Code folder (optional)
│
└── projects/
    └── article-name-example/
        ├── pom.xml
        ├── README.md                  # Links to article
        ├── src/main/java/...
        └── src/test/java/...
```

Or simpler, single project:

```
my-repo/
├── pom.xml
├── README.md                          # Main guide
├── docs/
│   └── ARTICLE.md                     # Your article
├── src/main/java/...
└── src/test/java/...
```

## Best Practices

### Code Quality

✅ **Do:**
- Use clear, descriptive class and method names
- Follow Java naming conventions
- Keep methods focused and testable
- Use dependency injection (@Autowired, constructor injection)
- Add proper exception handling
- Write meaningful error messages
- Include JavaDoc for public APIs
- Use modern Java features (records, sealed classes, pattern matching)

❌ **Avoid:**
- God objects that do too much
- Tight coupling between layers
- Unchecked exceptions without documentation
- Magic numbers or strings (use constants)
- Complex nested logic (extract to methods)
- Missing null checks
- Overly generic variable names

### Testing

✅ **Do:**
- Write unit tests for business logic
- Use mocks for dependencies
- Write integration tests for APIs
- Name tests clearly: `testXxxWhenXxxThenXxx()`
- Test both success and failure scenarios
- Use @DataJpaTest for repository tests
- Use @WebMvcTest for controller tests
- Use TestContainers for real databases in integration tests

❌ **Avoid:**
- Tests that depend on each other
- Mocking everything (mock sparingly)
- Ignoring tests (@Ignore without reason)
- Tests that take > 1 second (except integration tests)
- Testing private methods
- Hardcoded test data (use builders/factories)

### Documentation

✅ **Do:**
- Explain why, not what (code shows what, docs explain why)
- Include setup and run instructions
- Document dependencies and versions
- Provide quick start examples
- Link to related articles
- Explain design decisions

❌ **Avoid:**
- Keeping documentation out of sync with code
- Obvious comments that repeat code
- Documentation not updated with code changes

## Project Templates

### Template 1: Simple REST API

```
Key files:
- Entity (JPA)
- Repository (Spring Data)
- Service (business logic)
- Controller (REST endpoints)
- Service and Controller tests
- Integration tests
```

**Dependencies:**
- spring-boot-starter-web
- spring-boot-starter-data-jpa
- h2 or postgresql
- spring-boot-starter-validation

### Template 2: Design Pattern Showcase

```
Key files:
- Pattern interface
- Concrete implementations
- Client code showing usage
- Comprehensive unit tests
- Documentation of pattern
```

**Dependencies:**
- junit-jupiter (JUnit 5)
- mockito
- assertj

### Template 3: Concurrent Programming

```
Key files:
- Executor service examples
- Thread pool configurations
- Lock/synchronization examples
- Concurrent collections examples
- Benchmarking code (optional: jmh)
- Comprehensive tests
```

**Dependencies:**
- junit-jupiter
- awaitility (for testing async code)
- jmh (optional, for benchmarking)

### Template 4: Spring Boot Full Stack

```
Key files:
- Application configuration
- Entities with relationships
- Repositories with custom queries
- Services with business logic
- Controllers with REST endpoints
- Request/Response DTOs
- Global exception handler
- Unit tests
- Integration tests
```

**Dependencies:**
- spring-boot-starter-web
- spring-boot-starter-data-jpa
- spring-boot-starter-validation
- postgresql or mysql
- testcontainers
- mockito

## File Generation Checklist

### Configuration Files
- [ ] pom.xml with all dependencies
- [ ] application.yml or application.properties
- [ ] logback.xml or logback-spring.xml
- [ ] .gitignore with Java exclusions

### Source Code
- [ ] Main application class
- [ ] Entity/Model classes
- [ ] Repository interfaces
- [ ] Service classes
- [ ] Controller classes (if REST API)
- [ ] DTOs (Request/Response)
- [ ] Exception classes
- [ ] Utility classes
- [ ] Configuration classes

### Tests
- [ ] Unit tests for services
- [ ] Repository tests
- [ ] Controller tests
- [ ] Integration tests
- [ ] Test fixtures and builders
- [ ] Test configuration

### Documentation
- [ ] README.md with full setup instructions
- [ ] SETUP.md with development guide
- [ ] JavaDoc for public classes/methods
- [ ] Comments on complex logic
- [ ] Links to article

### Quality
- [ ] All tests pass (100% test success)
- [ ] No compiler warnings
- [ ] Code follows conventions
- [ ] Proper exception handling
- [ ] Logging at appropriate levels
- [ ] No hardcoded values

## Build and Run Commands

**Maven commands to document:**

```bash
# Install dependencies
mvn clean install

# Run tests
mvn test

# Run specific test
mvn test -Dtest=ClassName

# Build fat JAR (if Spring Boot)
mvn clean package

# Run application
java -jar target/app.jar

# Run with Maven plugin (Spring Boot)
mvn spring-boot:run

# Check dependencies
mvn dependency:tree

# Format code
mvn spotless:apply
```

## Integration with Article Workflow

1. **Write article** in `/docs/ARTICLE.md`
2. **Request Java code generation** mentioning article file
3. **Receive complete project** with:
   - Source code organized in `src/main/java/`
   - Tests in `src/test/java/`
   - README.md linking to article
   - Ready to run setup
4. **Link from article** to GitHub repository
5. **Readers can clone** and run the code
6. **Maintain together**: Article and code stay in sync

## Common Scenarios

### Scenario 1: Tutorial with Step-by-Step Code

Article shows steps 1-5. Code project shows complete working implementation.

Reader can:
- Follow along with article
- See each step's code
- Run complete project
- Modify and experiment

### Scenario 2: Design Pattern Implementation

Article explains pattern. Code shows real, working implementation.

Reader can:
- Understand pattern from article
- See production-ready code
- Run tests to see pattern in action
- Use as reference for own code

### Scenario 3: Architecture Example

Article shows system design. Code shows simplified but real implementation.

Reader can:
- Learn architecture concepts
- See how they're implemented
- Run and test the system
- Use as starting point for own project

## Tools & IDE Setup

**Recommended IDEs:**
- IntelliJ IDEA Community (free) or Ultimate
- Eclipse IDE for Java Developers
- VS Code with Extension Pack for Java

**Build tool:**
- Maven 3.8+

**Java versions:**
- Java 25 (latest LTS)
- Java 21 (stable LTS - largely used)
- Java 17 (LTS, good for production)
- Java 11 (older LTS, still supported)
- Java 8 (old LTS, do not use)

## Success Checklist

- [ ] Code compiles without warnings
- [ ] All tests pass
- [ ] Tests are meaningful (not just mocks everywhere)
- [ ] README is clear and complete
- [ ] Code follows Java conventions
- [ ] Article is linked from README
- [ ] Setup instructions are accurate
- [ ] Code is production-ready (not just demo)
- [ ] Key classes have JavaDoc
- [ ] Exception handling is appropriate
- [ ] No hardcoded values or magic numbers

---

This skill works best combined with:
- **java-content** for Java expertise and guidance
- **code-examples-generator** for snippet generation
- **markdown-formatter** for documentation formatting
- **architecture-design** for pattern explanations
- **image-generator-blog** for architecture diagrams in docs
