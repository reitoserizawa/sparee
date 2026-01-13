from marshmallow import Schema, fields


class UserBaseSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
