from marshmallow import fields
from .base import UserBaseSchema


class UserCreateSchema(UserBaseSchema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(
        required=True,
        load_only=True,
        validate=lambda p: len(p) >= 8
    )
