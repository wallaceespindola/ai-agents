---
name: python-content
description: Write engaging Python content covering modern Python features, data science, web development, async programming, and best practices. Use when creating articles about Python, Django, FastAPI, data analysis, machine learning, or Python ecosystem tools for developer audiences.
---

# Python Content Generation

## When to Use This Skill

Use this skill when:
- Writing tutorials on Python features or frameworks
- Explaining Python design patterns or best practices
- Creating articles about Django, FastAPI, Flask, or async Python
- Discussing Python data science (pandas, NumPy, scikit-learn)
- Covering Python tooling (Poetry, uv, pytest, Black, Ruff)
- Explaining Python async/await, type hints, or dataclasses
- Writing about machine learning with PyTorch or TensorFlow

## Quick Start: Article Structure

### For Tutorials
1. **Hook** (2-3 sentences): Problem the reader wants to solve
2. **Why It Matters** (1 paragraph): Benefits and use cases
3. **Prerequisites** (bullet points): Knowledge and tools needed
4. **Step-by-Step Implementation** (5-8 steps): Clear walkthrough
5. **Complete Code Example** (full, runnable script)
6. **Key Takeaways** (3-5 bullet points)
7. **Common Mistakes** (what NOT to do)
8. **Going Further** (next topics to explore)

### For Best Practices Articles
1. **Problem Statement**: What developers commonly do wrong
2. **Why It Matters**: Performance/readability/maintainability impact
3. **The Pythonic Way**: Recommended approach with explanation
4. **Code Comparison** (Before/After):
   - Before: Anti-pattern or naive approach
   - After: Pythonic solution
   - Analysis: Performance/readability improvements
5. **Real-world Example**: Example from production codebases
6. **When to Break the Rules**: Edge cases and exceptions
7. **References**: Related PEPs and documentation

## Python Core Concepts to Cover

### Modern Python Features (3.9+)
- Type hints and TypedDict: `def process(data: dict[str, int]) -> bool:`
- Pattern matching (3.10): `match obj:`
- Dataclasses: Cleaner than namedtuples
- Pydantic v2: Type validation and serialization
- Async/await: Real concurrent programming
- Walrus operator: `:=` in conditionals

### Web Development
- **FastAPI**: Modern, fast framework with auto-docs
- **Django**: Full-featured, batteries included
- **SQLAlchemy 2.0**: ORM with async support
- **Pydantic**: Data validation at application boundaries
- Testing: pytest with fixtures and mocking
- ASGI vs WSGI understanding

### Data Science & Analysis
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib/Seaborn**: Visualization
- **scikit-learn**: Machine learning
- **Polars**: Faster alternative to pandas
- **DuckDB**: SQL on data

### Async Python
- asyncio internals
- asyncpg, motor (async database drivers)
- aiohttp for async HTTP
- Structured concurrency patterns
- Testing async code
- Debugging async issues

### Performance & Optimization
- Profiling with cProfile and flame graphs
- Understanding GIL and when it matters
- Numba and Cython for performance
- Memory profiling with memory_profiler
- Vectorization with NumPy
- Async I/O vs threading vs multiprocessing

### Python Ecosystem
- **Dependency management**: Poetry, uv (modern alternatives to pip)
- **Code quality**: Ruff (fast linter/formatter), Black, mypy
- **Testing**: pytest, pytest-cov, hypothesis
- **Development**: pre-commit hooks, tox
- **Packaging**: setuptools, wheel, pyproject.toml

## Code Example Template

```python
"""
Module docstring explaining the purpose.

This module demonstrates [concept].
"""

from typing import TypedDict
from dataclasses import dataclass


@dataclass
class ExampleClass:
    """Example class with clear documentation."""

    name: str
    value: int = 0

    def process(self) -> str:
        """Process and return result."""
        return f"{self.name}: {self.value}"


async def async_example(data: dict[str, int]) -> list[str]:
    """Example async function."""
    results = []
    for key, val in data.items():
        # Process asynchronously
        result = await perform_async_task(key, val)
        results.append(result)
    return results


if __name__ == "__main__":
    # Example usage
    obj = ExampleClass("test", 42)
    print(obj.process())
```

