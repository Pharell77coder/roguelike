import pygame

from constants import *


class Tile:
    def __init__(self, image: str, color: str = BLACK, block: bool = False) -> None:
        self.image: str = image
        self.color: str = color
        self.block: bool = block

    def draw(self, surface: pygame.Surface, x: int, y: int) -> None:
        pygame.draw.rect(surface, self.color, (x * SIZE_MAPS, y * SIZE_MAPS, SIZE_MAPS-BORDER, SIZE_MAPS-BORDER))


plains = Tile("", (0, 200, 0))
forest = Tile("", (0, 128, 0))
pines = Tile("", (0, 100, 0))
mountain = Tile("", (139, 69, 19), block=True)
water = Tile("", (0, 191, 255), block=True)
