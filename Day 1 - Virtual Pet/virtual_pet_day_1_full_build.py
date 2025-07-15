import random

print("Welcome to your virtual pet!")

# Initial stats
hunger = 2
tired = 2
happy = 5

# Max and min boundaries
MAX_STAT = 10
MIN_STAT = 0

# Name your pet
pet_name = input("What would you like to name your pet? ")
print(f"\n{pet_name} is excited to meet you!\n")

# Game loop
while True:
    print(f"\n--- {pet_name}'s Stats ---")
    print(f"Hunger: {hunger}/10")
    print(f"Tiredness: {tired}/10")
    print(f"Happiness: {happy}/10")

    # Check for loss conditions
    if hunger >= MAX_STAT:
        print(f"\n{pet_name} is starving and gets sick! You rush them to the vet. Game over.")
        break
    if tired >= MAX_STAT:
        print(f"\n{pet_name} collapses from exhaustion. They need rest. Game over.")
        break
    if happy <= MIN_STAT:
        print(f"\n{pet_name} is too sad to keep going. They wander off. Game over.")
        break

    action = input("\nWhat do you want to do? (feed/play/sleep/quit) ").lower()

    if action == "quit":
        print(f"\nYou say goodbye to {pet_name}. Thanks for playing!")
        break

    elif action == "feed":
        food = input("What do you feed your pet? ").lower()
        if food in ["cookie", "apple", "carrot"]:
            print(f"{pet_name} eats the {food}.")
            hunger -= random.randint(1, 3)
            happy += 1
        else:
            print(f"{pet_name} sniffs the {food} and walks away. Not interested.")
            happy -= 1

    elif action == "play":
        print(f"You toss a toy to {pet_name}!")
        if random.random() < 0.8:
            print(f"{pet_name} plays happily!")
            happy += random.randint(1, 3)
            tired += 2
            hunger += 1
        else:
            print(f"{pet_name} ignores the toy. Maybe next time.")
            happy -= 1

    elif action == "sleep":
        print(f"{pet_name} goes to sleep...")
        rest = random.randint(2, 4)
        tired -= rest
        hunger += 1
        print(f"{pet_name} rested for a bit and feels better.")

    else:
        print("Invalid action. Try feed, play, sleep, or quit.")
        happy -= 1  # Frustrated by confusion

    # Passive stat changes each turn
    hunger += 1
    tired += 1
    happy -= 1

    # Enforce stat boundaries
    hunger = min(MAX_STAT, max(MIN_STAT, hunger))
    tired = min(MAX_STAT, max(MIN_STAT, tired))
    happy = min(MAX_STAT, max(MIN_STAT, happy))
