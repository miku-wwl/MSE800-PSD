# 动物园管理系统 - 装饰器实现

## 项目简介

这是一个简单的动物园管理系统，展示如何使用 **Python 装饰器** 实现：
- ✅ **权限控制** - 只有管理员才能执行某些操作
- 📋 **操作日志** - 记录每次操作的时间

## 项目结构

```
zoo_admin_project/
├── decorators.py    # 装饰器定义
├── admin.py         # 管理功能
├── main.py          # 入口程序
└── README.md        # 说明文档
```

## 核心概念

### 1. `@admin_required` 装饰器
检查用户是否是管理员，只有管理员才能执行被装饰的函数。

```python
@admin_required
def add_animal(user, name, count):
    # 只有管理员才能执行
    pass
```

### 2. `@log_action` 装饰器
自动记录函数的执行时间。

```python
@log_action
def view_animals():
    # 执行时会自动打印时间戳
    pass
```

## 装饰器堆叠

函数可以使用多个装饰器：

```python
@admin_required  # 第2个执行：检查权限
@log_action      # 第1个执行：记录日志
def add_animal(user, name, count):
    ...
```

**执行顺序：** 从下到上

## 运行程序

```bash
python main.py
```

## 输出示例

```
🦁 欢迎来到动物园管理系统 🦁

=== 演示1：查看所有动物 ===
【view_animals】 执行于 10:15:30
🐾 动物库存：
   狮子: 3 只
   大象: 2 只
   ...
【view_animals】 完成✓

=== 演示2：管理员添加动物 ===
【add_animal】 执行于 10:15:31
✓ 管理员 张三 验证通过
🦁 成功添加 2 只狮子
【add_animal】 完成✓
```

## 关键要点

| 点 | 说明 |
|----|------|
| **装饰器用途** | 添加额外功能而不改变原函数代码 |
| **@admin_required** | 权限验证 |
| **@log_action** | 操作记录 |
| **堆叠使用** | 多个装饰器可以组合 |
| **代码重用** | 避免重复写验证和日志代码 |

## 装饰器工作原理

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # 函数执行前
        result = func(*args, **kwargs)  # 执行原函数
        # 函数执行后
        return result
    return wrapper
```

装饰器本质上是一个**函数包装器**，可以在原函数执行前后添加代码。

