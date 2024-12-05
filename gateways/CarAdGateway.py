from abc import ABC, abstractmethod

from dtos.car_dto import CarDTO
from entities.car_ad import CarAd


class CarAdGateway(ABC):
    @abstractmethod
    async def add_ad(self, car: CarDTO, user_id, car_image_url):
        ...

    @abstractmethod
    async def delete_ad(self, ad_id):
        ...

    @abstractmethod
    async def get_by_user_id(self, user_id) -> CarAd:
        ...

    @abstractmethod
    async def get_all(self) -> list[CarAd]:
        ...
