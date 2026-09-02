from flask_jwt_extended import create_access_token
from services.user_service import UserService


class AuthService:
    def __init__(self):
        self.user_service = UserService()

    def login(self, email, password):
        user = self.user_service.get_by_email(email)

        if not user or password != user.password:
            return None

        return create_access_token(identity=str(user.id))
