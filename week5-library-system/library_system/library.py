import json
import os
from .book import Book
from .member import Member

class Library:
    """Main controller class managing books and members."""

    def __init__(self, books_file='data/books.json', members_file='data/members.json'):
        self.books_file = books_file
        self.members_file = members_file
        self.books = {}    # {isbn: Book}
        self.members = {}  # {member_id: Member}
        self.load_data()

    def add_book(self, book):
        if book.isbn in self.books:
            return False, "Book with this ISBN already exists."
        self.books[book.isbn] = book
        return True, "Book added successfully."

    def register_member(self, member):
        if member.member_id in self.members:
            return False, "Member ID already exists."
        self.members[member.member_id] = member
        return True, "Member registered successfully."

    def borrow_book(self, isbn, member_id):
        if isbn not in self.books:
            return False, "Book not found."
        if member_id not in self.members:
            return False, "Member not found."

        book = self.books[isbn]
        member = self.members[member_id]

        if not member.can_borrow():
            return False, f"Member reached borrow limit of {member.max_limit} books."

        success, msg = book.check_out(member_id)
        if success:
            member.borrow_book(isbn)
        return success, msg

    def return_book(self, isbn, member_id):
        if isbn not in self.books:
            return False, "Book not found."
        if member_id not in self.members:
            return False, "Member not found."

        book = self.books[isbn]
        member = self.members[member_id]

        success, msg = book.return_book()
        if success:
            member.return_book(isbn)
        return success, msg

    def search_books(self, query, search_type="title"):
        results = []
        query = query.lower()
        for book in self.books.values():
            if search_type == "title" and query in book.title.lower():
                results.append(book)
            elif search_type == "author" and query in book.author.lower():
                results.append(book)
            elif search_type == "isbn" and query in book.isbn.lower():
                results.append(book)
            elif search_type == "available" and book.available:
                results.append(book)
        return results

    def save_data(self):
        os.makedirs(os.path.dirname(self.books_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.members_file), exist_ok=True)

        with open(self.books_file, 'w') as f:
            json.dump([b.to_dict() for b in self.books.values()], f, indent=4)

        with open(self.members_file, 'w') as f:
            json.dump([m.to_dict() for m in self.members.values()], f, indent=4)

    def load_data(self):
        if os.path.exists(self.books_file):
            try:
                with open(self.books_file, 'r') as f:
                    books_data = json.load(f)
                    self.books = {b['isbn']: Book.from_dict(b) for b in books_data}
            except Exception:
                self.books = {}

        if os.path.exists(self.members_file):
            try:
                with open(self.members_file, 'r') as f:
                    members_data = json.load(f)
                    self.members = {m['member_id']: Member.from_dict(m) for m in members_data}
            except Exception:
                self.members = {}