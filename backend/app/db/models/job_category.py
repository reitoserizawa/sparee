from sqlalchemy import Column, Integer, String
from app.db.models.base import BaseModel


class JobCategory(BaseModel):
    __tablename__ = 'job_categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<JobCategory id={self.id} name={self.name}>"
