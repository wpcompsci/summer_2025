from character import create_character, display_stats
from world import explore_area
from combat import encounter_enemy
from store import visit_store
from save_load import save_game, load_game

print("=== Welcome to Python RPG Adventure ===")

use_saved = input("Load saved game? (yes/no): ").lower()
if use_saved == "yes":
    loaded = load_game()
    if loaded:
        name, hp, gold, inventory = loaded
    else:
        name, hp, gold, inventory = create_character()
else:
    name, hp, gold, inventory = create_character()

# Game Loop
while True:
    print(f"\n--- {name}'s Turn ---")
    display_stats(name, hp, gold, inventory)
    action = input("\nChoose an action (explore/fight/store/save/quit): ").lower()

    if action == "quit":
        print(f"Farewell, {name}!")
        break
    elif action == "explore":
        gold = explore_area(name, gold)
    elif action == "fight":
        hp, gold = encounter_enemy(name, hp, gold, inventory)
        if hp <= 0:
            print(f"{name} has fallen in battle. Game over.")
            break
    elif action == "store":
        gold, inventory = visit_store(gold, inventory)
    elif action == "save":
        save_game(name, hp, gold, inventory)
    else:
        print("Invalid action. Try again.")
