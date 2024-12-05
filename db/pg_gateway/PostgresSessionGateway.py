from sqlalchemy import select
from gateways.SessionGateway import SessionGateway
from db.models.session import SessionOrm
from db.db_main import db


class PostgresSessionGateway(SessionGateway):
    async def create_new(self, new_session):
        async with db.session_factory() as session:
            session_orm = SessionOrm(session_id=new_session.session_id, user_id=new_session.user_id)
            session.add(session_orm)
            await session.commit()

    async def delete_session(self, session_id):
        async with db.session_factory() as session:
            query = select(SessionOrm).filter_by(session_id=session_id)
            session_instance = (await session.execute(query)).scalars().one_or_none()
            await session.delete(session_instance)
            await session.commit()
