from pydantic import Field
from .base import AddressBaseModel
from typing import Optional


class AddressResponseModel(AddressBaseModel):
    id: int = Field(..., frozen=True)
    coordinates: Optional[dict] = Field(None, frozen=True)
    full_address: str = Field(..., frozen=True)

    model_config = {
        "from_attributes": True
    }
