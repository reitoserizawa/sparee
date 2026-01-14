from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.schemas.users.login import UserLoginSchema
from app.services.user_service import UserService
from app.utils.load_dict import load_dict

bp = Blueprint("login", __name__, url_prefix="/api/users")

login_schema = UserLoginSchema()
user_service = UserService()


@bp.route("/login", methods=["POST"])
def login_user():
    try:
        payload = load_dict(login_schema, request.json)
    except ValidationError as err:
        return jsonify(errors=err.messages), 400

    user = user_service.authenticate(payload["email"], payload["password"])
    if not user:
        return jsonify(errors=["Invalid email or password"]), 401

    token = user_service.generate_token(user)
    return jsonify({"user": user.username, "token": token}), 200
