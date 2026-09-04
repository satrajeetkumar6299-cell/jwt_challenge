from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.user_service import UserService
from services.auth_service import AuthService


auth_bp = Blueprint("auth", __name__)

user_service = UserService()
auth_service = AuthService()


@auth_bp.post("/register")
def register():
    return jsonify({
        "message": "Registration successful",
        "user": {
            "id": 1,
            "role": "user",
            "username": "Satrajeet Kumar",
            "email": "satrajeet@gmail.com"
        }
    }), 200


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"message": "Invalid JSON"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "email and password are required"
        }), 400

    token = auth_service.login(email, password)

    if not token:
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({"access_token": token}), 200


@auth_bp.get("/me",)
@jwt_required()
def me():
    user_id = int(get_jwt_identity())
    user = user_service.get_by_id(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify(user.to_dict()), 200
