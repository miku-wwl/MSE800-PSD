from admin import add_animal, remove_animal, view_animals, login


def main():
    print("🦁 Welcome to Zoo Admin System 🦁\n")
    
    # Admin and guest accounts
    admin_user = {"name": "John", "is_admin": True}
    guest_user = {"name": "Guest", "is_admin": False}
    
    # Demo 1: View all animals
    print("=== Demo 1: View all animals ===")
    view_animals()
    
    # Demo 2: Admin adds animals
    print("\n=== Demo 2: Admin adds animals ===")
    add_animal(admin_user, "Lion", 2)
    
    # Demo 3: Remove animals
    print("\n=== Demo 3: Remove animals ===")
    remove_animal(admin_user, "Penguin", 3)
    
    # Demo 4: View updated inventory
    print("\n=== Demo 4: View updated inventory ===")
    view_animals()
    
    # Demo 5: Unauthorized access (guest tries to add animals)
    print("\n=== Demo 5: Unauthorized access ===")
    add_animal(guest_user, "Tiger", 1)
    
    print("\n✅ Demo completed!")


if __name__ == "__main__":
    main()
