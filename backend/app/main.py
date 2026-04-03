import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import asyncio
from app.ws_manager import manager
from app.api.routes.dependencies import RequestLifecycleMiddleware
from app.errors.handlers import register_error_handlers
from app.api.routes import router

load_dotenv()

DEBUG = os.getenv("DEBUG", "true").lower() == "true"
ORIGINS = [
    "http://localhost:5173"
]


async def startup():
    asyncio.create_task(manager.start_redis_listener())


@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()
    yield
    await manager.shutdown_connections()


def create_app() -> FastAPI:
    app = FastAPI(title="Sparee", lifespan=lifespan)

    if DEBUG:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    app.add_middleware(RequestLifecycleMiddleware)
    app.include_router(router, prefix="/api")
    register_error_handlers(app)

    return app


app = create_app()
