from app.config import DataBaseConfig
from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()


app = create_app()

app.config.from_object(DataBaseConfig)

if __name__ == "__main__":
    app.run(
        debug=os.getenv("DEBUG", "false").lower() == "true",
        host=os.getenv("FLASK_HOST", "0.0.0.0"),
        port=int(os.getenv("FLASK_PORT", "5000"))
    )
