---
name: project-plan-generator
description: Create comprehensive project plans with timelines, milestones, and resource allocation
---

# Project Plan Generator Skill

## When to Use This Skill

- Planning new projects
- Estimating project timelines
- Allocating resources
- Identifying dependencies
- Risk planning
- Budget forecasting

## Quick Start

```
/project-plan-generator <project_description>
```

## Project Plan Template

```markdown
# Project Plan: [Project Name]

## Executive Summary
- Objectives
- Success criteria
- Timeline: Start - End
- Budget estimate

## Scope
- In-scope features
- Out-of-scope items
- Constraints and assumptions

## Timeline & Milestones

### Phase 1: Planning (Weeks 1-2)
- [ ] Requirements gathering
- [ ] Architecture design
- [ ] Team setup
- Deliverable: Requirements document

### Phase 2: Development (Weeks 3-8)
- [ ] Backend API
- [ ] Frontend UI
- [ ] Database setup
- Deliverable: MVP v1.0

### Phase 3: Testing (Weeks 9-10)
- [ ] QA testing
- [ ] Bug fixes
- [ ] Performance optimization
- Deliverable: Production-ready release

### Phase 4: Launch (Week 11)
- [ ] Production deployment
- [ ] Monitoring setup
- [ ] Documentation
- Deliverable: Live system

## Resource Allocation

| Role | FTE | Weeks | Total Effort |
|------|-----|-------|--------------|
| PM | 1.0 | 11 | 44 days |
| Architect | 0.5 | 11 | 22 days |
| Backend | 2.0 | 8 | 80 days |
| Frontend | 1.0 | 8 | 40 days |
| QA | 1.0 | 3 | 15 days |
| **Total** | | | 201 days |

## Budget Estimate

- Personnel: $400,000
- Infrastructure: $50,000
- Tools/Licenses: $25,000
- Contingency (15%): $81,250
- **Total: $556,250**

## Risk Management

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Scope creep | High | High | Strict change control |
| Resource shortage | Medium | High | Cross-training |
| Tech challenges | Medium | Medium | Proof of concept |

## Success Criteria
- [ ] All features implemented
- [ ] >95% test pass rate
- [ ] <100ms API response time
- [ ] Zero critical defects
- [ ] User acceptance achieved
```

## Integration with Other Skills

- **`sprint-planning`**: Detailed sprint planning
- **`risk-assessment`**: Risk identification
- **`status-report-generator`**: Progress reporting

