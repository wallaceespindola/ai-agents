---
name: architecture-review
description: Review and critique system architecture for scalability, maintainability, and best practices
---

# Architecture Review Skill

## When to Use This Skill

- Reviewing system architecture designs
- Identifying architectural anti-patterns
- Evaluating scalability and performance
- Assessing maintainability and complexity
- Validating technology choices
- Reviewing microservices designs
- Evaluating data flow and consistency
- Planning architectural refactoring

## Quick Start

```
/architecture-review <system_or_component_architecture>
```

**Example**:
```
/architecture-review Multi-tier e-commerce platform with microservices and distributed database
```

## How It Works

The skill performs comprehensive architecture assessment:

### 1. Architecture Patterns
- **Monolithic**: Single deployment unit
- **Microservices**: Independent services
- **Serverless**: Event-driven functions
- **Hybrid**: Combined approaches
- **Event-Driven**: Async message-based

### 2. Quality Assessment
- **Scalability**: Handle growth and load
- **Reliability**: Fault tolerance and resilience
- **Maintainability**: Code organization and clarity
- **Performance**: Response times and throughput
- **Security**: Data protection and access control

### 3. Technology Evaluation
- **Language Fit**: Does language match problem?
- **Framework Choice**: Appropriate for requirements?
- **Database**: Correct data model and scale?
- **Infrastructure**: Cloud, on-premise, hybrid?
- **Tools**: Testing, monitoring, deployment?

### 4. Design Review Areas
- **API Design**: Endpoint structure and contracts
- **Database Design**: Schema, indexing, partitioning
- **Caching Strategy**: Where and what to cache
- **Async Processing**: Queues and workers
- **Search**: Indexing and query performance

### 5. Anti-patterns Detection
- **God Objects**: Classes doing too much
- **Tight Coupling**: Hard to change independently
- **Data Silos**: Isolated data stores
- **Single Point of Failure**: No redundancy
- **Over-engineering**: Unnecessary complexity

### 6. Scalability Analysis
- **Vertical Scaling**: CPU, memory, storage
- **Horizontal Scaling**: Multiple servers
- **Database Scaling**: Replication, sharding
- **Caching Layers**: Distributed caching
- **Load Balancing**: Traffic distribution

### 7. Risk Assessment
- **Technical Debt**: Accumulated shortcuts
- **Vendor Lock-in**: Technology dependencies
- **Compliance**: Regulatory requirements
- **Security Gaps**: Potential vulnerabilities
- **Operational Burden**: Maintenance complexity

## Examples

### Example 1: Monolithic vs Microservices

```
MONOLITHIC ARCHITECTURE (Tight Coupling)
┌─────────────────────────────────────────┐
│ Application Server                      │
│ ┌──────────────────────────────────────┐│
│ │ User Service                         ││
│ │ - Register, Login, Profile           ││
│ └──────────────────────────────────────┘│
│ ┌──────────────────────────────────────┐│
│ │ Product Service                      ││
│ │ - Catalog, Search, Details           ││
│ └──────────────────────────────────────┘│
│ ┌──────────────────────────────────────┐│
│ │ Order Service                        ││
│ │ - Create, Track, History             ││
│ └──────────────────────────────────────┘│
│ ┌──────────────────────────────────────┐│
│ │ Payment Service                      ││
│ │ - Process, Refund, History           ││
│ └──────────────────────────────────────┘│
│ └─→ Single Database                    │
└─────────────────────────────────────────┘

Issues:
- Large deployments (full restart)
- Shared database (data silos)
- Scaling entire app for one bottleneck
- Technology locked to one stack


MICROSERVICES ARCHITECTURE (Loose Coupling)
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ User Service │  │Product Svc   │  │ Order Svc    │  │Payment Svc   │
│ (Node.js)    │  │ (Python)     │  │ (Java)       │  │ (Go)         │
├──────────────┤  ├──────────────┤  ├──────────────┤  ├──────────────┤
│ User DB      │  │ Product DB   │  │ Order DB     │  │Payment DB    │
│ (PostgreSQL) │  │ (MongoDB)    │  │ (MySQL)      │  │ (PostgreSQL) │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │                 │
       └─────────────────┴─────────────────┴─────────────────┘
                    Message Queue (RabbitMQ/Kafka)
                    API Gateway

Benefits:
- Independent deployments
- Technology diversity
- Separate scaling
- Fault isolation

Challenges:
- Distributed tracing
- Data consistency
- Network latency
- Operational complexity
```

### Example 2: Architecture Assessment

