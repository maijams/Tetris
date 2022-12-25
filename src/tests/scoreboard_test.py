import unittest
from repositories.scoreboard import ScoreBoard
import initialize_database as db


class TestScoreboard(unittest.TestCase):
    def setUp(self):
        self.scoreboard = ScoreBoard("test.db")
        db.initialize_database("test.db")

    def test_scoreboard_method_save_score_one_result(self):
        self.scoreboard.save_score(50)
        result = self.scoreboard.get_scoreboard()

        self.assertEqual(len(result), 1)

    def test_scoreboard_method_save_score_two_results(self):
        self.scoreboard.save_score(50)
        self.scoreboard.save_score(70)
        result = self.scoreboard.get_scoreboard()

        self.assertEqual(len(result), 2)

    def test_scoreboard_method_get_scoreboard_returns_results_in_correct_order(self):
        self.scoreboard.save_score(100)
        self.scoreboard.save_score(500)
        result = self.scoreboard.get_scoreboard()

        self.assertEqual(result[0][0], 500)
        self.assertEqual(result[1][0], 100)
