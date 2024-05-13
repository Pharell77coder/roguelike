import pygame

from constants import *


class Tile:
    def __init__(self, image: str, color: str = BLACK, block: bool = False) -> None:
        self.image: str = image
        self.color: str = color
        self.block: bool = block

    def draw(self, surface: pygame.Surface, x: int, y: int) -> None:
        pygame.draw.rect(surface, self.color, (x * SIZE_MAPS, y * SIZE_MAPS, SIZE_MAPS, SIZE_MAPS))


plains = Tile("", YELLOW)
forest = Tile("", GREEN)
pines = Tile("", CYAN)
mountain = Tile("", WHITE, block=True)
water = Tile("", BLUE, block=True)
