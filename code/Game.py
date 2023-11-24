import sys

import pygame

from code.Constants import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from code.Menu import Menu
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while (True):
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()
            else:
                pygame.quit()
                sys.exit()


