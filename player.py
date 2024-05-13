import pygame

from constants import *
from tile import Tile
from entity import Entity


class Player(Entity):
    def __init__(self, windows: pygame.Surface, x: int, y: int):
        super().__init__(windows, x, y)
        self.image: Tile = Tile("", RED, block=True)

    def move(self, maps: list[list[Tile]], keys: pygame.key) -> None:
        if keys[pygame.K_LEFT] and maps[self.position[0] - 1][self.position[1]].block == 0:
            self.position[0] = max(0, self.position[0] - 1)
        elif keys[pygame.K_RIGHT] and not self.collide(maps, self.position[0] + 1, self.position[1]):
            self.position[0] += 1
        elif keys[pygame.K_UP] and maps[self.position[0]][self.position[1] - 1].block == 0:
            self.position[1] = max(0, self.position[1] - 1)
        elif keys[pygame.K_DOWN] and not self.collide(maps, self.position[0], self.position[1] + 1):
            self.position[1] += 1
