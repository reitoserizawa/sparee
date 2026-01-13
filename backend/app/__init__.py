from flask import Flask
from dotenv import load_dotenv
import os
from app.config import DataBaseConfig
from app.database import db
from app.routes import register_blueprints

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "dev-key")
    app.config['DEBUG'] = os.getenv("DEBUG", "false").lower() == "true"

    app.config.from_object(DataBaseConfig)
    db.init_app(app)
    register_blueprints(app)

    with app.app_context():
        from . import models

    return app
