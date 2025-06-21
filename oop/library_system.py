class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)   

class PrintBook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title,author)  

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its sublclasses can be added.")
    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")                                