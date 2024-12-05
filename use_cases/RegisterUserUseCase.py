from config.settings import settings
from dtos.session_dto import SessionDTO
from dtos.user_dto import UserDTO
from exceptions.AuthException import AuthException
from gateways.SessionGateway import SessionGateway
from gateways.UserGateway import UserGateway
from nanoid import generate


class RegisterUserUseCase:
    def __init__(self, session_gw: SessionGateway, user_gw: UserGateway):
        self.__session_gw = session_gw
        self.__user_gw = user_gw

    async def run(self, user_dto: UserDTO):
        try:
            new_user_id = await self.__user_gw.add_user(user_dto)
            token = generate(size=settings.session_id_size)
            session_dto = SessionDTO(token, new_user_id)
            await self.__session_gw.create_new(session_dto)
            return token
        except Exception as e:
            raise AuthException('bad register data')
