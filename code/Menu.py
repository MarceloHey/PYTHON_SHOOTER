import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import WIN_WIDTH, COLOR_WHITE, COLOR_YELLOW, MENU_OPTIONS


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surface = pygame.image.load('./assets/menu_bg.png')
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./assets/menu.wav')
        # pygame.mixer_music.play(-1)
        # pygame.mixer_music.set_volume(0.2)

        current_option = 0

        while (True):
            self.window.blit(source=self.surface, dest=self.rect)
            self.menu_text(50, "MOUNTAIN", COLOR_WHITE, (WIN_WIDTH / 2, 50))
            self.menu_text(50, "SHOOTER", COLOR_WHITE, (WIN_WIDTH / 2, 100))

            # RENDER MENU
            for i in range(len(MENU_OPTIONS)):
                if current_option == i:
                    self.menu_text(30, MENU_OPTIONS[i], COLOR_YELLOW, (WIN_WIDTH / 2, 180 + 40 * i))
                else:
                    self.menu_text(30, MENU_OPTIONS[i], COLOR_WHITE, (WIN_WIDTH / 2, 180 + 40 * i))

            pygame.display.flip()

            # CHECK FOR MENU EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if current_option < len(MENU_OPTIONS) - 1:
                            current_option += 1
                        else:
                            current_option = 0

                    if event.key == pygame.K_UP:
                        if current_option > 0:
                            current_option -= 1
                        else:
                            current_option = len(MENU_OPTIONS) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[current_option]
        pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lacida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect)
        pass
