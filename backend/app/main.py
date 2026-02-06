from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.routes.dependencies import RequestLifecycleMiddleware
from app.errors.handlers import register_error_handlers
from app.api.routes import router

load_dotenv()


def create_app() -> FastAPI:
    app = FastAPI(title="Your App")
    app.add_middleware(RequestLifecycleMiddleware)
    app.include_router(router, prefix="/api")
    register_error_handlers(app)

    @app.on_event("startup")
    async def on_startup():
        from app.db.models.base import Base
        from app.db.database import engine
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    return app


app = create_app()
