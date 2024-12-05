from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped

from db.models.base import Base


class CarAdOrm(Base):
    __tablename__ = 'car_ad'

    user_id: Mapped[int] = mapped_column(ForeignKey(column='user.id', ondelete='CASCADE'))
    car_id: Mapped[int] = mapped_column(ForeignKey(column='car.id', ondelete='CASCADE'))
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
