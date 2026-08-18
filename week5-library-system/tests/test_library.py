import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import os
import shutil
from library_system.book import Book
from library_system.member import Member
from library_system.library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.test_dir = "tests/temp_data"
        os.makedirs(self.test_dir, exist_ok=True)
        self.books_file = os.path.join(self.test_dir, "test_books.json")
        self.members_file = os.path.join(self.test_dir, "test_members.json")
        
        self.library = Library(books_file=self.books_file, members_file=self.members_file)
        self.book = Book("Fluent Python", "Luciano Ramalho", "9781491946008")
        self.member = Member("Bob", "MEM002")

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_add_book_and_register_member(self):
        ok_b, _ = self.library.add_book(self.book)
        ok_m, _ = self.library.register_member(self.member)
        self.assertTrue(ok_b)
        self.assertTrue(ok_m)
        self.assertIn("9781491946008", self.library.books)
        self.assertIn("MEM002", self.library.members)

    def test_borrow_and_return_flow(self):
        self.library.add_book(self.book)
        self.library.register_member(self.member)

        # Borrow
        success, _ = self.library.borrow_book("9781491946008", "MEM002")
        self.assertTrue(success)
        self.assertFalse(self.library.books["9781491946008"].available)

        # Return
        success, _ = self.library.return_book("9781491946008", "MEM002")
        self.assertTrue(success)
        self.assertTrue(self.library.books["9781491946008"].available)

    def test_search_books(self):
        self.library.add_book(self.book)
        results = self.library.search_books("Fluent", search_type="title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].isbn, "9781491946008")

if __name__ == "__main__":
    unittest.main()