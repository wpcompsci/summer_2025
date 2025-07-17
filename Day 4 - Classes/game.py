from player import Player
from locations import location_map
from utils import clear_screen

def main():
    clear_screen()
    print("Welcome to the SUPER HAPPY MAGIC FOREST!!!\n"
          "Here everybody enjoys picnics, fun, and dancing all year round.\n"
          "Enjoy the rainbows, sunshine and good times.\n"
          "Well they used to, but some things are not right.\n")
    input("Press Enter to start the game.")

    player = Player()
    player.location = "old_oak"

    while True:
        current_location = location_map[player.location]
        clear_screen()
        current_location.enter(player)
        action = input(">>> ")
        current_location.handle_action(player, action)

if __name__ == "__main__":
    main()
