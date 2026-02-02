# Complete Agents Guide

Comprehensive guide to all 10 specialized agents in the AI Agents system, their capabilities, when to use them, and how they work together.

## Overview: 10 Agents, 95 Skills

The AI Agents system provides specialized agents for every major software engineering role:

| Agent | Role | Focus | Skills | Team Size |
|-------|------|-------|--------|-----------|
| Technical Writer | Content Creator | Writing, documentation, multi-platform publishing | 22 | Solo/Distributed |
| Java Developer | Backend Engineer | Java/Spring Boot, enterprise applications | 12 | Teams |
| Python Developer | Backend Engineer | Python/FastAPI, data processing, async | 6 | Teams |
| JavaScript Developer | Frontend Engineer | React/Next.js, web applications | 10 | Teams |
| Software Architect | System Designer | Architecture, scalability, design patterns | 7 | Leadership |
| QA/Tester | Quality Engineer | Test automation, test strategy, quality assurance | 7 | Teams |
| DevOps Engineer | Infrastructure | CI/CD, containerization, cloud operations | 7 | Teams |
| Project Manager | Technical Manager | Planning, sprint management, coordination | 6 | Leadership |
| Git/GitHub & Automation | DevOps/Automation | GitHub Actions, Git workflows, YAML config, build automation | 14 | DevOps/Teams |
| Spring/Quarkus & Build Systems | Backend Engineer | Spring Cloud, Quarkus, native builds, build optimization | 10 | Backend Teams |

---

## 1. Technical Writer Agent

**Description**: Senior technical software writer specializing in content creation, documentation, and multi-platform publishing.

### Expertise
- Technical content creation and optimization
- Multi-platform publishing (8 platforms)
- Code generation (Java, Python, JavaScript projects)
- Documentation and API reference
- Humanization standards and SEO optimization

### Associated Skills (22)
**Language Skills**: Java content, Python content, JavaScript content
**Platform Skills**: Dev.to, LinkedIn, Medium, Substack, DZone, JavaPro, InfoQ, Blog
**Generator Skills**: Java coder, Python coder, JavaScript coder
**Supporting Skills**: Slides creator, Image generator, Diagram creator, Markdown formatter, Code examples, Architecture & patterns, SEO optimizer

### When to Use
- Writing articles, tutorials, and guides
- Creating documentation for projects
- Generating complete code projects
- Publishing to multiple platforms
- Converting content between platforms
- Optimizing content for SEO
- Creating presentations from articles

### Example Workflows

**Workflow 1: Write and Multi-Platform Publish**
```
1. Use Technical Writer to create article
2. Use dev-to-formatter to adapt for Dev.to
3. Use linkedin-optimizer to adapt for LinkedIn
4. Use medium-optimizer to adapt for Medium
5. Publish to all three platforms
```

**Workflow 2: Generate Code Project**
```
1. Write article about Spring Boot patterns
2. Use java-coder skill to generate complete project
3. Project includes source, tests, README, pom.xml
4. Link article to code repository
5. Publish article with code
```

**Workflow 3: Create Presentation**
```
1. Write technical article
2. Use slides-creator to convert to slides
3. Download PowerPoint/Google Slides
4. Use for presentations or speaker deck
```

---

## 2. Java Developer Agent

**Description**: Senior Java/Spring Boot developer specializing in enterprise applications, microservices, and high-performance systems.

### Expertise
- Java 17+ language features
- Spring Boot 3.x framework
- Microservices architecture
- JPA/Hibernate and database optimization
- Testing (JUnit 5, Mockito, TestContainers)
- Performance optimization and profiling
- Security best practices

### Associated Skills (6)
- `java-code-review` - Review code for best practices
- `java-testing-strategy` - Design test strategies
- `java-performance-tuning` - Profile and optimize
- `java-security-audit` - Security vulnerability analysis
- `spring-boot-setup` - Generate project structures
- `java-documentation` - Create JavaDoc and technical docs

### When to Use
- Reviewing Java pull requests
- Designing test strategies for Java code
- Optimizing slow Java applications
- Auditing for security vulnerabilities
- Setting up new Spring Boot projects
- Creating comprehensive documentation
- Mentoring on Java best practices

### Example Workflows

**Workflow 1: Code Review & Improvement**
```
1. Use java-code-review on UserService.java
2. Identify 3 issues (N+1 query, memory leak, security)
3. Use java-performance-tuning to fix N+1 query
4. Use java-security-audit to fix security issues
5. Re-submit improved code
```

