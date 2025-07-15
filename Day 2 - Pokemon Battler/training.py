import random

def train(pokemon, level):
    print(f"\n{pokemon['name']} begins training...")
    if pokemon['stamina'] < 4 or pokemon['hp'] < 10:
        print(f"{pokemon['name']} is too tired or injured to train. Try after a battle.")
        return False

    max_attack = 6 + level
    max_hp = 30 + level * 2

    gain_attack = random.choice([0, 1])
    gain_hp = random.randint(1, 3)
    stamina_cost = 3

    if pokemon['attack'] >= max_attack and pokemon['hp'] >= max_hp:
        print(f"{pokemon['name']} is already at peak condition for level {level}.")
        return False

    if pokemon['attack'] < max_attack:
        pokemon['attack'] += gain_attack
        print(f"{pokemon['name']} gains +{gain_attack} attack.")

    if pokemon['hp'] < max_hp:
        pokemon['hp'] += gain_hp
        print(f"{pokemon['name']} gains +{gain_hp} max HP.")

    pokemon['stamina'] -= stamina_cost
    pokemon['hp'] -= 2
    print(f"{pokemon['name']} uses {stamina_cost} stamina and loses 2 HP while training.")
    return True
