import os
from dungeon import Dungeon
from player import Player
from get_key import get_key

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    dungeon = Dungeon()
    player = Player(1, 1)

    while True:
        clear_screen()
        dungeon.display(player, view_height=9, view_width=17)
        print(f"Health: {player.health} | Keys: {player.inventory.count('key')} | Gold: {player.gold}")


        if (player.y, player.x) == dungeon.goal_pos:
            print("🎉 You reached the goal!")
            if not dungeon.next_level():
                break
            player.y, player.x = 1, 1
            input("Press Enter to start next level...")

        print("Move with W/A/S/D, Q to quit")
        command = get_key()
        if command == 'q':
            print("Game over.")
            break

        player.move(command, dungeon)

if __name__ == "__main__":
    main()