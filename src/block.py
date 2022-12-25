import random


BLUE = (66, 135, 245)
PINK = (245, 66, 218)
GREEN = (147, 245, 66)
PURPLE = (137, 68, 227)
YELLOW = (230, 227, 94)
RED = (189, 45, 62)
ORANGE = (189, 98, 45)
LIGHTBLUE = (45, 189, 184)


class Block:
    '''Class that handles the events of a falling block.

    Attributes:
        location_x: Horizontal coordinate of the block in Pygame grid.
        location_y: Vertical coordinate of the block in Pygame grid.
    '''

    blocks = [
        [[1, 2, 5, 6]],
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 5, 6, 10], [5, 6, 8, 9]],
        [[2, 5, 6, 9], [5, 6, 10, 11]],
        [[1, 5, 9, 10], [5, 6, 7, 9], [5, 6, 10, 14], [6, 8, 9, 10]],
        [[2, 6, 9, 10], [5, 9, 10, 11], [5, 6, 9, 13], [4, 5, 6, 10]],
        [[1, 5, 6, 9], [5, 6, 7, 10], [6, 9, 10, 14], [5, 8, 9, 10]]
    ]

    colors = [BLUE, PINK, GREEN, PURPLE, YELLOW, RED, ORANGE, LIGHTBLUE]

    def __init__(self, location_x, location_y):
        '''Class constructor that creates a new falling block
        by randomly choosing the shape & color.

        Args:
            pos_x: Horizontal coordinate of the block in Pygame grid.
            pos_y: Vertical coordinate of the block in Pygame grid.
        '''

        self.pos_x = location_x
        self.pos_y = location_y
        self.shape = random.randint(0, len(self.blocks)-1)
        self.rotation = 0
        self.color = self.colors[random.randint(0, len(self.colors)-1)]

    def rotate(self):
        '''Rotates the block by changing the values in 4x4 area.

        If rotation value is already at the last possible rotation, rotation returns to zero.
        Else rotation is increased by one.
        '''

        if self.rotation == len(self.blocks[self.shape])-1:
            self.rotation = 0
        else:
            self.rotation += 1

    def reverse_rotate(self):
        '''Reverses the block rotation if the block collides with walls or other blocks.

        If rotation value is zero, rotation value is changed to last possible rotation.
        Else rotation is decreased by one.
        '''

        if self.rotation == 0:
            self.rotation = len(self.blocks[self.shape])-1
        else:
            self.rotation -= 1

    def figure(self):
        '''Returns:
            The current state of the block, i.e. the block shape & rotation combination.
        '''

        return self.blocks[self.shape][self.rotation]

    def move_down(self):
        '''Increases the y coordinate of the block by one.'''

        self.pos_y += 1

    def move_up(self):
        '''Decreases the y coordinate of the block by one.'''

        self.pos_y -= 1

    def move_sideways(self, direction):
        '''Change the x coordinate of the block by one.

        Args:
            direction: Direction where the block should be moved to. -1 = left, 1 = right.
        '''

        self.pos_x += direction

    def set_horizontal_position(self, pos_x):
        '''Set the horizontal position of the block.

        Args:
            pos_x: New position of the block.
        '''

        self.pos_x = pos_x
