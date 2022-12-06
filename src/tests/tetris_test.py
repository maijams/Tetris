import unittest
from tetris import Tetris


class TestTetris(unittest.TestCase):
    def setUp(self):
        self.tetris = Tetris(20, 10)

    def test_created_game_exists(self):
        self.assertNotEqual(self.tetris, None)

    def test_tetris_initialization_size_is_correct(self):
        self.assertEqual(self.tetris.height, 20)
        self.assertEqual(self.tetris.width, 10)

    def test_tetris_initialization_state_is_play(self):
        self.assertEqual(self.tetris.state, "play")

    def test_tetris_initialization_score_is_zero(self):
        self.assertEqual(self.tetris.points, 0)

    def test_tetris_initialization_block_is_none(self):
        self.assertEqual(self.tetris.block, None)

    def test_method_new_block_creates_block(self):
        self.tetris.new_block()
        self.assertNotEqual(self.tetris.block, None)

    def test_method_move_down_changes_block_location(self):
        self.tetris.new_block()
        y = self.tetris.block.pos_y
        self.tetris.move_down()
        self.assertEqual(self.tetris.block.pos_y, y+1)

    def test_method_move_sideways_works_when_moving_left(self):
        self.tetris.new_block()
        x = self.tetris.block.pos_x
        self.tetris.move_sideways(-1)
        self.assertEqual(self.tetris.block.pos_x, x-1)

    def test_method_move_sideways_works_when_moving_right(self):
        self.tetris.new_block()
        x = self.tetris.block.pos_x
        self.tetris.move_sideways(1)
        self.assertEqual(self.tetris.block.pos_x, x+1)

    def test_method_rotate_works(self):
        self.tetris.new_block()
        self.tetris.rotate()
        self.assertEqual(self.tetris.block.rotation, 1)

    def test_method_get_points_works(self):
        self.assertEqual(self.tetris.get_points(), 0)

    def test_method_get_state_works(self):
        self.assertEqual(self.tetris.get_state(), "play")

    def test_method_remove_rows_does_not_change_points_if_no_rows_removed(self):
        self.tetris.remove_rows()
        self.assertEqual(self.tetris.get_points(), 0)

    def test_method_freeze_game_ends_if_new_block_freezes(self):
        self.tetris.new_block()
        self.tetris.freeze()
        self.assertEqual(self.tetris.get_state(), "end")
