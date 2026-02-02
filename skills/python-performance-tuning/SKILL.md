---
name: python-performance-tuning
description: Profile and optimize Python code for better performance and resource efficiency
---

# Python Performance Tuning Skill

## When to Use This Skill

- Identifying performance bottlenecks in Python applications
- Profiling CPU and memory usage
- Optimizing database queries and I/O operations
- Improving algorithm efficiency (Big O analysis)
- Caching strategies and memoization
- Parallelization with multiprocessing and asyncio
- Database query optimization
- Reducing memory leaks and improving garbage collection

## Quick Start

```
/python-performance-tuning <component_or_module>
```

**Example**:
```
/python-performance-tuning User service with expensive queries and list operations
```

## How It Works

The skill performs comprehensive performance analysis and optimization:

### 1. Profiling Techniques
- **cProfile**: CPU profiling to identify slow functions
- **memory_profiler**: Line-by-line memory tracking
- **py-spy**: Sampling profiler for production code
- **timeit**: Precise timing of code snippets

### 2. CPU Optimization
- **Algorithm Complexity**: Big O analysis and optimization
- **Function Call Overhead**: Reduce unnecessary calls
- **Loop Optimization**: Vectorization and comprehensions
- **Compilation**: Numba JIT compilation for numerical code

### 3. Memory Optimization
- **Data Structure Selection**: Choose efficient collections
- **Memory Leaks**: Reference cycles and cleanup
- **Generators**: Lazy evaluation instead of lists
- **Slots**: Reduce object size with `__slots__`

### 4. I/O Optimization
- **Async I/O**: asyncio for concurrent operations
- **Batch Processing**: Reduce number of I/O operations
- **Caching**: Redis, lru_cache for repeated access
- **Connection Pooling**: Reuse database connections

### 5. Database Query Optimization
- **Query Analysis**: Identify N+1 problems
- **Indexing**: Database indexes for common queries
- **Query Execution**: EXPLAIN plans
- **Eager Loading**: Load relationships efficiently

### 6. Parallelization
- **multiprocessing**: True parallel execution (CPU-bound)
- **threading**: Concurrent I/O (I/O-bound)
- **asyncio**: Cooperative multitasking
- **Distributed Processing**: Celery, Ray for scale

### 7. Performance Metrics
- **Response Time**: Latency measurements
- **Throughput**: Operations per second
- **Resource Usage**: CPU and memory consumption
- **Scalability**: Performance under load

## Configuration

**requirements-dev.txt**:
```
pytest-benchmark==4.0.0
memory-profiler==0.61.0
py-spy==0.3.14
scalene==1.5.32
line-profiler==4.1.1
pympler==1.1.0
```

**Makefile**:
```makefile
profile-cpu:
	python -m cProfile -s cumtime main.py

profile-memory:
	python -m memory_profiler main.py

benchmark:
	pytest tests/ --benchmark-only

timeit:
	python -m timeit -s "from src import func" "func()"
```

## Examples

### Example 1: CPU Profiling and Optimization

```python
# src/fibonacci.py
def fibonacci_slow(n):
    """Slow recursive Fibonacci - O(2^n)"""
    if n <= 1:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)


def fibonacci_fast(n):
    """Optimized with memoization - O(n)"""
    cache = {}

    def fib(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib(n)


from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """Using functools.lru_cache - O(n)"""
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


# tests/test_performance.py
import pytest
import time


@pytest.mark.benchmark
def benchmark_fib(benchmark):
    """Benchmark the optimized version"""
    result = benchmark(fibonacci_fast, 35)
    assert result == 9227465


def test_performance_comparison():
    """Compare different implementations"""
    n = 30

    # Slow version - ~1 second
    start = time.time()
    result_slow = fibonacci_slow(n)
    time_slow = time.time() - start

    # Fast version - ~0.001 seconds
    start = time.time()
    result_fast = fibonacci_fast(n)
    time_fast = time.time() - start

    print(f"Slow: {time_slow:.4f}s, Fast: {time_fast:.4f}s")
    print(f"Speedup: {time_slow / time_fast:.0f}x")

    assert result_slow == result_fast
```

### Example 2: Memory Optimization with Generators

```python
# ❌ INEFFICIENT: Load entire file into memory
def read_large_file_slow(filepath):
    """Loads entire file at once - O(n) memory"""
    lines = []
    with open(filepath) as f:
        for line in f:
            lines.append(line.strip())
    return lines

def process_file_slow():
    lines = read_large_file_slow("huge_file.txt")
    count = sum(1 for line in lines if "keyword" in line)
    return count


# ✅ EFFICIENT: Generator for streaming processing
def read_large_file_fast(filepath):
    """Generator for memory-efficient reading - O(1) memory"""
    with open(filepath) as f:
        for line in f:
            yield line.strip()

def process_file_fast():
    count = sum(1 for line in read_large_file_fast("huge_file.txt")
                if "keyword" in line)
    return count


# Memory profiling
from memory_profiler import profile

@profile
def memory_test_slow():
    """Shows memory usage with slow approach"""
    lines = read_large_file_slow("large_file.txt")
    return len(lines)

@profile
def memory_test_fast():
    """Shows memory usage with generator approach"""
    count = sum(1 for _ in read_large_file_fast("large_file.txt"))
    return count
```

### Example 3: Database Query Optimization

