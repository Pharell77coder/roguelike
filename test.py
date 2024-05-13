from random import randint

ANSI_RESET = "\033[0m"
ANSI_YELLOW = "\033[33m"
ANSI_GREEN = "\033[32m"
ANSI_BLUE = "\033[34m"
ANSI_RED = "\033[31m"
ANSI_WHITE = "\033[97m"
ANSI_MAGENTA = "\033[35m"
ANSI_CYAN = "\033[36m"

class Tile:
    def __init__(self, symbol: str, color: str = ANSI_RESET, colored: bool = True) -> None:
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if colored else symbol

plains = Tile(".", ANSI_YELLOW)
forest = Tile("8", ANSI_GREEN)
pines = Tile("Y", ANSI_GREEN)
mountain = Tile("A", ANSI_WHITE)
water = Tile("~", ANSI_CYAN)
player = Tile("X", ANSI_RED)


class Map:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.map_data: list[list[Tile]]
        self.generate_map()
        self.generate_patch(forest, 2, 5, 7)
        self.generate_patch(pines, 2, 2, 5)
        self.generate_patch(mountain, 3, 5, 7)
        self.generate_patch(water, 1, 10, 12)

    def generate_map(self) -> None:
        self.map_data = [[plains for _ in range(self.width)] for _ in range(self.height)]

    def generate_patch(self, tile: Tile, num_patches: int, min_size: int, max_size: int,
                       irregular: bool = True) -> None:
        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            start_x = randint(1, self.width - width - 1)
            start_y = randint(1, self.height - height - 1)

            if irregular:
                init_start_x = randint(3, self.width - max_size)
            for i in range(height):
                if irregular:
                    width = randint(int(0.7 * max_size), max_size)
                    start_x = randint(3, self.width - max_size) - randint(1, 2)
                for j in range(width):
                    self.map_data[start_y + i][start_x + j] = tile

    def display_map(self) -> None:
        frame = "X" + self.width * "=" + "X"
        print(frame)
        for row in self.map_data:
            row_tiles = [tile.symbol for tile in row]
            print("|" + "".join(row_tiles) + "|")
        print(frame)


def run() -> None:
    while True:
        game_map.display_map()
        input("> ")

if __name__ == "__main__":
    map_w, map_h = 30, 15
    game_map = Map(map_w, map_h)
    run()

