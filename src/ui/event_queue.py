import pygame


class EventQueue:
    '''Class that handles pygame events.'''

    def get(self):
        '''Get all pygame events.

        Returns:
            List of pygame events.
        '''

        return pygame.event.get()
