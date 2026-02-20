import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.api.routes.dependencies import RequestLifecycleMiddleware
from app.errors.handlers import register_error_handlers
from app.api.routes import router

load_dotenv()

DEBUG = os.getenv("DEBUG", "true").lower() == "true"
ORIGINS = [
    "http://localhost:5173"
]


def create_app() -> FastAPI:
    app = FastAPI(title="Sparee")
    if DEBUG:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=ORIGINS,  # allow specific origins
            allow_credentials=True,
            allow_methods=["*"],     # allow GET, POST, OPTIONS, etc.
            allow_headers=["*"],     # allow all headers
        )
    app.add_middleware(RequestLifecycleMiddleware)
    app.include_router(router, prefix="/api")
    register_error_handlers(app)

    return app


app = create_app()
