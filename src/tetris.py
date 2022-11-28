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

    def move_sideways(self, direction):
        self.block.x += direction

    def rotate(self):
        self.block.rotate()
