import random

starter_pokemon = [
    {
        "name": "Charmander",
        "hp": 30,
        "attack": 6,
        "stamina": 10,
        "moves": [
            {"name": "Ember", "damage": (4, 7), "cost": 2},
            {"name": "Scratch", "damage": (2, 5), "cost": 1},
            {"name": "Flame Burst", "damage": (6, 10), "cost": 4}
        ]
    },
    {
        "name": "Squirtle",
        "hp": 35,
        "attack": 5,
        "stamina": 10,
        "moves": [
            {"name": "Bubble", "damage": (3, 6), "cost": 2},
            {"name": "Tackle", "damage": (2, 4), "cost": 1},
            {"name": "Water Gun", "damage": (5, 9), "cost": 4}
        ]
    }
]

enemy_pokemon = [
    {
        "name": "Zubat",
        "hp": 28,
        "attack": 4,
        "stamina": 10,
        "moves": [
            {"name": "Bite", "damage": (3, 5), "cost": 2},
            {"name": "Leech Life", "damage": (2, 4), "cost": 1},
            {"name": "Wing Attack", "damage": (5, 8), "cost": 4}
        ]
    },
    {
        "name": "Pidgey",
        "hp": 26,
        "attack": 4,
        "stamina": 10,
        "moves": [
            {"name": "Peck", "damage": (3, 5), "cost": 2},
            {"name": "Gust", "damage": (2, 4), "cost": 1},
            {"name": "Quick Attack", "damage": (5, 8), "cost": 4}
        ]
    }
]

def get_random_enemy(level=1):
    enemy = random.choice(enemy_pokemon)
    return {
        "name": enemy["name"],
        "hp": enemy["hp"] + level * 2,
        "attack": enemy["attack"] + level,
        "stamina": 10,
        "moves": enemy["moves"]
    }

def get_random_starter():
    poke = random.choice(starter_pokemon)
    return {
        "name": poke["name"],
        "hp": poke["hp"],
        "attack": poke["attack"],
        "stamina": 10,
        "moves": poke["moves"]
    }
