class User:
    def __init__(self):
        self.id = 1
        self.username = "sorav"
        self.email = "sorav@gmail.com"
        self.password = "1234567890"
        self.role = "user"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role
        }