```markdown
## Architecture Review Report

### 1. Current Architecture
- **Type**: Monolithic web application
- **Stack**: Node.js + Express + PostgreSQL
- **Deployment**: Single server + RDS
- **Team Size**: 8 engineers

### 2. Strengths
✓ Simple deployment pipeline
✓ Single database simplifies transactions
✓ Lower operational complexity
✓ Easier debugging and troubleshooting
✓ Works well for team size

### 3. Pain Points
✗ Deployment takes 30 minutes
✗ Database queries slow during peak
✗ Can't scale specific features independently
✗ Hard to adopt new technologies
✗ One engineer's mistake affects everyone

### 4. Recommendations

#### Short Term (3-6 months)
1. Implement caching layer (Redis)
   - Cache product catalog (TTL: 1 hour)
   - Cache user sessions
   - Expected: 40% DB query reduction

2. Database optimization
   - Add indexes on frequently queried columns
   - Implement connection pooling
   - Expected: 20% query improvement

3. API rate limiting
   - Prevent abuse
   - Smooth traffic spikes

#### Medium Term (6-12 months)
1. Async job processing
   - Extract email/notification sending
   - Use job queue (Bull/RabbitMQ)
   - Reduces response times by 50%

2. Read replicas
   - Separate read/write databases
   - Scale read-heavy operations
   - Maintain transaction consistency

#### Long Term (12+ months)
1. Microservices extraction
   - Extract payment service first (least coupled)
   - Then notification service
   - Eventually: auth, products, orders
   - One service at a time

### 5. Risk Assessment
- **Low Risk**: Add caching, indexing (days)
- **Medium Risk**: Async jobs, read replicas (weeks)
- **High Risk**: Microservices (months, needs architecture redesign)

### 6. Technology Choices
- ✓ Node.js: Good for I/O-heavy workloads
- ✓ PostgreSQL: ACID transactions, good for relational data
- ? Express: Consider Next.js for frontend integration
- Suggested: Add TypeScript for type safety
```

### Example 3: API Design Review

```typescript
// ❌ PROBLEMATIC API DESIGN
GET /api/user/123                    // User info
GET /api/user/123/orders             // User orders
GET /api/user/123/orders/456          // Specific order
POST /api/orders                      // Create order
PUT /api/orders/456                   // Update order
DELETE /api/orders/456                // Delete order
GET /api/admin/all-users              // List all users
POST /api/admin/users/123/disable     // Admin action

Issues:
- Inconsistent resource structure
- Mixed responsibilities in single endpoint
- Admin vs regular endpoints mixed
- No version prefix (API changes break clients)
- No pagination on list endpoints


// ✅ IMPROVED API DESIGN
GET /api/v1/users/:id                           // Get user
GET /api/v1/users/:id/orders                    // User orders (paginated)
GET /api/v1/users/:id/orders/:orderId           // Specific order
POST /api/v1/orders                             // Create order
PUT /api/v1/orders/:orderId                     // Update order
DELETE /api/v1/orders/:orderId                  // Delete order

// Admin API on separate subdomain
GET /api/v1/admin/users                         // List users (paginated)
POST /api/v1/admin/users/:id/disable            // Admin action
PUT /api/v1/admin/users/:id                     // Update user

// Consistent pagination
GET /api/v1/orders?page=1&limit=20&sort=-created_at

// Consistent error responses
{
  "error": {
    "code": "INVALID_INPUT",
    "message": "Email is required",
    "details": {
      "field": "email",
      "reason": "required"
    }
  }
}

Benefits:
- Clear resource hierarchy
- Consistent structure
- Easy to extend
- Client-friendly
- Versionable
```

### Example 4: Scalability Analysis

```
CURRENT STATE: Single server can handle 100 req/s

┌──────────────┐
│ Application  │ 100 req/s
│ Node.js      │ 500MB RAM
│ Express      │ 2 CPU cores
└──────────────┘

BOTTLENECK IDENTIFICATION:
- CPU: Single core processing
- Memory: Session storage growing
- Database: Shared queries bottleneck
- I/O: Network latency to services


SCALING STRATEGY:

Phase 1: Cache Layer
┌──────────────┐  ┌──────────┐
│ Application  │→ │ Redis    │  Capacity: 200 req/s
│ Node.js      │  │ Cache    │
└──────────────┘  └──────────┘
                     ↓
                  ┌──────────┐
                  │Database  │
                  └──────────┘

Phase 2: Horizontal Scaling
┌──────────────┐
│ Load Balancer│
└──────┬───────┘
       ├──────────┬──────────┬──────────┐
       ↓          ↓          ↓          ↓
    ┌────┐    ┌────┐    ┌────┐    ┌────┐
    │App1│    │App2│    │App3│    │App4│  Capacity: 400 req/s
    └────┘    └────┘    └────┘    └────┘
         └─────┬─────────┬─────┐
               ↓         ↓     ↓
            ┌──────┐  ┌──────────┐
            │Redis │  │Database  │
            └──────┘  │Replicas  │
                      └──────────┘

Phase 3: Database Sharding
Shard 1: Users A-M
Shard 2: Users N-Z

Total capacity after optimizations:
- Cache hit ratio: 70% → 70% requests never hit DB
- 30% hitting DB at 400 req/s = 120 req/s per DB
- Read replicas: 4x scaling
- Result: ~1,600 req/s
```

## Best Practices

### 1. Architecture Review Checklist
- [ ] Scalability plan documented
- [ ] Single points of failure identified
- [ ] Data consistency strategy clear
- [ ] Deployment strategy documented
- [ ] Disaster recovery plan exists
- [ ] Monitoring and alerting designed
- [ ] Security review completed
- [ ] Cost analysis performed

### 2. Documentation Requirements
- Architecture Decision Records (ADRs)
- System design diagrams
- Data flow documentation
- Technology stack rationale
- Deployment procedures

### 3. Red Flags
- No documented architecture
- Single point of failure
- No monitoring or observability
- Manual deployment processes
- No disaster recovery plan

## Integration with Other Skills

- **`system-design-doc`**: Detailed architecture documentation
- **`scalability-analysis`**: Deep performance analysis
- **`pattern-recommendation`**: Design pattern guidance
- **`api-design`**: REST API design review

