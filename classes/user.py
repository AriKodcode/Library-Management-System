class User:

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def str(self):
        if not self.borrowed_books:
            return f"User: {self.name} (ID: {self.user_id}) -> No borrowed books"
        else:
            return f"User: {self.name} (ID: {self.user_id}) -> Borrowed"

    def info_user_to_dict(self):
        return {"name": self.name,
                "user_id": self.user_id,
                "borrowed_books": self.borrowed_books

                }
