---
name: java-performance-tuning
description: Profile and optimize Java application performance, JVM tuning, and resource utilization
---

# Java Performance Tuning Skill

## When to Use This Skill

- Identifying performance bottlenecks in Java applications
- Optimizing slow database queries
- Tuning JVM garbage collection and memory
- Reducing CPU usage and latency
- Improving throughput in high-load scenarios
- Analyzing memory leaks and heap usage
- Optimizing collection usage and iterations
- Benchmarking performance improvements

## Quick Start

```
/java-performance-tuning <class_or_method>
```

**Example**:
```
/java-performance-tuning UserService.findAllUsers method is slow
```

## How It Works

The skill performs comprehensive performance analysis:

### 1. Profiling Analysis
- **CPU Profiling**: Identify hot methods consuming CPU
- **Memory Profiling**: Detect memory leaks and excessive allocations
- **Thread Analysis**: Monitor thread contention and blocking
- **GC Analysis**: Analyze garbage collection pauses

### 2. JVM Tuning
- **Heap Size**: Optimal heap allocation (-Xmx, -Xms)
- **GC Selection**: Choose appropriate GC algorithm (G1GC, ZGC, Shenandoah)
- **GC Tuning**: Tune young/old generation sizes
- **JVM Flags**: Performance optimization flags

### 3. Code Optimization
- **Algorithm Complexity**: O(n²) vs O(n) analysis
- **Collection Usage**: ArrayList vs LinkedList trade-offs
- **String Operations**: StringBuilder for concatenation
- **Object Creation**: Reduce temporary object allocation
- **Caching**: Memoization and cache strategies

### 4. Database Optimization
- **Query Analysis**: Identify N+1 queries and inefficient queries
- **Indexing**: Add missing indexes, analyze index usage
- **Connection Pooling**: Optimize connection pool size
- **Batch Processing**: Batch inserts/updates

### 5. Concurrency Optimization
- **Locking**: Identify contention points, reduce lock scope
- **Thread Pools**: Tune thread pool sizes for workload
- **Async Processing**: Use async/await for I/O operations
- **Reactive Streams**: Consider reactive programming patterns

## Configuration

**JVM Options for Production**:
```bash
# Heap sizing (for 8GB server)
-Xms4G -Xmx4G

# G1 Garbage Collector (default in Java 9+)
-XX:+UseG1GC
-XX:MaxGCPauseMillis=200

# Enable GC logging
-Xlog:gc*:file=gc.log:time,level,tags

# Additional tuning
-XX:+HeapDumpOnOutOfMemoryError
-XX:HeapDumpPath=/var/log/heap_dump.hprof
```

## Examples

### Example 1: Identifying N+1 Query Problem

```java
// ❌ ISSUE: N+1 queries
@Service
public class OrderService {
    public List<OrderDTO> getOrdersWithDetails() {
        List<Order> orders = orderRepository.findAll();  // 1 query: SELECT * FROM orders
        return orders.stream()
            .map(order -> new OrderDTO(
                order,
                itemRepository.findByOrder(order),  // N queries: SELECT * FROM items WHERE order_id = ?
                invoiceRepository.findByOrder(order)  // N more queries
            ))
            .collect(toList());
    }
}

// ✅ FIXED: Single query with JOINs
@Service
public class OrderService {
    public List<OrderDTO> getOrdersWithDetails() {
        List<Order> orders = orderRepository.findAllWithItemsAndInvoices();  // 1 query with JOIN
        return orders.stream()
            .map(OrderDTO::new)
            .collect(toList());
    }
}

// In OrderRepository:
@Repository
public interface OrderRepository extends JpaRepository<Order, Long> {
    @Query("""
        SELECT DISTINCT o FROM Order o
        LEFT JOIN FETCH o.items
        LEFT JOIN FETCH o.invoices
        """)
    List<Order> findAllWithItemsAndInvoices();
}
```

### Example 2: String Concatenation Optimization

```java
// ❌ ISSUE: Slow string concatenation in loop
public String buildReport(List<String> items) {
    String result = "";
    for (String item : items) {
        result += item + ", ";  // Creates new String object each iteration!
    }
    return result;
}
// Time complexity: O(n²) due to copying

// ✅ FIXED: Use StringBuilder
public String buildReport(List<String> items) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < items.size(); i++) {
        if (i > 0) sb.append(", ");
        sb.append(items.get(i));
    }
    return sb.toString();
}
// Time complexity: O(n)

// ✅ BEST: Use String.join (Java 8+)
public String buildReport(List<String> items) {
    return String.join(", ", items);
}
```

### Example 3: Collection Selection