**Workflow 2: New Microservice Setup**
```
1. Use spring-boot-setup to generate project
2. Use java-code-review on generated code
3. Use java-testing-strategy to design tests
4. Use java-documentation to create API docs
5. Push to repository
```

**Workflow 3: Performance Optimization**
```
1. Use java-performance-tuning to profile application
2. Identify bottlenecks (database, GC, CPU)
3. Use java-code-review to review proposed fixes
4. Use java-testing-strategy to add performance tests
5. Deploy improvements
```

### Collaboration Points
- **With Software Architect**: Architecture review before implementation
- **With QA/Tester**: Test strategy and automation
- **With DevOps Engineer**: Containerization and deployment
- **With Technical Writer**: Documentation and code examples

---

## 3. Python Developer Agent

**Description**: Senior Python developer specializing in backend systems, async programming, and data processing.

### Expertise
- Python 3.10+ with type hints
- FastAPI and async/await patterns
- SQLAlchemy and ORM optimization
- Async database drivers (asyncpg, motor)
- Testing (pytest, fixtures, parametrization)
- Type checking with mypy
- Performance profiling

### Associated Skills (6)
- `python-code-review` - Review code for Pythonic patterns
- `python-testing-strategy` - Design test strategies
- `python-performance-tuning` - Profile and optimize
- `python-type-checking` - Add type hints and validate
- `fastapi-setup` - Generate project structures
- `python-documentation` - Create docstrings and docs

### When to Use
- Reviewing Python pull requests
- Designing test strategies for Python code
- Optimizing slow Python applications
- Adding type hints to existing code
- Setting up new FastAPI projects
- Creating comprehensive documentation
- Mentoring on Python best practices

### Example Workflows

**Workflow 1: Type Safety Improvement**
```
1. Use python-type-checking to analyze current types
2. Add missing type hints throughout codebase
3. Run mypy to validate all types
4. Use python-code-review to review changes
5. Commit improved, type-safe code
```

**Workflow 2: Async API Performance**
```
1. Use python-performance-tuning to identify bottleneck
2. Optimize database queries with proper async patterns
3. Use python-code-review to validate async/await
4. Use python-testing-strategy to add async tests
5. Benchmark improvements
```

**Workflow 3: New Data Service**
```
1. Use fastapi-setup to generate project
2. Use python-type-checking to add type hints
3. Use python-testing-strategy to design tests
4. Use python-documentation to create API docs
5. Deploy service
```

### Collaboration Points
- **With Software Architect**: Architecture for async patterns
- **With QA/Tester**: Test automation and integration tests
- **With DevOps Engineer**: Containerization and monitoring
- **With Technical Writer**: API documentation and guides

---

## 4. JavaScript/Frontend Developer Agent

**Description**: Senior frontend developer specializing in React, Next.js, and modern web applications.

### Expertise
- React 18+ with hooks
- Next.js 15+ with App Router
- TypeScript strict mode
- Component testing (Jest, React Testing Library)
- Accessibility (WCAG 2.1)
- Performance optimization (Core Web Vitals)
- State management patterns

### Associated Skills (10)

**Core Development**:
- `javascript-code-review` - Review JS/TS code
- `typescript-migration` - Convert JS to TS incrementally
- `javascript-documentation` - Create JSDoc and component docs

**React Component Development**:
- `react-component-patterns` - Design reusable components with composition patterns
- `react-hooks-advanced` - Master custom hooks and complex logic extraction
- `react-state-management` - Implement state management (Context, Redux, Zustand)

**Testing & Quality**:
- `react-testing-strategy` - Design test strategies
- `frontend-performance` - Optimize bundle and rendering

**Project & Documentation**:
- `nextjs-setup` - Generate project structures
- `storybook-setup` - Set up component library documentation with Storybook

### When to Use
- Reviewing React/TypeScript pull requests
- Designing test strategies for components
- Optimizing Core Web Vitals and performance
- Migrating JavaScript to TypeScript
- Setting up new Next.js projects
- Creating component documentation
- Mentoring on React patterns

### Example Workflows

**Workflow 1: TypeScript Migration**
```
1. Use typescript-migration to plan migration
2. Migrate components incrementally
3. Use javascript-code-review to review changes
4. Use react-testing-strategy to update tests
5. Deploy full TypeScript codebase
```

