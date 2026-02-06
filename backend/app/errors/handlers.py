from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.errors.custom_exception import APIError
from app.errors.jwt_configuration_error import JWTConfigurationError


def register_error_handlers(app: FastAPI):
    @app.exception_handler(APIError)
    async def handle_api_error(request: Request, err: APIError):
        return JSONResponse(
            status_code=err.status_code,
            content={
                "error": {
                    "message": err.message,
                    "status_code": err.status_code,
                }
            },
        )

    @app.exception_handler(JWTConfigurationError)
    async def handle_jwt_config_error(
        request: Request, err: JWTConfigurationError
    ):
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "message": str(err),
                    "status_code": 500,
                }
            },
        )

    # Catch-all fallback
    @app.exception_handler(Exception)
    async def handle_generic_error(request: Request, err: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "message": "Internal server error",
                    "status_code": 500,
                }
            },
        )
