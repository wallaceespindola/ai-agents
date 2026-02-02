---
name: risk-assessment
description: Identify project risks, assess probability and impact, and create mitigation plans
---

# Risk Assessment Skill

## When to Use This Skill

- Project risk identification
- Risk probability and impact analysis
- Creating mitigation strategies
- Contingency planning
- Risk monitoring
- Escalation planning

## Quick Start

```
/risk-assessment <project_or_initiative>
```

## Risk Assessment Template

```markdown
# Risk Assessment Matrix

## Critical Risks (High Probability + High Impact)

### Risk 1: Key Team Member Departure
- **Probability**: Medium (30%)
- **Impact**: High ($200k+ cost)
- **Mitigation**: Cross-train backup, competitive salary review
- **Owner**: HR Manager
- **Review**: Monthly

### Risk 2: Technology Stack Mismatch
- **Probability**: Medium (40%)
- **Impact**: High (3 month delay)
- **Mitigation**: Proof of concept sprint, tech review
- **Owner**: Tech Lead
- **Review**: After POC

## High Risks (Either High Probability or High Impact)

### Risk 3: Scope Creep
- **Probability**: High (80%)
- **Impact**: Medium (2 week delay)
- **Mitigation**: Strict change control, MVP approach
- **Owner**: Product Manager

### Risk 4: Budget Overrun
- **Probability**: High (60%)
- **Impact**: Medium (10% budget increase)
- **Mitigation**: Weekly budget tracking, contingency fund
- **Owner**: Finance

## Medium Risks

### Risk 5: Third-party Service Outage
- **Probability**: Low (20%)
- **Impact**: Medium (1 day delay)
- **Mitigation**: Fallback provider, SLA requirements
- **Owner**: DevOps

### Risk 6: Performance Issues
- **Probability**: Medium (50%)
- **Impact**: Low (optimization sprint)
- **Mitigation**: Early performance testing, profiling
- **Owner**: Backend Lead

## Risk Response Strategies

1. **Avoid**: Change approach to eliminate risk
2. **Mitigate**: Reduce probability or impact
3. **Accept**: Live with the risk
4. **Transfer**: Shift risk to third party (insurance)

## Risk Register

| ID | Risk | Prob | Impact | Status | Owner | Mitigation | Review Date |
|----|------|------|--------|--------|-------|-----------|------------|
| R1 | Key person leaves | 30% | High | Active | HR | Cross-train | Monthly |
| R2 | Tech stack fails | 40% | High | Active | Tech Lead | POC | After POC |
| R3 | Scope creep | 80% | Med | Active | PM | Change control | Weekly |

## Contingency Plans

### If R1 Occurs (Key Team Member Leaves)
- Execute knowledge transfer from backup
- Hire replacement (2-4 week process)
- Adjust timeline by 1 month
- Cost: $50k replacement cost

### If R2 Occurs (Technology Stack Issues)
- Execute fallback technology plan
- 2-week rework sprint
- 2-week delay to timeline
```

## Integration with Other Skills

- **`project-plan-generator`**: Risk in project planning
- **`sprint-planning`**: Sprint-level risks
- **`status-report-generator`**: Risk status updates

