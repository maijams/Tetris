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


    def new_block(self):
        '''Creates a new falling block at the top of the game grid.'''
        
        self.block = Block(3, 0)


    def move_down(self):
        '''Moves the falling block one step downwards. 
        
        If block collides with other objects, the step is reversed and the block freezes.
        
        Returns:
            False if collision happens, otherwise True.
        '''
        
        self.block.pos_y += 1
        if self.collision():
            self.block.pos_y -= 1
            self.freeze()
            return False
        return True


    def move_sideways(self, direction):
        '''Moves the falling block in the given horizontal direction.
        
        If block collides with other objects, the step is reversed.
        
        Args:
            direction: Direction that block should be moved to. -1 = left, 1 = right.
        '''
        
        current_x = self.block.pos_x
        self.block.pos_x += direction
        if self.collision():
            self.block.pos_x = current_x


    def rotate(self):
        '''Rotates the falling block.
        
        If block collides with other objects, the step is reversed.
        '''
        
        self.block.rotate()
        if self.collision():
            self.block.reverse_rotate()


    def collision(self):
        '''Checks whether the falling block collides with walls, floor or other blocks.
        
        Returns:
            True, if collision happens. False, if no collision.
        '''
        
        collide = False
        for field_y in range(4):
            for field_x in range(4):
                square = field_y*4 + field_x
                if square in self.block.figure():
                    if self.block.pos_y + field_y >= self.height:
                        collide = True
                    elif self.block.pos_x + field_x >= self.width:
                        collide = True
                    elif self.block.pos_x + field_x < 0:
                        collide = True
                    elif self.field[self.block.pos_y+field_y][self.block.pos_x+field_x] != 0:
                        collide = True
        return collide


    def freeze(self):
        '''Updates the game field according to frozen block coordinates.
        
        Remove full rows & create a new block.
        
        If collision happens with the new block, game state is changed to "end".
        '''
        
        for field_y in range(4):
            for field_x in range(4):
                square = field_y*4 + field_x
                if square in self.block.figure():
                    self.field[self.block.pos_y+field_y][self.block.pos_x +
                                                         field_x] = self.block.color
        self.remove_rows()
        self.new_block()
        if self.collision():
            self.state = "end"


    def remove_rows(self):
        '''Remove full rows if they exist. Update points accordingly.'''
        
        rows = 0
        for field_y in range(1, self.height):
            if self.field[field_y].count(0) == 0:
                rows += 1
                for i in range(field_y, 1, -1):
                    for field_x in range(self.width):
                        self.field[i][field_x] = self.field[i-1][field_x]
        self.points += rows**2 * self.width


    def get_points(self):
        '''Returns:
            The amount of current points.
        '''
        
        return self.points


    def get_state(self):
        '''Returns:
            The current state of the game.
        '''
        return self.state
