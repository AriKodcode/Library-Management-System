class Book:

    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        available = "available" if self.is_available else "Not available"
        return f"{self.title} by {self.author}, isbn: {self.isbn}, -> is {available}"

    def get_book_info_dict(self):
        return {"title": self.title,
                "author": self.author,
                "isbn": self.isbn,
                "is available": self.is_available
                }
