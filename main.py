from library import Library
from user import User
from book_class import Book

x = Library([
         Book( "1984", "George Orwell",9780451524935,True),
         Book("Brave New World", "Aldous Huxley",9780060850524,True)
        ],
        [
        User("moshe",00,[]),
        User("dov",11,[])

        ])

if __name__ =="__main__":
    while True:
        print("1. Add Book\n2. Add User\n3. Borrow Book\n...7. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # ask for book info and add book
            Library.add_book(x,str(input("enter the book name")),str(input("enter the author name")),int(input("enter the ISBN book")))
        elif choice == "2":
            # ask for user info and add user
            Library.add_user(x,str(input("enter the user name")),int(input("enter the user id ")))
        elif choice == "3":
            #
            Library.borrow_book(x,int(input("enter the user id ")),int(input("enter the ISBN book")))
        elif choice == "4":
            #
            Library.return_book(x,int(input("enter the user id ")),int(input("enter the ISBN book")))
        elif choice == "5":
            #
            Library.list_available_books(x)
        elif choice == "6":
            #
            Library.search_book_by_title(x,str(input("enter the book name")))
        elif choice == "7":
            #
            Library.search_book_by_author(x,str(input("enter the author name")))
        elif choice == "8":
            # save data and exit
            break
        else:
            print("Invalid choice, try again.")



