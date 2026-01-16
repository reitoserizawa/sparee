from marshmallow import fields

from .base import AddressBaseSchema


class AddressResponseSchema(AddressBaseSchema):
    id = fields.Int(dump_only=True)
    location = fields.Method("get_location", dump_only=True)

    def get_location(self, obj):
        if obj.location:
            return {"lat": obj.lat, "lng": obj.lng}
        return None


class AddressListResponseSchema(AddressResponseSchema):
    class Meta:
        many = True
