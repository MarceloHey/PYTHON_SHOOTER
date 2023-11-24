import pygame.display
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, mode):
        self.window: Surface = window
        self.name = name
        self.mode = mode
        self.entity_list: list[Entity] = []

        self.entity_list.extend(EntityFactory.get_entity('lv1_bg'))

    def run(self):
        while True:
            for entity in self.entity_list:
                self.window.blit(source=entity.surface, dest=entity.rect)
                entity.move()
            pygame.display.flip()
        pass
