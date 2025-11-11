import json


class JsonFile:

    @staticmethod
    def convert_to_dict(users, books):
        list_of_users = []
        list_of_books = []

        for user in users:
            list_of_users.append(user.info_user_to_dict())

        for book in books:
            list_of_books.append(book.get_book_info_dict())

        return list_of_books, list_of_users

    @staticmethod
    def write(user, books):
        books_list, users_list = JsonFile.convert_to_dict(user, books)
        data = {"books": books_list,
                "users": users_list
                }

        with open("data.json", "w") as f:
            f.write(json.dumps(data))

    @staticmethod
    def read():
        with open("data.json", "r") as f:
            return json.loads(f.read())
