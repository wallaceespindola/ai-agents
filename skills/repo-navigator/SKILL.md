---
name: repo-navigator
description: Navigate and work across the 5 independent git repositories in ~/git/. Use when switching between hiddenbeer, skipy, fake-data-springboot, flashcards-app, or PythonRuns.
user-invocable: true
allowed-tools: Bash(git *), Bash(cd *), Bash(ls *), Read, Glob, Grep
---

# Multi-Repository Navigator

Navigate the five independent repositories in ~/git/:

| Project | Path | Stack | Ports |
|---------|------|-------|-------|
| **hiddenbeer** | `/Users/wallaceespindola/git/hiddenbeer/` | FastAPI + Next.js 15 + MongoDB | BE: 8004, FE: 3004 |
| **skipy** | `/Users/wallaceespindola/git/skipy/` | FastAPI + Next.js + Expo + MongoDB (pnpm monorepo) | API: 8100, Client: 8080, Admin: 8070, Manager: 8090 |
| **fake-data-springboot** | `/Users/wallaceespindola/git/fake-data-springboot/` | Java 21 + Spring Boot 3 + Maven | 8080 |
| **flashcards-app** | `/Users/wallaceespindola/git/flashcards-app/` | Flask + Python | 5000 |
| **PythonRuns** | `/Users/wallaceespindola/git/PythonRuns/` | Python + uv + pytest | N/A |

## Quick Commands

All projects use Makefiles - run `make help` in any project for available commands.

### Common Patterns

```bash
# Check current repo status
git status
git branch -vv

# See available make targets
make help

# Run tests
make test

# Start development servers
make dev              # or make dev-backend, make dev-frontend
```

## When Switching Projects

1. Use absolute paths: `/Users/wallaceespindola/git/PROJECT_NAME`
2. Check the Makefile for available commands
3. Respect each project's environment files (`.env.example` patterns)
4. Remember: each has its own CI/CD, dependencies, and git remote
5. Check which branch you're on before making changes

## Environment Setup

Each project has different setup requirements:

- **hiddenbeer**: `make setup` (installs deps + pre-commit + MongoDB)
- **skipy**: `pnpm install` (monorepo workspace install)
- **fake-data-springboot**: `make install` (Maven clean install)
- **flashcards-app**: `python -m venv .venv && pip install -r requirements.txt`
- **PythonRuns**: `make install` (uv venv + sync)

## Help the User

When navigating:
- Always check which repo they're currently working in
- Suggest relevant make commands from that repo's Makefile
- Don't mix patterns between repos (e.g., don't suggest pnpm for hiddenbeer)
- Remind about environment variables if starting dev servers
