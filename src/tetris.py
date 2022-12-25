from math import ceil
from block import Block


class Tetris:
    '''Class that handles the game state & events.

    Attributes:
        height: The height of the game grid.
        width: The width of the game grid.
    '''

    def __init__(self, height, width):
        '''Class constructor that creates a new Tetris game.

        Args:
            height: The height of the game grid.
            width: The width of the game grid.
        '''

        self.height = height
        self.width = width
        self.state = "play"
        self.block = None
        self.field = [[0]*width for _ in range(height)]
        self.points = 0
        self.level = 1

    def new_block(self):
        '''Creates a new falling block at the top of the game grid.'''

        self.block = Block(3, 0)

    def move_down(self):
        '''Moves the falling block one step downwards.

        If block collides with other objects, the step is reversed and the block freezes.

        Returns:
            False if collision happens, otherwise True.
        '''

        self.block.move_down()
        if self._collision():
            self.block.move_up()
            self._freeze()
            return False
        return True

    def move_sideways(self, direction):
        '''Moves the falling block in the given horizontal direction.

        If block collides with other objects, the step is reversed.

        Args:
            direction: Direction where the block should be moved to. -1 = left, 1 = right.
        '''

        current_x = self.block.pos_x
        self.block.move_sideways(direction)
        if self._collision():
            self.block.set_horizontal_position(current_x)

    def rotate(self):
        '''Rotates the falling block.

        If block collides with other objects, the step is reversed.
        '''

        self.block.rotate()
        if self._collision():
            self.block.reverse_rotate()

    def _collision(self):
        '''Checks whether the falling block collides with walls, floor or other blocks.

        Returns:
            True, if collision happens. False, if no collision.
        '''

        block_y = self.block.pos_y
        block_x = self.block.pos_x

        for field_y in range(4):
            for field_x in range(4):
                square = field_y*4 + field_x
                if square in self.block.figure():
                    if block_y + field_y >= self.height:
                        return True
                    if block_x + field_x >= self.width:
                        return True
                    if block_x + field_x < 0:
                        return True
                    if self.field[block_y + field_y][block_x + field_x] != 0:
                        return True
        return False

    def _freeze(self):
        '''Updates the game field according to frozen block coordinates.

        Remove full rows & create a new block.

        If collision happens with the new block, game state is changed to "end".
        '''

        block_y = self.block.pos_y
        block_x = self.block.pos_x

        for field_y in range(4):
            for field_x in range(4):
                square = field_y*4 + field_x
                if square in self.block.figure():
                    self.field[block_y + field_y][block_x +
                                                  field_x] = self.block.color
        self._remove_rows()
        self.new_block()
        if self._collision():
            self.state = "end"

    def _remove_rows(self):
        '''Remove full rows if they exist. Update points accordingly.'''

        rows = 0
        for field_y in range(1, self.height):
            if self.field[field_y].count(0) == 0:
                rows += 1
                for i in range(field_y, 1, -1):
                    for field_x in range(self.width):
                        self.field[i][field_x] = self.field[i-1][field_x]
        self.points += rows**2 * self.width
        self._update_level()

    def _update_level(self):
        '''Updates game level according to amount of points.

        New level every 200 points until maximum level 5 is reached
        '''

        if self.points == 0:
            self.level = 1
        elif self.points < 800:
            self.level = ceil(self.points / 199)
        else:
            self.level = 5
