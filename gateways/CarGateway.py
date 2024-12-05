from abc import ABC, abstractmethod

from dtos.car_dto import CarDTO
from entities.car import Car


class CarGateway(ABC):
    @abstractmethod
    async def add_car(self, car: CarDTO) -> int:
        ...

    @abstractmethod
    async def delete_car(self, car_id):
        ...

    @abstractmethod
    async def get_by_id(self, car_id) -> list[Car, str]:
        ...
