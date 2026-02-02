---
name: test-strategy-doc
description: Create comprehensive testing strategies covering unit, integration, E2E, and non-functional testing
---

# Test Strategy Documentation Skill

## When to Use This Skill

- Creating testing plans for projects
- Defining test scope and coverage
- Planning test automation
- Defining test environments
- Resource and timeline planning
- Risk-based testing approach
- Quality metrics and reporting

## Quick Start

```
/test-strategy-doc <project_or_application_type>
```

**Example**:
```
/test-strategy-doc Web application with critical payment processing
```

## How It Works

### Test Strategy Document Components

1. **Test Objectives**
   - Ensure system meets requirements
   - Identify defects early
   - Validate performance
   - Verify security

2. **Scope**
   - In-scope: Features to test
   - Out-of-scope: Features not testing
   - Constraints: Time, budget, resources

3. **Test Levels**
   - Unit: Individual components
   - Integration: Component interactions
   - System: Complete application
   - UAT: User acceptance testing

4. **Test Types**
   - Functional: Feature testing
   - Performance: Load and stress testing
   - Security: Vulnerability testing
   - Usability: User experience testing

5. **Test Approach**
   - Risk-based: Priority based on risk
   - Behavior-driven: BDD approach
   - Exploratory: Manual testing
   - Regression: Catch regressions

6. **Tools & Environments**
   - Test automation frameworks
   - Environments: Dev, QA, Staging
   - Bug tracking system
   - Test management tools

7. **Metrics & Reporting**
   - Test coverage percentage
   - Defect metrics (open, closed, by severity)
   - Test execution reports
   - Quality gates

## Example Test Strategy

```markdown
# Test Strategy: E-Commerce Platform

## 1. Test Objectives
- Ensure all user workflows function correctly
- Validate payment processing accuracy
- Verify performance under load
- Confirm security best practices

## 2. Test Scope

### In Scope
- User registration and login
- Product browsing and search
- Shopping cart and checkout
- Payment processing
- Order tracking
- User account management

### Out of Scope
- Third-party payment provider validation
- Email delivery (mocked)
- Analytics platform

## 3. Test Levels & Types

### Unit Testing (60% effort)
- Framework: Jest (JavaScript)
- Coverage goal: 80%
- Tests: 500+
- Automated: 100%

### Integration Testing (20% effort)
- Database interactions
- API endpoints
- Service integrations
- Tests: 100+
- Automated: 100%

### System Testing (15% effort)
- Complete workflows
- End-to-end scenarios
- Tests: 50+
- Automated: 80%
- Manual: 20%

### UAT (5% effort)
- Business process validation
- User acceptance
- Manual testing only
- Test cycles: 2

## 4. Test Data Management
- Production-like anonymized data
- Test user accounts
- Sample products and orders
- Consistent test environment

## 5. Test Environment

### Development
- Local machine, CI/CD pipeline
- Real-time feedback

### QA
- Staging environment
- Test data loaded
- Performance monitoring

### Production
- Smoke tests only
- No destructive testing

## 6. Risk-Based Priorities

### Critical (High Priority)
- Payment processing (50+ test cases)
- User authentication (30+ test cases)
- Data integrity (20+ test cases)

### Important (Medium Priority)
- Product search (15+ test cases)
- Order management (20+ test cases)

### Nice-to-Have (Low Priority)
- UI animations (5+ test cases)
- Email templates (5+ test cases)

## 7. Defect Management

### Severity Levels
- Critical: System down, data loss
- High: Feature broken, workaround exists
- Medium: Feature partially broken
- Low: Cosmetic issue

### Acceptance Criteria
- Critical: Fixed before release
- High: Fixed in current release
- Medium: Fixed in next release
- Low: Backlog

## 8. Test Metrics

### Coverage Metrics
- Code coverage: Target 80%
- Feature coverage: 100%
- Platform coverage: Win/Mac/Linux, Chrome/Firefox/Safari

### Defect Metrics
- Defect density: < 5 per 1000 LOC
- Escape rate: < 2% (defects found in production)
- Fix rate: 90% within 48 hours

### Test Execution
- Pass rate: > 98%
- Test execution time: < 30 minutes for full suite
- Flakiness: < 1% (tests that randomly fail)

## 9. Timeline

- Unit testing: Ongoing (daily)
- Integration testing: Weekly (after code changes)
- System testing: Bi-weekly
- UAT: Before release

## 10. Resources

- QA Lead: 1 person (test planning, strategy)
- QA Engineers: 3 people (test automation, execution)
- QA Testers: 2 people (manual testing, UAT)

## 11. Entry/Exit Criteria

### Entry (When testing begins)
- Requirements finalized
- Development 70% complete
- Test environment ready
- Test cases reviewed

### Exit (When testing stops)
- 98% test pass rate achieved
- All critical/high bugs fixed
- Coverage targets met
- UAT approved

## 12. Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Insufficient test data | Test delays | Create data generation scripts |
| Environment instability | Test failures | Dedicated QA environment |
| Scope creep | Timeline slips | Strict change control |
| Resource shortage | Coverage gaps | Cross-training, contractors |
```

## Integration with Other Skills

- **`test-automation-setup`**: Automation framework setup
- **`test-case-generator`**: Test case creation
- **`cicd-pipeline-setup`**: Automated testing in CI/CD
- **`bug-report-generator`**: Defect documentation

