from sqlalchemy import select

from db.models.session import SessionOrm
from dtos.user_dto import UserDTO
from entities.user import User
from exceptions.ObjectDoesNotExistsException import ObjectDoesNotExistsException
from gateways.UserGateway import UserGateway
from db.models.user import UserOrm
from db.db_main import db


class PostgresUserGateway(UserGateway):
    async def add_user(self, user: UserDTO):
        async with db.session_factory() as session:
            new_user = UserOrm(
                name=user.name, mobile_number=user.mobile_number, password=user.password)
            session.add(new_user)
            await session.commit()
            return new_user.id

    async def delete_user(self, user_id):
        async with db.session_factory() as session:
            user_to_delete = await session.get(UserOrm, ident=user_id)

            if not user_to_delete:
                raise ObjectDoesNotExistsException(
                    'cant delete not existent user')

            await session.delete(user_to_delete)
            await session.commit()

    async def get_by_id(self, user_id):
        async with db.session_factory() as session:
            user_orm = await session.get(UserOrm, ident=user_id)

            if not user_orm:
                raise ObjectDoesNotExistsException(
                    'user does not exist in data base')

            user = User(user_id, UserDTO(
                user_orm.name, user_orm.mobile_number, user_orm.password))
            return user

    async def get_all(self):
        async with db.session_factory() as session:
            result = await session.execute(select(UserOrm))
            return result.scalars().all()

    async def get_by_session_id(self, session_id):
        async with db.session_factory() as session:
            query = select(UserOrm).join(
                SessionOrm, SessionOrm.user_id == UserOrm.id).filter_by(session_id=session_id)
            user_data = await session.execute(query)
            user_data = user_data.scalars().one_or_none()
            return user_data
