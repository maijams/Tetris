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

        for field_y in range(self._game.height):
            for field_x in range(self._game.width):
                if self._game.field[field_y][field_x] != 0:
                    rect = pygame.Rect(
                        self._tile_size*field_x,
                        self._tile_size*field_y,
                        self._tile_size, self._tile_size
                    )
                    pygame.draw.rect(
                        self._game_screen,
                        self._game.field[field_y][field_x],
                        rect
                    )

        if self._game.block is not None:
            for field_y in range(4):
                for field_x in range(1, 5):
                    square = field_y*4 + field_x
                    if square in self._game.block.figure():
                        rect = pygame.Rect(
                            self._tile_size*(self._game.block.x + field_x-1),
                            self._tile_size*(self._game.block.y + field_y),
                            self._tile_size, self._tile_size
                        )
                        pygame.draw.rect(
                            self._game_screen,
                            self._game.block.color, rect
                        )

        [pygame.draw.rect(self._game_screen, (240, 240, 240), tile, 1)
         for tile in self._grid]

        self._display.blit(self._game_screen, (50, 40))
        pygame.display.update()
