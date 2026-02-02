---
name: scalability-analysis
description: Analyze system scalability, identify bottlenecks, and plan capacity growth
---

# Scalability Analysis Skill

## When to Use This Skill

- Analyzing capacity and performance limits
- Identifying system bottlenecks
- Planning for growth and traffic spikes
- Designing scaling strategies
- Cost estimation for infrastructure
- Load testing and benchmarking
- Horizontal vs vertical scaling decisions
- Database and cache scaling strategies

## Quick Start

```
/scalability-analysis <system_component_or_service>
```

**Example**:
```
/scalability-analysis E-commerce API handling Black Friday traffic
```

## How It Works

### 1. Capacity Planning
- Current capacity assessment
- Growth projections
- Peak load analysis
- Resource utilization targets

### 2. Bottleneck Identification
- CPU bound operations
- Memory limitations
- I/O constraints (disk, network)
- Database query performance
- External service limits

### 3. Scaling Strategies
- Horizontal scaling (more servers)
- Vertical scaling (bigger servers)
- Caching layers
- Database replication and sharding
- Load balancing and routing

### 4. Performance Metrics
- Throughput (requests/second)
- Latency (response time)
- Resource utilization (CPU, memory, disk)
- Queue depth
- Error rates

### 5. Load Testing
- Baseline performance
- Ramp-up testing
- Spike testing
- Soak testing
- Stress testing

### 6. Cost Analysis
- Infrastructure costs per scale tier
- Cost per request
- Break-even points
- ROI for optimizations

### 7. Monitoring & Alerting
- Key performance indicators
- Alert thresholds
- Scaling triggers
- Capacity planning metrics

## Examples

### Example 1: Scalability Assessment

```markdown
## Scalability Analysis Report

### Current State
- Users: 10,000 (growing 5% monthly)
- Daily Active: 2,000
- Peak QPS: 50 requests/second
- Infrastructure: Single t3.large EC2 + RDS

### Performance Baseline
- API latency (p99): 150ms
- Database query time (avg): 30ms
- Cache hit rate: 60%
- Error rate: 0.05%

### Bottleneck Analysis

#### 1. CPU Utilization
Current: 65% at peak
Issue: Single server running app + Redis
Solution: Separate Redis to cache layer

#### 2. Database Connections
Current: 100/150 connections used
Issue: Connection pooling not optimal
Solution: Implement PgBouncer connection pooling

#### 3. Database Query Performance
Current: Top 10 queries consume 70% of DB time
Issue: Missing indexes
Solution: Add 5 indexes (detailed in recommendations)

#### 4. Memory Usage
Current: 2.5GB/4GB available
Issue: Growing cache size
Solution: Implement cache eviction policies

### Growth Projection (12 months)
- Users: 15,000 (+50%)
- Daily Active: 3,500 (+75%)
- Peak QPS: 150 (+3x)
- Infrastructure: Needs scaling NOW

### Scaling Strategy

#### Phase 1: Optimization (Week 1-2, $0 cost)
1. Add database indexes (5 new)
   - Expected improvement: 40% query faster
   - Effort: 2 hours

2. Implement query caching
   - Cache TTL: 5 minutes
   - Savings: 50% fewer queries
   - Effort: 4 hours

3. Connection pooling
   - PgBouncer: 1000 max connections
   - Effort: 2 hours

Expected result: Handle 80 QPS

#### Phase 2: Caching Layer (Week 3-4, $50/month)
1. Redis cluster (separate from app)
   - Handles all session/cache data
   - Reduces database load 30%

2. Cache invalidation strategy
   - Time-based (TTL)
   - Event-based invalidation

Expected result: Handle 150 QPS

#### Phase 3: Horizontal Scaling (Month 2, $150/month)
1. Load balancer (ALB)
   - Distribute traffic across 3 app servers

2. Auto-scaling group
   - Min: 3, Max: 10 instances
   - Scale trigger: CPU > 70%

3. Database read replicas
   - 2 read replicas for read queries
   - Write goes to master

Expected result: Handle 400+ QPS

#### Phase 4: Database Sharding (Month 3-4, $300/month)
1. Shard by user_id
   - Shard 1: Users 1-5000
   - Shard 2: Users 5001-10000
   - Router directs queries

Expected result: Handle 800+ QPS

### Cost-Benefit Analysis

| Phase | Infrastructure Cost | Effort | Capacity Gain | ROI |
|-------|-------------------|---------|--------------|-----|
| 1 | $0 | 8h | 30 QPS | High |
| 2 | $50/mo | 16h | 70 QPS | Very High |
| 3 | $150/mo | 40h | 250 QPS | High |
| 4 | $300/mo | 80h | 400 QPS | Medium |

### Monitoring & Alerts

Key metrics to track:
- API latency (p50, p95, p99)
- Database query time
- Cache hit rate
- Server CPU and memory
- Request error rate
- Queue depth

Alert thresholds:
- Latency p99 > 500ms → Scale up
- Error rate > 1% → Investigate
- Cache hit rate < 50% → Adjust TTL
- Queue depth > 1000 → Add workers

### Timeline & Recommendations

**Immediate (This Week)**
- [ ] Run database slow query log analysis
- [ ] Identify 10 most expensive queries
- [ ] Plan Phase 1 implementation

**Short Term (This Month)**
- [ ] Implement Phase 1 optimizations
- [ ] Deploy Redis cache layer
- [ ] Set up monitoring

**Medium Term (2-3 Months)**
- [ ] Implement auto-scaling
- [ ] Add read replicas
- [ ] Load test with 200 concurrent users

**Long Term (3-6 Months)**
- [ ] Evaluate database sharding
- [ ] Consider microservices
- [ ] Plan for 50x growth

### Success Criteria

After implementation:
- [ ] Handle 150 QPS without manual intervention
- [ ] API latency p99 < 200ms
- [ ] Cache hit rate > 75%
- [ ] Auto-scaling working correctly
- [ ] Cost per request < $0.001
```

