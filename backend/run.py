from flask_migrate import Migrate
from app.database import db
from app import create_app
import os
from dotenv import load_dotenv

load_dotenv()

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(
        debug=os.getenv("DEBUG", "false").lower() == "true",
        host=os.getenv("FLASK_HOST", "0.0.0.0"),
        port=int(os.getenv("FLASK_PORT", "5000"))
    )
