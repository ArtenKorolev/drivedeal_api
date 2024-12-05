from dtos.car_dto import CarDTO
from entities.entity import Entity


class Car(Entity):
    def __init__(self, ident, data: CarDTO):
        super().__init__(ident)
        self.__data = data

    def validate_price(self):
        if not self.__check_that_is_not_negative(self.__price):
            raise ValueError('price cant be negative')

    def validate_mileage(self):
        if not self.__check_that_is_not_negative(self.__mileage):
            raise ValueError('mileage cant be negative')

    def __check_that_is_not_negative(self, value):
        return True if value >= 0 else False

    def get_name(self):
        return self.__data.name

    def get_model(self):
        return self.__data.model

    def get_price(self):
        return self.__data.price

    def get_mileage(self):
        return self.__data.mileage

    def get_body(self):
        return self.__data.body_type

    def get_power(self):
        return self.__data.power

    def get_disk_radius(self):
        return self.__data.disk_radius

    def get_transmission(self):
        return self.__data.transmission_type

    def get_drive(self):
        return self.__data.drive_type

    def get_engine(self):
        return self.__data.engine_type

    def get_volume(self):
        return self.__data.volume

    def get_color(self):
        return self.__data.color
