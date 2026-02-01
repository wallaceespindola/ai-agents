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
