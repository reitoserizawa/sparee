from flask import jsonify
from app.errors.custom_exception import APIError


def register_error_handlers(app):
    @app.errorhandler(APIError)
    async def handle_api_error(err: APIError):
        response = {
            "error": {
                "message": err.message,
                "status_code": err.status_code
            }
        }
        return jsonify(response), err.status_code

    # catch unhandled exceptions
    @app.errorhandler(Exception)
    async def handle_generic_error(err: Exception):
        response = {
            "error": {
                "message": str(err),
                "status_code": 500
            }
        }
        return jsonify(response), 500
