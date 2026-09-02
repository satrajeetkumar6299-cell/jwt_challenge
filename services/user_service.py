from models.user import User


class UserService:
    def __init__(self):
        self.user = User()

    def create_user(self, username, email, password):
        # This assignment version uses only one hardcoded user.
        if email == self.user.email:
            return None
        return None

    def get_by_email(self, email):
        if email == self.user.email:
            return self.user
        return None

    def get_by_id(self, user_id):
        if user_id == self.user.id:
            return self.user
        return None
