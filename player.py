import pygame

from constants import *
from tile import Tile
from entity import Entity


class Player(Entity):
    def __init__(self, windows: pygame.Surface, x: int, y: int):
        super().__init__(windows, x, y)
        self.image: Tile = Tile("", (200, 200, 200), block=True)

    def move(self, maps: list[list[Tile]], position: list[int],keys: pygame.key) -> None:
        if keys[pygame.K_LEFT] and not self.collide(maps, position, self.position[0] - 1, self.position[1]):
            self.position[0] -= 1
        if keys[pygame.K_RIGHT] and not self.collide(maps, position, self.position[0] + 1, self.position[1]):
            self.position[0] += 1
        if keys[pygame.K_UP] and  not self.collide(maps, position, self.position[0], self.position[1] - 1):
            self.position[1] -= 1
        if keys[pygame.K_DOWN] and not self.collide(maps, position, self.position[0], self.position[1] + 1):
            self.position[1] += 1
