class DeleteAdUseCase:
    def __init__(self, repo):
        self.__repo = repo

    async def run(self, ad_id):
        await self.__repo.delete_ad(ad_id)
