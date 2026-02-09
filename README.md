# AI Agents & Skills for Software Engineering

A comprehensive system of specialized AI agents for software engineering, system architecture, infrastructure automation, and project management.

**10 Agents + 95 Skills = Complete software engineering ecosystem**

With comprehensive React/Next.js support, GitHub automation, Spring Cloud microservices, and Quarkus development.

## ⚡ Quick Start (2 Minutes)

```bash
# 1. Set up your configuration
cp .env.example .env
nano .env  # Add your Anthropic API key

# 2. Choose an agent and skill based on your task
# Examples:
#   - Java Developer + spring-boot-setup → Generate Spring Boot microservice
#   - Python Developer + fastapi-setup → Generate FastAPI backend
#   - Architect + architecture-review → Design system architecture
#   - DevOps + github-actions-workflow → Set up CI/CD pipeline

# 3. Request what you need from the agent
# The agent uses skills to complete your task
```

**→ [Full Getting Started Guide](docs/GETTING_STARTED.md)**

---

## What's Included

### 10 Specialized Agents

#### **Technical Writer Agent**

- Expertise: Technical documentation, code documentation, multi-platform content publishing
- Skills: 22 skills for documentation generation, code examples, platform-specific formatting

#### **Java Developer Agent**

- Expertise: Java 17+, Spring Boot, microservices
- Skills: Code review, testing strategy, performance tuning, security audit, project setup, Spring Cloud, advanced
  security, documentation (12 skills total)

#### **Python Developer Agent**

- Expertise: Python 3.12+, FastAPI, async programming
- Skills: Code review, testing strategy, performance tuning, type checking, project setup, documentation (6 skills)

#### **JavaScript/Frontend Developer Agent**

- Expertise: React 18+, Next.js 15+, TypeScript, modern web applications
- Skills: Code review, component patterns, advanced hooks, state management, testing strategy, performance optimization,
  TypeScript migration, Storybook setup, project setup, documentation (10 skills total)

#### **Software Architect Agent**

- Expertise: System design, scalability, microservices architecture
- Skills: Architecture review, system design documentation, scalability analysis, design patterns, API design, database
  design, architecture diagrams (7 skills)

#### **QA/Software Tester Agent**

- Expertise: Test automation, quality assurance, continuous testing
- Skills: Test strategy, test automation setup, test case generation, API testing, E2E testing, performance testing, bug
  reporting (7 skills)

#### **DevOps Engineer Agent**

- Expertise: CI/CD, containerization, infrastructure-as-code, cloud operations
- Skills: CI/CD pipeline setup, Docker configuration, Kubernetes setup, IaC templates, monitoring setup, security
  scanning, deployment strategies (7 skills)

#### **Git/GitHub Automation Engineer Agent**

- Expertise: GitHub Actions, Git workflows, build automation, YAML configuration
- Skills: GitHub Actions workflows, Git workflow strategies, PR management, CLI automation, security scanning, commit
  strategies, YAML validation, Kubernetes manifests, Helm charts, Docker Compose, build optimization, SSH management,
  secrets management, pre-commit hooks (14 skills)

#### **Spring/Quarkus & Build Systems Engineer Agent**

- Expertise: Spring Cloud enterprise, Quarkus cloud-native, build optimization
- Skills: Spring Cloud microservices, OAuth2/JWT security, distributed config, reactive patterns, Quarkus framework,
  GraalVM native compilation, Quarkus extensions, Maven/Gradle optimization, build caching (10 skills)

#### **Project Manager Agent**

- Expertise: Agile methodologies, planning, risk management, stakeholder communication
- Skills: Project planning, sprint planning, risk assessment, status reporting, retrospectives, roadmap planning (6
  skills)

### 95 Specialized Skills

**Technical Writing (22 skills)** - Content creation, platform optimization, code generation, diagrams, SEO

**Java Development (12 skills)** - Code review, testing, performance, security, Spring Boot setup, Spring Cloud
microservices, advanced security, documentation

**Python Development (6 skills)** - Code review, testing, performance, type checking, project setup, documentation

**JavaScript/Frontend (10 skills)** - Code review, component patterns, advanced hooks, state management, testing,
performance optimization, TypeScript migration, Storybook setup, project setup, documentation

**Software Architecture (7 skills)** - System review, design documentation, scalability, patterns, API design, database
design, diagrams

**QA & Testing (7 skills)** - Test strategy, automation setup, test case generation, API testing, E2E testing,
performance testing, bug reporting

**DevOps & Infrastructure (7 skills)** - CI/CD pipelines, Docker, Kubernetes, IaC, monitoring, security scanning,
deployment strategies

**Project Management (6 skills)** - Project planning, sprint planning, risk assessment, status reports, retrospectives,
roadmap planning

