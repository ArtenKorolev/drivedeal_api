from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from db.models.base import Base


class UserOrm(Base):
    __tablename__ = 'user'

    name: Mapped[str]
    mobile_number: Mapped[str] = mapped_column(String(length=12), nullable=False)
    password: Mapped[str]
