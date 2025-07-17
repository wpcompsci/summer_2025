from location_base import Location

class OldOak(Location):
    def __init__(self):
        description = (
            "You have found the OLD OAK.\n"
            "It is the wisest oak tree in the whole forest.\n"
            "What would you like to do?"
        )
        exits = {'p': 'pixie_housing', 'e': 'evil_bunnies', 'r': 'rainbow_falls'}
        super().__init__('old_oak', description, exits)

    def show_actions(self):
        print("(t) Take an acorn\n(l) Leave")

    def handle_action(self, player, action):
        if action == 't':
            if player.has_item("acorn"):
                print("You already have an acorn.")
            else:
                player.add_item("acorn")
                print("You took an acorn.")
        else:
            super().handle_action(player, action)
