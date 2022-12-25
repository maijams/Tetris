import pygame
from tetris import Tetris


class GameLoop:
    '''Class that runs the game.

    Attributes:
        game: Tetris object.
        scoreboard: ScoreBoard object.
        renderer: Renderer object.
        event_queue: EventQueue object.
        clock: Clock object.
        tile_size: Value that determines the size of tetris tiles.
    '''

    def __init__(self, game, scoreboard, renderer, event_queue, clock, tile_size):
        '''Class constructor that creates a new gameloop.

        Args:
            game: Tetris object.
            scoreboard: ScoreBoard object.
            renderer: Renderer object.
            event_queue: EventQueue object.
            clock: Clock object.
            tile_size: Value that determines the size of tetris tiles.
        '''

        self._game = game
        self._scoreboard = scoreboard
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._tile_size = tile_size
        self._counter = 0
        self._speed_down = False

    def start(self):
        '''Handles the main loop of the game.'''

        level_speed = [0, 50, 40, 30, 20, 10]

        while True:
            self._counter += 1
            if self._counter > 10000:
                self._counter = 0

            if self._game.state == "end":
                if self._game.points > 0:
                    self._save_score()
                self._game.state = "done"

            if self._game.state == "play":
                level = self._game.level
                if self._counter % level_speed[level] == 0 or self._speed_down:
                    move_down = self._game.move_down()
                    if not move_down:
                        self._speed_down = False

            if self._handle_events() is False:
                break

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        '''Handles pygame events.

        Returns:
            False if event type is QUIT, otherwise True.
        '''

        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self._game.move_sideways(-1)

                if event.key == pygame.K_RIGHT:
                    self._game.move_sideways(1)

                if event.key == pygame.K_UP:
                    self._game.rotate()

                if event.key == pygame.K_DOWN:
                    self._speed_down = True

                if event.key == pygame.K_r:
                    self._restart_game()

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_DOWN:
                    self._speed_down = False

            elif event.type == pygame.QUIT:
                return False

        return True

    def _render(self):
        '''Renders current game display.'''

        self._renderer.render()

    def _save_score(self):
        '''Saves gamescore to database.'''

        self._scoreboard.save_score(self._game.points)

    def _restart_game(self):
        '''Restarts new game.'''

        height = self._game.height
        width = self._game.width
        new_game = Tetris(height, width)
        self._game = new_game
        self._game.new_block()
        self._renderer.game = new_game
