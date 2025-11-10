class Book:
    def __init__(self,title:str, author:str,ISBN:int, is_available:bool):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available = is_available

    def __str__(self):
        return (f"title: {self.title}\n author: {self.author}"
                f" ISBN: {self.ISBN}\n is_available:{self.is_available}")
