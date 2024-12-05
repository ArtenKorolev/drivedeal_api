from dataclasses import dataclass

from dtos.car_dto import CarDTO
from dtos.user_dto import UserDTO


@dataclass
class CarAdDTO:
    user: UserDTO
    car: CarDTO
