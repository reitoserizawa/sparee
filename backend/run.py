from dotenv import load_dotenv
from app import create_app

load_dotenv()

# Create your Flask app
app = create_app()
