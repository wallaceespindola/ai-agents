---
name: e2e-testing-setup
description: Set up end-to-end testing frameworks for complete user workflows
---

# E2E Testing Setup Skill

## When to Use This Skill

- Setting up browser automation testing
- Testing complete user journeys
- Cross-browser testing
- Mobile testing
- Continuous integration E2E tests
- Regression testing

## Quick Start

```
/e2e-testing-setup <application_type>
```

## Popular E2E Frameworks

- **Cypress**: Best DX, Chrome/Edge/Firefox
- **Playwright**: Multi-browser, cross-platform
- **Selenium**: Industry standard, all browsers
- **Puppeteer**: Chrome/Chromium focused

## Example: Cypress Test

```javascript
describe('E2E: Complete Purchase Flow', () => {
  beforeEach(() => {
    cy.visit('https://example.com');
    cy.login('test@example.com', 'password123');
  });

  it('should complete purchase from product to confirmation', () => {
    // Browse products
    cy.contains('Electronics').click();
    cy.contains('Laptop').click();

    // Add to cart
    cy.get('[data-testid="add-to-cart"]').click();
    cy.get('.cart-badge').should('contain', '1');

    // Checkout
    cy.get('[data-testid="checkout"]').click();
    cy.get('#address').type('123 Main St');
    cy.get('#city').type('New York');

    // Payment
    cy.frameLoaded('[title="Stripe"]');
    cy.iframe().find('[name="cardnumber"]').type('4111111111111111');
    cy.iframe().find('[name="exp-date"]').type('12/25');
    cy.iframe().find('[name="cvc"]').type('123');

    // Confirm
    cy.get('button:contains("Place Order")').click();
    cy.url().should('include', '/order-confirmation');
    cy.get('h1').should('contain', 'Thank you for your order');
  });
});
```

## Best Practices

1. **Test user workflows**: Not implementation details
2. **Use data-testid**: Avoid brittle selectors
3. **Wait strategically**: Use proper waits, not sleep()
4. **Keep tests focused**: One scenario per test
5. **Parallel execution**: Run tests in parallel
6. **Headless mode**: Faster execution

## Integration with Other Skills

- **`test-strategy-doc`**: E2E test planning
- **`cicd-pipeline-setup`**: E2E tests in CI/CD
- **`frontend-performance`**: Performance E2E tests

