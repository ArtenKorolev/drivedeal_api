class MAvitoResponse:
    def __init__(self, data, details):
        self.__data = data
        self.__details = details

    async def as_dict(self):
        return {
            'data': self.__data,
            'details': self.__details
        }
