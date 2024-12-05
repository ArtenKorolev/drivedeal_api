from dtos.car_dto import CarDTO


class CreateAdUseCase:
    def __init__(self, repo):
        self.__repository = repo

    async def run(self, car: CarDTO, user_id, img_url):
        await self.__repository.add_ad(car, user_id, img_url)
