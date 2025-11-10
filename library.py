from user import User
from book_class import Book


class Library:
     def __init__(self,users:list[User],books:list[Book]):
         self.users = users
         self.books = books


     def borrow_book(self,user_id, book_isbn):
        for i in range(len(self.users)):
            if self.users[i].id == user_id:
                for j in range(len(self.books)):
                    if self.books[j].ISBN == book_isbn:
                        if self.books[j].is_available == True:
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
