from datetime import datetime


def admin_required(func):
    """只有管理员才能执行的装饰器"""
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin"):
            print("❌ 权限不足！只有管理员可以执行此操作")
            return
        print(f"✓ 管理员 {user['name']} 验证通过")
        return func(user, *args, **kwargs)
    return wrapper


def log_action(func):
    """记录函数执行的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"\n【{func.__name__}】 执行于 {datetime.now().strftime('%H:%M:%S')}")
        result = func(*args, **kwargs)
        print(f"【{func.__name__}】 完成✓")
        return result
    return wrapper
