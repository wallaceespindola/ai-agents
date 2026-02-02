# AI Agents - Complete Reference

Complete listing of all 10 specialized AI agents and their 95 associated skills for the AI Agents system.

---

## 🎯 Quick Agent Selector

**Choose an agent based on your task:**

| Task | Agent | Example |
|------|-------|---------|
| Write articles, guides, documentation | Technical Writer | "Write a blog post about microservices" |
| Review Java code, Spring Boot setup | Java Developer | "Review my Spring Boot controller" |
| Review Python code, FastAPI setup | Python Developer | "Optimize my async Python function" |
| React/Next.js development, components | JavaScript Developer | "Design a reusable form component" |
| System design, architecture, patterns | Software Architect | "Design a scalable microservices architecture" |
| Test strategy, automation, QA | QA/Tester | "Create a test automation strategy" |
| CI/CD, containers, infrastructure | DevOps Engineer | "Set up Kubernetes deployment" |
| GitHub Actions, Git workflows, build systems | Git/GitHub Automation | "Create a GitHub Actions CI/CD pipeline" |
| Spring Cloud, Quarkus, build optimization | Spring/Quarkus Engineer | "Design a Spring Cloud microservices system" |
| Project planning, sprints, management | Project Manager | "Plan the next sprint with user stories" |

---

## 1️⃣ Technical Writer Agent

**Focus:** Content creation, documentation, multi-platform publishing

**Skills (22 total):**
- Java content, Python content, JavaScript content
- Dev.to, LinkedIn, Medium, Substack, DZone, JavaPro, InfoQ, Blog
- Java coder, Python coder, JavaScript coder
- Slides creator, Image generator, Diagram creator
- Markdown formatter, Code examples generator
- Architecture & patterns, SEO optimizer

**When to Use:**
- Writing technical articles and tutorials
- Creating project documentation
- Generating complete code examples
- Publishing to multiple platforms
- Creating presentations and slides

**Profile:** `agents/technical-writer/AGENT.md`

---

## 2️⃣ Java Developer Agent

**Focus:** Java/Spring Boot enterprise development, microservices

**Skills (12 total):**

*Core Java (6):*
- java-code-review - Code review with best practices
- java-testing-strategy - JUnit, Mockito, TestContainers
- java-performance-tuning - Profiling and optimization
- java-security-audit - OWASP, vulnerability scanning
- spring-boot-setup - Project generation
- java-documentation - JavaDoc and technical docs

*Spring Enterprise (2):*
- spring-boot-microservices - Spring Cloud services
- spring-boot-security-advanced - OAuth2, JWT, RBAC

*Shared Skills (4):*
- spring-boot-cloud-config - Distributed configuration
- spring-boot-reactive - WebFlux, Project Reactor
- maven-gradle-optimization - Build performance
- github-actions-workflows - CI/CD integration

**When to Use:**
- Reviewing Java/Spring code
- Designing microservices with Spring Cloud
- Implementing authentication/authorization
- Setting up Spring Boot projects
- Optimizing performance and security

**Profile:** `agents/java-developer/AGENT.md`

---

## 3️⃣ Python Developer Agent

**Focus:** Python/FastAPI backend, async programming, data processing

**Skills (6 total):**
- python-code-review - Pythonic patterns, PEP compliance
- python-testing-strategy - pytest, fixtures, mocking
- python-performance-tuning - Profiling, optimization
- python-type-checking - Type hints, mypy validation
- fastapi-setup - Project generation
- python-documentation - Docstrings, technical docs

**When to Use:**
- Reviewing Python code
- Setting up FastAPI projects
- Implementing async operations
- Adding type safety
- Optimizing performance

**Profile:** `agents/python-developer/AGENT.md`

---

## 4️⃣ JavaScript/Frontend Developer Agent

**Focus:** React/Next.js development, component architecture

**Skills (10 total):**

*Core (3):*
- javascript-code-review - Code quality, patterns
- typescript-migration - JS to TS conversion
- javascript-documentation - JSDoc, component docs

*React Components (3):*
- react-component-patterns - Design, composition
- react-hooks-advanced - Custom hooks, patterns
- react-state-management - Context, Redux, Zustand, TanStack Query

*Testing & Quality (2):*
- react-testing-strategy - Jest, React Testing Library
- frontend-performance - Bundle optimization, Core Web Vitals

