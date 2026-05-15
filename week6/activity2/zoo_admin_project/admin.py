from decorators import admin_required, log_action


# Animal inventory
animals = {"Lion": 3, "Elephant": 2, "Giraffe": 4, "Penguin": 10}


@admin_required
@log_action
def add_animal(user, name, count):
    """Add animals to inventory"""
    animals[name] = animals.get(name, 0) + count
    print(f"🦁 Successfully added {count} {name}(s)")


@admin_required
@log_action
def remove_animal(user, name, count):
    """Remove animals from inventory"""
    if animals.get(name, 0) >= count:
        animals[name] -= count
        print(f"🚫 Successfully removed {count} {name}(s)")
    else:
        print(f"❌ Not enough {name}. Available: {animals.get(name, 0)}")


@log_action
def view_animals():
    """Display all animals in inventory"""
    print("🐾 Animal Inventory:")
    for name, count in animals.items():
        print(f"   {name}: {count}")


@admin_required
@log_action
def login(user, username, password):
    """Admin login"""
    credentials = {"admin": "123456"}
    if credentials.get(username) == password:
        print(f"✓ Welcome {username}!")
        return True
    print(f"❌ Invalid username or password")
    return False
