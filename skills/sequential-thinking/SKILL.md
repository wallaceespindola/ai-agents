---
name: sequential-thinking
description: Break down complex problems into sequential, logical steps. Use when tackling complex bugs, designing algorithms, or reasoning through multi-step problems.
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash(*), Write, Edit
---

# Sequential Thinking Framework

Systematic approach to problem-solving through step-by-step reasoning.

## What is Sequential Thinking?

Sequential thinking is the process of breaking down complex problems into smaller, ordered steps that can be solved one at a time. Each step builds on the previous one, leading to a complete solution.

## When to Use Sequential Thinking

- 🐛 **Debugging complex issues** - Track down elusive bugs
- 🏗️ **Designing algorithms** - Build solutions step-by-step
- 🔍 **Analyzing code flow** - Understand execution paths
- 📊 **Database query optimization** - Reason through query plans
- 🔐 **Security analysis** - Trace attack vectors
- 🧩 **Refactoring** - Plan code restructuring
- 🚀 **Performance optimization** - Identify bottlenecks systematically
- 📝 **Writing complex features** - Break down requirements

## The Sequential Thinking Process

### Step 1: Define the Problem Clearly

**Ask**:
- What exactly is the problem?
- What is the expected behavior?
- What is the actual behavior?
- What error messages or symptoms appear?

**Example**:
```
Problem: User cannot reserve a beer
Expected: POST /reservations returns 201 with reservation
Actual: Returns 403 Forbidden
Error: "User has already reserved today"
```

### Step 2: Gather Information

**Collect**:
- Relevant code sections
- Error messages and stack traces
- Log files
- Database state
- Request/response data
- Environment variables

**Example**:
```bash
# Check logs
tail -f logs/api.log | grep "reservation"

# Check database
db.reservations.find({ user_id: "123", created_at: { $gte: today } })

# Check code
grep -r "already reserved" app/
```

### Step 3: Form a Hypothesis

**Hypothesis Template**:
"I think [X] is happening because [Y], which causes [Z]"

**Example**:
```
Hypothesis: The fraud prevention check is incorrectly counting
reservations from yesterday as "today" because it's using UTC time
instead of local timezone, causing false positives.
```

### Step 4: Break Down into Sequential Steps

**List each step** that should happen:

**Example (Reservation Flow)**:
```
Step 1: User submits reservation request
Step 2: API validates JWT token
Step 3: API checks if user exists
Step 4: API checks if offer exists and is active
Step 5: API checks fraud prevention (1 reservation per bar per day)
Step 6: API creates reservation document
Step 7: API updates offer remaining_quantity
Step 8: API returns reservation with 201 status
```

### Step 5: Trace Execution

**Walk through each step** with actual data:

**Example**:
```python
# Step 1: Request received
POST /api/v1/reservations
{
  "offer_id": "65a1b2c3d4e5f6g7h8i9j0k1",
  "bar_id": "75a1b2c3d4e5f6g7h8i9j0k2"
}

# Step 2: Token validation
token = "eyJhbGciOiJIUzI1NiIs..."
decoded = jwt.decode(token)  # ✅ Valid
user_id = "85a1b2c3d4e5f6g7h8i9j0k3"

# Step 3: User lookup
user = await User.find_one({"_id": user_id})  # ✅ Found

# Step 4: Offer lookup
offer = await Offer.find_one({"_id": offer_id})  # ✅ Found, active

# Step 5: Fraud check
today_start = datetime.now(UTC).replace(hour=0, minute=0)  # ⚠️ UTC!
existing = await Reservation.find_one({
  "user_id": user_id,
  "bar_id": bar_id,
  "created_at": {"$gte": today_start}
})
# Result: Found reservation from yesterday at 11 PM UTC
# In Brussels (UTC+1), that's today at midnight!
# ❌ False positive!

# Step 6: (Never reached due to fraud check failure)
```

### Step 6: Identify the Issue

**Pinpoint** where the actual behavior diverges from expected:

**Example**:
```
Issue found at Step 5 (Fraud Check):
- Using UTC timezone for "today" calculation
- Brussels is UTC+1, so yesterday 11 PM UTC = today 12 AM Brussels
- Existing reservation from yesterday in local time counts as "today" in UTC
- Fraud check incorrectly prevents new reservation
```

### Step 7: Formulate a Solution

**Design fix** based on root cause:

**Example**:
```python
# Before (wrong):
today_start = datetime.now(UTC).replace(hour=0, minute=0, second=0)

# After (correct):
from zoneinfo import ZoneInfo

BRUSSELS_TZ = ZoneInfo("Europe/Brussels")
now_brussels = datetime.now(BRUSSELS_TZ)
today_start = now_brussels.replace(hour=0, minute=0, second=0, microsecond=0)
today_start_utc = today_start.astimezone(UTC)  # Convert to UTC for DB query

existing = await Reservation.find_one({
    "user_id": user_id,
    "bar_id": bar_id,
    "created_at": {"$gte": today_start_utc}
})
```

