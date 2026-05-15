# README Assignment

## English

This project demonstrates how a Python decorator can add cross-cutting logging behavior to multiple functions.

### How the decorator is used

- `@log_activity` is placed above each function in `users.py`.
- The decorator returns a `wrapper` function.
- The wrapper prints a start banner, function name, and timestamp before the original function runs.
- After the original function finishes, the wrapper prints a completion message.

### Debugging notes

- `main.py` is the entry point and calls the sample actions in order.
- `student_login`, `submit_assignment`, and `view_grades` are all wrapped by the same decorator.
- The key check is whether each function still prints its own business message while also showing the decorator logs.
- The output confirms that the original arguments are preserved and the decorator runs every time.

### Findings

The decorator works correctly and keeps the code DRY. Instead of repeating logging code in every function, the project centralizes that behavior in one reusable decorator.