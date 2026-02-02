---
name: retrospective-facilitator
description: Facilitate sprint retrospectives and team reflection sessions
---

# Retrospective Facilitator Skill

## When to Use This Skill

- Conducting sprint retrospectives
- Team improvement planning
- Identifying blockers and solutions
- Celebrating wins
- Continuous improvement

## Quick Start

```
/retrospective-facilitator <sprint_or_project>
```

## Retrospective Format

```markdown
# Sprint 42 Retrospective
**Date**: Friday, Feb 16, 2024
**Duration**: 1.5 hours
**Attendees**: Full team (8 people)

## What Went Well ✅

### Team Collaboration
"Great communication between backend and frontend teams. Daily standups were very effective."
- Owner: Sarah (Frontend Lead)

### Velocity
"We completed 108 points, highest in 5 sprints"
- Owner: John (Backend Lead)

### Quality
"No critical bugs escaped to production"
- Owner: Mike (QA)

### Innovation
"The caching layer optimization reduced API latency by 40%"
- Owner: Dev Team

## What Didn't Go Well ❌

### Third-party Delays
"Payment provider API delay blocked us for 2 days"
- Impact: Minor (1 day schedule impact)
- Action: Use backup provider in future

### Database Performance
"Queries took longer than expected, needed optimization mid-sprint"
- Impact: Medium (2 days rework)
- Action: Earlier performance testing next sprint

### Communication
"Some team members didn't update tickets in real-time"
- Impact: Low (some confusion)
- Action: Update ticket workflow expectations

## Improvement Actions

### Action Items (Next Sprint)

| Action | Owner | Due | Status |
|--------|-------|-----|--------|
| Set up automated DB performance checks | John | Sprint 43 | TODO |
| Create API fallback strategy | Sarah | Sprint 43 | TODO |
| Define ticket update SLA | PM | Sprint 43 | TODO |
| Host Git workflow training | Lead Dev | Sprint 43 | TODO |

### What Will We Try Different?

1. **Earlier Performance Testing**
   - Rationale: Performance issues discovered mid-sprint
   - Solution: Add perf tests to Definition of Done
   - Owner: QA

2. **Backup Provider Integration**
   - Rationale: Third-party delays blocked progress
   - Solution: Integrate backup payment provider
   - Owner: Backend

3. **Automated Ticket Updates**
   - Rationale: Manual updates cause delays
   - Solution: GitHub Actions to auto-update tickets
   - Owner: DevOps

## Team Recognition

- **Best Collaborator**: Sarah (cross-team support)
- **Most Productive**: John (fixed complex cache issue)
- **Best Bug Hunter**: Mike (caught subtle race condition)

## Metrics Review

| Metric | Sprint 41 | Sprint 42 | Target | Status |
|--------|----------|----------|--------|--------|
| Velocity | 108pts | 108pts | 100pts | ✓ |
| Defects/1000 LOC | 0.9 | 0.8 | <1.0 | ✓ |
| Test Coverage | 80% | 82% | >80% | ✓ |
| Production Incidents | 1 | 0 | 0 | ✓ |

## Team Morale Check

- Satisfaction: 8.2/10 (↑ from 7.8)
- Confidence: 8.5/10 (→)
- Work-life balance: 7/10 (↓ 0.5 - deadline stress)

## Next Sprint Goals

1. Maintain velocity (target: 110pts)
2. Implement 2 improvement actions
3. Reduce technical debt by 2 items
4. Achieve 85% test coverage

## Follow-up

- **1-on-1s**: Schedule personal feedback with team members
- **Action Tracking**: Weekly check-in on improvement items
- **Next Retro**: Friday, Mar 1, 2024
```

## Retrospective Formats

### Start-Stop-Continue
- What should we **start** doing?
- What should we **stop** doing?
- What should we **continue** doing?

### Liked-Learned-Lacked
- What did we **like** about the sprint?
- What did we **learn**?
- What did we **lack**?

### 4Ls Framework
- **Liked**: Positive experiences
- **Learned**: Knowledge gains
- **Lacked**: Missing elements
- **Longed for**: Desired improvements

## Integration with Other Skills

- **`sprint-planning`**: Next sprint planning
- **`project-plan-generator`**: Project improvement
- **`status-report-generator`**: Team metrics reporting

