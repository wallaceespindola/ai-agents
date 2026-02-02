---
name: monitoring-setup
description: Set up monitoring, logging, and alerting for applications and infrastructure
---

# Monitoring Setup Skill

## When to Use This Skill

- Setting up application monitoring
- Creating dashboards and alerts
- Log aggregation and analysis
- Performance monitoring
- Error tracking and alerting
- Uptime monitoring

## Quick Start

```
/monitoring-setup <application_or_service>
```

## Popular Tools

- **Prometheus**: Metrics collection
- **Grafana**: Dashboards and visualization
- **ELK Stack**: Logging (Elasticsearch, Logstash, Kibana)
- **Datadog**: SaaS monitoring
- **New Relic**: Application performance monitoring

## Prometheus Scrape Config

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'app'
    static_configs:
      - targets: ['localhost:8080']
  - job_name: 'database'
    static_configs:
      - targets: ['localhost:5432']
```

## Grafana Dashboard Example

```json
{
  "dashboard": {
    "title": "Application Metrics",
    "panels": [
      {
        "title": "Request Rate",
        "targets": [
          {
            "expr": "rate(http_requests_total[5m])"
          }
        ]
      },
      {
        "title": "Response Time P99",
        "targets": [
          {
            "expr": "histogram_quantile(0.99, http_request_duration_seconds)"
          }
        ]
      },
      {
        "title": "Error Rate",
        "targets": [
          {
            "expr": "rate(http_requests_failed_total[5m])"
          }
        ]
      }
    ]
  }
}
```

## Alert Rules Example

```yaml
groups:
  - name: app_alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_failed_total[5m]) > 0.01
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"

      - alert: HighLatency
        expr: histogram_quantile(0.99, http_request_duration_seconds) > 1
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "High request latency detected"
```

## Integration with Other Skills

- **`cicd-pipeline-setup`**: Deploy monitoring
- **`infrastructure-as-code`**: Monitor infrastructure
- **`kubernetes-setup`**: Kubernetes monitoring

