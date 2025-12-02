from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "dev-key")
    app.config['DEBUG'] = os.getenv("DEBUG", "false").lower() == "true"

    from .routes import main
    app.register_blueprint(main)

    return app
