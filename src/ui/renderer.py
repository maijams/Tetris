import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Renderer:
    '''Class that handles the rendering of the game.

    Attributes:
        game_screen: Pygame surface that contains the tetris game.
        display: Pygame display.
        grid: Game grid consisting of pygame rectangles.
        game: Tetris object.
        scoreboard: ScoreBoard object.
        tile_size: Value that determines the size of tetris tiles.
    '''

    def __init__(self, game_screen, display, grid, game, scoreboard, tile_size):
        '''Class constructor that creates a new renderer.

        Args:
            game_screen: Pygame surface that contains the tetris game.
            display: Pygame display.
            grid: Game grid consisting of pygame rectangles.
            game: Tetris object.
            scoreboard: ScoreBoard object.
            tile_size: Value that determines the size of tetris tiles.
        '''

        self._game_screen = game_screen
        self._display = display
        self._grid = grid
        self.game = game
        self._scoreboard = scoreboard
        self._tile_size = tile_size

    def render(self):
        '''Draws elements on display & update pygame display.'''

        self._display.fill(BLACK)
        self._game_screen.fill(BLACK)

        self._draw_colored_squares()
        self._draw_active_block()
        self._draw_grid()
        self._display.blit(self._game_screen, (50, 40))

        self._draw_game_info()

        pygame.display.update()

    def _draw_colored_squares(self):
        '''Draws colored rectangles on game screen surface, according to game field data.'''

        for field_y in range(self.game.height):
            for field_x in range(self.game.width):
                color = self.game.field[field_y][field_x]
                if color != 0:
                    rect = pygame.Rect(
                        self._tile_size * field_x,
                        self._tile_size * field_y,
                        self._tile_size, self._tile_size
                    )
                    pygame.draw.rect(
                        self._game_screen,
                        color,
                        rect
                    )

    def _draw_active_block(self):
        '''Draws the falling (active) block on game screen surface by using pygame rectangles.'''

        block_y = self.game.block.pos_y
        block_x = self.game.block.pos_x

        for field_y in range(4):
            for field_x in range(4):
                square = field_y*4 + field_x
                if square in self.game.block.figure():
                    rect = pygame.Rect(
                        self._tile_size*(block_x + field_x),
                        self._tile_size*(block_y + field_y),
                        self._tile_size, self._tile_size
                    )
                    pygame.draw.rect(
                        self._game_screen,
                        self.game.block.color,
                        rect
                    )

    def _draw_grid(self):
        '''Draws tile grid on game screen surface by using pygame rectangles.'''

        for tile in self._grid:
            pygame.draw.rect(self._game_screen, (240, 240, 240), tile, 1)

    def _draw_scoreboard(self):
        '''Draws scoreboard on game display.'''

        font = pygame.font.SysFont('Arial', 30)
        heading = font.render("HIGH SCORES", True, RED)
        self._display.blit(heading, (720, 500))

        scoreboard = self._scoreboard.get_scoreboard()
        height = 550
        for row in scoreboard:
            string = f'{str(row[0]):4} points   {row[1]}'
            score = font.render(string, True, WHITE)
            self._display.blit(score, (670, height))
            height += 50

    def _draw_game_info(self):
        '''Draws game related info next to the game screen.'''

        font = pygame.font.SysFont('Arial', 30)

        level = font.render(
            "Level:   " + str(self.game.level), True, WHITE)
        self._display.blit(level, (760, 100))

        points = font.render(
            "Points:   " + str(self.game.points), True, WHITE)
        self._display.blit(points, (750, 200))

        if self.game.state == "done":
            game_over = font.render("Game Over !", True, RED)
            self._display.blit(game_over, (740, 350))
            self._draw_scoreboard()

        restart = font.render(
            "Press R to restart the game", True, BLUE)
        self._display.blit(restart, (650, 1120))
