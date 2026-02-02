---
name: status-report-generator
description: Generate project status reports with progress, risks, and blockers
---

# Status Report Generator Skill

## When to Use This Skill

- Weekly/biweekly project updates
- Executive reporting
- Stakeholder communication
- Issue escalation
- Progress tracking

## Quick Start

```
/status-report-generator <project_name>
```

## Status Report Template

```markdown
# Project Status Report
**Project**: E-Commerce Platform v2.0
**Reporting Period**: Week of Feb 5-11, 2024
**Status**: ON TRACK (Green)

## Executive Summary
Core features on schedule. Dashboard implementation completed. One dependency delay from payment provider.

## Progress (This Week)

### Completed
- ✓ User authentication system (100%)
- ✓ Product catalog API (95%)
- ✓ Shopping cart functionality (100%)

### In Progress
- 🔄 Payment integration (60%, due Feb 15)
- 🔄 Order tracking (40%, due Feb 20)
- 🔄 Admin dashboard (75%, due Feb 13)

### Not Started
- ⏳ Analytics module (planned Feb 24)
- ⏳ Mobile app (planned March 1)

## Velocity Tracking

| Sprint | Points Completed | Capacity | Utilization |
|--------|-----------------|----------|-------------|
| Sprint 40 | 95 | 110 | 86% |
| Sprint 41 | 108 | 110 | 98% |
| Sprint 42 | 85/110 (projected) | 110 | 77% |

## Key Metrics

- **Burn-down**: On track (68% complete)
- **Defect Rate**: 0.8 per 1000 LOC (target: <1.0)
- **Test Coverage**: 82% (target: 80%)
- **Production Incidents**: 0 this week

## Risks & Issues

### Critical Issues (Red)
- **Payment API Delay**: Third-party payment provider delayed SDK (1 week impact)
  - Mitigation: Use backup provider, parallel track
  - Owner: Backend Lead
  - Resolution: Feb 12

### High Issues (Yellow)
- **Database Performance**: Query optimization needed (estimated 3 days)
  - Status: In progress
  - Owner: DBA
  - Resolution: Feb 10

### Medium Issues (Blue)
- **iOS Testing**: Device availability limited
  - Mitigation: Rent devices from cloud provider
  - Cost: $500

## Blockers
- [ ] None currently

## Upcoming Milestones

- Feb 13: Admin dashboard complete
- Feb 15: Payment integration complete
- Feb 20: Beta launch (100 users)
- March 1: General availability

## Budget Status
- Spend to date: $285k / $350k budget (81%)
- Projected final: $340k (97%)
- Variance: -$10k (favorable)

## Team Status
- Headcount: 8/8 (full)
- Morale: High
- Turnover: 0

## Next Week Priorities
1. Complete payment integration
2. Begin order tracking feature
3. Performance testing
4. Prepare beta launch

## Stakeholder Decisions Needed
- [ ] Approve analytics module scope (required by Feb 12)
- [ ] Decision on iOS vs Android priority (due Feb 10)
```

## Status Color Coding

- 🟢 **Green**: On track
- 🟡 **Yellow**: Minor delays, manageable
- 🔴 **Red**: Major issues, needs escalation

## Integration with Other Skills

- **`project-plan-generator`**: Project planning
- **`risk-assessment`**: Risk updates
- **`sprint-planning`**: Sprint status