### Step 8: Test the Solution

**Verify fix** step-by-step:

```python
# Test Case 1: Same day reservation (should fail)
reservation1 = await create_reservation(user_id, bar_id)  # ✅ Created
reservation2 = await create_reservation(user_id, bar_id)  # ❌ 403 (correct)

# Test Case 2: Next day reservation (should succeed)
# Mock time to tomorrow
with freeze_time(tomorrow):
    reservation3 = await create_reservation(user_id, bar_id)  # ✅ Created

# Test Case 3: Reservation at 11:59 PM, then at 12:01 AM (should succeed)
with freeze_time("2024-02-13 23:59:00", tz_offset=+1):  # Brussels time
    reservation4 = await create_reservation(user_id, bar_id)  # ✅ Created

with freeze_time("2024-02-14 00:01:00", tz_offset=+1):
    reservation5 = await create_reservation(user_id, bar_id)  # ✅ Created (new day)
```

## Sequential Thinking Templates

### Debugging Template

```markdown
## Problem Statement
- What: [Describe issue]
- Expected: [What should happen]
- Actual: [What happens instead]
- Error: [Error message if any]

## Information Gathered
- Code: [Relevant files/functions]
- Logs: [Error logs, stack traces]
- Data: [Database state, request/response]
- Environment: [Variables, configuration]

## Hypothesis
I think [X] because [Y], causing [Z]

## Execution Flow
Step 1: [First operation] → [Result]
Step 2: [Second operation] → [Result]
Step 3: [Third operation] → [Result] ⚠️ Issue here
Step 4: [Would happen but blocked]

## Root Cause
[Specific line/logic causing the issue]

## Solution
[Proposed fix with code example]

## Testing Plan
- Test 1: [Normal case]
- Test 2: [Edge case 1]
- Test 3: [Edge case 2]
```

### Algorithm Design Template

```markdown
## Problem
[What needs to be solved]

## Constraints
- Input: [Format, size, range]
- Output: [Expected format]
- Performance: [Time/space complexity requirements]

## Approach
[High-level strategy]

## Sequential Steps
Step 1: [Initialize data structures]
Step 2: [First transformation]
Step 3: [Processing logic]
Step 4: [Edge case handling]
Step 5: [Return result]

## Example Walkthrough
Input: [Sample input]

Step 1: [State after step 1]
Step 2: [State after step 2]
Step 3: [State after step 3]
...
Output: [Final result]

## Complexity Analysis
- Time: O(?)
- Space: O(?)
```

### Database Query Optimization Template

```markdown
## Current Query
[Existing slow query]

## Performance Problem
- Execution time: [X ms/s]
- Records scanned: [Y]
- Index used: [Yes/No, which one]

## Sequential Analysis
Step 1: [Query parsing]
Step 2: [Index selection] ⚠️ No suitable index
Step 3: [Full collection scan]
Step 4: [Filtering]
Step 5: [Sorting]
Step 6: [Limit/Skip]

## Bottleneck
[Where time is spent]

## Optimization Strategy
Step 1: [Add index on X]
Step 2: [Rewrite query to use index]
Step 3: [Project only needed fields]

## After Optimization
- Execution time: [X ms]
- Records scanned: [Y]
- Index used: [Which one]
- Improvement: [X% faster]
```

## Common Sequential Reasoning Patterns

### 1. Trace Back (Reverse Engineering)

Start from the error and work backward:

```
Error at: Line 45 (variable is None)
           ↑
Step back: Where does this variable come from? Line 38
           ↑
Step back: What sets it? Function call on line 30
           ↑
Step back: What returns None? Database query when no result
           ↑
Root: Missing data in database OR wrong query
```

### 2. Trace Forward (Following the Flow)

Start from input and follow the path:

```
Input: User clicks "Reserve Beer"
  ↓
Step 1: Frontend sends POST /reservations
  ↓
Step 2: Backend validates token
  ↓
Step 3: Backend checks fraud prevention
  ↓
Step 4: ⚠️ Fraud check fails incorrectly
  ↓
Output: 403 Forbidden (wrong)
```

### 3. Divide and Conquer

Split the problem into independent parts:

```
Problem: Slow API response (2000ms)

Part 1: Database query time → 1500ms ⚠️ SLOW
Part 2: Business logic time → 100ms ✅ OK
Part 3: Response serialization → 400ms ⚠️ SLOW

Focus on Part 1 and Part 3 separately.
```

### 4. State Machine Reasoning