**Workflow 2: Performance Optimization**
```
1. Use frontend-performance to analyze bottlenecks
2. Fix bundle size, code splitting, image optimization
3. Use javascript-code-review to validate patterns
4. Use react-testing-strategy to add performance tests
5. Monitor Core Web Vitals improvement
```

**Workflow 3: New Application**
```
1. Use nextjs-setup to generate project
2. Use javascript-code-review on generated code
3. Use typescript-migration to ensure all TS
4. Use react-testing-strategy to design tests
5. Deploy application
```

### Collaboration Points
- **With Software Architect**: Application architecture and state management
- **With QA/Tester**: E2E testing and accessibility testing
- **With DevOps Engineer**: Build optimization and deployment
- **With Technical Writer**: Component documentation and guides

---

## 5. Software Architect Agent

**Description**: Senior software architect specializing in system design, scalability, and architectural patterns.

### Expertise
- System design and architecture patterns
- Microservices and service boundaries
- Scalability analysis and capacity planning
- Database architecture and optimization
- API design (REST, GraphQL, gRPC)
- Cloud architecture (AWS, Azure, GCP)
- Design patterns and trade-offs

### Associated Skills (7)
- `architecture-review` - Review and critique architecture
- `system-design-doc` - Create architecture documentation
- `scalability-analysis` - Analyze system scalability
- `pattern-recommendation` - Recommend design patterns
- `api-design` - Design APIs (REST, GraphQL)
- `database-schema-design` - Design optimal schemas
- `architecture-diagram` - Generate C4, UML, sequence diagrams

### When to Use
- Reviewing system architecture
- Designing new systems from scratch
- Planning system migrations
- Analyzing scalability concerns
- Selecting appropriate design patterns
- Designing database schemas
- Creating architecture documentation
- Making technology recommendations

### Example Workflows

**Workflow 1: Architecture Review**
```
1. Use architecture-review on current system
2. Identify 3-5 improvements
3. Use system-design-doc to document new design
4. Use scalability-analysis on new design
5. Present improvements to team
```

**Workflow 2: Microservice Design**
```
1. Use system-design-doc to plan microservices
2. Use api-design to design service APIs
3. Use database-schema-design for each service
4. Use architecture-diagram to visualize
5. Present to development team
```

**Workflow 3: Performance Scaling**
```
1. Use scalability-analysis on current system
2. Identify bottlenecks (database, cache, compute)
3. Use pattern-recommendation for solutions
4. Use system-design-doc for new architecture
5. Plan implementation with teams
```

### Collaboration Points
- **With All Developers**: Architecture guidance during implementation
- **With QA/Tester**: Test strategy for architectural components
- **With DevOps Engineer**: Infrastructure requirements
- **With Project Manager**: Timeline and complexity estimation

---

## 6. QA/Software Tester Agent

**Description**: Senior QA engineer specializing in test automation, quality assurance, and continuous testing.

### Expertise
- Test automation frameworks
- Test strategy and planning
- Unit, integration, API, and E2E testing
- Test case design and coverage
- Continuous testing in CI/CD
- Performance and load testing
- Accessibility testing

### Associated Skills (7)
- `test-strategy-doc` - Create test strategies
- `test-automation-setup` - Set up automation frameworks
- `test-case-generator` - Generate test cases
- `api-testing-setup` - Create API test suites
- `e2e-testing-setup` - Set up E2E testing
- `performance-testing` - Design performance tests
- `bug-report-generator` - Create detailed bug reports

### When to Use
- Designing test strategies for new features
- Setting up test automation frameworks
- Generating test cases from requirements
- Creating API test suites
- Setting up E2E testing
- Designing performance tests
- Creating detailed bug reports

### Example Workflows

**Workflow 1: Complete Test Strategy**
```
1. Use test-strategy-doc to plan testing approach
2. Use test-case-generator to create test cases
3. Use test-automation-setup to implement framework
4. Use api-testing-setup for API endpoints
5. Use e2e-testing-setup for critical flows
6. Integrate into CI/CD pipeline
```

**Workflow 2: Bug Analysis & Reporting**
```
1. Test application and find defect
2. Use bug-report-generator to create detailed report
3. Include reproduction steps, expected vs actual
4. Share with development team
5. Track fix and verify resolution
```

**Workflow 3: Performance Testing**
```
1. Use performance-testing to design load tests
2. Create test scenarios (100, 1000, 10000 users)
3. Run tests and collect metrics
4. Identify bottlenecks
5. Report findings to architecture team
```

