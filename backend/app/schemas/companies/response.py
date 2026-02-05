from pydantic import Field
from datetime import datetime
from .base import CompanyBaseModel
from ..addresses.response import AddressResponseModel


class CompanyResponseModel(CompanyBaseModel):
    id: int = Field(..., frozen=True)
    address: AddressResponseModel

    created_at: datetime
    updated_at: datetime
