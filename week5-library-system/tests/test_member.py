import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from library_system.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member("Alice", "MEM001", max_limit=2)

    def test_member_initialization(self):
        self.assertEqual(self.member.name, "Alice")
        self.assertEqual(self.member.member_id, "MEM001")
        self.assertEqual(len(self.member.borrowed_books), 0)

    def test_borrow_book(self):
        success, _ = self.member.borrow_book("12345")
        self.assertTrue(success)
        self.assertIn("12345", self.member.borrowed_books)

    def test_borrow_limit(self):
        self.member.borrow_book("12345")
        self.member.borrow_book("67890")
        success, msg = self.member.borrow_book("11111")
        self.assertFalse(success)
        self.assertIn("Maximum borrow limit", msg)

    def test_return_book(self):
        self.member.borrow_book("12345")
        success, _ = self.member.return_book("12345")
        self.assertTrue(success)
        self.assertNotIn("12345", self.member.borrowed_books)

if __name__ == "__main__":
    unittest.main()