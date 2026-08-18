import os
import sys

# Ensure correct import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from library_system.book import Book
from library_system.member import Member
from library_system.library import Library

def main():
    # Resolve relative paths for JSON persistence
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    books_path = os.path.join(base_dir, 'data', 'books.json')
    members_path = os.path.join(base_dir, 'data', 'members.json')

    library = Library(books_file=books_path, members_file=members_path)

    while True:
        print("\n================================")
        print("    LIBRARY MANAGEMENT SYSTEM")
        print("================================")
        print(f"Loaded {len(library.books)} books from file")
        print(f"Loaded {len(library.members)} members from file")
        print("\n1. Add New Book")
        print("2. Register New Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. View All Books")
        print("7. View All Members")
        print("8. View Overdue Books")
        print("9. Save & Exit")
        print("0. Exit Without Saving")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            isbn = input("Enter ISBN: ")
            year = input("Enter Year (optional): ")
            book = Book(title, author, isbn, year if year else None)
            ok, msg = library.add_book(book)
            print(f"Result: {msg}")

        elif choice == '2':
            name = input("Enter Member Name: ")
            member_id = input("Enter Member ID: ")
            member = Member(name, member_id)
            ok, msg = library.register_member(member)
            print(f"Result: {msg}")

        elif choice == '3':
            isbn = input("Enter Book ISBN: ")
            member_id = input("Enter Member ID: ")
            ok, msg = library.borrow_book(isbn, member_id)
            print(f"Result: {msg}")

        elif choice == '4':
            isbn = input("Enter Book ISBN: ")
            member_id = input("Enter Member ID: ")
            ok, msg = library.return_book(isbn, member_id)
            print(f"Result: {msg}")

        elif choice == '5':
            print("\nSearch books by:\n1. Title\n2. Author\n3. ISBN\n4. Show all available books")
            opt = input("Enter search option: ").strip()
            type_map = {'1': 'title', '2': 'author', '3': 'isbn', '4': 'available'}
            if opt in type_map:
                query = "" if opt == '4' else input("Enter search query: ").strip()
                results = library.search_books(query, search_type=type_map[opt])
                print(f"\nFound {len(results)} books:")
                for idx, b in enumerate(results, 1):
                    print(f"\n{idx}. {b.title}\n   Author: {b.author}\n   ISBN: {b.isbn}\n   Status: {'Available' if b.available else f'Borrowed by {b.borrowed_by}'}")
            else:
                print("Invalid option.")

        elif choice == '6':
            print("\nAll Books:")
            for b in library.books.values():
                print(f"- {b}")

        elif choice == '7':
            print("\nAll Members:")
            for m in library.members.values():
                print(f"- {m}")

        elif choice == '8':
            overdue = [b for b in library.books.values() if b.is_overdue()]
            print(f"\nFound {len(overdue)} overdue books:")
            for b in overdue:
                print(f"- {b.title} (Borrowed by: {b.borrowed_by}, Due: {b.due_date})")

        elif choice == '9':
            library.save_data()
            print("Data saved successfully. Exiting...")
            break

        elif choice == '0':
            print("Exiting without saving changes...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()