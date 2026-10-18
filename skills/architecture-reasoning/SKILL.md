---
name: architecture-reasoning
description: Deep architectural analysis and design reasoning for software systems. Use when designing new systems, evaluating architecture decisions, or refactoring existing codebases.
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash(make *), Bash(docker *), WebSearch
---

# Architecture Reasoning Framework

Systematic approach to software architecture design and evaluation.

## When to Use This Skill

- Designing new system architecture
- Evaluating architectural trade-offs
- Refactoring or modernizing existing systems
- Choosing between architectural patterns
- Scaling considerations
- Performance optimization planning
- Security architecture review

## Architecture Analysis Framework

### 1. Requirements Analysis

**Functional Requirements:**
- What does the system need to do?
- What are the core use cases?
- What are the performance requirements?
- What are the scalability requirements?

**Non-Functional Requirements:**
- Performance (latency, throughput)
- Scalability (horizontal, vertical)
- Reliability (uptime, fault tolerance)
- Security (authentication, authorization, data protection)
- Maintainability (code quality, documentation)
- Observability (logging, monitoring, tracing)

### 2. Current State Assessment

For existing systems:
- **Technology Stack**: What's currently used?
- **Pain Points**: What's not working well?
- **Bottlenecks**: Where are the performance issues?
- **Technical Debt**: What needs refactoring?
- **Data Flow**: How does data move through the system?

### 3. Architecture Patterns Evaluation

**Monolithic vs Microservices:**
- Monolithic: Simple deployment, easier local dev, single codebase
- Microservices: Independent scaling, technology flexibility, complexity

**Layered Architecture:**
- Presentation → Business Logic → Data Access
- Clear separation of concerns
- Easy to understand and maintain

**Event-Driven Architecture:**
- Asynchronous processing
- Loose coupling
- Better scalability
- More complex debugging

**CQRS (Command Query Responsibility Segregation):**
- Separate read and write models
- Optimized queries
- Complex to implement

**Hexagonal/Clean Architecture:**
- Business logic independent of frameworks
- Testable without external dependencies
- More boilerplate

### 4. Technology Selection Criteria

**Database Choice:**
- Relational (PostgreSQL, MySQL): ACID, complex queries, transactions
- Document (MongoDB): Flexible schema, horizontal scaling, geospatial
- Key-Value (Redis): Caching, sessions, real-time
- Time-Series (InfluxDB, TimescaleDB): Metrics, IoT data

**API Design:**
- REST: Standard, cacheable, stateless
- GraphQL: Flexible queries, reduce over-fetching
- gRPC: High performance, type-safe, streaming
- WebSocket: Real-time, bidirectional

**Frontend Architecture:**
- SSR (Server-Side Rendering): SEO, fast initial load
- CSR (Client-Side Rendering): Rich interactions, SPA
- SSG (Static Site Generation): Fast, cacheable, low cost
- Islands/Partial Hydration: Best of both worlds

### 5. Scalability Analysis

**Horizontal Scaling:**
- Add more instances
- Requires stateless design
- Load balancing needed
- Better fault tolerance

**Vertical Scaling:**
- Bigger machines
- Simpler architecture
- Hardware limits
- Single point of failure

**Caching Strategy:**
- CDN (static assets)
- Application cache (Redis, Memcached)
- Database query cache
- Client-side cache

**Database Scaling:**
- Read replicas
- Sharding
- Connection pooling
- Denormalization

### 6. Security Architecture

**Authentication & Authorization:**
- OAuth 2.0 / OIDC
- JWT tokens
- Session-based
- API keys

**Data Security:**
- Encryption at rest
- Encryption in transit (TLS/SSL)
- Secrets management (Vault, AWS Secrets Manager)
- PII handling

**API Security:**
- Rate limiting
- Input validation
- CORS configuration
- API gateway

**Network Security:**
- Firewall rules (UFW, security groups)
- VPN for internal services
- DDoS protection
- WAF (Web Application Firewall)

### 7. Observability & Monitoring

**Logging:**
- Structured logging (JSON)
- Centralized logging (ELK, CloudWatch)
- Log levels (DEBUG, INFO, WARN, ERROR)
- Request tracing

