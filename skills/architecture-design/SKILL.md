---
name: architecture-design
description: Write comprehensive articles on software architecture, system design, architectural patterns, and design decisions. Use when creating technical content about architecture patterns, design principles, system design interviews, and enterprise architecture patterns.
---

# Architecture & Software Design Content

## When to Use This Skill

Use this skill when:
- Writing articles about architectural patterns (MVC, MVVM, CQRS, Event Sourcing)
- Explaining system design and architecture decisions
- Creating content about design principles (SOLID, DRY, KISS)
- Writing about enterprise architecture patterns
- Discussing microservices architecture and organization
- Explaining domain-driven design (DDD)
- Creating system design interview preparation content
- Writing case studies on architectural decisions

## Core Architectural Concepts

### Architectural Patterns

#### Monolithic Architecture
- Single deployable unit
- All features in one codebase
- Tight coupling between modules
- Simpler initially, scales with difficulty
- When to use, when to avoid

#### Microservices Architecture
- Independent services, each with own database
- Service-to-service communication
- Independent scaling and deployment
- Operational complexity increases
- Organizational alignment (Conway's Law)
- Trade-offs and when to use

#### Layered (N-Tier) Architecture
- Presentation → Business → Persistence layers
- Clear separation of concerns
- Good for traditional applications
- Can become "big ball of mud"
- Testing and maintainability

#### Event-Driven Architecture
- Services communicate via events
- Asynchronous, loosely coupled
- Eventual consistency considerations
- Kafka, RabbitMQ, event brokers
- Complex but highly scalable

#### CQRS (Command Query Responsibility Segregation)
- Separate models for read and write
- Optimize each for its use case
- Event Sourcing often paired
- Complexity trade-off
- When it's worth the complexity

#### Event Sourcing
- Store all changes as events
- Rebuild state from event history
- Audit trail built-in
- Temporal queries possible
- Complexity and learning curve

#### Hexagonal Architecture (Ports & Adapters)
- Core domain isolated from external concerns
- Adapter pattern for dependencies
- Testable, independent of frameworks
- Growing in popularity
- Clean Architecture variation

### Design Principles

#### SOLID Principles
- **S**ingle Responsibility: One reason to change
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Subtypes must be substitutable
- **I**nterface Segregation: Don't force fat interfaces
- **D**ependency Inversion: Depend on abstractions, not concretions

#### DRY (Don't Repeat Yourself)
- Avoid duplication
- Single source of truth
- When NOT to DRY (premature abstraction)
- Balancing with YAGNI

#### KISS (Keep It Simple, Stupid)
- Simpler is better
- Avoid over-engineering
- Complexity should be justified
- Trade-off with extensibility

#### YAGNI (You Aren't Gonna Need It)
- Don't build features you don't need
- Avoid premature optimization
- Add complexity when needed
- Refactor later if necessary

#### GRASP (General Responsibility Assignment Software Patterns)
- Information Expert
- Creator
- Controller
- Low Coupling
- High Cohesion
- Polymorphism
- Pure Fabrication
- Indirection
- Protected Variations

### System Design Concepts

#### Scalability
- **Vertical scaling**: Bigger machines
- **Horizontal scaling**: More machines
- **Load balancing**: Distributing requests
- **Caching**: Reducing database load
- **Database scaling**: Sharding, replication
- **Asynchronous processing**: Queues, workers

#### Reliability & Resilience
- **Fault tolerance**: System continues despite failures
- **Redundancy**: Backup systems
- **Circuit breakers**: Preventing cascading failures
- **Retry logic**: Handling transient failures
- **Timeouts**: Preventing hanging requests
- **Bulkheads**: Isolating failures

#### Consistency & Availability
- **CAP Theorem**: Can't have all three
- **ACID transactions**: Consistency guarantee
- **Eventual consistency**: Scaling at cost of consistency
- **Read replicas**: Scaling reads
- **Sharding**: Scaling writes

#### Database Design
- **Normalization**: Reducing redundancy
- **Denormalization**: Optimizing reads
- **Indexing strategy**: Performance optimization
- **Query optimization**: Reducing load
- **Replication**: High availability
- **Sharding**: Scaling writes

#### API Design
- **RESTful principles**: Statelessness, resources
- **GraphQL**: Query flexibility
- **gRPC**: High performance
- **Versioning strategies**: API evolution
- **Error handling**: Consistent error responses
- **Authentication**: Token, OAuth, mTLS

#### Deployment Architecture
- **Monolithic deployment**: Single package
- **Containerization**: Docker, Kubernetes
- **Serverless**: Function as a service
- **Infrastructure as Code**: Terraform, CloudFormation
- **CI/CD pipelines**: Automated deployment
- **Blue-green deployment**: Zero-downtime updates

## Article Structures for Architecture Content

### Pattern Explanation Structure

```
INTRODUCTION (300-400 words)
- Problem the pattern solves
- Why it matters
- When you should consider it
- Historical context

PATTERN OVERVIEW (400-600 words)
- Core concept explanation
- Key components
- How it works (high level)
- Terminology

ARCHITECTURE DIAGRAM (visual)
- System components
- Interactions between components
- Data flow

IMPLEMENTATION EXAMPLE (800-1200 words)
- Real code showing pattern
- Setup and configuration
- Step-by-step walkthrough
- Code explanation

WHEN TO USE (400-600 words)
- Ideal use cases
- Scale at which it makes sense
- Team structure implications
- Business requirements fit

WHEN NOT TO USE (300-400 words)
- Complexity it introduces
- Operational overhead
- When simpler approaches suffice
- Common mistakes

REAL-WORLD EXAMPLE (500-700 words)
- Company or project using this
- How they implemented it
- Metrics and results
- Lessons learned

COMPARISON (400-500 words)
- How it compares to alternatives
- Trade-offs vs. other patterns
- When each is appropriate
- Evolution path

CHALLENGES & SOLUTIONS (400-600 words)
- Common implementation challenges
- Monitoring and observability
- Testing strategies
- Debugging techniques

FURTHER READING (200-300 words)
- Related patterns
- Books and references
- Tools and frameworks
- Community discussions
```

### System Design Interview Structure

```
INTRODUCTION (200-300 words)
- System to design
- Interview approach
- What interviewer is evaluating

REQUIREMENTS (300-500 words)
- Functional requirements (what it does)
- Non-functional requirements (scale, performance)
- Constraints (budget, tech stack)
- Back-of-envelope calculations

ARCHITECTURE (600-800 words)
- High-level architecture
- Key components
- Data flow
- Diagram showing architecture

DETAILED DESIGN (800-1000 words)
- API design
- Database schema
- Caching strategy
- Load balancing approach

SCALING (500-700 words)
- Horizontal scaling
- Database scaling
- Caching optimization
- Bottleneck identification

TRADE-OFFS (400-600 words)
- Consistency vs. availability
- Latency vs. accuracy
- Operational complexity vs. features
- Cost vs. performance

MONITORING (300-400 words)
- Key metrics
- Alerting strategy
- Logging approach
- Performance monitoring

EXAMPLE SOLUTIONS (500-700 words)
- Google's approach
- Amazon's approach
- Facebook's approach
- Lessons from each

COMMON MISTAKES (300-500 words)
- Over-engineering early
- Ignoring operational concerns
- Not considering scale
- Poor communication
```

### Design Decision / Case Study Structure

```
CONTEXT (400-600 words)
- Company/project background
- Original system
- Constraints (team, budget, time)
- Business requirements

THE PROBLEM (500-700 words)
- What was broken
- Why it was a problem
- Business impact
- Scale challenges

OPTIONS CONSIDERED (600-900 words)
- Option 1: Description + trade-offs
- Option 2: Description + trade-offs
- Option 3: Description + trade-offs
- Why final option was chosen

THE SOLUTION (700-1000 words)
- Architecture chosen
- Implementation approach
- Timeline and phases
- Key decisions made

IMPLEMENTATION CHALLENGES (500-700 words)
- Unexpected obstacles
- How they were overcome
- Lessons learned
- What went well

RESULTS & METRICS (400-600 words)
- Performance improvements
- Reliability improvements
- Cost changes
- Team velocity changes

KEY LESSONS (400-600 words)
- What would you do differently
- What worked well
- Mistakes to avoid
- Guidance for similar situations

RELATED TOPICS (300-400 words)
- Other architectures considered
- Evolution plans
- Related systems
- Further reading
```

## Key Architectural Concepts to Cover

### By Language/Framework Context

#### Java/Spring Boot Architecture
- Spring Data patterns (repositories, specifications)
- Service layer patterns
- Controller/DTO patterns
- Testing architecture (TestContainers)
- Distributed tracing (Spring Cloud Sleuth)
- Messaging patterns (RabbitMQ, Kafka)
- Security architecture (OAuth2, JWT)

#### Python/FastAPI Architecture
- Dependency injection patterns
- Async/await architecture
- Middleware and interceptors
- Database patterns (SQLAlchemy)
- Testing architecture (pytest fixtures)
- Celery/RQ for async tasks
- Authentication and authorization

#### JavaScript/Node.js Architecture
- MVC patterns in Express
- Middleware architecture
- Service/repository patterns
- Async patterns and callbacks
- TypeScript for type safety
- Testing architecture (Jest)
- Message queues and events

### Organizational Patterns

#### Conway's Law
- Team structure reflects architecture
- Organization design impacts software design
- Microservices require organization changes
- Cross-functional teams
- Communication structures

#### Team Topologies
- Stream-aligned teams
- Enabling teams
- Complicated-subsystem teams
- Platform teams
- Team interactions

### Cloud Architecture

#### AWS Patterns
- EC2 patterns and scaling
- Lambda serverless patterns
- RDS vs. DynamoDB
- SQS/SNS messaging
- S3 and object storage
- CloudFront CDN
- API Gateway patterns

#### Kubernetes Patterns
- Deployments and replicas
- Services and networking
- StatefulSets for stateful services
- ConfigMaps and Secrets
- Ingress and routing
- Resource management
- Health checks and recovery

## Writing Tips for Architecture Content

### Explain Complex Ideas Simply
- Start with the simplest explanation
- Use analogies from real world
- Gradually add complexity
- Use visuals heavily
- Show working code examples

### Include Architecture Diagrams
- Use consistent shapes and colors
- Label all components
- Show data flow with arrows
- Include external dependencies
- Create multiple levels of detail

### Discuss Trade-Offs
- No architecture is perfect
- Discuss what you're trading off
- Why one choice over another
- Operational impact
- Cost implications

### Show Real Code
- Don't just explain; show implementation
- Use production patterns
- Include error handling
- Show testing approach
- Real-world examples matter

### Cover Operations
- How do you monitor this?
- What metrics matter?
- How do you debug?
- What can go wrong?
- How do you scale?

### Acknowledge Complexity
- When complexity is justified
- When you should keep it simple
- Organizational implications
- Operational requirements
- Team capabilities needed

## Architecture Content Ideas

### By Skill Level

**Beginner:**
- "Understanding Monolithic Architecture"
- "REST API Design Basics"
- "Database Normalization Explained"
- "What is SOLID?"
- "Service-Oriented Architecture 101"

**Intermediate:**
- "Microservices: When and How"
- "Event-Driven Architecture Patterns"
- "CQRS and Event Sourcing"
- "Domain-Driven Design Principles"
- "API Versioning Strategies"

**Advanced:**
- "Scaling Microservices to 10,000 RPS"
- "Distributed Transactions and Sagas"
- "Stream Processing Architecture"
- "System Design: Building YouTube"
- "Chaos Engineering in Production"

### Case Study Topics
- "How Uber Scaled Their Architecture"
- "Netflix's Microservices Evolution"
- "Amazon's Two-Pizza Teams"
- "Airbnb's Service-Oriented Architecture"
- "Our Migration From Monolith to Microservices"

### Interview Prep Topics
- "Design Twitter"
- "Design Uber"
- "Design YouTube"
- "Design Dropbox"
- "Design Slack"
- "Design Notification System"
- "Design Database"

## Tools for Architecture Diagrams

- **Draw.io**: Free, simple diagram tool
- **Lucidchart**: Professional, expensive
- **Excalidraw**: Hand-drawn style, free
- **ArchiMate**: Standard notation for architecture
- **C4 Model**: Hierarchical architecture diagrams
- **Mermaid**: Diagram as code (see diagram skill)
- **PlantUML**: UML diagrams as code (see diagram skill)

## Architecture Content Checklist

- [ ] Problem statement is clear
- [ ] Pattern/concept explained simply first
- [ ] Architecture diagram included
- [ ] Trade-offs discussed
- [ ] Real code examples shown
- [ ] When to use/when not to use addressed
- [ ] Operational concerns covered
- [ ] Real-world examples or case studies
- [ ] Compared to alternatives
- [ ] Challenges and solutions discussed
- [ ] Scale/performance implications clear
- [ ] References to further reading
- [ ] Terminology clearly defined
- [ ] Diagrams are clear and labeled

## Common Architecture Mistakes to Avoid

❌ **Over-engineering from start**: Build simple, refactor when needed
❌ **Ignoring operational concerns**: Monitoring, debugging, scaling matter
❌ **Architecture without business context**: Understand why you need this
❌ **Microservices for startup**: Monolith is faster initially
❌ **Technology-driven decisions**: Business requirements should drive architecture
❌ **Ignoring team capabilities**: Can your team operate this architecture?
❌ **No testing strategy**: Architecture must be testable
❌ **Ignoring consistency requirements**: Some systems need ACID, not eventual consistency
❌ **Premature optimization**: Profile first, optimize second
❌ **No monitoring**: Can't operate what you can't measure

---

This skill works best combined with:
- **diagram-mermaid** and **diagram-plantuml** for architecture diagrams
- **code-examples-generator** for implementation examples
- **java-content**, **python-content**, **javascript-content** for language-specific examples
- **sr-tech-blog** for long-form blog articles
- **medium-optimizer** or **dzone-article** for publication
- **seo-optimizer** for discovery of architecture content
