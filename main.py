import random

import pygame
import sys

from maps import Map
from constants import *
from player import Player
from entity import Entity


class Game:
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()
        self.windows = pygame.display.set_mode((FENETRE_LARGEUR, FENETRE_HAUTEUR))
        pygame.display.set_caption("Roguelike")
        self.clock = pygame.time.Clock()

    def run(self):
        maps = Map(SIZE_MAPS, SIZE_MAPS)
        player = Player(self.windows, 0, 0)
        entities = [Entity(self.windows, random.randint(0, SIZE_MAPS - 1), random.randint(0, SIZE_MAPS - 1)) for _ in range(NUMBERS_ENTITIES)]
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            direction = pygame.key.get_pressed()
            #position = [player.position] + [entity.position for entity in entities]
            player.move(maps.map_data, keys = direction)
            for entity in entities:
                entity.move(maps.map_data, keys = random.randint(0, 4))
            self.windows.fill(BLACK)
            maps.draw_map(self.windows)
            player.draw()
            for entity in entities:
                entity.draw()
            pygame.display.flip()
            self.clock.tick(FPS)


# Fonction principale du jeu
def main():
    game = Game()
    game.run()


# Lancement du jeu
if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
