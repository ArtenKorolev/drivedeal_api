from sqlalchemy import select
from db.db_main import db
from db.models.user import UserOrm


class GetUserByNameUseCase:
    def __init__(self, user_gw):
        self.__user_gw = user_gw

    async def run(self, name):
        async with db.session_factory() as session:
            query = select(UserOrm).filter_by(name=name)
            user = await session.execute(query)
            return user.scalars().one()