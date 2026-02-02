from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.users.create import UserCreateSchema
from app.schemas.users.response import UserResponseSchema
from app.services.user_service import UserService

from app.decorators.with_session import with_session
from app.errors.custom_exception import APIError
from app.utils.load_dict import load_dict

bp = Blueprint("users", __name__, url_prefix="/api/users")

create_schema = UserCreateSchema()
response_schema = UserResponseSchema()
user_service = UserService()


@bp.route("", methods=["POST"])
@with_session
async def create_user(session: AsyncSession):
    try:
        payload = load_dict(create_schema, request.json)
    except ValidationError as err:
        raise APIError(message=str(err), status_code=400)

    existing = await user_service.get_from_email(session, email=payload["email"])
    if existing:
        raise APIError(
            message=f"Email {payload['email']} already exists",
            status_code=400
        )
    user = await user_service.create_user(session, payload)

    return jsonify(response_schema.dump(user)), 201
