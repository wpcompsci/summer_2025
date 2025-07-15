from pet_actions import feed_pet, play_with_pet, pet_sleep
from data import FOOD_OPTIONS
from utils import print_stats, apply_passive_changes, enforce_stat_limits, check_end_conditions
from save_load import save_game, load_game

# Load or create a new pet
use_saved = input("Load saved game? (yes/no) ").lower()
if use_saved == "yes":
    loaded = load_game()
    if loaded:
        pet_name, hunger, tired, happy = loaded
    else:
        pet_name = input("Pet name: ")
        hunger, tired, happy = 2, 2, 5
else:
    pet_name = input("What would you like to name your pet? ")
    hunger, tired, happy = 2, 2, 5

print(f"Welcome to the game, {pet_name}!")

# Main loop
while True:
    print_stats(pet_name, hunger, tired, happy)

    if check_end_conditions(pet_name, hunger, tired, happy):
        break

    action = input("\nChoose an action (feed/play/sleep/save/quit): ").lower()

    if action == "quit":
        print(f"Goodbye, {pet_name}!")
        break
    elif action == "feed":
        print("Available food options:", ", ".join(FOOD_OPTIONS.keys()))
        food = input("What do you want to feed your pet? ").lower()
        hunger, happy = feed_pet(pet_name, food, hunger, happy, FOOD_OPTIONS)
    elif action == "play":
        hunger, tired, happy = play_with_pet(pet_name, hunger, tired, happy)
    elif action == "sleep":
        tired, hunger = pet_sleep(pet_name, tired, hunger)
    elif action == "save":
        save_game(pet_name, hunger, tired, happy)
    else:
        print("Invalid action.")
        happy -= 1

    apply_passive_changes(hunger, tired, happy)
    enforce_stat_limits(hunger, tired, happy)
