from dtos.user_dto import UserDTO


class CreateUserUseCase:
    def __init__(self, repo):
        self.__repository = repo

    async def run(self, user: UserDTO):
        await self.__repository.add_user(user)
