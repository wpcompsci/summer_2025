from pokemon_data import get_random_enemy, get_random_starter
from battle import battle, restore_pokemon
from training import train
from save_system import save_game, load_game

def main():
    print("Welcome to the Pokémon Battle Simulator!")
    pokemon, level = load_game()

    if not pokemon:
        pokemon = get_random_starter()
        base_stats = {"hp": pokemon["hp"]}
        level = 1
        print(f"You've received {pokemon['name']}!")
    else:
        base_stats = {"hp": pokemon["hp"]}

    while True:
        print(f"\nYour Pokémon: {pokemon['name']} | HP: {pokemon['hp']} | ATK: {pokemon['attack']} | Stamina: {pokemon['stamina']}")
        print(f"Level: {int(level)}")
        print("Options: [B]attle | [T]rain | [S]ave | [Q]uit")
        choice = input("> ").lower()

        if choice == 'b':
            enemy = get_random_enemy(int(level))
            win = battle(pokemon, enemy)
            if win:
                level += 1
                print("You leveled up!")
                restore_pokemon(pokemon, base_stats)
                print(f"{pokemon['name']} is fully healed and rested.")
            else:
                break
        elif choice == 't':
            trained = train(pokemon, int(level))
            if trained:
                print("Enemies are getting stronger too...")
                level += 0.25
        elif choice == 's':
            save_game(pokemon, int(level))
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
