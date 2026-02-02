---
name: pattern-recommendation
description: Recommend design patterns and architectural patterns for specific problems
---

# Pattern Recommendation Skill

## When to Use This Skill

- Solving recurring design problems
- Improving code structure and organization
- Scaling architectural patterns
- Reducing technical debt
- Implementing best practices
- Training teams on design patterns
- Refactoring existing code

## Quick Start

```
/pattern-recommendation <problem_or_scenario>
```

**Example**:
```
/pattern-recommendation Managing user preferences across multiple services
```

## How It Works

Recommends patterns based on problem context.

## Creational Patterns

### Singleton Pattern
**Problem**: Need single shared instance
```python
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

config = Config()  # Always same instance
```

### Factory Pattern
**Problem**: Creating different object types
```python
class PaymentFactory:
    @staticmethod
    def create_processor(method):
        if method == 'stripe':
            return StripeProcessor()
        elif method == 'paypal':
            return PayPalProcessor()
```

### Builder Pattern
**Problem**: Complex object construction
```python
class QueryBuilder:
    def __init__(self):
        self.filters = []

    def where(self, condition):
        self.filters.append(condition)
        return self

    def build(self):
        return Query(self.filters)

query = QueryBuilder().where('age > 18').where('city = NYC').build()
```

## Structural Patterns

### Adapter Pattern
**Problem**: Incompatible interfaces
```python
class LegacyPaymentSystem:
    def process(self, amount): pass

class ModernPaymentAdapter:
    def __init__(self, legacy):
        self.legacy = legacy

    def charge(self, amount):
        return self.legacy.process(amount)
```

### Facade Pattern
**Problem**: Complex subsystem interface
```python
class OrderFacade:
    def __init__(self):
        self.payment = PaymentService()
        self.inventory = InventoryService()
        self.shipping = ShippingService()

    def process_order(self, order):
        self.payment.charge(order.amount)
        self.inventory.reserve(order.items)
        self.shipping.schedule(order)
```

### Proxy Pattern
**Problem**: Control access to expensive resource
```python
class ExpensiveDataProxy:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            self._data = fetch_expensive_data()
        return self._data
```

## Behavioral Patterns

### Observer Pattern
**Problem**: Notify multiple objects of changes
```python
class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, handler):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(handler)

    def publish(self, event, data):
        for handler in self.subscribers.get(event, []):
            handler(data)

bus = EventBus()
bus.subscribe('user_created', send_welcome_email)
bus.publish('user_created', user)
```

### Strategy Pattern
**Problem**: Multiple algorithms for same task
```python
class SortingStrategy:
    def sort(self, data): pass

class QuickSort(SortingStrategy):
    def sort(self, data):
        return sorted(data, key=lambda x: x)

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, data):
        return self.strategy.sort(data)
```

### Chain of Responsibility
**Problem**: Pass request through handlers
```python
class RequestHandler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, request):
        if self.can_handle(request):
            return self.process(request)
        elif self.next:
            return self.next.handle(request)

auth = AuthHandler(logging=LoggingHandler())
auth.handle(request)
```

## Architectural Patterns

### MVC (Model-View-Controller)
**Use when**: Building web applications
```
Controller → Model → View
User → Button Click → Controller → Update Model → Render View
```

### Repository Pattern
**Use when**: Abstracting data access
```python
class UserRepository:
    def find_by_id(self, id): pass
    def save(self, user): pass
    def find_all(self): pass

# Multiple implementations: SQL, MongoDB, REST API
```

### Dependency Injection
**Use when**: Loose coupling and testability
```python
class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo  # Injected dependency
```

### Event Sourcing
**Use when**: Need complete audit trail
```
Event: UserCreated(id=1, email=test@example.com)
Event: UserEmailUpdated(id=1, new_email=new@example.com)
Event: UserDeleted(id=1)

Reconstruct state by replaying events
```

### CQRS (Command Query Responsibility Segregation)
**Use when**: Read and write have different scales
```
Write Model: Optimized for updates
Read Model: Denormalized for fast queries
Sync: Event stream keeps them consistent
```

## Best Practices

1. **Understand the Problem**
   - What problem are you solving?
   - What constraints do you have?
   - What trade-offs are acceptable?

2. **Choose Wisely**
   - Avoid over-engineering
   - Balance flexibility and simplicity
   - Consider team knowledge

3. **Document Decision**
   - Why this pattern?
   - Alternative considered
   - Trade-offs made

## Integration with Other Skills

- **`architecture-review`**: Pattern suitability review
- **`system-design-doc`**: Pattern documentation
- **`code-review`**: Pattern implementation review

