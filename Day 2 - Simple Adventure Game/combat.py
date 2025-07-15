import random
from enemies import get_random_enemy


def encounter_enemy(name, hp, gold, inventory):
    enemy = get_random_enemy()
    enemy_name = enemy["name"]
    enemy_hp = enemy["hp"]
    defense = calculate_defense(inventory)

    print(f"{name} encounters a {enemy_name}!")

    while enemy_hp > 0 and hp > 0:
        action = input("Do you want to (attack/use/run)? ").lower()
        if action == "attack":
            damage = random.randint(1, 3)
            enemy_hp -= damage
            print(f"You hit the {enemy_name} for {damage} damage.")
            if enemy_hp <= 0:
                loot = random.randint(*enemy["gold"])
                gold += loot
                print(f"You defeated the {enemy_name} and gained {loot} gold.")
                break
            enemy_attack = max(0, random.randint(*enemy["attack"]) - defense)
            hp -= enemy_attack
            print(f"The {enemy_name} hits you for {enemy_attack} damage.")
        elif action == "use":
            if "Potion" in inventory:
                heal = 5
                hp += heal
                inventory.remove("Potion")
                print(f"You use a Potion and recover {heal} HP.")
            else:
                print("You have no Potions.")
        elif action == "run":
            print("You escaped!")
            break
        else:
            print("Invalid action.")
    return hp, gold


def calculate_defense(inventory):
    defense = 0
    if "Shield" in inventory:
        defense += 1
    if "Helmet" in inventory:
        defense += 1
    return defense