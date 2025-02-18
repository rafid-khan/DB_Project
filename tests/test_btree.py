import unittest
import sys
import os

# Ensure the root directory is in the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.btree import BTree 

class TestBTree(unittest.TestCase):
    def setUp(self):
        self.btree = BTree(t=2)

    def test_insert_and_search(self):
        self.btree.insert(10)
        self.btree.insert(20)
        self.assertTrue(self.btree.search(10))
        self.assertFalse(self.btree.search(30))

if __name__ == '__main__':
    unittest.main()
