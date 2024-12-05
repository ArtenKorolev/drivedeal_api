from entities.entity import Entity
from entities.car import Car
from entities.user import User


class CarAd(Entity):
    def __init__(self, ident, car, user):
        super().__init__(ident)
        self.__car = car
        self.__user = user

    def get_car_entity(self):
        return self.__car

    def get_user_entity(self):
        return self.__user