### Example 2: Load Testing Script

```javascript
// Load testing with k6
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 100 },   // Ramp to 100 users
    { duration: '5m', target: 100 },   // Hold at 100
    { duration: '2m', target: 200 },   // Ramp to 200
    { duration: '5m', target: 200 },   // Hold at 200
    { duration: '2m', target: 0 },     // Ramp down to 0
  ],
};

export default function () {
  const res = http.get('https://api.example.com/products');

  check(res, {
    'status is 200': (r) => r.status === 200,
    'latency < 200ms': (r) => r.timings.duration < 200,
  });

  sleep(1);
}

// Run: k6 run load-test.js
// Results show:
// - Request rate: 100-200 RPS
// - Latency: 50-150ms
// - Error rate: 0.1%
```

### Example 3: Database Scaling Strategy

```sql
-- Current: Single database query takes 500ms
SELECT u.*, o.*
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > NOW() - INTERVAL '30 days'
ORDER BY u.created_at DESC;

-- Optimized: Add indexes
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Results: Query now takes 50ms (10x faster)

-- Scaling to 1M users:
-- Shard by user_id
CREATE TABLE users_shard_1 PARTITION OF users
  FOR VALUES FROM (1) TO (500000);

CREATE TABLE users_shard_2 PARTITION OF users
  FOR VALUES FROM (500000) TO (1000000);

-- Queries now search 500k users instead of 1M
-- 2x faster per shard
```

## Best Practices

1. **Profile Before Optimizing**
   - Measure current performance
   - Identify real bottlenecks
   - Avoid premature optimization

2. **Load Test Realistically**
   - Use production-like data
   - Simulate real traffic patterns
   - Test error scenarios

3. **Monitor in Production**
   - Continuous performance monitoring
   - Alert on anomalies
   - Track trends over time

4. **Scale Proactively**
   - Plan 2-3x current capacity
   - Gradual scaling vs reactive

5. **Cost Optimization**
   - Measure cost per operation
   - Right-size resources
   - Auto-scaling to match demand

## Integration with Other Skills

- **`system-design-doc`**: Scalability documentation
- **`database-schema-design`**: Query optimization
- **`cicd-pipeline-setup`**: Load testing in pipeline
- **`monitoring-setup`**: Performance tracking

