from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Enum
from enum import Enum as PyEnum
from geoalchemy2 import Geometry
from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import Point

from typing import Optional, cast


class AddressStatus(PyEnum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class Address(BaseModel):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    country = Column(String(100), nullable=False, default="USA")

    location = Column(
        Geometry(geometry_type='POINT', srid=4326), nullable=True)

    geocode_status = Column(
        Enum(AddressStatus, name="geocode_status"),
        default=AddressStatus.PENDING,
        nullable=False
    )

    @property
    def coordinates(self) -> Optional[dict]:
        if self.location is not None:
            geom = cast(Point, to_shape(cast(WKBElement, self.location)))
            return {"lat": geom.y, "lng": geom.x}
        return None

    @property
    def full_address(self) -> str:
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}"

    def set_status(self, status: AddressStatus):
        self.geocode_status = status

    def set_location(self, lng: Optional[float], lat: Optional[float]) -> None:
        if lng is not None and lat is not None:
            self.location = from_shape(Point(lng, lat), srid=4326)
        else:
            self.location = None

    def __repr__(self) -> str:
        return f"<Address {self.street}, {self.city}>"
