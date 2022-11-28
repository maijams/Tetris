import pygame


class GameLoop:
    def __init__(self, game, renderer, event_queue, clock, tile_size):
        self._game = game
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._tile_size = tile_size
        self._counter = 0

    def start(self):
        while True:
            if self._game.block is None:
                self._game.new_block()

            self._counter += 1
             
            if self._game.state == "play" and self._counter % 50 == 0:
                self._game.move_down()

            if self._handle_events() == False:
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
                    pass
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
