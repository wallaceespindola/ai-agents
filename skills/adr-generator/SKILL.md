---
name: adr-generator
description: Generate Architecture Decision Records (ADRs) to document important architectural decisions. Use when making significant technical choices that need to be recorded for future reference.
user-invocable: true
allowed-tools: Write, Read, Grep, Glob, Bash(git *)
---

# Architecture Decision Record (ADR) Generator

Automate the creation of ADRs using the standard ADR format to document architectural decisions.

## What is an ADR?

An Architecture Decision Record (ADR) is a document that captures an important architectural decision made along with its context and consequences.

**Why use ADRs?**
- Document the "why" behind technical decisions
- Onboard new team members faster
- Avoid revisiting old debates
- Track evolution of the system
- Share knowledge across the team

## When to Create an ADR

Create an ADR when making decisions about:

- ✅ Framework or library choices
- ✅ Database selection
- ✅ API design patterns
- ✅ Authentication/authorization approach
- ✅ Deployment architecture
- ✅ Data storage strategy
- ✅ Third-party service integrations
- ✅ Build/test/deployment tools
- ✅ Code organization patterns
- ✅ Performance optimization strategies

**Don't create ADRs for:**
- ❌ Small implementation details
- ❌ Easily reversible decisions
- ❌ Personal coding style preferences
- ❌ Obvious or standard choices

## ADR Format (MADR - Markdown ADR)

ADRs follow this structure:

```markdown
# ADR-XXXX: [Decision Title]

**Status**: [Proposed | Accepted | Deprecated | Superseded]

**Date**: YYYY-MM-DD

**Decision Makers**: [Names/Roles]

**Technical Story**: [Link to ticket/issue if applicable]

## Context and Problem Statement

[Describe the context and problem that needs a decision.
What is the issue we're trying to solve?]

## Decision Drivers

* [Driver 1 - e.g., performance requirement]
* [Driver 2 - e.g., team expertise]
* [Driver 3 - e.g., cost constraints]
* [Driver 4 - e.g., scalability needs]

## Considered Options

1. **Option 1**: [Brief description]
2. **Option 2**: [Brief description]
3. **Option 3**: [Brief description]

## Decision Outcome

**Chosen option**: "[Option X]"

**Rationale**: [Explain why this option was chosen over others]

### Positive Consequences

* [Benefit 1]
* [Benefit 2]
* [Benefit 3]

### Negative Consequences

* [Trade-off 1]
* [Trade-off 2]
* [Trade-off 3]

## Pros and Cons of the Options

### Option 1: [Name]

**Pros**:
* [Pro 1]
* [Pro 2]

**Cons**:
* [Con 1]
* [Con 2]

### Option 2: [Name]

**Pros**:
* [Pro 1]
* [Pro 2]

**Cons**:
* [Con 1]
* [Con 2]

### Option 3: [Name]

**Pros**:
* [Pro 1]
* [Pro 2]

**Cons**:
* [Con 1]
* [Con 2]

## Links

* [Related ADRs]
* [External references]
* [Documentation]
* [Discussion threads]

## Notes

[Any additional context, implementation notes, or follow-up actions]
```

## File Naming Convention

ADRs should be stored in `docs/adr/` or `docs/architecture/decisions/`:

```
docs/adr/
├── 0001-use-mongodb-for-database.md
├── 0002-adopt-fastapi-for-backend.md
├── 0003-use-nextjs-for-frontend.md
├── 0004-implement-jwt-authentication.md
└── README.md
```

**Naming pattern**: `XXXX-short-title-in-kebab-case.md`

## ADR Status Lifecycle

```
[Proposed] → [Accepted] → [Deprecated]
                ↓
           [Superseded by ADR-YYYY]
```

- **Proposed**: Under discussion, not yet decided
- **Accepted**: Decision made and implemented
- **Deprecated**: No longer relevant but kept for history
- **Superseded**: Replaced by a newer ADR (link to it)

## Example ADRs for Your Projects

### Example 1: Database Choice

