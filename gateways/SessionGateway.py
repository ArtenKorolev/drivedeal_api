from abc import ABC, abstractmethod
from dtos.session_dto import SessionDTO


class SessionGateway(ABC):
    @abstractmethod
    async def create_new(self, new_session: SessionDTO):
        pass

    @abstractmethod
    async def delete_session(self, session_id):
        pass
