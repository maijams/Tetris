import pygame


class Renderer:
    def __init__(self, display, game_screen, grid):
        self._display = display
        self._game_screen = game_screen
        self._grid = grid

    def render(self):
        [pygame.draw.rect(self._game_screen, (255,255,255), tile, 1) for tile in self._grid]
        self._display.blit(self._game_screen, (50, 40))
        pygame.display.update()