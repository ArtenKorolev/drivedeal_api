class GetAdsByUserId:
    def __init__(self, repo):
        self.__repo = repo

    async def run(self, user_id):
        return await self.__repo.get_by_user_id(user_id)