```python
# src/models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")


# ❌ N+1 PROBLEM: Queries for each user's posts
def get_users_with_posts_slow(session):
    users = session.query(User).all()  # 1 query

    for user in users:
        print(f"{user.name}: {len(user.posts)} posts")  # N queries

    # Total: 1 + N queries


# ✅ OPTIMIZED: Eager loading all relationships
from sqlalchemy.orm import joinedload

def get_users_with_posts_fast(session):
    users = session.query(User).options(
        joinedload(User.posts)
    ).all()  # 1 efficient query

    for user in users:
        print(f"{user.name}: {len(user.posts)} posts")  # No additional queries


# ✅ ALTERNATIVE: Explicit JOIN
def get_users_with_post_count_fast(session):
    from sqlalchemy import func

    users = session.query(
        User,
        func.count(Post.id).label("post_count")
    ).outerjoin(Post).group_by(User.id).all()

    for user, count in users:
        print(f"{user.name}: {count} posts")
```

### Example 4: Async I/O for Concurrent Operations

```python
# ❌ SYNCHRONOUS: Sequential execution
import requests
import time

def fetch_urls_slow(urls):
    """Fetch URLs sequentially - O(n) time"""
    results = []
    start = time.time()

    for url in urls:
        response = requests.get(url)  # Waits for each response
        results.append(response.json())

    print(f"Time: {time.time() - start:.2f}s")
    return results


# ✅ ASYNCHRONOUS: Concurrent execution
import aiohttp
import asyncio

async def fetch_urls_fast(urls):
    """Fetch URLs concurrently - O(max_time) time"""
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        results = [await r.json() for r in responses]

    print(f"Time: {time.time() - start:.2f}s")
    return results


# Usage
urls = ["https://api.example.com/1", "https://api.example.com/2"]

# Sequential: ~5 seconds (1 + 1 + 1 + ...)
# asyncio: ~1 second (concurrent)
results = asyncio.run(fetch_urls_fast(urls))
```

### Example 5: Caching Strategies

```python
from functools import lru_cache
import redis
import json
import time


# ✅ BUILT-IN: LRU Cache for functions
@lru_cache(maxsize=128)
def expensive_computation(n):
    """Cache results of expensive function"""
    time.sleep(1)  # Simulate work
    return n * n


# ✅ REDIS: Distributed cache for production
class CachedUserService:
    def __init__(self, redis_client):
        self.redis = redis_client
        self.cache_ttl = 3600  # 1 hour

    def get_user(self, user_id):
        # Check cache first
        cache_key = f"user:{user_id}"
        cached = self.redis.get(cache_key)

        if cached:
            return json.loads(cached)

        # Fetch from database
        user = self.db.query(User).get(user_id)

        # Store in cache
        self.redis.setex(
            cache_key,
            self.cache_ttl,
            json.dumps(user.to_dict())
        )

        return user

    def invalidate_user_cache(self, user_id):
        """Invalidate cache when user is updated"""
        self.redis.delete(f"user:{user_id}")


# ✅ MANUAL CACHING: With validation
class CachedUserRepository:
    def __init__(self, session):
        self.session = session
        self._cache = {}
        self._last_fetch = {}

    def get_user(self, user_id):
        """Get user with cache expiration"""
        now = time.time()
        cache_key = f"user:{user_id}"

        # Check if cache is still valid (5 minutes)
        if cache_key in self._cache:
            if now - self._last_fetch[cache_key] < 300:
                return self._cache[cache_key]

        # Fetch from database
        user = self.session.query(User).get(user_id)

        # Update cache
        self._cache[cache_key] = user
        self._last_fetch[cache_key] = now

        return user
```

### Example 6: Data Structure Optimization

```python
# ❌ INEFFICIENT: List for lookups - O(n)
class SlowUserStore:
    def __init__(self):
        self.users = []  # Using list

    def find_user(self, email):
        for user in self.users:  # Linear search
            if user.email == email:
                return user
        return None


# ✅ EFFICIENT: Dict/Set for lookups - O(1)
class FastUserStore:
    def __init__(self):
        self.users = {}  # Using dict with email as key

    def find_user(self, email):
        return self.users.get(email)  # Constant time lookup


# ✅ MEMORY EFFICIENT: Using __slots__
class OptimizedUser:
    """Reduce object size from ~280 bytes to ~56 bytes"""
    __slots__ = ['id', 'email', 'name']

    def __init__(self, id, email, name):
        self.id = id
        self.email = email
        self.name = name


# Comparison
regular_user = {'id': 1, 'email': 'test@example.com', 'name': 'Test'}
optimized_user = OptimizedUser(1, 'test@example.com', 'Test')

import sys
print(f"Dict size: {sys.getsizeof(regular_user)}")  # 240+ bytes
print(f"Slots size: {sys.getsizeof(optimized_user)}")  # ~56 bytes
```

## Best Practices

### 1. Profiling Workflow
```python
# Step 1: Profile to identify bottlenecks
# Step 2: Analyze the most expensive operations
# Step 3: Optimize one thing at a time
# Step 4: Measure improvement
# Step 5: Repeat until acceptable performance

import cProfile
import pstats

def profile_function():
    profiler = cProfile.Profile()
    profiler.enable()

    # Code to profile
    expensive_function()

    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)  # Top 10 functions
```

### 2. Performance Testing
```python
# pytest-benchmark for performance testing
def test_function_performance(benchmark):
    result = benchmark(function_to_test, arg1, arg2)
    assert result == expected_value

# Run: pytest --benchmark-only
```

### 3. Avoid Premature Optimization
- Profile first to identify real bottlenecks
- Focus on most impactful optimizations
- Ensure readability and maintainability
- Document performance-critical code

### 4. Common Bottlenecks
- N+1 database queries
- Inefficient algorithms (bubble sort, recursive fibonacci)
- Unnecessary file I/O
- Blocking I/O operations
- Memory leaks and circular references

## Integration with Other Skills

- **`python-testing-strategy`**: Benchmark tests for performance-critical code
- **`python-code-review`**: Performance review during code reviews
- **`database-schema-design`**: Index and query optimization
- **`cicd-pipeline-setup`**: Performance regression testing in CI/CD

