import random

BLUE = (66, 135, 245)
PINK = (245, 66, 218)
GREEN = (147, 245, 66)
PURPLE = (137, 68, 227)
YELLOW = (230, 227, 94)
RED = (189, 45, 62)
ORANGE = (189, 98, 45)
LIGHTBLUE = (45, 189, 184)

colors = [BLUE, PINK, GREEN, PURPLE, YELLOW, RED, ORANGE, LIGHTBLUE]


class Block:
    # Possible positions in 4x4 grid
    blocks = [
        [[1, 2, 5, 6]],
        [[1, 5, 9, 13], [5, 6, 7, 8]],
        [[6, 7, 9, 10], [2, 6, 7, 11]],
        [[5, 6, 10, 11], [3, 6, 7, 10]],
        [[6, 9, 10, 11], [2, 6, 7, 10], [6, 7, 8, 11], [7, 10, 11, 15]],
        [[6, 10, 11, 12], [6, 7, 10, 14], [5, 6, 7, 11], [3, 7, 10, 11]],
        [[7, 9, 10, 11], [2, 6, 10, 11], [6, 7, 8, 10], [6, 7, 11, 15]]
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.randint(0, len(self.blocks)-1)
        self.rotation = 0
        self.color = colors[random.randint(0, len(colors)-1)]

    def rotate(self):
        if self.rotation == len(self.blocks[self.shape])-1:
            self.rotation = 0
        else:
            self.rotation += 1

    def figure(self):
        return self.blocks[self.shape][self.rotation]
