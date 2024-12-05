from db.models.car import CarOrm
from db.models.user import UserOrm
from dtos.car_dto import CarDTO


class CarMapper:
    async def to_orm(self, car: CarDTO, model_id, image_id):

        car_orm = CarOrm(name=car.name,
                         model_id=model_id,
                         color=car.color,
                         engine_type=car.engine_type,
                         drive_type=car.drive_type,
                         transmission_type=car.transmission_type,
                         disk_radius=car.disk_radius,
                         price=car.price,
                         mileage=car.mileage,
                         engine_volume=car.volume,
                         body_type=car.body_type,
                         power=car.power,
                         image=image_id
                         )

        return car_orm

    async def to_dto(self, car: CarOrm, model):
        return CarDTO(name=car.name,
                      model=model,
                      price=car.price,
                      mileage=car.mileage,
                      body_type=car.body_type,
                      power=car.power,
                      disk_radius=car.disk_radius,
                      color=car.color,
                      volume=car.engine_volume,
                      transmission_type=car.transmission_type,
                      engine_type=car.engine_type,
                      drive_type=car.drive_type
                      )