### Collaboration Points
- **With All Developers**: Test implementation feedback
- **With Software Architect**: Test strategy for architecture
- **With DevOps Engineer**: CI/CD test automation
- **With Project Manager**: Test timeline and coverage goals

---

## 7. DevOps Engineer Agent

**Description**: Senior DevOps engineer specializing in CI/CD, containerization, and infrastructure-as-code.

### Expertise
- CI/CD pipeline design and implementation
- Docker containerization
- Kubernetes orchestration
- Infrastructure-as-Code (Terraform, CloudFormation)
- Cloud architecture (AWS, Azure, GCP)
- Monitoring and observability
- Security scanning and compliance

### Associated Skills (7)
- `cicd-pipeline-setup` - Create CI/CD pipelines
- `docker-setup` - Create Dockerfile and docker-compose
- `kubernetes-setup` - Create Kubernetes manifests
- `infrastructure-as-code` - Create IaC templates
- `monitoring-setup` - Set up monitoring and alerting
- `security-scanning` - Integrate security scanning
- `deployment-strategy` - Design deployment strategies

### When to Use
- Setting up CI/CD pipelines
- Containerizing applications
- Setting up Kubernetes clusters
- Creating infrastructure templates
- Setting up monitoring and alerting
- Integrating security scanning
- Planning deployment strategies

### Example Workflows

**Workflow 1: Complete CI/CD Pipeline**
```
1. Use cicd-pipeline-setup to design pipeline
2. Use docker-setup to create Dockerfile
3. Use security-scanning to add SAST/dependency checks
4. Use test automation integration
5. Use deployment-strategy for production rollout
6. Use monitoring-setup for observability
```

**Workflow 2: Kubernetes Deployment**
```
1. Use docker-setup to containerize application
2. Use kubernetes-setup to create manifests
3. Use monitoring-setup for Prometheus/Grafana
4. Use security-scanning for container security
5. Deploy to Kubernetes cluster
```

**Workflow 3: Infrastructure Scaling**
```
1. Use infrastructure-as-code for base setup
2. Use kubernetes-setup for auto-scaling
3. Use monitoring-setup for metrics
4. Use deployment-strategy for rolling updates
5. Scale to production workload
```

### Collaboration Points
- **With All Developers**: Container requirements, deployment process
- **With QA/Tester**: Test automation in CI/CD pipeline
- **With Software Architect**: Infrastructure requirements
- **With Project Manager**: Deployment timeline

---

## 8. Project Manager Agent

**Description**: Senior technical project manager specializing in Agile planning, estimation, and coordination.

### Expertise
- Agile and Scrum methodologies
- Project and sprint planning
- Team estimation and velocity
- Risk identification and management
- Stakeholder communication
- Roadmap planning
- Metrics and reporting

### Associated Skills (6)
- `project-plan-generator` - Create project plans
- `sprint-planning` - Plan sprints with stories
- `risk-assessment` - Identify and assess risks
- `status-report-generator` - Create status reports
- `retrospective-facilitator` - Facilitate retrospectives
- `roadmap-planner` - Create product roadmaps

### When to Use
- Planning new projects
- Planning sprints
- Assessing project risks
- Creating status reports
- Facilitating team retrospectives
- Planning product roadmaps
- Communicating with stakeholders

### Example Workflows

**Workflow 1: New Project Setup**
```
1. Use project-plan-generator to create plan
2. Use roadmap-planner to create product roadmap
3. Use sprint-planning for first sprint
4. Use risk-assessment to identify risks
5. Kickoff with team
```

**Workflow 2: Sprint Execution**
```
1. Use sprint-planning to plan sprint
2. Coordinate with technical teams
3. Use status-report-generator to track progress
4. Use risk-assessment if blockers appear
5. Use retrospective-facilitator to close sprint
```

**Workflow 3: Risk Management**
```
1. Use risk-assessment to identify risks
2. Plan mitigation strategies
3. Use sprint-planning to allocate resources
4. Monitor risk status in sprints
5. Use status-report-generator to report risks
```

### Collaboration Points
- **With All Technical Agents**: Planning and estimation
- **With Software Architect**: Complexity and timeline estimation
- **With Stakeholders**: Communication and reporting

---

## Agent Collaboration Matrix

### Who Works With Whom

