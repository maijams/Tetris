from block import Block


class Tetris:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.state = "play"
        self.block = None
        self.field = [[0]*width for _ in range(height)]
        self.points = 0

    def new_block(self):
        self.block = Block(4, 0)

    def move_down(self):
        self.block.y += 1
        if self.collision():
            self.block.y -= 1
            self.freeze()

    def move_sideways(self, direction):
        current_x = self.block.x
        self.block.x += direction
        if self.collision():
            self.block.x = current_x

    def rotate(self):
        self.block.rotate()

    def collision(self):
        collide = False
        for field_y in range(4):
            for field_x in range(1, 5):
                square = field_y*4 + field_x
                if square in self.block.figure():
                    if self.block.y + field_y > self.height - 1:
                        collide = True
                    elif self.block.x + field_x > self.width:
                        collide = True
                    elif self.block.x + field_x < 1:
                        collide = True
                    elif self.field[self.block.y+field_y][self.block.x+field_x-1] != 0:
                        collide = True
        return collide

    def freeze(self):
        for field_y in range(4):
            for field_x in range(1, 5):
                square = field_y*4 + field_x
                if square in self.block.figure():
                    self.field[self.block.y+field_y][self.block.x +
                    field_x-1] = self.block.color
        self.remove_rows()
        self.new_block()
        if self.collision():
            self.state = "end"

    def remove_rows(self):
        rows = 0
        for field_y in range(1, self.height):
            if self.field[field_y].count(0) == 0:
                rows += 1
                for i in range(field_y, 1, -1):
                    for field_x in range(self.width):
                        self.field[i][field_x] = self.field[i-1][field_x]
        self.points += rows**2 * self.width
        
    def get_points(self):
        return self.points
    
    def get_state(self):
        return self.state
    
