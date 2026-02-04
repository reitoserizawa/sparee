from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.routes.dependencies import RequestLifecycleMiddleware
from app.api.routes import router

load_dotenv()


def create_app() -> FastAPI:
    app = FastAPI(title="Your App")
    app.add_middleware(RequestLifecycleMiddleware)
    app.include_router(router)
    return app


app = create_app()
