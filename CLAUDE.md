# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

**ai-agents** is a repository for developing, testing, and experimenting with Claude AI agents using the Anthropic API. Projects here focus on building autonomous agents powered by Claude models with tool use, multi-step reasoning, and complex task orchestration.

## Supported Languages & Frameworks

- **Python** (primary): Anthropic SDK, asyncio, FastAPI, Flask
- **TypeScript/Node.js**: Anthropic SDK for JS, Express
- **Testing**: pytest (Python), Jest/Vitest (JavaScript)

## Project Setup

### Environment Configuration

Each project must securely manage the Anthropic API key:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

Store in `.env` file (never commit):

```
ANTHROPIC_API_KEY=sk-ant-...
```

Load using:
- **Python**: `python-dotenv` with `load_dotenv()` or manual `os.getenv()`
- **Node.js**: `dotenv` package

### Creating a New Agent Project

1. Create a project directory: `project-name/`
2. Set up dependencies using **uv** (recommended):
   ```bash
   cd project-name
   uv init --python 3.11
   uv add anthropic
   ```
3. Create a `Makefile` with standard commands:
   ```makefile
   setup:
       uv sync
   dev:
       uv run python main.py
   test:
       uv run pytest tests/
   lint:
       uv run ruff check .
   ```

## Anthropic SDK Usage

### Python

```python
from anthropic import Anthropic

client = Anthropic(api_key="sk-ant-...")

# Simple message
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude!"}]
)

# With tools
tools = [
    {
        "name": "get_weather",
        "description": "Get weather for a location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in Paris?"}]
)
```

### TypeScript

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const response = await client.messages.create({
  model: "claude-3-5-sonnet-20241022",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello, Claude!" }],
});
```

## Agent Patterns

### Multi-Step Reasoning

Agents often need multiple turns to solve problems. Implement agentic loops:

```python
messages = [{"role": "user", "content": "Solve this complex task..."}]

while True:
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        tools=tools,
        messages=messages
    )

    # Handle tool use
    if response.stop_reason == "tool_use":
        # Process tool calls and add results to messages
        pass
    elif response.stop_reason == "end_turn":
        break
```

### Tool Use

Agents use tools to interact with external systems. Define tools with clear descriptions and schemas. Always validate tool inputs and handle errors gracefully.

### System Prompts

Use system prompts to define agent behavior:

```python
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    system="You are a helpful assistant that analyzes data and provides insights.",
    messages=[{"role": "user", "content": "Analyze this dataset..."}]
)
```

## Testing Agent Projects

- **Unit tests**: Test individual tool implementations
- **Integration tests**: Test agent loops with mocked Claude responses
- **End-to-end tests**: Test full agent workflows (may incur API costs)

```bash
# Run tests
make test

# Run specific test file
uv run pytest tests/test_agent.py

# With coverage
uv run pytest --cov=src tests/
```

## Common Commands

```bash
# Setup
make setup              # Install dependencies

# Development
make dev                # Run agent
make lint               # Check code quality
make format             # Format code

