from models import Book, Member

class Library:
    def __init__(self):
        self.books = {}     # {isbn: Book_Object}
        self.members = {}  # {member_id: Member_Object}
    def add_book(self, title: str, author: str, isbn: str):
        if not title or not author or not isbn:
            raise ValueError("Error: Fields cannot be empty.")
        if isbn in self.books:
            raise ValueError("Error: ISBN already exists.")
        new_book = Book(title, author, isbn)
        self.books[isbn] = new_book
        print("Book added successfully!")
    def register_member(self, name: str, age: int, member_id: str):
        if not name or not member_id:
            raise ValueError("Error: Fields cannot be empty.")
        if age <= 0:
            raise ValueError("Error: Age must be greater than 0.")
        if member_id in self.members:
            raise ValueError("Error: Member ID already exists.")
        new_member = Member(name, age, member_id)
        self.members[member_id] = new_member
        print("Member registered successfully!")
    def borrow_book(self, member_id: str, isbn: str):
        if member_id not in self.members:
            print("Member not found.")
            return
        if isbn not in self.books:
            print("Book not found.")
            return
        member = self.members[member_id]
        book = self.books[isbn]
        if not book.available:
            print("Sorry! This book is currently unavailable.")
            return
        if book in member.borrowed_books:
            print("A member cannot borrow the same book twice.")
            return
        book.available = False
        member.borrowed_books.append(book)
        print("Book borrowed successfully.")

    def return_book(self, member_id: str, isbn: str):
        if member_id not in self.members:
            print("Member not found.")
            return
        if isbn not in self.books:
            print("Book not found.")
            return
        member = self.members[member_id]
        book = self.books[isbn]
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print("Book returned successfully.")
        else:
            print("This member did not borrow this book.")
    def show_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print(f"{'-' * 13} BOOK LIST {'-' * 13}")
        for book in self.books.values():
            book.display_book()
            print("-" * 37)
    def show_members(self):
        if not self.members:
            print("No registered members found.")
            return
        print(f"{'-' * 11} MEMBER LIST {'-' * 12}")
        for member in self.members.values():
            member.display_info()
            print("-" * 36)

    def search_book(self, title: str):
        if not title:
            print("Error: Search title cannot be empty.")
            return
        found = False
        for book in self.books.values():
            if book.title.lower() == title.lower():
                if not found:
                    print("Book Found!")
                    found = True
                book.display_book()
        if not found:
            print("Book not found.")