import pygame


class Clock:
    '''Class that handles the clock of the game.'''

    def __init__(self):
        '''Class constructor that creates a new pygame clock.'''

        self._clock = pygame.time.Clock()

    def tick(self, fps):
        '''Makes the game clock tick.

        Args:
            fps: Frames per second.
        '''

        self._clock.tick(fps)
