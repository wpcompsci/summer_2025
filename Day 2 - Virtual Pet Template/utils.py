MAX_STAT = 10
MIN_STAT = 0


def print_stats(pet_name, hunger, tired, happy):
    """Prints current pet stats."""
    print(f"\n--- {pet_name}'s Stats ---")
    print(f"Hunger: {hunger}/10")
    print(f"Tiredness: {tired}/10")
    print(f"Happiness: {happy}/10")


def apply_passive_changes(hunger, tired, happy):
    """Passive effects each turn."""
    hunger += 1
    tired += 1
    happy -= 1


def enforce_stat_limits(hunger, tired, happy):
    """Keep all stats within bounds."""
    hunger = min(MAX_STAT, max(MIN_STAT, hunger))
    tired = min(MAX_STAT, max(MIN_STAT, tired))
    happy = min(MAX_STAT, max(MIN_STAT, happy))


def check_end_conditions(pet_name, hunger, tired, happy):
    """Checks game over conditions."""
    if hunger >= MAX_STAT:
        print(f"{pet_name} is starving. Game over.")
        return True
    if tired >= MAX_STAT:
        print(f"{pet_name} is exhausted. Game over.")
        return True
    if happy <= MIN_STAT:
        print(f"{pet_name} is too sad. Game over.")
        return True
    return False
