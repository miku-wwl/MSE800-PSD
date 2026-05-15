from decorators import admin_required, log_action


# 动物库存
animals = {"狮子": 3, "大象": 2, "长颈鹿": 4, "企鹅": 10}


@admin_required
@log_action
def add_animal(user, name, count):
    """添加动物"""
    animals[name] = animals.get(name, 0) + count
    print(f"🦁 成功添加 {count} 只{name}")


@admin_required
@log_action
def remove_animal(user, name, count):
    """删除动物"""
    if animals.get(name, 0) >= count:
        animals[name] -= count
        print(f"🚫 成功删除 {count} 只{name}")
    else:
        print(f"❌ {name}不足，现有：{animals.get(name, 0)} 只")


@log_action
def view_animals():
    """查看所有动物"""
    print("🐾 动物库存：")
    for name, count in animals.items():
        print(f"   {name}: {count} 只")


@admin_required
@log_action
def login(user, username, password):
    """管理员登录"""
    credentials = {"admin": "123456"}
    if credentials.get(username) == password:
        print(f"✓ 欢迎 {username}！")
        return True
    print(f"❌ 用户名或密码错误")
    return False