**Git/GitHub & Automation (14 skills)** - GitHub Actions workflows, Git workflows, PR management, CLI automation,
security scanning, YAML config, Kubernetes manifests, Helm charts, Docker Compose, build optimization, SSH management,
secrets management, pre-commit hooks

**Spring/Quarkus & Build Systems (10 skills)** - Spring Cloud microservices, advanced security, cloud config, reactive
programming, Quarkus framework, GraalVM native compilation, Quarkus extensions, Maven/Gradle optimization, build caching

---

## 📊 System Capabilities

### Software Engineering Coverage

- **Code Development**: Java, Python, JavaScript with specialized expertise
- **Quality Assurance**: Comprehensive testing from unit tests to E2E automation
- **Architecture**: System design, scalability analysis, design patterns
- **Infrastructure**: CI/CD pipelines, containerization, Kubernetes, infrastructure-as-code
- **Project Management**: Agile planning, sprint management, risk assessment, roadmaps
- **Technical Writing**: Multi-platform content creation, documentation, code generation

### Agent Collaboration Workflows

```
Full-Stack Feature Development:
Project Manager → Architect → Java/Python/JS Developers →
QA/Tester → DevOps Engineer → Technical Writer

System Redesign:
Architect → Project Manager → All Developers → QA/Tester →
DevOps Engineer → Technical Writer

Performance Optimization:
Architect → Developers → DevOps Engineer → QA/Tester →
Technical Writer
```

### Multi-Language Project Generation

- **Java**: Maven/Spring Boot with tests, documentation, Dockerfile
- **Python**: Poetry/FastAPI with tests, type hints, Dockerfile
- **JavaScript**: npm/React with TypeScript, Jest, Dockerfile

---

## 🔒 Secure Configuration

Your personal data stays private and local:

```bash
cp .env.example .env          # Create local config (never committed)
# Edit with your details
AUTHOR_NAME=Your Name
GITHUB_URL=https://github.com/you
LINKEDIN_URL=https://linkedin.com/in/you
# ... and 40+ other variables
```

**Your `.env` file**:

- ✅ Never committed to git (.gitignore protection)
- ✅ Contains all your personal URLs and emails
- ✅ Automatically used by all skills
- ✅ Pre-filled with your discovered profiles

---

## 📚 Documentation

**Start Here**:

- **[Getting Started Guide](docs/GETTING_STARTED.md)** ← Begin here
- **[Configuration Guide](docs/CONFIGURATION.md)** - Set up `.env` with API keys
- **[Quick Agent Selector](AGENTS.md)** - Find the right agent for your task

**Comprehensive Guides**:

- **[AGENTS_GUIDE.md](docs/AGENTS_GUIDE.md)** - Complete agent guide with collaboration patterns
- **[System Architecture](docs/guides/SYSTEM_MAP.md)** - Agent relationships and data flows
- **[Skills Index](docs/guides/SKILLS_INDEX.md)** - All 95 skills described with examples

**Reference**:

- **[AGENTS.md](AGENTS.md)** - Quick reference for all 10 agents and 95 skills
- **[Project Specifications](docs/guides/PROJECT_SPECIFICATIONS.md)** - Java and Python templates
- **[Complete System Overview](docs/guides/COMPLETE_SYSTEM.md)** - Full system documentation
- **[.copilot-instructions](.copilot-instructions)** - GitHub Copilot context for the system

---

## 🚀 Common Workflows

### Workflow 1: Build a Java Microservice

```
1. Use Java Developer Agent with spring-boot-setup skill
2. Request: "Generate Spring Boot microservice with [requirements]"
3. Get complete Maven project with:
   - Spring Boot 3.x with Actuator (health, metrics, info endpoints)
   - Spring Data JPA + H2 (dev) / PostgreSQL (prod)
   - Kafka integration for async events
   - Swagger UI + OpenAPI documentation
   - >80% unit test coverage with JUnit 5 & Mockito
   - GitHub Actions CI/CD workflows
   - Docker multi-stage build + docker-compose.yml
   - Comprehensive README with setup instructions
4. Production-ready structure following Spring Boot best practices
```

### Workflow 2: Set Up a Python FastAPI Project

```
1. Use Python Developer Agent with fastapi-setup skill
2. Request: "Generate FastAPI project with [requirements]"
3. Get complete project with:
   - FastAPI with async SQLAlchemy 2.x + aiokafka
   - Health, metrics (Prometheus), and info endpoints
   - Pydantic v2 models with validation
   - Structured JSON logging with request tracing
   - >80% test coverage with pytest & pytest-asyncio
   - GitHub Actions with Black, Ruff, mypy, pytest
   - Docker multi-stage build + docker-compose.yml
   - Comprehensive README with API documentation
4. Ready for async, high-performance backends
```

### Workflow 3: Design System Architecture

