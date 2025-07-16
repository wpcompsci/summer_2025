import random
import os

class Dungeon:
    def __init__(self):
        self.levels = [
            self.load_level_from_file("level1.txt"),
            self.load_level_from_file("level2.txt")
        ]  # Add more levels as needed
        self.current_level_index = 0
        self.map = self.levels[self.current_level_index]
        self.goal_pos = self.find_tile('X')

    def load_level_from_file(self, filename):
        path = os.path.join("levels", filename)
        with open(path, 'r') as f:
            raw_map = [line.rstrip("\\n") for line in f.readlines()]
        return self.pad_map(raw_map)

    def pad_map(self, raw_map):
        max_width = max(len(row) for row in raw_map)
        return [list(row.ljust(max_width)) for row in raw_map]

    def find_tile(self, symbol):
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == symbol:
                    return (y, x)
        return (1, 1)  # fallback if not found

    def load_level1(self):
        raw_map = [
            "########################################",
            "#     #    k####    #  G  #     D#  H ##",
            "# ### #  ####     #   #  #  ### #     #",
            "#   #     #        #####  #     #     #",
            "# # #####     ######      #######  ###",
            "# #      ####            #         #X#",
            "# ####      ####   #######  ####  #  #",
            "#     #########     #     #      #   #",
            "###              ##########    #######",
            "#    #    #     #      #   ##     #  #",
            "########################################",
        ]
        return self.pad_map(raw_map)

    def can_enter(self, tile, player):
        if tile == '#':
            return False
        elif tile == 'D':
            if 'key' in player.inventory:
                print("🔓 You unlocked the door!")
                return True
            else:
                print("🔐 The door is locked. You need a key.")
                return False
        return True

    def interact_tile(self, player):
        tile = self.map[player.y][player.x]
        if tile == 'k':
            print("🗝️  You picked up a key!")
            player.inventory.append('key')
            self.map[player.y][player.x] = ' '
        elif tile == 'D' and 'key' in player.inventory:
            print("🔓 You used a key to unlock the door.")
            self.map[player.y][player.x] = ' '
            player.inventory.remove('key')
        elif tile == 'G':
            amount = random.randint(5, 20)
            print(f"💰 You found gold! +{amount}")
            player.gold += amount
            self.map[player.y][player.x] = ' '
        elif tile == 'H':
            amount = random.randint(5, 15)
            player.health = min(player.health + amount, 100)
            print(f"❤️ You found a health potion! +{amount} HP")
            self.map[player.y][player.x] = ' '

    def next_level(self):
        self.current_level_index += 1
        if self.current_level_index >= len(self.levels):
            print("🎉 You completed all levels!")
            return False
        self.map = self.levels[self.current_level_index]
        self.goal_pos = self.place_goal()
        return True

    def display(self, player, view_height=9, view_width=17):
        half_h = view_height // 2
        half_w = view_width // 2

        max_y = len(self.map)
        max_x = len(self.map[0])

        start_y = max(0, min(player.y - half_h, max_y - view_height))
        end_y = start_y + view_height

        start_x = max(0, min(player.x - half_w, max_x - view_width))
        end_x = start_x + view_width

        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                if (y, x) == (player.y, player.x):
                    print("@", end="")
                else:
                    print(self.map[y][x], end="")
            print()

    def tile_at(self, y, x):
        if 0 <= y < len(self.map) and 0 <= x < len(self.map[0]):
            return self.map[y][x]
        return "#"