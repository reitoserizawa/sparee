from app.database import db
from app.models.base import BaseModel
from geoalchemy2 import Geometry
from geoalchemy2.shape import from_shape
from datetime import datetime
from shapely.geometry import Point


class Address(BaseModel):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(100), nullable=False, default="USA")

    location = db.Column(
        Geometry(geometry_type='POINT', srid=4326), nullable=False)

    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, street: str, city: str, state: str, postal_code: str, lat: float, lng: float, country: str = "USA") -> None:
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.location = from_shape(Point(lng, lat), srid=4326)

    def __repr__(self) -> str:
        return f"<Address {self.street}, {self.city}>"
