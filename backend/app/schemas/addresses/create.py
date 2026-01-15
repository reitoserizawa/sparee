from marshmallow import fields, post_load
from .base import AddressBaseSchema


class AddressCreateSchema(AddressBaseSchema):
    street = fields.Str(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)
    postal_code = fields.Str(required=True)
    country = fields.Str(required=True)

    @post_load
    def make_address(self, data, **kwargs):
        data.pop("lat", None)
        data.pop("lng", None)
        return data