| Agent | Works With | For | Frequency |
|-------|-----------|-----|-----------|
| Technical Writer | All agents | Documentation, guides, content | Continuous |
| Java Developer | Architect, QA, DevOps, Spring/Quarkus, Git/GitHub, Writer | Implementation, testing, deployment | Daily |
| Python Developer | Architect, QA, DevOps, Writer | Implementation, testing, deployment | Daily |
| JavaScript Developer | Architect, QA, DevOps, Writer | Implementation, testing, deployment | Daily |
| Software Architect | All developers, DevOps, PM | Design, review, guidance | Weekly |
| QA/Tester | All developers, DevOps, Git/GitHub | Testing, automation, quality | Daily |
| DevOps Engineer | All developers, Architect, Git/GitHub, Spring/Quarkus | Deployment, infrastructure, monitoring | Daily |
| Project Manager | All agents | Planning, coordination, reporting | Daily |
| Git/GitHub & Automation | All developers, DevOps, Architect | CI/CD, automation, Git workflows | Daily |
| Spring/Quarkus & Build | Java Developer, DevOps, Git/GitHub, Architect | Microservices, native builds, optimization | Daily |

---

## Common Multi-Agent Workflows

### Workflow 1: Full-Stack Feature Development

**Timeline**: 2-4 weeks

```
Week 1:
├─ Project Manager: Break down feature into stories
├─ Software Architect: Design feature architecture
└─ All Developers: Review design, ask questions

Week 2:
├─ Java/Python/JS Developers: Implement per architecture
├─ QA/Tester: Design test strategy
└─ DevOps Engineer: Prepare deployment pipeline

Week 3:
├─ QA/Tester: Execute test suite
├─ Java/Python/JS Developers: Fix bugs
└─ DevOps Engineer: Test deployment

Week 4:
├─ DevOps Engineer: Deploy to production
├─ Project Manager: Release communication
└─ Technical Writer: Document feature
```

### Workflow 2: System Architecture Review & Redesign

**Timeline**: 3-8 weeks

```
Week 1:
├─ Software Architect: Review current architecture
├─ Project Manager: Assess impact and timeline
└─ DevOps Engineer: Infrastructure assessment

Week 2-4:
├─ Software Architect: Design new architecture
├─ All Developers: Deep-dive on implementation
└─ QA/Tester: Plan testing for redesign

Week 5-6:
├─ All Developers: Implement new architecture
├─ QA/Tester: Regression testing
└─ DevOps Engineer: Infrastructure changes

Week 7-8:
├─ DevOps Engineer: Deploy to production
├─ QA/Tester: Verify in production
└─ Technical Writer: Document new architecture
```

### Workflow 3: Performance Optimization Sprint

**Timeline**: 1-3 weeks

```
Week 1:
├─ Software Architect: Scalability analysis
├─ All Developers: Profiling and identification
└─ QA/Tester: Performance test suite

Week 2:
├─ All Developers: Implement optimizations
├─ QA/Tester: Verify improvements
└─ DevOps Engineer: Infrastructure optimization

Week 3:
├─ DevOps Engineer: Deploy optimizations
├─ QA/Tester: Production monitoring
└─ Technical Writer: Document improvements
```

---

## Choosing the Right Agent

### For Code Development
- **Java**: Use Java Developer Agent
- **Python**: Use Python Developer Agent
- **JavaScript/React/Next.js**: Use JavaScript Developer Agent

### For Code Quality
- **Any language**: Use QA/Tester Agent for test strategy
- **Testing framework**: Use QA/Tester Agent

### For System Design
- **New architecture**: Use Software Architect Agent
- **Scalability**: Use Software Architect Agent
- **Database design**: Use Software Architect Agent
- **API design**: Use Software Architect Agent

### For Infrastructure
- **CI/CD pipelines**: Use DevOps Engineer Agent
- **Docker/Kubernetes**: Use DevOps Engineer Agent
- **Monitoring**: Use DevOps Engineer Agent
- **Deployment**: Use DevOps Engineer Agent

### For Project Coordination
- **Planning**: Use Project Manager Agent
- **Sprint management**: Use Project Manager Agent
- **Risk assessment**: Use Project Manager Agent
- **Status reporting**: Use Project Manager Agent

### For Content & Documentation
- **Articles and guides**: Use Technical Writer Agent
- **Code generation**: Use Technical Writer Agent
- **Documentation**: Use Technical Writer Agent or language-specific agent

---

## Skill Cross-Reference

