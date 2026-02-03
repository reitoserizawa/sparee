from flask import Blueprint, request, jsonify, g
from marshmallow import ValidationError

from app.schemas.users.login import UserLoginSchema
from app.services.user_service import UserService

from app.utils.load_dict import load_dict

bp = Blueprint("login", __name__, url_prefix="/api/users")

login_schema = UserLoginSchema()
user_service = UserService()


@bp.route("/login", methods=["POST"])
async def login_user():
    session = g.session
    try:
        payload = load_dict(login_schema, request.json)
    except ValidationError as err:
        return jsonify(errors=err.messages), 400

    user = await user_service.authenticate(session, payload["email"], payload["password"])
    if not user:
        return jsonify(errors=["Invalid email or password"]), 401

    token = user_service.generate_token(user)
    return jsonify({"user": user.username, "token": token}), 200
