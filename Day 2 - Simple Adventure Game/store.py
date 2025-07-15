STORE_ITEMS = {
    "Potion": {"price": 3, "type": "heal", "value": 5},
    "Shield": {"price": 5, "type": "defense", "value": 1},
    "Helmet": {"price": 4, "type": "defense", "value": 1}
}

def visit_store(gold, inventory):
    print("\n--- Welcome to the Shop ---")
    for item, data in STORE_ITEMS.items():
        print(f"{item}: {data['price']} gold")

    while True:
        choice = input("Buy what? (or 'exit'): ").title()
        if choice == "Exit":
            break
        elif choice in STORE_ITEMS:
            item_data = STORE_ITEMS[choice]
            if gold >= item_data["price"]:
                inventory.append(choice)
                gold -= item_data["price"]
                print(f"You bought a {choice}.")
            else:
                print("Not enough gold.")
        else:
            print("Invalid item.")
    return gold, inventory

