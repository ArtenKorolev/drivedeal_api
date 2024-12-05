from sqlalchemy import select

from entities.car_model import CarModel
from exceptions.ObjectDoesNotExistsException import ObjectDoesNotExistsException
from gateways.CarModelGateway import CarModelGateway
from db.db_main import db
from db.models.car_model import CarModelOrm


class PostgresCarModelGateway(CarModelGateway):
    async def get_by_name(self, name):
        async with db.session_factory() as session:
            query = select(CarModelOrm).filter_by(model_name=name)
            model = (await session.execute(query)).scalars().first()

            if not model:
                raise ObjectDoesNotExistsException('this model does not exist in data base')

            return model

    async def get_by_id(self, ident):
        async with db.session_factory() as session:
            model = await session.get(CarModelOrm, ident=ident)

            if not model:
                raise ObjectDoesNotExistsException('this model does not exist in data base')

            return CarModel(ident, model.model_name)
