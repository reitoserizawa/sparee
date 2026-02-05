from app.db.models.base import BaseModel
from sqlalchemy import Integer, String, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum as PyEnum
from geoalchemy2 import Geometry
from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import Point
from typing import Optional, cast, TYPE_CHECKING

if TYPE_CHECKING:
    from app.db.models.company import Company


class AddressStatus(PyEnum):
    pending = "pending"
    success = "success"
    failed = "failed"


class Address(BaseModel):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    street: Mapped[str] = mapped_column(
        String(255), nullable=False)
    city: Mapped[str] = mapped_column(
        String(100), nullable=False)
    state: Mapped[str] = mapped_column(
        String(100), nullable=False)
    postal_code: Mapped[str] = mapped_column(
        String(20), nullable=False)
    country: Mapped[str] = mapped_column(
        String(100), nullable=False, default="USA")
    location: Mapped[Optional[WKBElement]] = mapped_column(
        Geometry(geometry_type='POINT', srid=4326), nullable=True)

    geocode_status: Mapped[AddressStatus] = mapped_column(
        SAEnum(AddressStatus, name="geocode_status"),
        default=AddressStatus.pending,
        nullable=False
    )

    companies: Mapped[list["Company"]] = relationship(
        "Company",
        back_populates="address",
    )

    @property
    def coordinates(self) -> Optional[dict[str, float]]:
        if self.location is not None:
            geom = cast(Point, to_shape(self.location))
            return {"lat": geom.y, "lng": geom.x}
        return None

    @property
    def full_address(self) -> str:
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}"

    def set_status(self, status: AddressStatus) -> None:
        self.geocode_status = status

    def set_location(self, lng: Optional[float], lat: Optional[float]) -> None:
        if lng is not None and lat is not None:
            self.location = from_shape(Point(lng, lat), srid=4326)
        else:
            self.location = None

    def __repr__(self) -> str:
        return f"<Address {self.street}, {self.city}>"
