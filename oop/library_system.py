class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"    

class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)   
        self.file_size = file_size
    def __str__(self):
        return f"{self.title} by {self.author}"     
class PrintBook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title,author)  
        self.page_count = page_count
    def __str__(self):
        return f"{self.title} by {self.author}"     
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
            if isinstance(book, EBook):
               print(f"{book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
               print(f"{book.title} by {book.author}, Page Count: {book.page_count}") 
            else:
               print(f"{book.title} by {book.author}")     
                                               