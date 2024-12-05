from sqlalchemy import select

from entities.car import Car
from mappers.car_mapper import CarMapper
from db.db_main import db
from db.models.car import CarOrm
from db.models.image import ImageOrm
from dtos.car_dto import CarDTO
from dtos.image_dto import ImageDTO
from exceptions.ObjectDoesNotExistsException import ObjectDoesNotExistsException
from gateways.CarGateway import CarGateway


class PostgresCarGateway(CarGateway):
    def __init__(self, model_repo, image_repo):
        self.__model_repo = model_repo
        self.__image_repo = image_repo

    async def add_car(self, car: CarDTO, image_url) -> int:
        async with db.session_factory() as session:
            model = await self.__model_repo.get_by_name(car.model)
            image_id = await self.__image_repo.add_image(ImageDTO(image_url))
            model_id = model.id

            car_orm = await CarMapper().to_orm(car, model_id, image_id)

            session.add(car_orm)
            await session.commit()

            return car_orm.id

    async def delete_car(self, car_id):
        async with db.session_factory() as session:
            car_to_delete = await session.get(ident=car_id)

            if not car_to_delete:
                raise ObjectDoesNotExistsException(
                    'cant delete not exists car')

            await session.delete(car_to_delete)
            await session.commit()

    async def get_by_id(self, car_id):
        async with db.session_factory() as session:
            car = await session.get(CarOrm, ident=car_id)

            if not car:
                raise ObjectDoesNotExistsException('this car does not exist')

            model = await self.__model_repo.get_by_id(car.model_id)
            car_dto = await CarMapper().to_dto(car, model)
            image = (await self.__image_repo.get_by_id(car.image)).url
            return [Car(car_id, car_dto), image]
