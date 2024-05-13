import pygame

from constants import *
from tile import Tile


class Entity:
    def __init__(self, windows: pygame.Surface, x: int, y: int):
        self.windows: pygame.Surface = windows
        self.position: list = [x, y]
        self.image: Tile = Tile("", MAGENTA, block=True)

    def move(self, maps: list[list[Tile]], keys: int) -> None:
        if keys == 0 and maps[self.position[0] - 1][self.position[1]].block == 0:
            self.position[0] = max(0, self.position[0] - 1)
        elif keys == 1 and not self.collide(maps, self.position[0] + 1, self.position[1]):
            self.position[0] += 1
        elif keys == 2 and maps[self.position[0]][self.position[1] - 1].block == 0:
            self.position[1] = max(0, self.position[1] - 1)
        elif keys == 3 and not self.collide(maps, self.position[0], self.position[1] + 1):
            self.position[1] += 1

    def draw(self) -> None:
        self.image.draw(self.windows, self.position[0], self.position[1])

    @staticmethod
    def collide(maps: list[list[Tile]], x: int, y: int) -> bool:
        if x < len(maps) and y < len(maps[0]):
            return maps[x][y].block
        return True
