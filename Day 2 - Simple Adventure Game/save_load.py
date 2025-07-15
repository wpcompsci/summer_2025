def save_game(name, hp, gold, inventory):
    """Saves character state to a file."""
    with open("rpg_save.txt", "w") as f:
        f.write(f"{name},{hp},{gold},{'|'.join(inventory)}\n")
    print("Game saved!")

def load_game():
    """Loads character state from a file."""
    try:
        with open("rpg_save.txt", "r") as f:
            data = f.readline().strip().split(",")
            name = data[0]
            hp = int(data[1])
            gold = int(data[2])
            inventory = data[3].split("|") if data[3] else []
            return name, hp, gold, inventory
    except FileNotFoundError:
        print("No saved game found.")
        return None
