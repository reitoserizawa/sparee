from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.models.base import BaseModel


class JobCategory(BaseModel):
    __tablename__ = 'job_categories'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<JobCategory id={self.id} name={self.name}>"
