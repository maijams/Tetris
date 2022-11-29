import unittest
from block import Block


class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block(4, 0)

    def test_created_block_exists(self):
        self.assertNotEqual(self.block, None)

    def test_block_initialization_location_is_correct(self):
        self.assertEqual(self.block.x, 4)
        self.assertEqual(self.block.y, 0)

    def test_block_initialization_rotation_is_correct(self):
        self.assertEqual(self.block.rotation, 0)

    def test_block_rotation_works_with_small_i(self):
        self.block.shape = 1
        self.block.rotate()
        self.assertEqual(self.block.rotation, 1)

    def test_block_rotation_works_with_large_i_and_returns_to_zero(self):
        self.block.shape = 1
        self.block.rotate()
        self.block.rotate()
        self.assertEqual(self.block.rotation, 0)

    def test_method_figure_returns_correct_figure(self):
        self.block.shape = 3
        self.assertEqual(self.block.figure(), [5, 6, 10, 11])
