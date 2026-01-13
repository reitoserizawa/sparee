from marshmallow import fields
from .base import UserBaseSchema


class UserCreateSchema(UserBaseSchema):
    password = fields.Str(
        required=True,
        load_only=True,
        validate=lambda p: len(p) >= 8
    )
