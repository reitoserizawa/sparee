from app.database import db
from app.models.base import BaseModel
from sqlalchemy.orm import backref
from datetime import datetime


class Company(BaseModel):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    address = db.relationship(
        "Address", backref=backref("company", uselist=False))

    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    deleted_at = db.Column(
        db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Company id={self.id} name={self.name}>"
