import pygame
import random

from tile import Tile


class Entity:
    def __init__(self, windows: pygame.Surface, x: int, y: int):
        self.windows: pygame.Surface = windows
        self.position: list = [x, y]
        self.image: Tile = Tile("", (0, 0, (random.randint(0, 255))), block=True)
        self.current_time: pygame.time = pygame.time.get_ticks()
        self.horizontal = random.choice(['up', 'down', 'idle'])
        self.vertical = random.choice(['right', 'left', 'idle'])

    def move(self, maps: list[list[Tile]], position: list[int], current) -> None:
        if current - self.current_time > random.uniform(100, 1000):
            self.horizontal = random.choice(['up', 'down', 'idle'])
            self.vertical = random.choice(['right', 'left', 'idle'])
            self.current_time = pygame.time.get_ticks()
        if self.vertical == 'left' and not self.collide(maps, position, self.position[0] - 1, self.position[1]):
            self.position[0] -= 1
        if self.vertical == 'right' and not self.collide(maps, position, self.position[0] + 1, self.position[1]):
            self.position[0] += 1
        if self.horizontal == 'up' and  not self.collide(maps, position, self.position[0], self.position[1] - 1):
            self.position[1] -= 1
        if self.horizontal == 'down' and not self.collide(maps, position, self.position[0], self.position[1] + 1):
            self.position[1] += 1

    def draw(self) -> None:
        self.image.draw(self.windows, self.position[0], self.position[1])

    def collide(self, maps: list[list[Tile]], position: list[int], x: int, y: int) -> bool:
        if (0 <= x < len(maps) and 0 <= y < len(maps[0])):
            for pos in position:
                if pos == [x, y]:
                    return True
            return maps[x][y].block
        return True
