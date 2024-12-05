from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from db.models.base import Base


class SessionOrm(Base):
    __tablename__ = 'session'

    session_id:Mapped[str]
    user_id:Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))