*Project & Documentation (2):*
- nextjs-setup - Next.js project generation
- storybook-setup - Component documentation

**When to Use:**
- React/Next.js development
- Component design and patterns
- Custom hook creation
- State management implementation
- Performance optimization
- Component documentation

**Profile:** `agents/javascript-developer/AGENT.md`

---

## 5️⃣ Software Architect Agent

**Focus:** System design, architecture patterns, scalability

**Skills (7 total):**
- architecture-review - System critique and recommendations
- system-design-doc - Architecture documentation
- scalability-analysis - Capacity planning, bottleneck identification
- pattern-recommendation - Design patterns
- api-design - REST, GraphQL, gRPC APIs
- database-schema-design - Schema optimization
- architecture-diagram - C4, UML, sequence diagrams

**When to Use:**
- Designing new systems
- Reviewing existing architecture
- Planning microservices
- Optimizing scalability
- Selecting design patterns
- Creating architecture documentation

**Profile:** `agents/software-architect/AGENT.md`

---

## 6️⃣ QA/Software Tester Agent

**Focus:** Test automation, quality assurance, testing strategies

**Skills (7 total):**
- test-strategy-doc - Comprehensive test planning
- test-automation-setup - Framework configuration
- test-case-generator - Test case creation
- api-testing-setup - REST/GraphQL testing
- e2e-testing-setup - Selenium, Playwright, Cypress
- performance-testing - Load testing, metrics
- bug-report-generator - Detailed bug reporting

**When to Use:**
- Creating test strategies
- Setting up test automation
- Designing test cases
- API testing
- E2E testing
- Performance testing
- Quality assurance planning

**Profile:** `agents/qa-tester/AGENT.md`

---

## 7️⃣ DevOps Engineer Agent

**Focus:** CI/CD, containerization, infrastructure

**Skills (7 total):**
- cicd-pipeline-setup - GitHub Actions, GitLab CI, Jenkins
- docker-setup - Dockerfile, docker-compose
- kubernetes-setup - K8s manifests, Helm charts
- infrastructure-as-code - Terraform, CloudFormation
- monitoring-setup - Prometheus, Grafana, ELK
- security-scanning - SAST, DAST, dependency scanning
- deployment-strategy - Blue-green, canary, rolling

**When to Use:**
- Setting up CI/CD pipelines
- Containerizing applications
- Kubernetes deployment
- Infrastructure provisioning
- Monitoring and observability
- Security scanning
- Deployment planning

**Profile:** `agents/devops-engineer/AGENT.md`

---

## 8️⃣ Git/GitHub & Automation Engineer Agent

**Focus:** GitHub automation, CI/CD workflows, YAML configuration

**Skills (14 total):**

*Git & GitHub (6):*
- github-actions-workflows - Workflow design
- git-workflow-strategy - Git Flow, GitHub Flow, trunk-based
- github-pr-management - PR automation
- github-cli-automation - Scripting, batch operations
- github-security-scanning - Dependabot, CodeQL, secrets
- git-commit-strategy - Conventional commits, signing

*Config Management (5):*
- yaml-validation-config - YAML validation, linting
- kubernetes-yaml-generation - K8s manifests
- docker-compose-setup - Multi-container orchestration
- helm-charts-creation - Helm charts
- github-actions-yaml - Workflow YAML

*Build & Secrets (3):*
- build-optimization - Maven, Gradle, npm optimization
- ssh-key-management - SSH keys, certificates
- secrets-management - Vault, GitHub Secrets, AWS
- pre-commit-hooks-setup - Pre-commit framework

**When to Use:**
- Setting up GitHub Actions
- Planning Git branching strategies
- Automating GitHub operations
- Validating YAML configurations
- Generating Kubernetes manifests
- Optimizing builds
- Managing secrets

**Profile:** `agents/git-automation-engineer/AGENT.md`

---

## 9️⃣ Spring/Quarkus & Build Systems Engineer Agent

**Focus:** Spring Cloud enterprise, Quarkus cloud-native, build optimization

**Skills (10 total):**

*Spring Boot Enterprise (4):*
- spring-boot-microservices - Spring Cloud architecture
- spring-boot-security-advanced - OAuth2, OpenID Connect, JWT, RBAC
- spring-boot-cloud-config - Distributed configuration
- spring-boot-reactive - WebFlux, Project Reactor

