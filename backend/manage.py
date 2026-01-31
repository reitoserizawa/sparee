from flask_migrate import Migrate
from app.database import db
from app import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app()
migrate = Migrate(app, db, compare_type=True)
