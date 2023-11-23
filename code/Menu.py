import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import WIN_WIDTH, WIN_HEIGHT


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surface = pygame.image.load('./assets/menu_bg.png')
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./assets/menu.wav')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.2)

        while(True):
            self.window.blit(source=self.surface, dest=self.rect)
            self.menu_text(50, "Mountain", (255, 255, 255), (WIN_WIDTH / 2, WIN_HEIGHT / 2))

            pygame.display.flip()
        pass

    def menu_text(self, text_size: int, text: str, text_color:tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lacida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect)
        pass