```markdown
# ADR-0001: Use MongoDB for Database

**Status**: Accepted

**Date**: 2024-02-13

**Decision Makers**: Development Team

## Context and Problem Statement

We need to choose a database for the HiddenBeer application that supports
geospatial queries for finding nearby bars and can handle flexible document
structures for bars, offers, and reservations.

## Decision Drivers

* Need for geospatial queries (find bars within 1km radius)
* Flexible schema for evolving features
* Async Python support (Motor driver)
* Team familiarity
* Hosting costs

## Considered Options

1. PostgreSQL with PostGIS extension
2. MongoDB with geospatial indexes
3. MySQL with spatial extensions

## Decision Outcome

**Chosen option**: "MongoDB with geospatial indexes"

**Rationale**: MongoDB provides native geospatial support with 2dsphere indexes,
has excellent async Python support via Motor/Beanie ODM, and offers flexible
schema for rapid iteration.

### Positive Consequences

* Native geospatial query support
* Flexible schema allows fast feature development
* Excellent async support with Beanie ODM
* TTL indexes for auto-expiring documents (OTP codes, reservations)
* Team already has MongoDB experience

### Negative Consequences

* No ACID transactions across documents (acceptable for our use case)
* Requires careful index management for performance
* Schema flexibility can lead to inconsistencies without validation

## Pros and Cons of the Options

### PostgreSQL with PostGIS

**Pros**:
* ACID transactions
* Mature ecosystem
* SQL familiarity

**Cons**:
* PostGIS adds complexity
* Async support less mature (asyncpg)
* Schema migrations required for changes

### MongoDB with Geospatial Indexes

**Pros**:
* Native 2dsphere geospatial indexes
* Excellent async support (Motor, Beanie)
* Flexible schema
* TTL indexes for auto-expiry

**Cons**:
* No multi-document transactions (workaround with single-document updates)
* Need to enforce schema in application layer

### MySQL with Spatial Extensions

**Pros**:
* ACID transactions
* SQL familiarity

**Cons**:
* Spatial support less mature than PostGIS
* Limited async Python support
* Less flexible schema

## Links

* [MongoDB Geospatial Queries](https://docs.mongodb.com/manual/geospatial-queries/)
* [Beanie ODM Documentation](https://beanie-odm.dev/)

## Notes

Implementation uses:
- Beanie ODM for async MongoDB access
- 2dsphere indexes for geospatial queries
- TTL indexes for auto-expiring documents
- Compound indexes for fraud prevention
```

### Example 2: Framework Choice

```markdown
# ADR-0002: Use FastAPI for Backend Framework

**Status**: Accepted

**Date**: 2024-02-13

## Context and Problem Statement

Need to choose a Python web framework for building the HiddenBeer API that
supports async operations, has good documentation, and provides automatic
API documentation.

## Decision Drivers

* Async/await support for MongoDB operations
* Automatic API documentation (Swagger/OpenAPI)
* Type safety with Pydantic
* Performance requirements
* Developer experience

## Considered Options

1. FastAPI
2. Flask with async support
3. Django with DRF

## Decision Outcome

**Chosen option**: "FastAPI"

**Rationale**: FastAPI provides native async support, automatic API docs via
OpenAPI, type safety with Pydantic, and excellent performance. It's specifically
designed for modern async Python APIs.

### Positive Consequences

* Native async/await support (works perfectly with Motor/Beanie)
* Automatic interactive API docs (Swagger UI)
* Type safety with Pydantic schemas
* Fast performance (comparable to Node.js/Go)
* Modern Python features (type hints, dependency injection)

### Negative Consequences

* Smaller ecosystem compared to Flask/Django
* Requires understanding of async programming
* Less mature than Flask (but stable enough)

## Links

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [FastAPI vs Flask Performance](https://www.techempower.com/benchmarks/)
```

## Generating ADRs

When generating an ADR:

1. **Identify the decision**: What needs to be decided?
2. **Gather context**: Why is this decision needed?
3. **List options**: What are 2-4 alternatives?
4. **Evaluate trade-offs**: Pros and cons of each option
5. **Make recommendation**: Which option is best and why?
6. **Document consequences**: What are the implications?

## ADR Directory Structure

Create this structure in your projects:

```bash
# Create ADR directory
mkdir -p docs/adr

# Create README
cat > docs/adr/README.md << 'EOF'
# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for [Project Name].

## What is an ADR?

An ADR documents an important architectural decision made along with its context
and consequences.

## ADR Index

* [ADR-0001](0001-use-mongodb-for-database.md) - Use MongoDB for Database
* [ADR-0002](0002-adopt-fastapi-for-backend.md) - Adopt FastAPI for Backend
* [ADR-0003](0003-use-nextjs-for-frontend.md) - Use Next.js for Frontend

## Creating New ADRs

1. Copy the template from existing ADRs
2. Increment the number (find next available XXXX)
3. Use kebab-case for filename
4. Update this README with a link to the new ADR
EOF
```

## Integration with Git

Commit ADRs to version control:

```bash
# Add ADR to git
git add docs/adr/0001-decision-title.md
git commit -m "docs: add ADR-0001 for [decision]"
```

## ADR Tools

- **adr-tools**: CLI for managing ADRs (`brew install adr-tools`)
- **log4brains**: Web UI for ADRs (`npx log4brains`)
- **Manual**: Just create markdown files (simplest approach)

## Output

When this skill is invoked, it will:

1. Ask for the decision context
2. Identify options considered
3. Generate a complete ADR in markdown format
4. Suggest a filename
5. Offer to create the file in `docs/adr/`

## Remember

> "The goal of ADRs is not perfection, but thoughtful documentation of the 'why' behind decisions. Future you (and your team) will thank you."

Good ADRs are:
- **Concise**: Get to the point quickly
- **Contextual**: Explain why the decision was needed
- **Honest**: Document trade-offs and risks
- **Timely**: Written when the decision is fresh
- **Immutable**: Don't edit old ADRs, supersede them with new ones
