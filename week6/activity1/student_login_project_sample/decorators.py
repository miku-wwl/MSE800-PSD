from datetime import datetime



def log_activity(func):

    # Debugging note: this decorator wraps any function and adds
    # timestamped activity logs without changing the function body.

    def wrapper(*args, **kwargs):
        # Debugging note: the wrapper is the place where the extra logging
        # happens before and after the original function executes.
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        result = func(*args, **kwargs)

        print("Activity completed.")
        print("===================================\n")

        return result

    return wrapper
