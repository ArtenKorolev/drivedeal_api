from entities.entity import Entity
from dtos.user_dto import UserDTO


class User(Entity):
    def __init__(self, ident, data: UserDTO):
        super().__init__(ident)
        self.__data = data

    def get_name(self):
        return self.__data.name

    def get_number(self):
        return self.__data.mobile_number
