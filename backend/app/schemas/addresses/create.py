from pydantic import Field
from .base import AddressBaseModel


class AddressCreateModel(AddressBaseModel):
    street: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    postal_code: str = Field(...)
    country: str = Field(...)

    class Config:
        extra = "forbid"
