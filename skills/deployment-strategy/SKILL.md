---
name: deployment-strategy
description: Design deployment strategies including blue-green, canary, and rolling deployments
---

# Deployment Strategy Skill

## When to Use This Skill

- Planning safe deployments
- Minimizing downtime and risk
- Rollback planning
- A/B testing deployments
- Progressive rollout strategies
- Disaster recovery planning

## Quick Start

```
/deployment-strategy <application_type>
```

## Deployment Strategies

### Blue-Green Deployment
```
Blue (Current) → Green (New)
Instant switch with zero downtime
Easy rollback to blue
Requires double infrastructure
```

### Canary Deployment
```
1% → 5% → 25% → 100%
Gradual rollout to reduce risk
Monitor metrics at each stage
Automatic rollback on errors
```

### Rolling Deployment
```
Old V1.0 → Mix → New V1.1
Gradual replacement of instances
No extra infrastructure needed
Slightly longer deployment
```

## Example: Canary Deployment

```yaml
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: app
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app
  progressDeadlineSeconds: 300
  service:
    port: 80
  analysis:
    interval: 60s
    threshold: 5
    maxWeight: 50
    stepWeight: 10
    metrics:
    - name: error-rate
      thresholdRange:
        max: 5
      interval: 1m
    - name: latency
      thresholdRange:
        max: 500
      interval: 30s
  skipAnalysis: false
  webhooks:
  - name: smoke-tests
    url: http://flagger-loadtester/
    metadata:
      type: smoke
      cmd: "curl -sd 'test' http://app-canary:80/token | grep token"
```

## Rollback Triggers

- Error rate > threshold
- Latency > SLO
- Resource exhaustion
- Manual intervention
- Health check failures

## Integration with Other Skills

- **`cicd-pipeline-setup`**: Automate deployments
- **`kubernetes-setup`**: K8s deployments
- **`monitoring-setup`**: Monitor deployments

