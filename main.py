import random
import pygame
import sys
import threading
import time

from maps import Map
from constants import *
from player import Player
from entity import Entity
from ennemy import Ennemy

class Game:
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()
        self.windows = pygame.display.set_mode((FENETRE_LARGEUR, FENETRE_HAUTEUR))
        pygame.display.set_caption("Roguelike")
        self.clock = pygame.time.Clock()
        self.create_world()

    def create_world(self):
        self.maps = Map(SIZE_MAPS, SIZE_MAPS)
        self.player = Player(self.windows, 0, 0)
        self.entities = [self.player,]
        coordonnées = [[0,0]]
        i = 0
        while i < NUMBERS_ENTITIES:
            x = random.randint(0, SIZE_MAPS - 1)
            y = random.randint(0, SIZE_MAPS - 1)
            if not self.maps.map_data[x][y].block and [x,y] not in coordonnées:
                self.entities.append(Entity(self.windows, x,y))
                i +=1
            coordonnées.append([x, y])

        while i < NUMBERS_ENTITIES + NUMBERS_ENNEMIES:
            x = random.randint(0, SIZE_MAPS - 1)
            y = random.randint(0, SIZE_MAPS - 1)
            if not self.maps.map_data[x][y].block and [x,y] not in coordonnées:
                self.entities.append(Ennemy(self.windows, x,y))
                i +=1
            coordonnées.append([x, y])

    def update_entity(self, entity):
        if entity == self.player:
            direction = pygame.key.get_pressed()
            position = [entity.position for entity in self.entities]
            self.player.move(self.maps.map_data, position, keys=direction)
            self.player.draw()
        else:
            position = [self.player.position] + [other_entity.position for other_entity in self.entities if
                                                other_entity != entity]
            entity.move(self.maps.map_data, position, pygame.time.get_ticks())
            entity.draw()
    def run(self):        # Créez des threads pour chaque entité
        threads = [threading.Thread(target=self.update_entity, args=(entity,)) for entity in self.entities]

        # Démarrez tous les threads
        for thread in threads:
            thread.start()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.windows.fill(BLACK)
            self.maps.draw_map(self.windows)

            # Mise à jour de chaque entité
            for entity in self.entities:
                self.update_entity(entity)

            pygame.display.flip()
            self.clock.tick(FPS)

        # Attendez que tous les threads soient terminés avant de quitter
        for thread in threads:
            thread.join()



# Fonction principale du jeu
def main():
    game = Game()
    game.run()


# Lancement du jeu
if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
