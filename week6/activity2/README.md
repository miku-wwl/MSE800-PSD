# Week 6 - Activity 2: Zoo Admin System

## Overview

A simple zoo admin system using Python **decorators** to implement access control and operation logging.

## Core Decorators

1. **`@admin_required`** - Only admin can execute the function
2. **`@log_action`** - Automatically log function execution time

## Quick Start

```bash
cd zoo_admin_project
python main.py
```

## Output

- ✅ Successful admin operations (add/remove animals)
- ❌ Guest access denied
- 📋 Timestamp logging for each operation

## Decorator Stacking

```python
@admin_required  # 2nd: check permission
@log_action      # 1st: log action
def add_animal(user, name, count):
    ...
```

## Files

- `decorators.py` - Decorator definitions
- `admin.py` - Admin functions
- `main.py` - Demo program
- `README.md` - Detailed documentation

