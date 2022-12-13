import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Renderer:
    def __init__(self, game_screen, display, grid, game, scoreboard, tile_size):
        self._game_screen = game_screen
        self._display = display
        self._grid = grid
        self._game = game
        self._scoreboard = scoreboard
        self._tile_size = tile_size

    def render(self):
        self._display.fill(BLACK)
        self._game_screen.fill(BLACK)

        self.draw_colored_squares()
        self.draw_active_block()
        self.draw_grid()
        self._display.blit(self._game_screen, (50, 40))

        font = pygame.font.SysFont('Arial', 30)

        points = font.render(
            "Points: " + str(self._game.get_points()), True, WHITE)
        self._display.blit(points, (690, 100))

        if self._game.get_state() == "done":
            game_over = font.render("Game Over !", True, WHITE)
            self._display.blit(game_over, (750, 250))
            self.draw_scoreboard()

        pygame.display.update()

    def draw_colored_squares(self):
        for field_y in range(self._game.height):
            for field_x in range(self._game.width):
                color = self._game.field[field_y][field_x]
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

    def draw_active_block(self):
        for field_y in range(4):
            for field_x in range(4):
                square = field_y*4 + field_x
                if square in self._game.block.figure():
                    rect = pygame.Rect(
                        self._tile_size*(self._game.block.pos_x + field_x),
                        self._tile_size*(self._game.block.pos_y + field_y),
                        self._tile_size, self._tile_size
                    )
                    pygame.draw.rect(
                        self._game_screen,
                        self._game.block.color,
                        rect
                    )

    def draw_grid(self):
        for tile in self._grid:
            pygame.draw.rect(self._game_screen, (240, 240, 240), tile, 1)

    def draw_scoreboard(self):
        font = pygame.font.SysFont('Arial', 30)
        heading = font.render("HIGH SCORES", True, WHITE)
        self._display.blit(heading, (720, 550))

        scoreboard = self._scoreboard.get_scoreboard()
        height = 600
        for row in scoreboard:
            string = f'{row[0]} points   {row[1]}'
            score = font.render(string, True, WHITE)
            self._display.blit(score, (680, height))
            height += 50
