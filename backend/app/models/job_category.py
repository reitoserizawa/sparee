from app.database import db
from app.models.base import BaseModel


class JobCategory(BaseModel):
    __tablename__ = 'job_categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<JobCategory id={self.id} name={self.name}>"
