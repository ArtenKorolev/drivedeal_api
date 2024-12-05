from pydantic import BaseModel
from dtos.car_dto import CarDTO


class SCar(BaseModel, CarDTO):
    pass

class SCarCreate(SCar):
    pass
