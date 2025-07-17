class Player:
    def __init__(self):
        self.inventory = []
        self.location = None

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    def has_item(self, item):
        return item in self.inventory
