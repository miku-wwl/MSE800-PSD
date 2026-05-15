# Week 6 - Activity 2：动物园管理系统

## 简介

一个简单的动物园管理系统，使用 Python **装饰器** 实现权限控制和操作日志。

## 核心装饰器

1. **`@admin_required`** - 只有管理员才能执行该函数
2. **`@log_action`** - 自动记录函数的执行时间

## 快速运行

```bash
cd zoo_admin_project
python main.py
```

## 输出内容

- ✅ 管理员成功操作（添加、删除动物）
- ❌ 游客被拒绝访问
- 📋 每个操作都有时间戳日志

## 装饰器堆叠

```python
@admin_required  # 第2个：检查权限
@log_action      # 第1个：记录日志
def add_animal(user, name, count):
    ...
```

## 文件说明

- `decorators.py` - 装饰器定义
- `admin.py` - 管理功能
- `main.py` - 演示程序
- `README.md` - 详细文档

