from block import Block


class Tetris:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.state = "play"
        self.score = 0
        self.block = None
        self.field = [[0]*width for _ in range(height)]

    def new_block(self):
        self.block = Block(4, -1)

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
        for Y in range(4):
            for X in range(1, 5):
                square = Y*4 + X
                if square in self.block.figure():
                    if self.block.y + Y > self.height - 1:
                        collide = True
                    elif self.block.x + X > self.width:
                        collide = True
                    elif self.block.x + X < 1:
                        collide = True
                    elif self.field[self.block.y+Y][self.block.x+X-1] != 0:
                        collide = True
        return collide

    def freeze(self):
        for Y in range(4):
            for X in range(1, 5):
                square = Y*4 + X
                if square in self.block.figure():
                    self.field[self.block.y+Y][self.block.x +
                                               X-1] = self.block.color
        self.remove_lines()
        self.new_block()
        if self.collision():
            self.state = "end"

    def remove_lines(self):
        for Y in range(1, self.height):
            if self.field[Y].count(0) == 0:
                for i in range(Y, 1, -1):
                    for X in range(self.width):
                        self.field[i][X] = self.field[i-1][X]
