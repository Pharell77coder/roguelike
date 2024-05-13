import pygame
import random

from tile import Tile, plains, forest, pines, mountain, water


class Map:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.map_data: list[list[Tile]] | None = None
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
            width = random.randint(min_size, max_size)
            height = random.randint(min_size, max_size)
            start_x = random.randint(1, self.width - width - 1)
            start_y = random.randint(1, self.height - height - 1)

            for i in range(height):
                if irregular:
                    width = random.randint(int(0.7 * max_size), max_size)
                    start_x = random.randint(3, self.width - max_size) - random.randint(1, 2)
                for j in range(width):
                    self.map_data[start_y + i][start_x + j] = tile

    def draw_map(self, window: pygame.Surface) -> None:
        for x, row in enumerate(self.map_data):
            for y, tile in enumerate(row):
                tile.draw(window, x, y)
