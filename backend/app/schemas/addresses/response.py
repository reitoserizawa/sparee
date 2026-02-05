from pydantic import Field, computed_field
from .base import AddressBaseModel
from typing import Optional


class AddressResponseModel(AddressBaseModel):
    id: int = Field(..., frozen=True)

    @computed_field
    @property
    def location(self) -> Optional[dict]:
        return self.coordinates if self.coordinates else None

    class Config:
        orm_mode = True
        from_attributes = True
