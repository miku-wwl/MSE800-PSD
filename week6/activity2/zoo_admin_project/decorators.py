from datetime import datetime


def admin_required(func):
    """Decorator that checks admin privileges before executing function"""
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin"):
            print("❌ Permission denied! Admin access required.")
            return
        print(f"✓ Admin {user['name']} verified")
        return func(user, *args, **kwargs)
    return wrapper


def log_action(func):
    """Decorator that logs function execution with timestamp"""
    def wrapper(*args, **kwargs):
        print(f"\n[{func.__name__}] executed at {datetime.now().strftime('%H:%M:%S')}")
        result = func(*args, **kwargs)
        print(f"[{func.__name__}] completed ✓")
        return result
    return wrapper