# Testing
make test               # Run all tests
make test-coverage      # Run tests with coverage report
```

## Model Selection

Default model for most agents: **claude-3-5-sonnet-20241022**

- **Sonnet**: Balanced speed/intelligence, best for agentic loops
- **Opus**: More powerful reasoning, use for complex tasks
- **Haiku**: Fast/cheap, use for simple tasks or high-volume calls

## Important Notes

- Never commit API keys or tokens (`.env` files are in `.gitignore`)
- Agent conversations can be logged for debugging; add `agent-logs/` and `conversation-history/` to `.gitignore` if storing locally
- Test agents thoroughly before deploying; tool use errors can cascade
- Use streaming for long-running agent tasks to improve perceived responsiveness
- Consider cost implications of multi-step agentic loops with expensive models

## Project Specifications by Language

### Java Project Specifications

When creating Java projects (especially Spring Boot), always follow the standard specifications in `agents/java-developer/AGENT.md`. Key requirements:

### Core Stack
- Java 21, Spring Boot (latest stable), Maven
- Spring Boot Actuator (with custom health endpoint + Maven filtering)
- Spring Data JPA + H2
- Kafka (events configuration)

### REST API Standards
- All responses must include `timestamp` field
- Swagger UI + OpenAPI documentation
- Static test page (`/static/index.html`)
- Path variables (not query params)
- GET alternatives for POST endpoints

### Required Artifacts
- Comprehensive unit tests (>80% coverage)
- Postman collection (with baseUrl variable)
- Dockerfile + docker-compose.yml
- Makefile (setup, dev, test, build, docker, clean)
- GitHub Workflows (build, test, CodeQL)
- Dependabot configured
- Apache 2.0 LICENSE

### Code Quality
- Java Records for DTOs
- Lombok for boilerplate (`@Slf4j`, `@RequiredArgsConstructor`, etc.)
- Compact, well-documented code
- Latest stable library versions

### Author Information
Include in all projects:
- Name: Wallace Espindola
- Email: wallace.espindola@gmail.com
- LinkedIn: https://www.linkedin.com/in/wallaceespindola/
- GitHub: https://github.com/wallaceespindola/

**See `agents/java-developer/AGENT.md` for complete specifications and checklist.**

### Python Project Specifications

When creating Python projects (especially FastAPI), always follow the standard specifications in `agents/python-developer/AGENT.md`. Key requirements:

#### Core Stack
- Python 3.12+, FastAPI (latest stable), uv or Poetry
- SQLAlchemy 2.x (async) + Alembic migrations
- SQLite (dev) / PostgreSQL (prod)
- aiokafka for Kafka (events configuration)

#### REST API Standards
- All responses include `timestamp` field
- Swagger/OpenAPI documentation
- Static test page (`/static/index.html`)
- Path variables (not query params)
- GET alternatives for POST endpoints

#### Required Artifacts
- >80% unit test coverage (pytest, pytest-asyncio)
- Postman collection (with baseUrl variable)
- Dockerfile (multi-stage build)
- docker-compose.yml with full stack (app, db, Kafka)
- Makefile (venv, dev, test, lint, format, typecheck, docker, clean)
- GitHub Workflows (format, lint, type check, test, coverage)
- Dependabot configured
- CodeQL security scanning
- Apache 2.0 LICENSE

#### Observability
- `/health` endpoint (with dependency checks)
- `/metrics` endpoint (Prometheus instrumentation)
- `/info` endpoint (with build metadata)

#### Code Quality
- Black formatting
- isort import sorting
- Ruff linting
- mypy strict type checking
- Pre-commit hooks
- Pydantic v2 models for DTOs
- Structured JSON logging
- Request ID correlation middleware

#### Author Information
Include in all projects:
- Name: Wallace Espindola
- Email: wallace.espindola@gmail.com
- LinkedIn: https://www.linkedin.com/in/wallaceespindola/
- GitHub: https://github.com/wallaceespindola/

**See `agents/python-developer/AGENT.md` for complete specifications and checklist.**

## Project Structure Example

```
my-agent/
├── Makefile
├── pyproject.toml
├── README.md
├── .env.example
├── src/
│   ├── __init__.py
│   ├── agent.py         # Main agent logic
│   ├── tools.py         # Tool definitions
│   └── config.py        # Configuration
├── tests/
│   ├── __init__.py
│   ├── test_agent.py
│   └── test_tools.py
└── logs/                # (ignored, for local debugging)
```

---

## AI Agents System Overview

This repository contains a complete ecosystem of 10 specialized AI agents with 95 integrated skills for comprehensive software engineering tasks. Each agent is a Claude-powered specialist designed to handle specific domains of software development.

### The 10 Agents

| # | Agent | Focus | Skills |
|---|-------|-------|--------|
| 1️⃣ | **Technical Writer** | Content creation, documentation, multi-platform publishing | 22 |
| 2️⃣ | **Java Developer** | Java/Spring Boot enterprise development, microservices | 12 |
| 3️⃣ | **Python Developer** | Python/FastAPI backend, async programming, data processing | 6 |
| 4️⃣ | **JavaScript Developer** | React/Next.js development, component architecture | 10 |
| 5️⃣ | **Software Architect** | System design, architecture patterns, scalability | 7 |
| 6️⃣ | **QA/Tester** | Test automation, quality assurance, testing strategies | 7 |
| 7️⃣ | **DevOps Engineer** | CI/CD, containerization, infrastructure-as-code | 7 |
| 8️⃣ | **Git/GitHub Automation** | GitHub Actions, Git workflows, build automation | 14 |
| 9️⃣ | **Spring/Quarkus Engineer** | Spring Cloud microservices, Quarkus, native compilation | 10 |
| 🔟 | **Project Manager** | Agile planning, sprint management, project coordination | 6 |

**Total: 10 Agents + 95 Skills**

### Skills by Category

**Technical Writing (22 skills)**
- Content creation across 8 platforms (Dev.to, Medium, LinkedIn, Substack, DZone, JavaPro, InfoQ, Blog)
- Code examples, slides, diagrams, image generation, SEO optimization

**Backend Development (28 skills)**
- **Java** (12): code review, testing, performance tuning, security audit, Spring Boot setup, Spring Cloud microservices, advanced security, distributed config, reactive programming
- **Python** (6): code review, testing, performance tuning, type checking, FastAPI setup, documentation
- **Spring/Quarkus** (10): Spring Cloud architecture, OAuth2/JWT security, distributed config, reactive patterns, Quarkus framework, GraalVM native compilation, build optimization

**Frontend Development (10 skills)**
- **JavaScript/React/Next.js**: code review, component patterns, advanced hooks, state management, testing, performance optimization, TypeScript migration, Storybook setup, project setup

**Architecture & Design (7 skills)**
- System design, scalability analysis, design patterns, API design (REST/GraphQL), database schema design, architecture diagrams (C4/UML)

**Quality & Testing (7 skills)**
- Test strategy, test automation setup, test case generation, API testing, E2E testing, performance testing, bug reporting

**Infrastructure & DevOps (7 skills)**
- CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins)
- Docker containerization, Kubernetes orchestration, Helm charts
- Infrastructure-as-code (Terraform, CloudFormation)
- Monitoring (Prometheus, Grafana, ELK, DataDog)
- Security scanning and vulnerability management
- Deployment strategies (blue-green, canary, rolling)

**Git/GitHub Automation (14 skills)**
- **Git & GitHub (6)**: GitHub Actions workflows, Git workflow strategies, PR management, CLI automation, security scanning, commit strategies
- **Config Management (5)**: YAML validation, Kubernetes manifests, Docker Compose, Helm charts, GitHub Actions YAML
- **Build & Secrets (3)**: build optimization, SSH key management, secrets management, pre-commit hooks

**Project Management (6 skills)**
- Project planning, sprint planning, risk assessment, status reporting, sprint retrospectives, roadmap planning

### Technology Coverage

**Languages & Backends**
- Java 17+, Spring Boot 3.x, Spring Cloud, Quarkus, GraalVM native
- Python 3.10+, FastAPI, async/await, type hints
- JavaScript/TypeScript, React 18+, Next.js 15+

**Frontend Frameworks**
- React with hooks, state management (Context, Redux, Zustand, TanStack Query)
- Next.js with App Router
- Component libraries: shadcn/ui, Storybook
- TypeScript strict mode

**Infrastructure & DevOps**
- **Containerization**: Docker, Docker Compose, Podman
- **Orchestration**: Kubernetes, Helm, Kustomize
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins, CircleCI
- **Infrastructure-as-Code**: Terraform, CloudFormation, Ansible
- **Monitoring**: Prometheus, Grafana, ELK Stack, DataDog
- **Cloud Platforms**: AWS, Azure, GCP

**Testing & Quality**
- Java: JUnit 5, Mockito, TestContainers
- Python: pytest, unittest, hypothesis
- JavaScript: Jest, React Testing Library, Cypress, Playwright
- Performance: JMeter, Locust, Artillery

**Architecture & Security**
- Microservices patterns, distributed systems
- OAuth2, OpenID Connect, JWT authentication, RBAC
- Secrets management (Vault, AWS Secrets Manager)
- Security scanning (SonarQube, Trivy, OWASP Dependency-Check)

### Documentation & References

- **AGENTS.md**: Complete reference of all 10 agents with profiles, skills, and workflows
- **AGENTS_GUIDE.md**: Comprehensive guide including agent collaboration patterns and multi-agent workflows
- **SKILLS_INDEX.md**: Detailed catalog of all 95 skills with usage guidance
- **SYSTEM_MAP.md**: Architecture overview and relationships between agents
- **GETTING_STARTED.md**: Setup and onboarding guide

See `/agents/{name}/AGENT.md` for individual agent details and `/skills/{name}/SKILL.md` for skill documentation.
