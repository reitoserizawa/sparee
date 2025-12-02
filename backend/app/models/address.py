from app.database import db
from geoalchemy2 import Geometry
from datetime import datetime


class Address(db.Model):
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

    def __init__(self, street, city, state, postal_code, country="USA"):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country

    def __repr__(self):
        return f"<Address {self.street}, {self.city}>"
