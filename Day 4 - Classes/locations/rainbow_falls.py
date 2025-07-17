from location_base import Location

class RainbowFalls(Location):
    def __init__(self):
        description = (
            "You have found the RAINBOW FALLS.\n"
            "The rainbows are very colorful and love to dance.\n"
            "What would you like to do?"
        )
        exits = {'o': 'old_oak', 'p': 'pixie_housing'}
        super().__init__('rainbow_falls', description, exits)

    def show_actions(self):
        print("(a) Ask the rainbows to dance\n(l) Leave")

    def handle_action(self, player, action):
        if action == 'a':
            print("The rainbows dance for you. You feel happy.")
        else:
            super().handle_action(player, action)
