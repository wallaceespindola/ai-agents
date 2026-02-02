---
name: test-case-generator
description: Generate comprehensive test cases from requirements using black box and white box techniques
---

# Test Case Generator Skill

## When to Use This Skill

- Creating test cases from requirements
- Generating edge case and boundary value tests
- Creating combinatorial test cases
- Documenting test scenarios
- Preparing for QA execution
- Regression testing planning

## Quick Start

```
/test-case-generator <feature_or_requirement>
```

**Example**:
```
/test-case-generator User registration form with email validation
```

## Test Case Techniques

### 1. Boundary Value Analysis
Test at boundaries of valid input ranges.

```
Login Form - Password field:
- Valid: 8-20 characters
- Boundary test cases:
  - 7 characters: "Pass12!" (invalid - below min)
  - 8 characters: "Pass1234" (valid - at min)
  - 20 characters: "P1234567890123456890" (valid - at max)
  - 21 characters: "P12345678901234567890X" (invalid - above max)
```

### 2. Equivalence Partitioning
Group inputs into classes with similar behavior.

```
User Age field (must be 18-100):
- Invalid: < 18
- Valid: 18-100
- Invalid: > 100

Test cases:
- Age 10 (invalid class)
- Age 18 (boundary)
- Age 50 (valid class)
- Age 100 (boundary)
- Age 101 (invalid class)
```

### 3. State Transition Testing
Test transitions between states.

```
Order workflow states:
- Pending → Processing (valid)
- Processing → Shipped (valid)
- Shipped → Delivered (valid)
- Delivered → Pending (invalid)
- Pending → Delivered (invalid - skips steps)

Test cases:
- Create order (Pending state)
- Mark as processing (valid transition)
- Mark as shipped (valid transition)
- Try to mark as pending (invalid - should fail)
```

### 4. Decision Table Testing
Test combinations of conditions.

```
Purchase eligibility:
- Age >= 18
- Account verified
- Card on file

Decision Table:
| Age | Verified | Card | Eligible | Test |
|-----|----------|------|----------|------|
| Y   | Y        | Y    | Y        | T1   |
| Y   | Y        | N    | N        | T2   |
| Y   | N        | Y    | N        | T3   |
| N   | Y        | Y    | N        | T4   |
| Y   | N        | N    | N        | T5   |
| N   | N        | N    | N        | T6   |
```

## Example Test Cases

```markdown
## Feature: User Login

### Test Case 1: Successful Login with Valid Credentials
- Precondition: User account exists, user is on login page
- Steps:
  1. Enter email "test@example.com"
  2. Enter password "Password123!"
  3. Click "Login" button
- Expected Result: User redirected to dashboard

### Test Case 2: Login with Invalid Email
- Precondition: Login page is open
- Steps:
  1. Enter email "invalid-email"
  2. Enter password "Password123!"
  3. Click "Login" button
- Expected Result: Error "Invalid email format"

### Test Case 3: Login with Empty Password
- Precondition: Login page is open
- Steps:
  1. Enter email "test@example.com"
  2. Leave password empty
  3. Click "Login" button
- Expected Result: Error "Password is required"

### Test Case 4: Login with Non-existent User
- Precondition: User doesn't exist
- Steps:
  1. Enter email "nonexistent@example.com"
  2. Enter password "Password123!"
  3. Click "Login" button
- Expected Result: Error "Invalid email or password"

### Test Case 5: Login with Too Many Attempts
- Precondition: User has failed 5+ login attempts
- Steps:
  1. Enter incorrect email/password
  2. Attempt 6th login
- Expected Result: Account locked, error "Account temporarily locked"
```

## Integration with Other Skills

- **`test-strategy-doc`**: Test case planning
- **`test-automation-setup`**: Automate test cases
- **`cicd-pipeline-setup`**: Run tests in CI/CD

