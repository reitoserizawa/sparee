from marshmallow import fields
from .base import CompanyBaseSchema
from ..addresses.response import AddressResponseSchema


class CompanyResponseSchema(CompanyBaseSchema):
    id = fields.Int(dump_only=True)
    address = fields.Nested(AddressResponseSchema, dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
