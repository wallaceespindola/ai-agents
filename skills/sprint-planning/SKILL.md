---
name: sprint-planning
description: Plan sprints with user stories, estimation, and team capacity planning
---

# Sprint Planning Skill

## When to Use This Skill

- Planning sprint work
- Breaking down features into stories
- Capacity planning
- Prioritization
- Sprint goals definition
- Velocity tracking

## Quick Start

```
/sprint-planning <sprint_backlog_and_capacity>
```

## Sprint Planning Template

```markdown
# Sprint 42 Planning

## Sprint Duration
2 weeks (Feb 5-16, 2024)

## Sprint Goal
"Implement user dashboard with analytics and reporting"

## Team Capacity
- Frontend: 40 points/2 weeks
- Backend: 40 points/2 weeks
- QA: 30 points/2 weeks
- **Total: 110 points**

## Sprint Backlog

### Backend Stories (40 pts)
- US-101: Create analytics API endpoint (13pts)
- US-102: Database query optimization (8pts)
- US-103: Cache layer implementation (10pts)
- US-104: Error handling (5pts)
- US-105: Performance testing (4pts)

### Frontend Stories (40 pts)
- US-201: Dashboard layout (13pts)
- US-202: Analytics chart component (10pts)
- US-203: Real-time data updates (13pts)
- US-204: Responsive design (4pts)

### QA Stories (30 pts)
- US-301: Test plan creation (8pts)
- US-302: API testing (10pts)
- US-303: UI testing (8pts)
- US-304: Performance testing (4pts)

## Capacity Notes
- Frontend engineer Alice: 2 weeks PTO (reduce to 30pts)
- Backend team: Full capacity
- QA: Full capacity

## Dependencies
- Analytics API (backend) must complete before dashboard (frontend)

## Risks
- Database migration complexity
- Third-party API delays
- Testing timeline pressure

## Definition of Done
- Code reviewed and approved
- Tests written and passing
- QA approved
- Documentation updated
```

## Story Points Guide

```
1 Point: < 1 hour (trivial task)
2 Points: 1-2 hours (very simple)
3 Points: 2-4 hours (simple)
5 Points: 4-8 hours (medium)
8 Points: 1-2 days (complex)
13 Points: 2-3 days (very complex)
21+ Points: Needs further breakdown
```

## Integration with Other Skills

- **`project-plan-generator`**: Long-term planning
- **`risk-assessment`**: Sprint risk identification
- **`retrospective-facilitator`**: Sprint retrospectives

