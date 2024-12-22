from typing import Annotated
from fastapi import APIRouter, Cookie, Depends, HTTPException, Response, status
from nanoid import generate

from db.pg_gateway.PostgresSessionGateway import PostgresSessionGateway
from db.pg_gateway.PostgresUserGateway import PostgresUserGateway
from dtos.session_dto import SessionDTO
from exceptions.AuthException import AuthException
from use_cases.GetUserByNameUseCase import GetUserByNameUseCase
from web.response import MAvitoResponse
from web.schemas.auth_schemas import SUserCreate, SUserLogin
from use_cases.RegisterUserUseCase import RegisterUserUseCase
from config.settings import settings


auth_router = APIRouter(prefix='/auth', tags=['Authenticate'])


@auth_router.post('/register')
async def register_new_user(response: Response, new_user: Annotated[SUserCreate, Depends()]):
    try:
        user_gw = PostgresUserGateway()
        session_gw = PostgresSessionGateway()

        use_case = RegisterUserUseCase(session_gw, user_gw)

        session_id = await use_case.run(new_user)
        response.status_code = 201
        response.set_cookie(settings.cookie_session_key, session_id)
        return await MAvitoResponse(None, 'registered').as_dict()
    except AuthException as e:
        response.status_code = 422
        return await MAvitoResponse(None, e.what()).as_dict()
    except Exception as e:
        response.status_code = 500
        return await MAvitoResponse(None, 'unknown exception').as_dict()


@auth_router.post('/login')
async def login_user(response: Response, loginning_user: Annotated[SUserLogin, Depends()]):
    try:
        user_gw = PostgresUserGateway()
        session_gw = PostgresSessionGateway()

        get_by_name = GetUserByNameUseCase(user_gw)

        user_params = loginning_user.model_dump()

        user = await get_by_name.run(user_params['name'])

        if not user:
            response.status_code = 404
            return await MAvitoResponse(None, 'user does not exist').as_dict()
        if user.password != user_params['password']:
            response.status_code = 401
            return await MAvitoResponse(None, 'invalid password').as_dict()

        session_id = generate(size=settings.session_id_size)
        new_session = SessionDTO(session_id, user.id)
        await session_gw.create_new(new_session)
        response.set_cookie(settings.cookie_session_key, session_id)
        response.status_code = 200
        return await MAvitoResponse(None, 'loginned').as_dict()
    except AuthException as e:
        response.status_code = 422
        return await MAvitoResponse(None, e.what()).as_dict()
    except Exception as e:
        response.status_code = 500
        return await MAvitoResponse(None, 'internal server error').as_dict()


@auth_router.get('/logout')
async def logout_user(response: Response, session_id: str = Cookie(None, alias=settings.cookie_session_key)):
    try:
        session_gw = PostgresSessionGateway()

        if not session_id:
            response.status_code = 401
            return await MAvitoResponse(None, 'not authorized').as_dict()

        await session_gw.delete_session(session_id)
        response.delete_cookie(settings.cookie_session_key)
        return await MAvitoResponse(None, 'logouted').as_dict()
    except AuthException as e:
        response.status_code = 422
        return MAvitoResponse(None, e.what()).as_dict()
    except Exception as e:
        response.status_code = 500
        return await MAvitoResponse(None, 'unknown exception').as_dict()


async def get_user_data_from_cookie(session_id: str = Cookie(None, alias=settings.cookie_session_key)):
    print(session_id)

    if not session_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='not authorized')

    user_data = await PostgresUserGateway().get_by_session_id(session_id)
    return user_data


@auth_router.get('/profile')
async def get_user_profile(user_data=Depends(get_user_data_from_cookie)):
    return await MAvitoResponse(user_data, None).as_dict()
