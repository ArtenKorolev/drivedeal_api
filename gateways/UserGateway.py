from abc import ABC, abstractmethod

from dtos.user_dto import UserDTO
from entities.user import User


class UserGateway(ABC):
    @abstractmethod
    async def add_user(self, user: UserDTO):
        ...

    @abstractmethod
    async def delete_user(self, user_id):
        ...

    @abstractmethod
    async def get_by_id(self, user_id) -> User:
        ...

    @abstractmethod
    async def get_all(self) -> list[User]:
        ...

    @abstractmethod
    async def get_by_session_id(self, session_id):
        ...