**Guidelines for code examples:**
- Always include type hints (Python 3.9+)
- Write docstrings for functions and classes
- Use modern Python idioms
- Keep examples concise (50-100 lines max)
- Include `if __name__ == "__main__":` for runnable examples
- Show imports clearly
- Use meaningful variable names
- Comment only non-obvious logic

## Audience-Specific Tips

### For Backend/API Developers
- Focus on FastAPI, Django, async patterns
- Discuss database optimization
- Cover deployment (Docker, containers)
- Include testing strategies

### For Data Scientists
- Emphasize practical data manipulation
- Show Jupyter notebook techniques
- Include visualization examples
- Discuss performance on large datasets

### For DevOps/Infrastructure
- Cover scripting and automation
- Discuss CI/CD integration
- Include containerization
- Focus on system programming aspects

### For Beginners Transitioning to Python
- Explain Python-specific concepts
- Compare to other languages
- Show Pythonic idioms
- Avoid obscure features initially

## SEO Keywords for Python Content

- Python 3.9, Python 3.10, Python 3.11, Python 3.12
- FastAPI, Django, Flask
- async/await, asyncio
- Type hints, Pydantic
- Poetry, uv
- Data science, pandas, NumPy
- Machine learning, scikit-learn
- Web development
- pytest, testing
- Performance optimization
- Python best practices, Pythonic code

## Examples

### Example 1: FastAPI Article Hook
"FastAPI has become the go-to choice for building modern Python APIs, but many developers miss its most powerful feature: automatic OpenAPI documentation. Combine that with Pydantic validation, and you get a framework that catches bugs at the API boundary before they hit your business logic."

### Example 2: Async Python Article
"The async/await syntax makes concurrent Python elegant. But understanding the event loop, tasks, and when to use asyncio vs threading is crucial. Here's the mental model that makes it all click."

### Example 3: Pattern Article
**Before (❌ Not Pythonic):**
```python
result = []
for i in range(len(data)):
    if data[i] > 10:
        result.append(data[i] * 2)
return result
```

**After (✅ Pythonic):**
```python
return [x * 2 for x in data if x > 10]
```

## Common Pitfalls to Mention

1. **Mutable default arguments**: `def func(items=[]):`  ❌
2. **Not using virtual environments**: Dependency conflicts
3. **Ignoring type hints**: Loss of IDE support and refactoring safety
4. **Async anti-patterns**: Blocking calls in async functions
5. **Too much metaprogramming**: Reduces readability
6. **Poor exception handling**: Catching all exceptions silently
7. **N+1 query problems**: In database interactions
8. **Not using context managers**: Resource leaks
9. **Premature optimization**: GIL isn't always the bottleneck

## Research & Validation

Before publishing:
- Test all examples in Python REPL or IDE
- Check compatibility with Python 3.9+
- Verify framework versions are current
- Run examples with modern tooling (uv, Ruff, pytest)
- Check for security issues (OWASP)
- Validate performance claims with benchmarks
- Review type hints with mypy in strict mode

## Async Python Patterns

### Pattern 1: Concurrent I/O
```python
import asyncio
import aiohttp

async def fetch_urls(urls: list[str]) -> list[str]:
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [await r.text() for r in responses]
```

### Pattern 2: Structured Concurrency
```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(async_func_1())
        task2 = tg.create_task(async_func_2())
    # Both completed successfully or exception raised
```

## Content Variations by Platform

- **LinkedIn Pulse**: Career paths in Python, industry trends
- **Medium**: Deep technical dives with architecture
- **Dev.to**: Quick tips, code snippets, practical solutions
- **Substack**: Learning journey, personal insights
- **JavaPro Equivalent**: Enterprise Python patterns
