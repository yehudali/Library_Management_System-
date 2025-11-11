from user import User
from book_class import Book


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


    def borrow_book(self,user_id, book_isbn):
        for i in range(len(self.users)):
            if self.users[i].id == user_id:
                for j in range(len(self.books)):
                    if self.books[j].ISBN == book_isbn:
                        if self.books[j].is_available :
                            self.books[j].is_available = False
                            self.users[i].borrowed_books.append(book_isbn)



    def return_book(self,user_id, book_isbn):
        for i in range(len(self.users)):
            if self.users[i].id == user_id:
                for j in range(len(self.books)):
                    if self.books[j].ISBN == book_isbn:
                        if book_isbn in self.users[i].borrowed_books:
                            self.books[j].is_available = True
                            self.users[i].borrowed_books.remove(book_isbn)

    def list_available_books(self):
        listi=[]
        for book in self.books:
            if book.is_available :
                listi.append(book.title)
        return listi

    def search_book(self,search_word:str):
        for book in self.books:
            if book.title == search_word or book.author == search_word:
                return book
        return "The book is not found"
