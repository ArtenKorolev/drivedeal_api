class GetAllAdUseCase:
    def __init__(self, repo):
        self.__repo = repo

    async def run(self):
        return await self.__repo.get_all()