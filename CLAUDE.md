# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Quick Navigation

```
ai-agents/
├── agents/          # 10 specialized agent definitions (AGENT.md per agent)
├── skills/          # 95 skill definitions (SKILL.md per skill)
├── docs/            # Guides: AGENTS_GUIDE.md, GETTING_STARTED.md, SKILLS_INDEX.md
├── AGENTS.md        # Full agent reference with profiles and skill mappings
└── CLAUDE.md        # This file
```

Key references: `AGENTS.md` · `docs/AGENTS_GUIDE.md` · `docs/guides/SKILLS_INDEX.md`

---

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
   uv init --python 3.12
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
    model="claude-sonnet-4-6",
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
    model="claude-sonnet-4-6",
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
  model: "claude-sonnet-4-6",
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
        model="claude-sonnet-4-6",
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
    model="claude-sonnet-4-6",
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

Default model for most agents: **claude-sonnet-4-6**

| Model | ID | Use case |
|-------|----|----------|
| **Sonnet 4.6** | `claude-sonnet-4-6` | Balanced speed/intelligence — default for agentic loops |
| **Opus 4.6** | `claude-opus-4-6` | Strongest reasoning — use for complex multi-step tasks |
| **Haiku 4.5** | `claude-haiku-4-5-20251001` | Fast and cheap — high-volume calls, simple tasks |

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
- Java 21+, Spring Boot (latest stable), Maven
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

10 specialized Claude-powered agents with 95 integrated skills covering the full software engineering lifecycle.

| Agent | Focus | Skills |
|-------|-------|--------|
| Technical Writer | Content, docs, 8 publishing platforms | 22 |
| Java Developer | Spring Boot, microservices, enterprise | 12 |
| Python Developer | FastAPI, async, data processing | 6 |
| JavaScript Developer | React, Next.js, TypeScript | 10 |
| Software Architect | System design, patterns, scalability | 7 |
| QA/Tester | Test automation, quality assurance | 7 |
| DevOps Engineer | CI/CD, Docker, Kubernetes, IaC | 7 |
| Git/GitHub Automation | Actions, workflows, build, secrets | 14 |
| Spring/Quarkus Engineer | Spring Cloud, Quarkus, GraalVM native | 10 |
| Project Manager | Agile, sprint, risk, roadmap | 6 |

**Total: 10 Agents + 95 Skills**

Full details: `AGENTS.md` · `docs/AGENTS_GUIDE.md` · `docs/guides/SKILLS_INDEX.md`

See `/agents/{name}/AGENT.md` for individual agent details and `/skills/{name}/SKILL.md` for skill documentation.