```
1. Use Software Architect Agent with architecture-review skill
2. Request: "Review and improve architecture for [system description]"
3. Get:
   - Architecture analysis and design recommendations
   - Scalability analysis with capacity planning
   - Design patterns recommendations (e.g., SAGA, CQRS, Event Sourcing)
   - API design review (REST, GraphQL, gRPC)
   - Database schema design with optimization tips
   - C4/UML architecture diagrams with Mermaid/PlantUML
   - Deployment strategy recommendations
4. Collaborate with DevOps Engineer for infrastructure implementation
```

### Workflow 4: Set Up CI/CD & Infrastructure

```
1. Use DevOps Engineer Agent + Git/GitHub Automation Agent
2. Request: "Set up CI/CD pipeline for [project type]"
3. Get:
   - GitHub Actions workflows (build, test, lint, security scanning)
   - Docker & Docker Compose configurations
   - Kubernetes manifests & Helm charts (if needed)
   - Infrastructure-as-Code templates (Terraform, CloudFormation)
   - Security scanning (CodeQL, OWASP Dependency-Check)
   - Monitoring setup (Prometheus, Grafana)
4. Fully automated pipeline from commit to production
```

### Workflow 5: Full-Stack Feature Development

```
1. Project Manager Agent: Plan feature + user stories
2. Architect Agent: Design system changes
3. Java/Python/JavaScript Developers: Implement features
4. QA/Tester Agent: Design test strategy & automate tests
5. DevOps Engineer: Deploy to staging/production
6. Technical Writer Agent: Document feature (if user-facing)
7. All agents iterate based on feedback
```

---

## ✨ Key Features

**🎯 10 Specialized Agents**

- Each agent is a Claude-powered expert in their domain
- Agents collaborate seamlessly for complex workflows
- Consistent coding standards and best practices
- Full stack coverage from architecture to deployment

**🔐 Secure & Private**

- API keys in `.env` (local, never committed)
- `.env.example` safe to share (template only)
- All configuration environment-based
- Team-friendly (each person has own `.env`)

**📦 95 Integrated Skills**

- Each skill is a focused, reusable capability
- Skills work independently or in combination
- Clear documentation for each skill
- Covering all aspects of software engineering

**💻 Production-Ready Code**

- Generate complete, runnable projects
- >80% test coverage included
- GitHub Actions CI/CD workflows
- Docker containerization + orchestration
- Following industry best practices

**🎨 Architecture & Documentation**

- System design and architecture diagrams (Mermaid, PlantUML)
- OpenAPI/Swagger for all APIs
- Comprehensive README and documentation
- Database schema design and optimization
- Clear code comments and JavaDoc

**🚀 Multi-Language Support**

- Java 21+ with Spring Boot & Spring Cloud
- Python 3.12+ with FastAPI & async patterns
- JavaScript/TypeScript with React & Next.js
- Unified project structure across languages

---

---

## Project Structure

```
.
├── README.md                              ← You are here
├── CLAUDE.md                              ← Claude Code configuration
├── .env.example                           ← Configuration template
├── .env                                   ← Your personal data (not committed)
├── LICENSE
├── .gitignore
│
├── agents/
│   ├── technical-writer/AGENT.md          ← Writing expertise
│   ├── java-developer/AGENT.md            ← Java/Spring Boot development
│   ├── python-developer/AGENT.md          ← Python/FastAPI development
│   ├── javascript-developer/AGENT.md      ← React/Next.js development
│   ├── software-architect/AGENT.md        ← System design & architecture
│   ├── qa-tester/AGENT.md                 ← Test automation & QA
│   ├── devops-engineer/AGENT.md           ← CI/CD & infrastructure
│   ├── git-automation-engineer/AGENT.md   ← GitHub Actions & Git automation
│   ├── spring-quarkus-engineer/AGENT.md   ← Spring Cloud & Quarkus development
│   └── project-manager/AGENT.md           ← Agile planning & management
│
├── skills/
│   ├── java-*/                            ← 6 Java development skills
│   ├── python-*/                          ← 6 Python development skills
│   ├── javascript-*/                      ← 6 JavaScript development skills
│   ├── react-*/                           ← 4 React component skills
│   ├── architecture-*/                    ← 7 Architecture & design skills
│   ├── test-*/                            ← 7 QA & testing skills
│   ├── cicd-*, docker-*, kubernetes-*     ← 7 DevOps & infrastructure skills
│   ├── github-*, git-*, yaml-*, build-*   ← 14 Git/GitHub automation skills
│   ├── spring-*, quarkus-*, maven-*       ← 10 Spring/Quarkus & build skills
│   ├── project-*/                         ← 6 Project management skills
│   ├── ...                                ← 22 Technical writing skills
│   └── */SKILL.md                         ← 95 total skills
│
└── docs/
    ├── GETTING_STARTED.md                 ← START HERE
    ├── CONFIGURATION.md                   ← Setup guide
    ├── AGENTS_GUIDE.md                    ← Complete agent guide with workflows
    │
    └── guides/
        ├── COMPLETE_SYSTEM.md             ← Full system documentation
        ├── SYSTEM_MAP.md                  ← Architecture & relationships
        ├── SKILLS_INDEX.md                ← All 95 skills reference
        └── PROJECT_SPECIFICATIONS.md      ← Java & Python project templates
```

