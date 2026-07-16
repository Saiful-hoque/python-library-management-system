class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
class Member(Person):
    def __init__(self, name: str, age: int, member_id: str):
        super().__init__(name, age)
        self.member_id = member_id
        self.borrowed_books = []  
    def display_info(self):
        print(f"Member ID : {self.member_id}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Borrowed Books : {len(self.borrowed_books)}")
class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True  
    @property
    def available(self):
        return self.__available
    @available.setter
    def available(self, status: bool):
        if isinstance(status, bool):
            self.__available = status
    def display_book(self):
        status = "Available" if self.__available else "Borrowed"
        print(f"ISBN : {self.isbn}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Status : {status}")