### Quick Skill Lookup

#### Code Review
- `java-code-review` → Java Developer
- `python-code-review` → Python Developer
- `javascript-code-review` → JavaScript Developer
- `architecture-review` → Software Architect

#### Testing
- `java-testing-strategy` → Java Developer
- `python-testing-strategy` → Python Developer
- `react-testing-strategy` → JavaScript Developer
- `test-strategy-doc` → QA/Tester
- `test-automation-setup` → QA/Tester
- `test-case-generator` → QA/Tester
- `api-testing-setup` → QA/Tester
- `e2e-testing-setup` → QA/Tester

#### Performance & Optimization
- `java-performance-tuning` → Java Developer
- `python-performance-tuning` → Python Developer
- `frontend-performance` → JavaScript Developer
- `scalability-analysis` → Software Architect
- `performance-testing` → QA/Tester

#### Setup & Generation
- `spring-boot-setup` → Java Developer
- `fastapi-setup` → Python Developer
- `nextjs-setup` → JavaScript Developer
- `docker-setup` → DevOps Engineer
- `kubernetes-setup` → DevOps Engineer
- `infrastructure-as-code` → DevOps Engineer
- `cicd-pipeline-setup` → DevOps Engineer

#### Architecture & Design
- `architecture-review` → Software Architect
- `system-design-doc` → Software Architect
- `api-design` → Software Architect
- `database-schema-design` → Software Architect
- `architecture-diagram` → Software Architect
- `pattern-recommendation` → Software Architect

#### Security
- `java-security-audit` → Java Developer
- `security-scanning` → DevOps Engineer

#### Documentation
- `java-documentation` → Java Developer
- `python-documentation` → Python Developer
- `javascript-documentation` → JavaScript Developer

#### Project Management
- `project-plan-generator` → Project Manager
- `sprint-planning` → Project Manager
- `risk-assessment` → Project Manager
- `status-report-generator` → Project Manager
- `retrospective-facilitator` → Project Manager
- `roadmap-planner` → Project Manager

#### Technical Writing
- All 22 Technical Writer skills → Technical Writer Agent

---

## 9. Git/GitHub & Automation Engineer Agent

**Description**: Senior Git and GitHub automation specialist with expertise in CI/CD workflows, DevOps automation, YAML configuration, and build systems optimization.

### Expertise
- GitHub Actions workflows and CI/CD automation
- Git workflows (Git Flow, GitHub Flow, trunk-based development)
- GitHub API and CLI automation
- YAML configuration (Kubernetes, Docker, Helm, GitHub Actions)
- Build optimization (Maven, Gradle, npm/yarn)
- Secrets management and SSH security
- Pre-commit hooks and Git integrations
- GitHub security scanning (Dependabot, CodeQL, SAST)

### Associated Skills (14)

**Git & GitHub (6)**:
- `github-actions-workflows` - Design GitHub Actions CI/CD workflows
- `git-workflow-strategy` - Plan Git workflows and branching strategies
- `github-pr-management` - Automate PR workflows and code reviews
- `github-cli-automation` - Automate GitHub operations via CLI
- `github-security-scanning` - Setup Dependabot, CodeQL, secret scanning
- `git-commit-strategy` - Implement conventional commits and signing

**Config Management (5)**:
- `yaml-validation-config` - Validate and optimize YAML configurations
- `kubernetes-yaml-generation` - Generate K8s manifests and configs
- `docker-compose-setup` - Configure Docker Compose for local development
- `helm-charts-creation` - Create and manage Helm charts
- `github-actions-yaml` - Write complex GitHub Actions YAML workflows

**Build & Secrets (3)**:
- `build-optimization` - Optimize Maven, Gradle, npm builds
- `ssh-key-management` - Manage SSH keys and certificates securely
- `secrets-management` - Implement secure secrets management
- `pre-commit-hooks-setup` - Configure pre-commit hooks and automation

### When to Use
- Designing GitHub Actions CI/CD workflows
- Planning Git branching strategies
- Automating GitHub operations at scale
- Validating and generating YAML configurations
- Optimizing build times and caching
- Managing secrets and SSH keys securely
- Setting up pre-commit hooks for code quality

### Example Workflows

**Workflow 1: Complete CI/CD Setup**
```
1. Use git-workflow-strategy to plan branching
2. Use github-actions-workflows to create build pipeline
3. Use github-security-scanning to add security checks
4. Use pre-commit-hooks-setup for local checks
5. Use secrets-management for secure config
6. Deploy to production
```

