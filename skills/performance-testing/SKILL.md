---
name: performance-testing
description: Design and execute performance, load, and stress testing
---

# Performance Testing Skill

## When to Use This Skill

- Load testing APIs and services
- Stress testing system limits
- Spike testing traffic spikes
- Soak testing long-running stability
- Identifying performance bottlenecks
- Capacity planning

## Quick Start

```
/performance-testing <component_or_service>
```

## Load Testing Example with k6

```javascript
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 100 },   // Ramp to 100 users
    { duration: '5m', target: 100 },   // Hold
    { duration: '2m', target: 200 },   // Increase to 200
    { duration: '5m', target: 200 },   // Hold
    { duration: '2m', target: 0 },     // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(99)<500'],  // p99 latency < 500ms
    http_req_failed: ['rate<0.1'],     // Error rate < 0.1%
  },
};

export default function () {
  const response = http.get('https://api.example.com/products');

  check(response, {
    'status 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
}
```

## Performance Metrics

- **Latency**: Response time (p50, p95, p99)
- **Throughput**: Requests per second
- **Error Rate**: Failed requests percentage
- **CPU/Memory**: Resource utilization
- **Connection Pool**: Active connections

## JMeter Example

```xml
<jmeterTestPlan>
  <ThreadGroup guiclass="ThreadGroupGui" testname="Load Test">
    <elementProp name="ThreadGroup.main_controller">
      <stringProp name="ThreadGroup.num_threads">100</stringProp>
      <stringProp name="ThreadGroup.ramp_time">60</stringProp>
    </elementProp>
  </ThreadGroup>

  <HTTPSampler guiclass="HttpTestSampleGui" testname="Get Products">
    <stringProp name="HTTPSampler.domain">api.example.com</stringProp>
    <stringProp name="HTTPSampler.path">/products</stringProp>
  </HTTPSampler>
</jmeterTestPlan>
```

## Testing Types

- **Load**: Normal expected load
- **Stress**: Beyond capacity until break
- **Spike**: Sudden traffic increase
- **Soak**: Long duration at normal load
- **Ramp**: Gradually increasing load

## Best Practices

1. **Realistic scenarios**: Use production-like data
2. **Gradual increase**: Don't go to max instantly
3. **Monitor resources**: CPU, memory, disk
4. **Multiple regions**: Test geo-distributed scenarios
5. **Baseline**: Know current performance
6. **Thresholds**: Define acceptable limits

## Integration with Other Skills

- **`scalability-analysis`**: Identify limits
- **`system-design-doc`**: Performance requirements
- **`cicd-pipeline-setup`**: Automated perf tests

