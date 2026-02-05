from pydantic import Field
from datetime import datetime
from .base import CompanyBaseModel
from ..addresses.response import AddressResponseModel


class CompanyResponseModel(CompanyBaseModel):
    id: int = Field(..., read_only=True)
    address: AddressResponseModel = Field(..., read_only=True)

    created_at: datetime = Field(..., read_only=True)
    updated_at: datetime = Field(..., read_only=True)