```java
// ❌ ISSUE: Wrong collection type
List<String> items = new LinkedList<>();  // O(n) access time
for (int i = 0; i < items.size(); i++) {
    String item = items.get(i);  // O(n) operation in loop: O(n²) total
}

// ✅ FIXED: Use ArrayList for random access
List<String> items = new ArrayList<>();  // O(1) access time
for (int i = 0; i < items.size(); i++) {
    String item = items.get(i);  // O(1) operation: O(n) total
}

// ✅ ALSO GOOD: Use enhanced for loop
for (String item : items) {  // O(n), works with both ArrayList and LinkedList
    // ...
}
```

### Example 4: Connection Pool Tuning

```java
// In application.properties
spring.datasource.hikari.maximum-pool-size=20
spring.datasource.hikari.minimum-idle=5
spring.datasource.hikari.connection-timeout=30000
spring.datasource.hikari.idle-timeout=600000
spring.datasource.hikari.max-lifetime=1800000

# Calculation for pool size:
# pool_size = ((core_count * 2) + effective_spindle_count)
# For 4 core CPU with 1 disk: ((4 * 2) + 1) = 9
```

### Example 5: Memory Leak Detection

```java
// ❌ ISSUE: Static collection grows indefinitely
@Service
public class CacheService {
    private static final Map<String, UserData> cache = new HashMap<>();

    public void cacheUser(String id, UserData data) {
        cache.put(id, data);  // Never removed, grows until OutOfMemoryError
    }

    public UserData getUser(String id) {
        return cache.get(id);
    }
}

// ✅ FIXED: Use time-based eviction
@Service
public class CacheService {
    private final Map<String, CacheEntry> cache = new ConcurrentHashMap<>();
    private static final long CACHE_TTL_MILLIS = 3600000;  // 1 hour

    public void cacheUser(String id, UserData data) {
        cache.put(id, new CacheEntry(data, System.currentTimeMillis()));
    }

    public UserData getUser(String id) {
        CacheEntry entry = cache.get(id);
        if (entry != null && !isExpired(entry)) {
            return entry.data;
        }
        cache.remove(id);
        return null;
    }

    private boolean isExpired(CacheEntry entry) {
        return System.currentTimeMillis() - entry.timestamp > CACHE_TTL_MILLIS;
    }
}

// ✅ BEST: Use Google Guava Cache
private final LoadingCache<String, UserData> cache = CacheBuilder.newBuilder()
    .expireAfterWrite(1, TimeUnit.HOURS)
    .maximumSize(10000)
    .build(CacheLoader.from(this::loadUser));
```

## Best Practices

### 1. Object Pooling
```java
// Reuse expensive objects instead of creating new ones
private final Queue<ByteBuffer> bufferPool = new LinkedList<>();

public ByteBuffer acquireBuffer(int size) {
    ByteBuffer buffer = bufferPool.poll();
    if (buffer == null || buffer.capacity() < size) {
        return ByteBuffer.allocate(size);
    }
    buffer.clear();
    return buffer;
}

public void releaseBuffer(ByteBuffer buffer) {
    bufferPool.offer(buffer);
}
```

### 2. Lazy Initialization
```java
// Delay expensive object creation
private volatile ExpensiveObject instance;

public ExpensiveObject getInstance() {
    if (instance == null) {
        synchronized (this) {
            if (instance == null) {  // Double-checked locking
                instance = new ExpensiveObject();
            }
        }
    }
    return instance;
}

// OR use Java 9+ VarHandle for lock-free initialization
```

### 3. Batch Processing
```java
// Process in batches to reduce memory and improve throughput
public void processLargeDataset(Stream<Record> records) {
    records.collect(Collectors.toList())
        .stream()
        .collect(Collectors.groupingBy(
            r -> r.getId() / BATCH_SIZE,
            Collectors.toList()
        ))
        .values()
        .forEach(this::processBatch);
}

private void processBatch(List<Record> batch) {
    // Process batch more efficiently
}
```

## GC Tuning Reference

| GC Algorithm | Best For | Latency | Throughput |
|--------------|----------|---------|-----------|
| G1GC | Mixed workloads, 4GB+ heaps | Low | High |
| ZGC | Ultra-low latency | Very Low | Medium |
| Shenandoah | Consistent latency | Low | High |
| Epsilon | Throughput-focused, minimal GC | Very High | Very High |

## Integration with Other Skills

- **`java-code-review`**: Identify performance issues during code review
- **`java-testing-strategy`**: Performance tests and benchmarking
- **`java-security-audit`**: Security vs performance trade-offs
- **`spring-boot-setup`**: Optimal default configurations

## Performance Analysis Checklist

- [ ] CPU profile shows which methods consume most CPU
- [ ] Memory profile shows heap usage and potential leaks
- [ ] GC logs show pause times and frequency
- [ ] Database queries analyzed for efficiency
- [ ] Collection usage appropriate for access patterns
- [ ] Thread pool sizes tuned for workload
- [ ] Connection pools sized correctly
- [ ] Caching strategy implemented
- [ ] Load testing confirms improvements
- [ ] Monitoring in place for production
