import random

# Dictionary of enemies
ENEMIES = {
    "Goblin": {"hp": 5, "attack": (1, 2), "gold": (2, 5)},
    "Skeleton": {"hp": 6, "attack": (2, 3), "gold": (3, 6)},
    "Orc": {"hp": 8, "attack": (2, 4), "gold": (4, 8)},
    "Bandit": {"hp": 7, "attack": (1, 3), "gold": (3, 7)},
}


def get_random_enemy():
    """Randomly selects an enemy from the list."""
    name = random.choice(list(ENEMIES.keys()))
    stats = ENEMIES[name].copy()
    stats["name"] = name
    return stats
