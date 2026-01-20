from marshmallow import fields
from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import to_shape

from .base import AddressBaseSchema


class AddressResponseSchema(AddressBaseSchema):
    id = fields.Int(dump_only=True)
    location = fields.Method("get_location", dump_only=True)

    def get_location(self, obj):
        if obj.coordinates:
            return obj.coordinates
        return None
