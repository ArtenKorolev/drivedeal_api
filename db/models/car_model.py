from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from db.models.base import Base


class CarModelOrm(Base):
    __tablename__ = 'car_model'

    model_name: Mapped[str]
    image: Mapped[int] = mapped_column(ForeignKey(column='image.id', ondelete='SET NULL'))
