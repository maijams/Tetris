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
    # Possible positions in 4x4 grid
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
        self.pos_x = location_x
        self.pos_y = location_y
        self.shape = random.randint(0, len(self.blocks)-1)
        self.rotation = 0
        self.color = self.colors[random.randint(0, len(self.colors)-1)]

    def rotate(self):
        if self.rotation == len(self.blocks[self.shape])-1:
            self.rotation = 0
        else:
            self.rotation += 1

    def reverse_rotate(self):
        if self.rotation == 0:
            self.rotation = len(self.blocks[self.shape])-1
        else:
            self.rotation -= 1

    def figure(self):
        return self.blocks[self.shape][self.rotation]
