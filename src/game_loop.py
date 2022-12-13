import pygame


class GameLoop:
    '''Class that handles '''
    def __init__(self, game, scoreboard, renderer, event_queue, clock, tile_size):
        self._game = game
        self._scoreboard = scoreboard
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._tile_size = tile_size
        self._counter = 0
        self._speed_down = False

    def start(self):
        while True:
            if self._game.block is None:
                self._game.new_block()

            self._counter += 1
            if self._counter > 10000:
                self._counter = 0

            if self._counter % 50 == 0 or self._speed_down:
                if self._game.get_state() == "play":
                    move_down = self._game.move_down()
                    if not move_down:
                        self._speed_down = False

            if self._game.get_state() == "end":
                self._scoreboard.save_score(self._game.get_points())
                self._game.state = "done"

            if self._handle_events() == "quit":
                break

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self._speed_down = False
            elif event.type == pygame.QUIT:
                return "quit"
        return "continue"

    

    def _render(self):
        self._renderer.render()
