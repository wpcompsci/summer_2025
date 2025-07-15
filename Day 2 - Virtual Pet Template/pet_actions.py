import random


def feed_pet(pet_name, food, hunger, happy, food_dict):
    """Feeds the pet and updates hunger and happiness."""
    if food in food_dict:
        effects = food_dict[food]
        hunger += effects["hunger"]
        happy += effects["happy"]
        print(f"{pet_name} eats the {food}.")
    else:
        print(f"{pet_name} doesn't want the {food}.")
        happy -= 1
    return hunger, happy


def play_with_pet(pet_name, hunger, tired, happy):
    """Handles play logic."""
    print(f"You play with {pet_name}.")
    if random.random() < 0.8:
        happy += random.randint(1, 3)
        tired += 2
        hunger += 1
        print(f"{pet_name} is having fun!")
    else:
        happy -= 1
        print(f"{pet_name} ignores you.")
    return hunger, tired, happy


def pet_sleep(pet_name, tired, hunger):
    """Handles sleeping logic."""
    rest = random.randint(2, 4)
    tired -= rest
    hunger += 1
    print(f"{pet_name} sleeps and recovers {rest} energy.")
    return tired, hunger
