from sqlalchemy.orm import Mapped

from db.models.base import Base


class ImageOrm(Base):
    __tablename__ = 'image'

    url: Mapped[str]
