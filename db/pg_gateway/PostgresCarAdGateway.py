from sqlalchemy import select

from dtos.car_dto import CarDTO
from db.models.car_ad import CarAdOrm
from entities.car_ad import CarAd
from exceptions.ObjectDoesNotExistsException import ObjectDoesNotExistsException
from gateways.CarAdGateway import CarAdGateway
from db.db_main import db


class PostgresCarAdGateway(CarAdGateway):
    def __init__(self, car_repo, user_repo):
        self.__car_repo = car_repo
        self.__user_repo = user_repo

    async def add_ad(self, car: CarDTO, user_id, car_image_url):
        car_id = await self.__car_repo.add_car(car, car_image_url)

        async with db.session_factory() as session:
            ad_orm = CarAdOrm(user_id=user_id, car_id=car_id)
            session.add(ad_orm)
            await session.commit()

    async def delete_ad(self, ad_id):
        async with db.session_factory() as session:
            ad_to_delete = await session.get(CarAdOrm, ident=ad_id)

            if not ad_to_delete:
                raise ObjectDoesNotExistsException('cant delete not exists ad')

            await session.commit()

    async def get_all(self):
        async with db.session_factory() as session:
            query = select(CarAdOrm)
            ads = (await session.execute(query)).scalars().all()

            return await self.__get_ads_entities_by_ads_orm(ads)

    async def __get_ads_entities_by_ads_orm(self, ads):
        ads_entities = []
        for i in ads:
            user = await self.__user_repo.get_by_id(i.user_id)
            repo_response = await self.__car_repo.get_by_id(i.car_id)
            car = repo_response[0]

            ads_entities.append([CarAd(i.id, car, user), repo_response[1]])

        return ads_entities

    async def get_by_user_id(self, user_id):
        async with db.session_factory() as session:
            query = select(CarAdOrm).filter_by(user_id=user_id)
            ads_orm = await session.execute(query)

            if not ads_orm:
                raise ObjectDoesNotExistsException(
                    'cant get ads by not exists user id')

            return self.__get_ads_entities_by_ads_orm(ads_orm)
