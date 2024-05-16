import pygame
import random

from entity import Entity
from tile import Tile
from player import Player

class Ennemy(Entity):
    def __init__(self, windows: pygame.Surface, x: int, y: int):
        super().__init__(windows, x, y)
        self.windows: pygame.Surface = windows
        self.position: list = [x, y]
        self.image: Tile = Tile("", (random.randint(0, 255), 0, 0), block=True)
        self.current_time = pygame.time.get_ticks()
        self.keys = random.randint(0, 4)

    def collide(self, maps: list[list[Tile]], position: list[int], x: int, y: int) -> bool:
        if (0 <= x < len(maps) and 0 <= y < len(maps[0])):
            for pos in position:
                if pos == [x, y]:
                    if isinstance(self, Player):
                        del self
                    else:
                        return True
            return maps[x][y].block
        return True