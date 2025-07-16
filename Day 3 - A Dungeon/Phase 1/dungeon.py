import random

class Dungeon:
    def __init__(self):
        self.levels = [self.load_level1(), self.load_level2()]
        self.current_level_index = 0
        self.map = self.levels[self.current_level_index]
        self.goal_pos = self.place_goal()

    def pad_map(self, raw_map):
        max_width = max(len(row) for row in raw_map)
        return [list(row.ljust(max_width)) if isinstance(row, str) else row + [' '] * (max_width - len(row)) for row in
                raw_map]

    def load_level1(self):
        raw_map = [
            "########################################",
            "#     #       ####    #     #      #  #",
            "# ### #  ####     #   #  #  #  ### #  #",
            "#   #     #        #####  #     #    #",
            "# # #####     ######      #######  ###",
            "# #      ####            #         # #",
            "# ####      ####   #######  ####  #  #",
            "#     #########     #     #      #   #",
            "###              ##########    #######",
            "#    #    #     #      #   ##     #  #",
            "########################################",
        ]
        return self.pad_map(raw_map)

    def load_level2(self):
        raw_map = [
            "########################################",
            "#    #       #       ###      #     # #",
            "# ## ##### # #  ###     ####  #  #  # #",
            "#  #     # #      #   #    #  #     # #",
            "##   ## ####  #######    #  ####### # #",
            "#        #        ##     #         #  #",
            "# ######    #######  #######  ###  #  #",
            "#     ########    ##     #     #     ##",
            "###              ##########    ####### ",
            "#    #  # #   #     #   ##   #     #  #",
            "########################################",
        ]
        return self.pad_map(raw_map)

    def place_goal(self):
        empty_spaces = [(y, x) for y in range(len(self.map))
                        for x in range(len(self.map[0]))
                        if self.map[y][x] == ' ']
        goal_y, goal_x = random.choice(empty_spaces)
        self.map[goal_y][goal_x] = 'X'
        return (goal_y, goal_x)

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