**Metrics:**
- Application metrics (response time, error rate)
- Infrastructure metrics (CPU, memory, disk)
- Business metrics (users, conversions)
- Time-series database (Prometheus, Grafana)

**Tracing:**
- Distributed tracing (Jaeger, Zipkin)
- Request correlation IDs
- Span tracking across services

**Alerting:**
- Error rate thresholds
- Performance degradation
- Resource exhaustion
- On-call rotation

### 8. Deployment Architecture

**Deployment Strategies:**
- Blue-Green: Zero downtime, instant rollback
- Canary: Gradual rollout, reduced risk
- Rolling: Sequential update, no downtime
- Recreate: Simple, brief downtime

**Infrastructure:**
- Containers (Docker)
- Orchestration (Kubernetes, Docker Compose, systemd)
- Serverless (Lambda, Cloud Functions)
- VPS (DigitalOcean, Linode, Hetzner)

**CI/CD:**
- Automated testing
- Automated deployment
- Environment parity (dev, staging, prod)
- Rollback procedures

### 9. Cost Optimization

**Infrastructure Costs:**
- Right-sizing instances
- Auto-scaling policies
- Spot instances (AWS, GCP)
- Reserved instances

**Operational Costs:**
- Monitoring costs
- Data transfer costs
- Third-party services
- Developer time

### 10. Migration & Evolution Strategy

**Strangler Fig Pattern:**
- Gradually replace old system
- Run both systems in parallel
- Route traffic to new system incrementally
- Retire old system when complete

**Feature Flags:**
- Toggle features on/off
- A/B testing
- Gradual rollout
- Emergency kill switch

## Architecture Decision Template

When making architecture decisions, document:

1. **Context**: What's the situation?
2. **Decision**: What did we decide?
3. **Rationale**: Why did we decide this?
4. **Alternatives**: What else did we consider?
5. **Consequences**: What are the trade-offs?
6. **Status**: Proposed, Accepted, Deprecated, Superseded

## Common Anti-Patterns to Avoid

❌ **Premature Optimization**: Don't optimize before measuring
❌ **Over-Engineering**: Keep it simple (YAGNI - You Aren't Gonna Need It)
❌ **Tight Coupling**: Avoid dependencies that make changes hard
❌ **Missing Observability**: Always add logging and monitoring
❌ **Ignoring Security**: Security is not an afterthought
❌ **No Testing Strategy**: Tests prevent regressions
❌ **Vendor Lock-In**: Consider portability and exit strategies
❌ **Ignoring CAP Theorem**: Can't have Consistency, Availability, and Partition tolerance

## Architecture Review Checklist

- [ ] Does it meet functional requirements?
- [ ] Does it meet non-functional requirements?
- [ ] Is it scalable (can it handle 10x load)?
- [ ] Is it secure (defense in depth)?
- [ ] Is it observable (logs, metrics, traces)?
- [ ] Is it maintainable (clear code, good docs)?
- [ ] Is it testable (unit, integration, e2e)?
- [ ] Is it cost-effective (infrastructure + operational costs)?
- [ ] Is it reliable (fault tolerance, redundancy)?
- [ ] Can it be deployed safely (rollback, blue-green)?
- [ ] Is technical debt documented?
- [ ] Are failure modes understood?

## Output Format

When performing architecture reasoning, provide:

1. **Current State Analysis** (if applicable)
2. **Requirements Summary**
3. **Proposed Architecture** (diagrams welcome)
4. **Technology Stack Justification**
5. **Scalability Plan**
6. **Security Considerations**
7. **Deployment Strategy**
8. **Trade-offs & Risks**
9. **Migration Plan** (if refactoring)
10. **Next Steps**

## Tools to Leverage

- **Mermaid MCP**: Create architecture diagrams
- **PlantUML MCP**: Create UML diagrams
- **Context7 MCP**: Research latest framework best practices
- **Docker MCP**: Analyze container architecture
- **MongoDB/PostgreSQL MCP**: Database schema analysis

## Remember

> "The best architecture is the one that solves the problem at hand with the minimum complexity necessary. It's not about using the latest tech, it's about making thoughtful trade-offs."

Good architecture is:
- **Fit for purpose** - Solves the actual problem
- **Evolvable** - Can change as requirements change
- **Observable** - Can see what's happening
- **Testable** - Can verify it works
- **Documented** - Team understands it