Track state transitions:

```
Reservation States:
  pending → active → redeemed ✅ Happy path
  pending → active → expired ✅ Timeout
  pending → expired ✅ Not claimed
  active → active ❌ Cannot re-activate
  redeemed → active ❌ Cannot undo redemption
```

## Tools for Sequential Thinking

### 1. Print/Log Statements

```python
print(f"Step 1: User ID = {user_id}")
print(f"Step 2: Offer found = {offer is not None}")
print(f"Step 3: Fraud check - today_start = {today_start}")
print(f"Step 4: Existing reservations = {len(existing)}")
```

### 2. Debugger (pdb, debugpy)

```python
import pdb

def create_reservation(user_id, bar_id):
    pdb.set_trace()  # Pause execution here
    # Step through with: n (next), s (step into), c (continue)
    user = get_user(user_id)
    ...
```

### 3. Logging

```python
import logging

logger = logging.getLogger(__name__)

def process_payment(amount):
    logger.info(f"Step 1: Processing payment for {amount}")
    logger.debug(f"Step 2: Stripe key: {stripe_key[:10]}...")
    logger.info(f"Step 3: Payment successful: {charge_id}")
```

### 4. Assertions

```python
def calculate_discount(price, discount_percent):
    assert 0 <= discount_percent <= 100, "Discount must be 0-100%"
    discount_amount = price * (discount_percent / 100)
    assert discount_amount <= price, "Discount can't exceed price"
    return price - discount_amount
```

### 5. Explain-like-I'm-5 (ELI5)

Explain the flow in simple terms:

```
"When a user reserves a beer:
1. We check who they are (authentication)
2. We check if the beer offer exists
3. We check if they already got a beer today
4. If all good, we create a reservation
5. We give them a QR code
6. They show it at the bar to get their beer"
```

## Sequential Thinking Checklist

When solving a problem:

- [ ] Problem clearly defined?
- [ ] Information gathered (code, logs, data)?
- [ ] Hypothesis formed?
- [ ] Execution flow mapped out step-by-step?
- [ ] Each step traced with actual data?
- [ ] Divergence point identified?
- [ ] Root cause understood?
- [ ] Solution designed?
- [ ] Edge cases considered?
- [ ] Tests written for each step?

## Common Pitfalls

❌ **Jumping to conclusions**: Don't assume, verify each step
❌ **Skipping steps**: Don't skip "obvious" steps, trace them all
❌ **Tunnel vision**: Consider alternative paths
❌ **Ignoring edge cases**: Test boundary conditions
❌ **Not documenting reasoning**: Write down your thought process

## Examples from Your Projects

### Example 1: Geospatial Query Not Finding Bars

```markdown
## Problem
GET /bars/nearby returns empty array despite bars existing in DB

## Sequential Analysis

Step 1: Parse request
- lat: 50.8503, lon: 4.3517, radius: 1000 (meters)
- ✅ Valid coordinates

Step 2: Build MongoDB query
```python
{
  "location": {
    "$near": {
      "$geometry": {
        "type": "Point",
        "coordinates": [4.3517, 50.8503]  # [lon, lat]
      },
      "$maxDistance": 1000
    }
  }
}
```
- ✅ Query syntax correct

Step 3: Check 2dsphere index
```python
db.bars.getIndexes()
# Result: location_2d (wrong! Should be 2dsphere)
```
- ❌ Using 2d index instead of 2dsphere

Step 4: Fix index
```python
db.bars.dropIndex("location_2d")
db.bars.createIndex({"location": "2dsphere"})
```

Step 5: Retry query
- ✅ Returns 5 bars within 1km

## Root Cause
Wrong index type (2d vs 2dsphere for geospatial queries)
```

### Example 2: JWT Token Expiry Issue

```markdown
## Problem
Access tokens expire after 1 minute instead of 15 minutes

## Sequential Analysis

Step 1: Check token creation
```python
access_token = create_access_token(
    data={"sub": user_id},
    expires_delta=timedelta(minutes=15)
)
```
- ✅ Expires delta set to 15 minutes

Step 2: Inspect create_access_token function
```python
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=1)  # ⚠️ Hardcoded!
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY)
```
- ❌ Function ignores expires_delta parameter

Step 3: Fix function
```python
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta  # ✅ Use parameter
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY)
```

## Root Cause
Function had hardcoded 1-minute expiry, ignoring the parameter
```

## Remember

> "The secret to solving hard problems is to break them down into many small, easy problems that you solve one at a time."

Sequential thinking is:
- **Methodical**: Follow a systematic process
- **Traceable**: Document each step
- **Verifiable**: Test each assumption
- **Reproducible**: Others can follow your reasoning
- **Thorough**: Don't skip steps
