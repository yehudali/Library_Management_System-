from book_class import Book
from user import User

class Library:
    def __init__(self, books:list[Book], users:list[User]):
        self.books = books
        self.users = users

    def add_book(self,title:str, author:str,ISBN:int, is_available:bool):
        book=Book(title,author,ISBN,is_available)
        self.books.append(book)

