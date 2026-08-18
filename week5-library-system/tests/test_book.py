import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from library_system.book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("Python Basics", "John Doe", "1234567890", 2023)

    def test_book_initialization(self):
        self.assertEqual(self.book.title, "Python Basics")
        self.assertEqual(self.book.author, "John Doe")
        self.assertEqual(self.book.isbn, "1234567890")
        self.assertTrue(self.book.available)
        self.assertIsNone(self.book.borrowed_by)

    def test_check_out_success(self):
        success, msg = self.book.check_out("MEM001")
        self.assertTrue(success)
        self.assertFalse(self.book.available)
        self.assertEqual(self.book.borrowed_by, "MEM001")

    def test_check_out_already_borrowed(self):
        self.book.check_out("MEM001")
        success, msg = self.book.check_out("MEM002")
        self.assertFalse(success)
        self.assertEqual(msg, "Book is already checked out")

    def test_return_book(self):
        self.book.check_out("MEM001")
        success, msg = self.book.return_book()
        self.assertTrue(success)
        self.assertTrue(self.book.available)
        self.assertIsNone(self.book.borrowed_by)

    def test_to_and_from_dict(self):
        data = self.book.to_dict()
        new_book = Book.from_dict(data)
        self.assertEqual(new_book.title, self.book.title)
        self.assertEqual(new_book.isbn, self.book.isbn)

if __name__ == "__main__":
    unittest.main()