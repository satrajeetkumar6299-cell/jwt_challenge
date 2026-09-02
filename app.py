from flask import Flask
from config import Config
from extensions import jwt
from routes.auth import auth_bp
from routes.tasks import tasks_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(tasks_bp, url_prefix="/tasks")

    return app


app = create_app()


@app.route("/")
def home():
    return {
        "message": "Flask JWT is running"
    }, 200


if __name__ == "__main__":
    app.run(debug=True)
