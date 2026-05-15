# Zoo Admin System - Decorator Implementation

## Project Overview

A simple zoo admin system demonstrating how to use **Python decorators** to implement:
- ✅ **Access Control** - Only admins can execute certain operations
- 📋 **Action Logging** - Record timestamp of each operation

## Project Structure

```
zoo_admin_project/
├── decorators.py    # Decorator definitions
├── admin.py         # Admin functions
├── main.py          # Entry point
└── README.md        # Documentation
```

## Core Concepts

### 1. `@admin_required` Decorator
Checks if user is admin before executing the decorated function.

```python
@admin_required
def add_animal(user, name, count):
    # Only admin can execute this
    pass
```

### 2. `@log_action` Decorator
Automatically logs function execution with timestamp.

```python
@log_action
def view_animals():
    # Automatically prints timestamp when executed
    pass
```

## Decorator Stacking

Functions can use multiple decorators:

```python
@admin_required  # Executed 2nd: check permission
@log_action      # Executed 1st: log action
def add_animal(user, name, count):
    ...
```

**Execution order:** Bottom to top

## Running the Program

```bash
python main.py
```

## Output Example

```
🦁 Welcome to Zoo Admin System 🦁

=== Demo 1: View all animals ===
[view_animals] executed at 10:15:30
🐾 Animal Inventory:
   Lion: 3
   Elephant: 2
   ...
[view_animals] completed ✓

=== Demo 2: Admin adds animals ===
[add_animal] executed at 10:15:31
✓ Admin John verified
🦁 Successfully added 2 Lion(s)
[add_animal] completed ✓
```

## Key Points

| Point | Explanation |
|-------|-------------|
| **Decorator Purpose** | Add functionality without changing original function |
| **@admin_required** | Verify admin privileges |
| **@log_action** | Record operation logs |
| **Stacking** | Multiple decorators can be combined |
| **Code Reuse** | Avoid repeating verification and logging code |

## How Decorators Work

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Before function execution
        result = func(*args, **kwargs)  # Execute original function
        # After function execution
        return result
    return wrapper
```

A decorator is essentially a **function wrapper** that adds code before and after the original function executes.

