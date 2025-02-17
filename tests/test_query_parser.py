import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from query_parser import QueryParser

class TestQueryParser(unittest.TestCase):
    def setUp(self):
        self.parser = QueryParser()

    def test_create_table(self):
        result = self.parser.parse("CREATE TABLE users (id INT, name TEXT)")
        self.assertEqual(result["action"], "create_table")
        self.assertEqual(result["table"], "users")
    
    def test_insert(self):
        result = self.parser.parse("INSERT INTO users VALUES (1, 'Alice')")
        self.assertEqual(result["action"], "insert")
        self.assertEqual(result["table"], "users")

    def test_select(self):
        result = self.parser.parse("SELECT * FROM users")
        self.assertEqual(result["action"], "select")
        self.assertEqual(result["table"], "users")

if __name__ == '__main__':
    unittest.main()