**Workflow 2: Kubernetes Deployment**
```
1. Use yaml-validation-config to validate configs
2. Use kubernetes-yaml-generation to create manifests
3. Use helm-charts-creation for package management
4. Use github-actions-workflows to automate deployment
5. Use docker-compose-setup for local testing
```

### Collaboration Points
- **With DevOps Engineer**: Infrastructure and deployment
- **With All Developers**: CI/CD integration and automation
- **With Software Architect**: Build architecture and optimization
- **With Project Manager**: Automation timeline planning

---

## 10. Spring/Quarkus & Build Systems Engineer Agent

**Description**: Senior engineer specializing in Spring Boot enterprise frameworks, Quarkus cloud-native development, and build system optimization.

### Expertise
- Spring Boot 3.x enterprise frameworks
- Spring Cloud microservices ecosystem
- Advanced Spring Security and OAuth2/OpenID Connect
- Spring WebFlux and reactive programming
- Quarkus cloud-native framework
- GraalVM native image compilation
- Maven and Gradle build optimization
- Build caching and performance tuning

### Associated Skills (10)

**Spring Boot Enterprise (4)**:
- `spring-boot-microservices` - Design Spring Cloud microservices
- `spring-boot-security-advanced` - Implement OAuth2, JWT, OpenID Connect, RBAC
- `spring-boot-cloud-config` - Distributed configuration management
- `spring-boot-reactive` - Build reactive applications with WebFlux

**Quarkus & Native (3)**:
- `quarkus-framework` - Set up Quarkus applications and extensions
- `quarkus-graalvm-native` - Compile to native images with GraalVM
- `quarkus-extensions` - Manage and develop Quarkus extensions

**Build Systems (2)**:
- `maven-gradle-optimization` - Optimize Maven and Gradle builds
- `build-cache-management` - Implement build caching strategies

### When to Use
- Building microservices with Spring Cloud
- Implementing advanced authentication and authorization
- Creating reactive applications with Reactor/WebFlux
- Building cloud-native Quarkus applications
- Optimizing build times and resource usage
- Compiling applications to native images
- Implementing distributed configuration

### Example Workflows

**Workflow 1: Microservices Architecture**
```
1. Use spring-boot-microservices to design services
2. Use spring-boot-security-advanced for service auth
3. Use spring-boot-cloud-config for distributed config
4. Use maven-gradle-optimization for builds
5. Integrate with DevOps for deployment
```

**Workflow 2: Quarkus Native Application**
```
1. Use quarkus-framework to set up project
2. Use quarkus-extensions to add capabilities
3. Use quarkus-graalvm-native to compile
4. Use build-cache-management to optimize
5. Deploy as container or serverless
```

**Workflow 3: Reactive System**
```
1. Use spring-boot-reactive for WebFlux setup
2. Use spring-boot-microservices for service communication
3. Use spring-boot-cloud-config for configuration
4. Use build-optimization for performance
5. Test under load and optimize further
```

### Collaboration Points
- **With Java Developer Agent**: Implementation guidance and patterns
- **With DevOps Engineer**: Containerization and deployment
- **With Git/GitHub Automation**: CI/CD integration
- **With Software Architect**: System design and patterns

---

## Getting Started

1. **Identify your task**: What do you need to do?
2. **Choose the right agent**: Use the matrix above
3. **Select a skill**: Each agent has specialized skills
4. **Use the skill**: Provide clear task description
5. **Review results**: Refine if needed

### Example Scenarios

**"I need to review my Python code"**
→ Use Python Developer Agent → java-code-review skill

**"I need to set up a CI/CD pipeline"**
→ Use DevOps Engineer Agent → cicd-pipeline-setup skill

**"I need to design a new API"**
→ Use Software Architect Agent → api-design skill

**"I need to plan the next sprint"**
→ Use Project Manager Agent → sprint-planning skill

**"I need to write documentation"**
→ Use Technical Writer Agent → appropriate skill based on content type

---

## Notes

- Agents are independent but collaborative
- Multiple agents can work on the same task
- Project Manager coordinates team efforts
- Software Architect reviews technical decisions
- Technical Writer documents everything
- DevOps Engineer enables deployment

For detailed skill descriptions, see [Skills Index](guides/SKILLS_INDEX.md).
For system architecture, see [System Architecture](guides/SYSTEM_MAP.md).
