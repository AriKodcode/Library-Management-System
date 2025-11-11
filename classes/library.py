class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self, book):
        self.list_of_books.append(book)
        print("Book added successfully")

    def add_user(self, user):
        self.list_of_users.append(user)
        print("user added successfully")

    def borrow_book(self, user_id, book_isbn):
        for book in self.list_of_books:
            if book.isbn == book_isbn:
                if book.is_available:
                    for user in self.list_of_users:
                        if user.user_id == user_id:
                            user.borrowed_books.append(book)
                            book.is_available = False
                            print("The book was successfully borrowed.")
                else:
                    print("book is not available")

    def return_book(self, user_id, book_isbn):
        for book in self.list_of_books:
            if book.isbn == book_isbn:
                for user in self.list_of_users:
                    if user.user_id == user_id:
                        user.borrowed_books.remove(book)
                        book.is_available = True

    def list_available_books(self):
        for book in self.list_of_books:
            if book.is_available:
                print(book)


    def search_book(self, title):
        for book in self.list_of_books:
            if book.title == title:
                return book
        return "the book is not in library"