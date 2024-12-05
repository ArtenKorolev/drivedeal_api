from entities.entity import Entity


class CarModel(Entity):
    def __init__(self, ident, name):
        super().__init__(ident)
        self.__name = name

    def get_name(self):
        return self.__name
