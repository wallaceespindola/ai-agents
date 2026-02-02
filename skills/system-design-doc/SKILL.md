---
name: system-design-doc
description: Create comprehensive system design documentation including architecture, data flow, and deployment
---

# System Design Documentation Skill

## When to Use This Skill

- Documenting complete system architecture
- Creating design documents for implementation
- Planning system components and interactions
- Documenting data flow and storage
- Planning deployment infrastructure
- Creating onboarding documentation
- Recording architectural decisions
- Planning system evolution

## Quick Start

```
/system-design-doc <system_name_and_scope>
```

**Example**:
```
/system-design-doc Real-time collaborative document editor with WebSocket
```

## How It Works

### 1. System Overview
- High-level architecture diagram
- System components and responsibilities
- Technology stack rationale
- Deployment environments
- Team structure alignment

### 2. Components & Services
- Service responsibilities
- Internal APIs and contracts
- External dependencies
- Scaling strategy per component
- Technology choices rationale

### 3. Data Design
- Entity relationships
- Data storage strategy
- Replication and backup
- Data consistency model
- Migration strategy

### 4. API Design
- REST endpoints or gRPC services
- Request/response schemas
- Error handling
- Authentication and authorization
- Rate limiting and quotas

### 5. Infrastructure
- Cloud provider or on-premise
- Kubernetes deployment
- Load balancing strategy
- Database replication
- Disaster recovery

### 6. Non-Functional Requirements
- Performance targets (latency, throughput)
- Availability (SLA, uptime requirements)
- Scalability limits
- Security requirements
- Compliance (GDPR, SOC2, etc.)

### 7. Operational Aspects
- Monitoring and alerting
- Log aggregation
- Debugging and troubleshooting
- On-call procedures
- Cost estimation

## Configuration

**System Design Document Template**:

```markdown
# System Design: [System Name]

## 1. Overview
- Purpose and goals
- Key features
- Success metrics

## 2. Architecture
- High-level diagram
- Components
- Technology stack

## 3. Data Design
- Schema and models
- Storage strategy
- Replication approach

## 4. API Design
- Endpoint documentation
- Authentication
- Error handling

## 5. Infrastructure
- Deployment architecture
- Scaling strategy
- Security measures

## 6. Non-Functional Requirements
- Performance targets
- Availability goals
- Compliance needs

## 7. Implementation Plan
- Development phases
- Timeline
- Risks and mitigations
```

## Examples

### Example 1: Complete System Design Document

```markdown
# System Design: Real-Time Notification Service

## 1. Overview

### Purpose
Deliver push notifications to users across multiple channels (email, SMS, in-app) with real-time delivery tracking.

### Key Features
- Multi-channel delivery (email, SMS, in-app)
- Real-time delivery status tracking
- User preference management
- Batch processing for high volume
- Delivery retry mechanism

### Success Metrics
- 99.9% message delivery rate
- <5 second notification delivery (in-app)
- <100ms API response time
- Support 1M notifications/day

## 2. Architecture

### High-Level Diagram
```
┌──────────────────────────────────────────────────────┐
│                    API Gateway                        │
└────────────┬─────────────────────────────┬────────────┘
             │                             │
      ┌──────▼─────────┐          ┌────────▼─────────┐
      │Notification    │          │Preference        │
      │Service (Node)  │          │Service (Python)  │
      └──────┬─────────┘          └────────┬─────────┘
             │                             │
             └──────────┬──────────────────┘
                        │
             ┌──────────▼─────────────┐
             │  Message Queue        │
             │  (RabbitMQ/Kafka)     │
             └──────────┬─────────────┘
                        │
        ┌───────────┬───┴────┬──────────┐
        │           │        │          │
    ┌───▼──┐  ┌───▼──┐ ┌──▼────┐ ┌──▼────┐
    │Email │  │ SMS  │ │In-App │ │Webhook│
    │Worker│  │Worker│ │Worker │ │Worker │
    └──────┘  └──────┘ └───────┘ └───────┘
        │       │         │         │
    ┌───▼──┐  ┌─▼────┐ ┌──▼────┐ ┌──▼────┐
    │Sendgrid│ │Twilio│ │Redis  │ │HTTP   │
    └────────┘ └──────┘ └───────┘ └───────┘
```

### Components

#### 1. API Service (Node.js)
- Receives notification requests from clients
- Validates input and user permissions
- Publishes to message queue
- Returns tracking ID to client

#### 2. Preference Service (Python)
- Manages user notification preferences
- Handles opt-in/opt-out logic
- Caches frequently accessed preferences

#### 3. Message Queue (RabbitMQ)
- Buffers notification requests
- Ensures reliable delivery to workers
- Enables horizontal scaling of workers

#### 4. Worker Services
- Email Worker: Sends via SendGrid API
- SMS Worker: Sends via Twilio API
- In-App Worker: Stores in Redis + WebSocket
- Webhook Worker: Sends to external endpoints

#### 5. Storage
- PostgreSQL: User data, preferences
- Redis: Session cache, real-time status
- MongoDB: Audit logs, historical data

## 3. Data Design

### Database Schema

**users table**
```sql
CREATE TABLE users (
  id BIGINT PRIMARY KEY,
  email VARCHAR(255) UNIQUE,
  phone VARCHAR(20),
  created_at TIMESTAMP
);

CREATE TABLE notification_preferences (
  id BIGINT PRIMARY KEY,
  user_id BIGINT REFERENCES users,
  channel VARCHAR(50), -- 'email', 'sms', 'in_app'
  enabled BOOLEAN,
  updated_at TIMESTAMP
);

