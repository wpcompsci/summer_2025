class Player:
    def __init__(self, start_y, start_x):
        self.y = start_y
        self.x = start_x

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
        if dungeon.tile_at(new_y, new_x) != '#':
            self.y = new_y
            self.x = new_x