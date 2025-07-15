import random
import time

def display_moves(pokemon):
    print("\nChoose a move:")
    for i, move in enumerate(pokemon["moves"]):
        print(f"{i + 1}. {move['name']} (Damage: {move['damage'][0]}–{move['damage'][1]}, Stamina: {move['cost']})")
    time.sleep(0.5)

def choose_move(pokemon):
    while True:
        display_moves(pokemon)
        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(pokemon["moves"]):
                move = pokemon["moves"][choice]
                if pokemon["stamina"] >= move["cost"]:
                    return move
                else:
                    print("Not enough stamina.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")

def enemy_choose_move(enemy):
    affordable = [m for m in enemy["moves"] if m["cost"] <= enemy["stamina"]]
    return random.choice(affordable if affordable else enemy["moves"])

def restore_pokemon(pokemon, base_stats):
    pokemon["hp"] = base_stats["hp"]
    pokemon["stamina"] = 10

def battle(player, enemy):
    print(f"\nA wild {enemy['name']} appears!")
    time.sleep(1)

    while player["hp"] > 0 and enemy["hp"] > 0:
        print(f"\n🟢 {player['name']} — HP: {player['hp']}, Stamina: {player['stamina']}")
        print(f"🔴 {enemy['name']} — HP: {enemy['hp']}, Stamina: {enemy['stamina']}")
        time.sleep(0.5)

        move = choose_move(player)
        damage = random.randint(*move["damage"])
        print(f"\n{player['name']} uses {move['name']}!")
        time.sleep(1)
        print(f"It deals {damage} damage!")
        enemy["hp"] -= damage
        player["stamina"] -= move["cost"]
        time.sleep(1)

        if enemy["hp"] <= 0:
            print(f"\n{enemy['name']} fainted! You win!")
            time.sleep(1)
            return True

        emove = enemy_choose_move(enemy)
        edamage = random.randint(*emove["damage"])
        print(f"\n{enemy['name']} uses {emove['name']}!")
        time.sleep(1)
        print(f"It hits for {edamage} damage!")
        player["hp"] -= edamage
        enemy["stamina"] -= emove["cost"]
        time.sleep(1)

        if player["hp"] <= 0:
            print(f"\n{player['name']} fainted... Game over.")
            return False

        player["stamina"] = min(player["stamina"] + 2, 10)
        enemy["stamina"] = min(enemy["stamina"] + 2, 10)

    return False
