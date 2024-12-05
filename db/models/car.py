from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from db.models.base import Base


class CarOrm(Base):
    __tablename__ = 'car'

    name: Mapped[str]
    model_id: Mapped[int] = mapped_column(ForeignKey(column='car_model.id', ondelete='SET NULL'))
    price: Mapped[int]
    mileage: Mapped[int]
    body_type: Mapped[str]
    power: Mapped[int]
    disk_radius: Mapped[int]
    transmission_type: Mapped[str]
    drive_type: Mapped[str]
    engine_type: Mapped[str]
    image: Mapped[int] = mapped_column(ForeignKey(column='image.id', ondelete='SET NULL'))
    engine_volume: Mapped[float]
    color: Mapped[str]
