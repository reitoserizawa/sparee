from marshmallow import fields
from .base import CompanyBaseSchema
from ..addresses.create import AddressCreateSchema


class CompanyCreateSchema(CompanyBaseSchema):
    name = fields.Str(required=True)
    address = fields.Nested(AddressCreateSchema, required=True)
