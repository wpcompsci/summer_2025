def save_game(pet_name, hunger, tired, happy):
    """Saves the pet's state to a file."""
    with open("savefile.txt", "w") as f:
        f.write(f"{pet_name},{hunger},{tired},{happy}\n")
    print("Game saved!")


def load_game():
    """Loads the pet's state from a file."""
    try:
        with open("savefile.txt", "r") as f:
            data = f.readline().strip().split(",")
            return data[0], int(data[1]), int(data[2]), int(data[3])
    except FileNotFoundError:
        print("No save file found.")
        return None
