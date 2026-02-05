from pydantic import BaseModel


class AddressBaseModel(BaseModel):
    street: str
    city: str
    state: str
    postal_code: str
    country: str
