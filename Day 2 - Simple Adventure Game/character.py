def create_character():
    """Creates a new character with default stats."""
    name = input("Enter your hero's name: ")
    hp = 10
    gold = 5
    inventory = ["Sword"]
    print(f"Welcome, {name} the Brave!")
    return name, hp, gold, inventory


def display_stats(name, hp, gold, inventory):
    """Displays current character stats."""
    print(f"Name: {name}")
    print(f"HP: {hp}")
    print(f"Gold: {gold}")
    print("Inventory:", ", ".join(inventory))
