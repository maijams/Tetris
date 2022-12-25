import unittest
from entities.block import Block


class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block(4, 0)

    def test_created_block_exists(self):
        self.assertNotEqual(self.block, None)

    def test_block_initialization_location_is_correct(self):
        self.assertEqual(self.block.pos_x, 4)
        self.assertEqual(self.block.pos_y, 0)

    def test_block_initialization_rotation_is_correct(self):
        self.assertEqual(self.block._rotation, 0)

    def test_block_method_rotate_works_with_small_i(self):
        self.block._shape = 1
        self.block.rotate()

        self.assertEqual(self.block._rotation, 1)

    def test_block_method_rotate_works_with_large_i_and_returns_to_zero(self):
        self.block._shape = 1
        self.block.rotate()
        self.block.rotate()

        self.assertEqual(self.block._rotation, 0)

    def test_block_method_reverse_rotate_works_with_small_i(self):
        self.block._shape = 1
        self.block.reverse_rotate()

        self.assertEqual(self.block._rotation, 1)

    def test_block_method_reverse_rotate_works_with_large_i(self):
        self.block._shape = 1
        self.block.reverse_rotate()
        self.block.reverse_rotate()

        self.assertEqual(self.block._rotation, 0)

    def test_block_method_figure_returns_correct_figure(self):
        self.block._shape = 3

        self.assertEqual(self.block.figure(), [2, 5, 6, 9])

    def test_block_method_move_down_works(self):
        self.block.move_down()

        self.assertEqual(self.block.pos_y, 1)

    def test_block_method_move_up_works(self):
        self.block.move_up()

        self.assertEqual(self.block.pos_y, -1)

    def test_block_method_move_sideways_works_left(self):
        self.block.move_sideways(-1)

        self.assertEqual(self.block.pos_x, 3)

    def test_block_method_move_sideways_works_right(self):
        self.block.move_sideways(1)

        self.assertEqual(self.block.pos_x, 5)

    def test_block_method_set_horizontal_position_works(self):
        self.block.set_horizontal_position(6)

        self.assertEqual(self.block.pos_x, 6)
