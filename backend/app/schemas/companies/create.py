from pydantic import Field
from .base import CompanyBaseModel
from ..addresses.create import AddressCreateModel


class CompanyCreateModel(CompanyBaseModel):
    name: str = Field(...)
    address: AddressCreateModel = Field(...)
