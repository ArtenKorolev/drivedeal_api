from db.db_main import db
from db.models.image import ImageOrm
from dtos.image_dto import ImageDTO
from gateways.ImageGateway import ImageGateway


class PostgresImageGateway(ImageGateway):
    async def get_by_id(self, image_id):
        async with db.session_factory() as session:
            image = await session.get(ImageOrm, ident=image_id)
            return image

    async def add_image(self, image_dto: ImageDTO):
        async with db.session_factory() as session:
            new_image = ImageOrm(url=image_dto.url)
            session.add(new_image)
            await session.commit()
            return new_image.id
