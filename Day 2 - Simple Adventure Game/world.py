import random


def explore_area(name, gold):
    """Simulates exploration, may find treasure or nothing."""
    print(f"{name} explores the surrounding area...")
    if random.random() < 0.5:
        found = random.randint(1, 5)
        gold += found
        print(f"You found {found} gold!")
    else:
        print("Nothing found this time.")
    return gold
