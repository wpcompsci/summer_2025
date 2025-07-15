import json

def save_game(pokemon, level):
    with open("save_file.json", "w") as f:
        json.dump({"pokemon": pokemon, "level": level}, f)
    print("Game saved!")

def load_game():
    try:
        with open("save_file.json", "r") as f:
            data = json.load(f)
            print("Game loaded!")
            return data["pokemon"], data["level"]
    except FileNotFoundError:
        print("No save file found.")
        return None, 1