*Quarkus & Native (3):*
- quarkus-framework - Quarkus setup, extensions
- quarkus-graalvm-native - GraalVM native compilation
- quarkus-extensions - Extension development

*Build Systems (2):*
- maven-gradle-optimization - Build performance
- build-cache-management - Caching strategies

*Shared Skills (1):*
- github-actions-workflows - CI/CD integration

**When to Use:**
- Spring Cloud microservices
- Advanced authentication/authorization
- Cloud-native applications with Quarkus
- Native image compilation
- Build optimization
- Distributed configuration

**Profile:** `agents/spring-quarkus-engineer/AGENT.md`

---

## 🔟 Project Manager Agent

**Focus:** Agile planning, sprint management, project coordination

**Skills (6 total):**
- project-plan-generator - Comprehensive project planning
- sprint-planning - Sprint planning with estimation
- risk-assessment - Risk identification and mitigation
- status-report-generator - Status reports, dashboards
- retrospective-facilitator - Sprint retrospectives
- roadmap-planner - Product roadmaps

**When to Use:**
- Planning new projects
- Sprint planning
- Risk assessment
- Status reporting
- Team retrospectives
- Roadmap planning

**Profile:** `agents/project-manager/AGENT.md`

---

## 📊 Skill Categories Summary

### Technical Writing (22 skills)
Content creation, documentation, multi-platform publishing

### Backend Development (28 skills)
- Java: 12 skills
- Python: 6 skills
- Spring/Quarkus: 10 skills

### Frontend Development (10 skills)
- JavaScript/React/Next.js: 10 skills

### Architecture & Design (7 skills)
- System design, patterns, scalability, APIs, databases

### Quality & Testing (7 skills)
- Test strategy, automation, performance testing

### Infrastructure & DevOps (14 skills)
- DevOps: 7 skills
- Git/GitHub Automation: 14 skills

### Project Management (6 skills)
- Planning, sprints, risk, roadmaps

---

## 🔄 Agent Collaboration Map

```
                    ┌─────────────────┐
                    │  Project Manager│
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
   ┌────▼──────┐      ┌─────▼──────┐      ┌─────▼──────┐
   │ Java Dev  │      │Python Dev  │      │ JS Dev     │
   └────┬──────┘      └─────┬──────┘      └─────┬──────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
   ┌────▼──────┐      ┌─────▼──────┐      ┌─────▼──────┐
   │ Architect │      │  QA/Tester │      │  DevOps    │
   └────┬──────┘      └────────────┘      └─────┬──────┘
        │                                        │
        │  ┌──────────────────────────────────┐ │
        └──┤ Git/GitHub & Automation Engineer ├─┘
           └──────────────────────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │                                 │
   ┌────▼──────────────────────┐  ┌──────▼────┐
   │Spring/Quarkus & Build     │  │Tech Writer│
   └───────────────────────────┘  └───────────┘
```

---

## 🎯 Common Workflows

### Workflow 1: Full-Stack Feature Development
```
Project Manager → Architect → (Java/Python/JS Devs) → QA/Tester →
DevOps → Git/GitHub → Tech Writer
```

### Workflow 2: Spring Cloud Microservices
```
Architect → Spring/Quarkus Engineer → Java Developer →
Git/GitHub Automation → DevOps → QA/Tester → Tech Writer
```

### Workflow 3: CI/CD Setup
```
Git/GitHub Engineer → DevOps Engineer → All Developers → QA/Tester
```

### Workflow 4: Cloud-Native Application
```
Spring/Quarkus Engineer → Git/GitHub Automation → DevOps →
QA/Tester → Project Manager
```

---

## 📚 Documentation

**Quick References:**
- All agents: `agents/{name}/AGENT.md`
- All skills: `skills/{name}/SKILL.md`
- Complete guide: `docs/AGENTS_GUIDE.md`
- System overview: `docs/guides/SYSTEM_MAP.md`
- Skills index: `docs/guides/SKILLS_INDEX.md`

---

## ✨ Total System

- **10 Agents** - Specialized roles
- **95 Skills** - Comprehensive capabilities
- **35,700+ lines** - Production-ready documentation
- **Real-world examples** - Every skill includes practical examples
- **Best practices** - Industry-standard guidance

---

**Last Updated:** 2026-02-02
**Total Skills:** 95
**Total Agents:** 10
