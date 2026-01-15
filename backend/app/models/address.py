from app.database import db
from app.models.base import BaseModel
from geoalchemy2 import Geometry
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

from typing import Optional


class Address(BaseModel):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(100), nullable=False, default="USA")

    location = db.Column(
        Geometry(geometry_type='POINT', srid=4326), nullable=True)

    geocode_status = db.Column(
        db.Enum("pending", "success", "failed", name="geocode_status"),
        default="pending",
        nullable=False
    )

    @property
    def lat(self) -> Optional[float]:
        if self.location:
            return self.location.y
        return None

    @property
    def lng(self) -> Optional[float]:
        if self.location:
            return self.location.x
        return None

    def set_location(self, lng: Optional[float], lat: Optional[float]) -> None:
        if lng is not None and lat is not None:
            self.location = from_shape(Point(lng, lat), srid=4326)
        else:
            self.location = None

    def __repr__(self) -> str:
        return f"<Address {self.street}, {self.city}>"
