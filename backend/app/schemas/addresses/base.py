from marshmallow import Schema, fields


class AddressBaseSchema(Schema):
    street = fields.Str()
    city = fields.Str()
    state = fields.Str()
    postal_code = fields.Str()
    country = fields.Str()
