from book_class import Book
from user import User

class Library:
    def __init__(self, books:list[Book], users:list[User]):
        self.books = books
        self.users = users

    def add_book(self,title:str, author:str,ISBN:int):
        book=Book(title,author,ISBN, True)
        self.books.append(book)

    def add_user(self,name:str,id:int):
        user = User(name,id,[])
        self.users.append(user)

    def list_available_books(self):
        listi=[]
        for book in self.books:
            if book.is_available == True:
                listi.append(book.title)
        return listi


