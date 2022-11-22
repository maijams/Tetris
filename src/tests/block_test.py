import unittest
from block import Block


class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block(4,0)
        
    # Initialization works    
    def test_created_block_exists(self):
        self.assertNotEqual(self.block, None)
        
    def test_block_location_is_correct(self):
        self.assertEqual(self.block.x, 4)
        self.assertEqual(self.block.y, 0)
    