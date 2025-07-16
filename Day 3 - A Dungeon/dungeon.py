import random
import os
import time


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
            raw_map = [line.rstrip('\n') for line in f.readlines()]

        # 🔍 Debugging aid: check line lengths
        for i, row in enumerate(raw_map):
            print(f"Line {i + 1:02}: {len(row)} chars -> {repr(row)}")

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
        elif tile == 'E':
            return True
        elif tile == 'D':
            if 'key' in player.inventory:
                print("🔓 You unlocked the door!")
                return True
            else:
                print("🔐 The door is locked. You need a key.")
                return False
        return True

    def move_enemies(self, player):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # N, S, W, E
        enemy_positions = []

        # Find all current enemies
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == 'E':
                    enemy_positions.append((y, x))

        # Try moving each enemy
        for y, x in enemy_positions:
            random.shuffle(directions)
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if (ny, nx) == (player.y, player.x):
                    print("⚔️ An enemy strikes you!")
                    player.take_damage(random.randint(1, 5))
                    time.sleep(0.5)
                    break  # Stop moving this enemy
                elif self.tile_at(ny, nx) == ' ':
                    self.map[ny][nx] = 'E'
                    self.map[y][x] = ' '
                    break

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

        elif tile == 'E':
            enemy_hp = random.randint(10, 20)
            print(f"👾 You encounter an enemy with {enemy_hp} HP!")

            while enemy_hp > 0 and player.health > 0:
                input("🗡️ Press Enter to attack...")

                # Player attacks
                dmg = random.randint(5, 10)
                enemy_hp -= dmg
                print(f"🗡️  You hit the enemy for {dmg} damage! Enemy HP: {max(enemy_hp, 0)}")
                time.sleep(0.5)

                # Enemy retaliates only if still alive
                if enemy_hp > 0:
                    retaliation = random.randint(1, 5)
                    print(f"👾 Enemy strikes back for {retaliation} damage!")
                    player.take_damage(retaliation)
                    time.sleep(0.5)

                if player.health <= 0:
                    print("💀 You were defeated by the enemy!")
                    return

            print("✅ Enemy defeated!")
            loot = random.randint(5, 15)
            print(f"💰 You collect {loot} gold!")
            player.gold += loot
            self.map[player.y][player.x] = ' '
            input("Press Enter to continue...")


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
