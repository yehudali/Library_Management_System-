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
                        self.books[j].is_available = False
                        self.users[i].borrowed_books.append(book_isbn)


x = Library([User("moshe",0,[]),User("moty",1,[])],[Book("jjj","arik",123,True),Book("sss","dov",124,True)])
x.borrow_book(2,124)
print(x.users[1].borrowed_books)

