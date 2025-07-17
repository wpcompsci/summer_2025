from utils import clear_screen

class Location:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

    def enter(self, player):
        print(self.description)
        self.show_actions()

    def show_actions(self):
        print("(l) Leave")

    def handle_action(self, player, action):
        if action == 'l':
            self.leave(player)

    def leave(self, player):
        print("Where would you like to go?")
        for key, destination in self.exits.items():
            print(f"({key}) {destination.replace('_', ' ').title()}")
        choice = input(">>> ")
        if choice in self.exits:
            player.location = self.exits[choice]
        else:
            print("Invalid choice.")
