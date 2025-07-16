class Player:
    def __init__(self, start_y, start_x):
        self.y = start_y
        self.x = start_x
        self.inventory = []
        self.loot = []
        self.health = 100
        self.gold = 0

    def move(self, direction, dungeon):
        dy, dx = 0, 0
        if direction == 'w':
            dy = -1
        elif direction == 's':
            dy = 1
        elif direction == 'a':
            dx = -1
        elif direction == 'd':
            dx = 1
        else:
            return

        new_y = self.y + dy
        new_x = self.x + dx

        tile = dungeon.tile_at(new_y, new_x)
        if dungeon.can_enter(tile, self):
            self.y = new_y
            self.x = new_x
            dungeon.interact_tile(self)
