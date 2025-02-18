import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.storage import Storage


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Storage("test.db")

    def test_write_and_read(self):
        self.storage.write_record("1,Alice")
        self.storage.write_record("2,Bob")
        records = self.storage.read_records()
        self.assertEqual(records, ["1,Alice", "2,Bob"])

if __name__ == '__main__':
    unittest.main()
