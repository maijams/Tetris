import pygame


class Renderer:
    def __init__(self, game, display, game_screen, grid, tile_size):
        self._game = game
        self._display = display
        self._game_screen = game_screen
        self._grid = grid
        self._tile_size = tile_size

    def render(self):
        self._game_screen.fill((0, 0, 0))
        [pygame.draw.rect(self._game_screen, (255, 255, 255), tile, 1)
         for tile in self._grid]
        
        for Y in range(self._game.height):
            for X in range(self._game.width):
                if self._game.field[Y][X] != 0:
                    rect = pygame.Rect(self._tile_size*X, self._tile_size*Y, self._tile_size, self._tile_size)
                    pygame.draw.rect(self._game_screen,
                                         self._game.field[Y][X], rect)
        
        if self._game.block is not None:
            for y in range(4):
                for x in range(1, 5):
                    square = y*4 + x
                    if square in self._game.block.figure():
                        rect = pygame.Rect(self._tile_size*(self._game.block.x + x-1), self._tile_size*(
                            self._game.block.y + y), self._tile_size, self._tile_size)
                        pygame.draw.rect(self._game_screen,
                                         self._game.block.color, rect)

        self._display.blit(self._game_screen, (50, 40))
        pygame.display.update()
