from location_base import Location
from utils import end_game

class EvilBunnies(Location):
    def __init__(self):
        description = (
            "You have found the EVIL BUNNIES.\n"
            "They are very evil and love to bite.\n"
            "What would you like to do?"
        )
        exits = {'o': 'old_oak', 'p': 'pixie_housing'}
        super().__init__('evil_bunnies', description, exits)

    def show_actions(self):
        print("(f) Fight the EVIL BUNNIES\n(r) Run away")

    def handle_action(self, player, action):
        if action == 'f':
            if player.has_item("acorn"):
                print("You throw the acorn at the bunnies. They run away. You win!")
            else:
                print("The bunnies bite you. You lose.")
            end_game()
        elif action == 'r':
            self.leave(player)
        else:
            print("You were too slow. The bunnies bite you. You lose.")
            end_game()
