from abc import ABC, abstractmethod

from dtos.image_dto import ImageDTO


class ImageGateway(ABC):
    @abstractmethod
    def get_by_id(self, image_id) -> str:
        ...

    @abstractmethod
    def add_image(self, image_dto: ImageDTO):
        ...
