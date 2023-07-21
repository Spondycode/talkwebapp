import datetime


class User:
    def __init__(self, name, email, hashed_password):
        self.id = 1  # change when ids are created
        self.name = name
        self.email = email
        self.hash_password = hashed_password
        self.created_date = None
        self.profile_image = ""
        self.last_login: datetime.datetime = None
