import unittest
from clock import Clock


class TestClock(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()

    def test_created_clock_exists(self):
        self.assertNotEqual(self.clock, None)
