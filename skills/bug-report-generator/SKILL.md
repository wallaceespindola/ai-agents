---
name: bug-report-generator
description: Create detailed bug reports with reproduction steps, expected vs actual results
---

# Bug Report Generator Skill

## When to Use This Skill

- Documenting defects found during testing
- Creating actionable bug reports for developers
- Organizing bugs by priority and severity
- Tracking bugs through resolution
- Generating bug reports and metrics

## Quick Start

```
/bug-report-generator <feature_and_issue_description>
```

## Bug Report Template

```markdown
# Bug Report: [Title]

## Summary
Brief description of the issue.

## Environment
- OS: Windows 10, macOS 12, Ubuntu 20.04
- Browser: Chrome 100, Firefox 99
- Application Version: 2.1.0
- Date Found: 2024-02-02
- Tester: John Doe

## Steps to Reproduce
1. Navigate to [URL]
2. Click on [button/link]
3. Enter [data]
4. Click [button]

## Expected Result
What should happen

## Actual Result
What actually happened

## Severity
- Critical: System crash, data loss
- High: Feature broken, no workaround
- Medium: Feature partially broken
- Low: Cosmetic issue

## Screenshots/Logs
[Attach relevant screenshots, error logs]

## Suggested Fix
Optional suggestion for fix

## Related Issues
Links to similar bugs or features
```

## Example Bug Report

```markdown
# Bug Report: Payment Processing Fails with Visa Cards

## Summary
Users are unable to complete purchases with Visa cards. The payment button appears to freeze after clicking.

## Environment
- OS: Windows 10
- Browser: Chrome 120
- App Version: 3.2.1
- Date: 2024-02-02
- Tester: QA Engineer #3

## Steps to Reproduce
1. Navigate to https://example.com
2. Login with test account
3. Add any product to cart
4. Click "Proceed to Checkout"
5. Enter shipping address
6. Select "Visa" from payment methods
7. Enter card: 4111111111111111
8. Click "Place Order"

## Expected Result
- Order confirmation page appears
- Order confirmation email sent
- Order appears in order history

## Actual Result
- "Place Order" button shows loading spinner
- After 30 seconds: generic error "Payment processing failed"
- No order is created
- No error in browser console
- No email sent

## Severity
**Critical** - Blocks all Visa card purchases

## Error Messages
```
POST /api/payments failed with 500
Internal Server Error
```

## Logs
Server logs (from application logs):
```
ERROR: Payment Gateway connection timeout
Timeout connecting to payment-gateway:8443
Connection refused
```

## Screenshots
[Payment error screen]
[Browser console]
[Server error log]

## Attempted Workarounds
- Clearing browser cache: Not effective
- Using different browser: Still fails
- Using MasterCard: Works fine

## Possible Root Cause
Network connectivity issue or payment gateway misconfiguration for Visa processing endpoint.

## Suggested Fix
- Check payment gateway Visa endpoint configuration
- Verify network routing to payment processor
- Add connection retry logic with exponential backoff

## Related Issues
- Similar issue with American Express (#BR-523)
- Payment timeout issues (#BR-512)

## Developer Notes
- Assigned to: Backend Team
- Fixed in: 3.2.2 (pending verification)
```

## Bug Report Best Practices

1. **Be Specific**: Include exact steps, not generalities
2. **Reproduce Consistently**: Can it be repeated reliably?
3. **Minimize Steps**: Shortest path to reproduce
4. **Include Environment**: OS, browser, app version
5. **Attach Evidence**: Screenshots, logs, recordings
6. **Describe Impact**: How many users affected?
7. **Suggest Fix**: Optional but helpful

## Integration with Other Skills

- **`test-strategy-doc`**: Test planning finds bugs
- **`cicd-pipeline-setup`**: Automated detection
- **`monitoring-setup`**: Production bug detection

