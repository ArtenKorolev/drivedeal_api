from abc import ABC, abstractmethod
from entities.car_model import CarModel


class CarModelGateway(ABC):
    @abstractmethod
    def get_by_name(self, ident) -> CarModel:
        ...

    @abstractmethod
    def get_by_id(self, ident) -> CarModel:
        ...
