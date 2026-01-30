import os
from dotenv import load_dotenv
import uvicorn
from app import create_app

load_dotenv()

# Create your Flask app
app = create_app()

if __name__ == "__main__":
    # Run with an async-friendly ASGI server
    uvicorn.run(
        "run:app",                  # module:app
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        reload=os.getenv("DEBUG", "false").lower() == "true",
        log_level="info"
    )
