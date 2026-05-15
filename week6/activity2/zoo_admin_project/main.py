from admin import add_animal, remove_animal, view_animals, login


def main():
    print("🦁 欢迎来到动物园管理系统 🦁\n")
    
    # 管理员账户
    admin_user = {"name": "张三", "is_admin": True}
    guest_user = {"name": "游客", "is_admin": False}
    
    # 演示1：查看所有动物
    print("=== 演示1：查看所有动物 ===")
    view_animals()
    
    # 演示2：管理员添加动物
    print("\n=== 演示2：管理员添加动物 ===")
    add_animal(admin_user, "狮子", 2)
    
    # 演示3：删除动物
    print("\n=== 演示3：删除动物 ===")
    remove_animal(admin_user, "企鹅", 3)
    
    # 演示4：查看更新后的库存
    print("\n=== 演示4：查看更新后的库存 ===")
    view_animals()
    
    # 演示5：未授权访问（游客试图添加动物）
    print("\n=== 演示5：未授权访问 ===")
    add_animal(guest_user, "老虎", 1)
    
    print("\n✅ 演示完成！")


if __name__ == "__main__":
    main()