---

## Getting Help

1. **New to the system?** → [Getting Started Guide](docs/GETTING_STARTED.md)
2. **Which agent for my task?** → [Quick Agent Selector](AGENTS.md#-quick-agent-selector)
3. **Need to configure API keys?** → [Configuration Guide](docs/CONFIGURATION.md)
4. **Need agent details?** → [AGENTS.md](AGENTS.md) or [AGENTS_GUIDE.md](docs/AGENTS_GUIDE.md)
5. **Looking for a specific skill?** → [Skills Index](docs/guides/SKILLS_INDEX.md)
6. **Curious about system architecture?** → [System Architecture](docs/guides/SYSTEM_MAP.md)
7. **Need project templates?** → [Project Specifications](docs/guides/PROJECT_SPECIFICATIONS.md)

---

## Key Points

✅ **10 Agents + 95 Skills** - Complete software engineering ecosystem

✅ **Full-Stack Development** - Java, Python, JavaScript (with React/Next.js focus)

✅ **Git/GitHub Automation** - GitHub Actions workflows, git strategies, YAML config, CI/CD automation

✅ **Spring Cloud & Quarkus** - Microservices, advanced security, reactive programming, native compilation

✅ **React & Next.js Focused** - Component patterns, hooks, state management, Storybook, testing

✅ **Quality & Testing** - Comprehensive QA and test automation

✅ **Infrastructure & DevOps** - CI/CD, containerization, Kubernetes, monitoring

✅ **System Architecture** - Design patterns, scalability, API design

✅ **Project Management** - Agile planning, sprint management, roadmaps

✅ **Technical Writing** - Multi-platform publishing, code generation, documentation

✅ **Agent Collaboration** - 10 specialized agents work together on complex workflows

---

## Next Steps

1. Read **[Getting Started Guide](docs/GETTING_STARTED.md)**
2. View **[AGENTS.md](AGENTS.md)** for quick agent selector and skill reference
3. Review **[AGENTS_GUIDE.md](docs/AGENTS_GUIDE.md)** to understand available agents and workflows
4. Create `.env` file: `cp .env.example .env` and configure your Anthropic API key
5. Review **[Skills Index](docs/guides/SKILLS_INDEX.md)** for detailed skill descriptions
6. Choose an agent based on your software engineering task
7. Use the appropriate skill with that agent (e.g., `spring-boot-setup` with Java Developer Agent)
8. Explore agent collaboration workflows for complex multi-team projects
9. Check **[Project Specifications](docs/guides/PROJECT_SPECIFICATIONS.md)** for Java and Python templates

**Welcome to your AI-powered software engineering system!** 🚀

---

## About the Author

**Wallace Espindola** - Senior Software Engineer / Solution Architect

- Expertise: Java, Python, JavaScript, Cloud Architecture, Microservices, Databases
- Focus: Building production-ready systems and sharing knowledge

### Connect & Follow

- **GitHub**: [github.com/wallaceespindola](https://github.com/wallaceespindola)
- **LinkedIn**: [linkedin.com/in/wallaceespindola](https://www.linkedin.com/in/wallaceespindola/)
- **Dev.to**: [dev.to/wallaceespindola](https://dev.to/wallaceespindola)
- **Medium**: [medium.com/@wallaceespindola](https://medium.com/@wallaceespindola)
- **Speaker Deck**: [speakerdeck.com/wallacese](https://speakerdeck.com/wallacese)
- **Substack**: [wallaceespindola.substack.com](https://wallaceespindola.substack.com)
- **DZone**: [dzone.com/users/1254611/wallacese](https://dzone.com/users/1254611/wallacese.html)
- **Sessionize**: [sessionize.com/wallace-espindola](https://sessionize.com/wallace-espindola/)
- **Twitter/X**: [x.com/wsespindola](https://x.com/wsespindola)

### Quick Links

- **Linktree**: [linktr.ee/wallace.espindola](https://linktr.ee/wallace.espindola)
- **Solo.to**: [solo.to/wallace.espindola](https://solo.to/wallace.espindola)
- **Gravatar**: [gravatar.com/wallacese](https://gravatar.com/wallacese)

---

*This system provides specialized AI agents for comprehensive software engineering tasks. Whether you're developing
code, managing quality assurance, designing architecture, setting up infrastructure, or managing projects - there's an
agent ready to help. All agents work together seamlessly for complex, multi-team workflows.*
