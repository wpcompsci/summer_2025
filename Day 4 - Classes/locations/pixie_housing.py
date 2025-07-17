from location_base import Location

class PixieHousing(Location):
    def __init__(self):
        description = (
            "You have found the PIXIE HOUSING.\n"
            "The pixies are very friendly and love to dance.\n"
            "What would you like to do?"
        )
        exits = {'o': 'old_oak', 'r': 'rainbow_falls', 'e': 'evil_bunnies'}
        super().__init__('pixie_housing', description, exits)

    def show_actions(self):
        print("(s) Ask the pixies for a secret\n(l) Leave")

    def handle_action(self, player, action):
        if action == 's':
            print("The pixies tell you a secret: 'Bunnies hate acorns.'")
        else:
            super().handle_action(player, action)
