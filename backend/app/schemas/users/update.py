from marshmallow import fields
from marshmallow.validate import Length
from .base import UserBaseSchema


class UserUpdateSchema(UserBaseSchema):
    username = fields.Str(required=False)
    email = fields.Email(required=False)
    password = fields.Str(load_only=True, validate=Length(min=8))
