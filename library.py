from book_class import Book
from user import User

class Library:
    def __init__(self, books:list[Book], users:list[User]):
        self.books = books
        self.users = users

    def add_book(self,title:str, author:str,ISBN:int, is_available:bool):
        book=Book(title,author,ISBN,is_available)
        self.books.append(book)

    def add_user(self,name:str,id:int, borrowed_books:list[int]):
        user = User(name,id,borrowed_books)
        self.users.append(user)

    def list_available_books(self):
        listi=[]
        for book in self.books:
            if book.is_available == True:
                listi.append(book.title)
        return listi