CREATE TABLE notifications (
  id BIGINT PRIMARY KEY,
  user_id BIGINT REFERENCES users,
  title VARCHAR(255),
  message TEXT,
  created_at TIMESTAMP,
  delivered_at TIMESTAMP
);

CREATE TABLE delivery_logs (
  id BIGINT PRIMARY KEY,
  notification_id BIGINT REFERENCES notifications,
  channel VARCHAR(50),
  status VARCHAR(50), -- 'pending', 'delivered', 'failed'
  error_message TEXT,
  created_at TIMESTAMP
);
```

### Data Flow

1. **Request Phase**
   - Client sends notification
   - API validates and enriches data
   - Message published to queue

2. **Processing Phase**
   - Workers consume from queue
   - Check user preferences
   - Format for specific channel

3. **Delivery Phase**
   - Send via channel provider
   - Track delivery status
   - Retry on failure

4. **Tracking Phase**
   - Update delivery_logs
   - Cache status in Redis
   - Publish WebSocket event

## 4. API Design

### POST /api/v1/notifications

**Request**:
```json
{
  "user_id": "123",
  "title": "Order Shipped",
  "message": "Your order #456 has shipped",
  "channels": ["email", "in_app"],
  "priority": "high"
}
```

**Response**:
```json
{
  "notification_id": "ntf_xyz789",
  "status": "queued",
  "estimated_delivery": "2024-02-02T10:30:00Z"
}
```

**Error Response**:
```json
{
  "error": {
    "code": "INVALID_CHANNELS",
    "message": "Unknown channel: sms",
    "fields": ["channels"]
  }
}
```

### GET /api/v1/notifications/:id/status

**Response**:
```json
{
  "notification_id": "ntf_xyz789",
  "status": "delivered",
  "channels": {
    "email": {
      "status": "delivered",
      "delivered_at": "2024-02-02T10:25:00Z"
    },
    "in_app": {
      "status": "delivered",
      "delivered_at": "2024-02-02T10:24:00Z"
    }
  }
}
```

## 5. Infrastructure

### Deployment (Kubernetes)

```yaml
# Notification Service Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: notification-service
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: api
        image: notification-service:latest
        ports:
        - containerPort: 8000
        env:
        - name: QUEUE_URL
          value: amqp://rabbitmq:5672
        - name: DB_URL
          value: postgresql://postgres:5432/notifications

# Workers scaled separately
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: email-worker
spec:
  replicas: 5  # More workers during peak hours
  template:
    spec:
      containers:
      - name: worker
        image: email-worker:latest
        env:
        - name: SENDGRID_API_KEY
          valueFrom:
            secretKeyRef:
              name: sendgrid-secret
              key: api-key
```

### Scaling Strategy

**API Service**
- HPA: Scale 1-10 replicas based on CPU > 70%
- Request rate: up to 10k req/s per replica

**Workers**
- Email Worker: 5-20 replicas (high latency, large batch)
- SMS Worker: 2-10 replicas (medium latency)
- In-App Worker: 3-15 replicas (low latency)

**Database**
- Read replicas for read-heavy queries
- Connection pooling (PgBouncer)
- Sharding for delivery_logs table

## 6. Non-Functional Requirements

### Performance
- API response time: < 100ms (p99)
- Notification delivery: < 5 seconds for in-app
- Queue processing: < 1 minute backlog

### Availability
- Target SLA: 99.9% (43 minutes downtime/month)
- Multi-region deployment for disaster recovery
- Health checks and auto-restart

### Security
- API authentication via JWT tokens
- TLS encryption for all communication
- PII data masked in logs
- Rate limiting: 1000 req/minute per user

### Compliance
- GDPR: User data can be deleted on request
- CCPA: Data retention policies
- SOC 2: Audit logging and monitoring

## 7. Implementation Plan

### Phase 1 (Weeks 1-2): Foundation
- [ ] Set up infrastructure (Kubernetes cluster)
- [ ] Implement API Service core
- [ ] Set up message queue
- [ ] Database schema

### Phase 2 (Weeks 3-4): Workers
- [ ] Email worker
- [ ] SMS worker
- [ ] In-app worker
- [ ] Delivery tracking

### Phase 3 (Weeks 5-6): Features
- [ ] User preferences
- [ ] Batch processing
- [ ] Retry mechanism
- [ ] Status API

### Phase 4 (Weeks 7-8): Production
- [ ] Load testing
- [ ] Security audit
- [ ] Documentation
- [ ] Deployment and monitoring

### Timeline
- Development: 8 weeks
- Testing: 2 weeks
- Production rollout: 1 week (gradual)

### Risk Mitigation
- Risk: Queue fills up
  Mitigation: Auto-scaling workers, DLQ for failed messages

- Risk: High email volume causes SendGrid rate limit
  Mitigation: Batching, priority queues, fallback providers

- Risk: Database becomes bottleneck
  Mitigation: Read replicas, caching layer, sharding
```

## Best Practices

1. **Complete Coverage**: Include all aspects (technical, operational, business)
2. **Visual Diagrams**: Use C4 model or similar
3. **Decision Records**: Document why choices were made
4. **Evolution Plan**: How will system grow?
5. **Team Alignment**: Ensure team understands design

## Integration with Other Skills

- **`architecture-review`**: Architecture critique
- **`scalability-analysis`**: Performance planning
- **`database-schema-design`**: Data model details
- **`deployment-strategy`**: Implementation plan

