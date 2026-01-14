from marshmallow import Schema, fields


class UserBaseSchema(Schema):
    username = fields.Str()
    email = fields.Email()
