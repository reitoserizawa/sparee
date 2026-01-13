from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.schemas.users.create import UserCreateSchema
from app.schemas.users.response import UserResponseSchema
from app.services.user_service import UserService

from utils.load_dict import load_dict

bp = Blueprint("users", __name__, url_prefix="/api/users")

create_schema = UserCreateSchema()
response_schema = UserResponseSchema()
user_service = UserService()


@bp.route("", methods=["POST"])
def create_user():
    try:
        payload = load_dict(create_schema, request.json)
    except ValidationError as err:
        return {"errors": err.messages}, 400

    user = user_service.create_user(payload)

    return jsonify(response_schema.dump(user)), 201
