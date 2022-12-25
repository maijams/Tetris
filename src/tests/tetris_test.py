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

    def test_tetris_method_new_block_creates_block(self):
        self.tetris.new_block()

        self.assertNotEqual(self.tetris.block, None)

    def test_tetris_method_move_down_changes_block_location(self):
        self.tetris.new_block()
        block_y = self.tetris.block.pos_y
        self.tetris.move_down()

        self.assertEqual(self.tetris.block.pos_y, block_y+1)

    def test_tetris_method_move_sideways_works_when_moving_left(self):
        self.tetris.new_block()
        block_x = self.tetris.block.pos_x
        self.tetris.move_sideways(-1)

        self.assertEqual(self.tetris.block.pos_x, block_x-1)

    def test_tetris_method_move_sideways_works_when_moving_right(self):
        self.tetris.new_block()
        block_x = self.tetris.block.pos_x
        self.tetris.move_sideways(1)

        self.assertEqual(self.tetris.block.pos_x, block_x+1)

    def test_tetris_method_rotate_works(self):
        self.tetris.new_block()
        result = self.tetris.rotate()

        if self.tetris.block._shape == 0:
            self.assertEqual(self.tetris.block._rotation, 0)
        else:
            self.assertEqual(self.tetris.block._rotation, 1)

        self.assertTrue(result)

    def test_tetris_method_remove_rows_does_not_change_points_if_no_rows_removed(self):
        self.tetris._remove_rows()

        self.assertEqual(self.tetris.points, 0)

    def test_tetris_method_freeze_game_ends_if_new_block_freezes(self):
        self.tetris.new_block()
        self.tetris._freeze()

        self.assertEqual(self.tetris.state, "end")

    def test_tetris_method_update_level_works_level_1(self):
        self.tetris.points = 0
        self.tetris._update_level()
        self.assertEqual(self.tetris.level, 1)

        self.tetris.points = 199
        self.tetris._update_level()
        self.assertEqual(self.tetris.level, 1)

    def test_tetris_method_update_level_works_level_2(self):
        self.tetris.points = 200
        self.tetris._update_level()
        self.assertEqual(self.tetris.level, 2)

        self.tetris.points = 399
        self.tetris._update_level()
        self.assertEqual(self.tetris.level, 2)

    def test_tetris_method_update_level_works_level_3(self):
        self.tetris.points = 400
        self.tetris._update_level()
        self.assertEqual(self.tetris.level, 3)

        self.tetris.points = 599
        self.tetris._update_level()
        self.assertEqual(self.tetris.level, 3)

    def test_tetris_method_update_level_works_level_4(self):
        self.tetris.points = 600
        self.tetris._update_level()
        self.assertEqual(self.tetris.level, 4)

        self.tetris.points = 799
        self.tetris._update_level()
        self.assertEqual(self.tetris.level, 4)

    def test_tetris_method_update_level_works_level_5(self):
        self.tetris.points = 800
        self.tetris._update_level()
        self.assertEqual(self.tetris.level, 5)

        self.tetris.points = 1100
        self.tetris._update_level()
        self.assertEqual(self.tetris.level, 5)

    def test_tetris_method_collision_returns_false_when_no_collision(self):
        self.tetris.new_block()
        self.tetris.block._shape = 0
        self.tetris.field[2][5] = (255, 255, 255)
        result = self.tetris._collision()

        self.assertFalse(result)

    def test_tetris_method_collision_with_other_block(self):
        self.tetris.new_block()
        self.tetris.block._shape = 0
        self.tetris.field[1][5] = (255, 255, 255)
        result = self.tetris._collision()

        self.assertTrue(result)

    def test_tetris_method_collision_with_right_wall(self):
        self.tetris.new_block()
        self.tetris.block.set_horizontal_position(9)
        result = self.tetris._collision()

        self.assertTrue(result)

    def test_tetris_method_collision_with_left_wall(self):
        self.tetris.new_block()
        self.tetris.block.set_horizontal_position(-2)
        result = self.tetris._collision()

        self.assertTrue(result)

    def test_tetris_method_collision_with_floor(self):
        self.tetris.new_block()
        self.tetris.block.pos_y = 19
        result = self.tetris._collision()

        self.assertTrue(result)

    def test_tetris_method_move_down_returns_false_when_collision(self):
        self.tetris.new_block()
        self.tetris.block._shape = 0
        self.tetris.field[2][5] = (255, 255, 255)
        result = self.tetris.move_down()

        self.assertFalse(result)

    def test_tetris_method_move_sideways_returns_false_when_collision(self):
        self.tetris.new_block()
        self.tetris.block._shape = 0
        self.tetris.block.set_horizontal_position(7)
        result = self.tetris.move_sideways(1)

        self.assertFalse(result)

    def test_tetris_method_rotate_returns_false_when_collision(self):
        self.tetris.new_block()
        self.tetris.block._shape = 1
        self.tetris.block.set_horizontal_position(7)
        result = self.tetris.rotate()

        self.assertFalse(result)

    def test_tetris_method_remove_rows_with_one_row(self):
        WHITE = (255, 255, 255)
        self.tetris.field[8] = [WHITE]*10
        self.tetris._remove_rows()

        self.assertEqual(self.tetris.points, 10)

    def test_tetris_method_remove_rows_with_two_rows(self):
        WHITE = (255, 255, 255)
        self.tetris.field[8] = [WHITE]*10
        self.tetris.field[9] = [WHITE]*10
        self.tetris._remove_rows()

        self.assertEqual(self.tetris.points, 40)

    def test_tetris_method_freeze_works_when_game_ends(self):
        self.tetris.new_block()
        self.tetris._freeze()
        
        self.assertEqual(self.tetris.state, "end")