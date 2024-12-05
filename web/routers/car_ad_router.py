from typing import Annotated

from fastapi import APIRouter, Depends, Response

from db.pg_gateway.PostgresCarModelGateway import PostgresCarModelGateway
from db.pg_gateway.PostgresImageGateway import PostgresImageGateway
from entities.car import Car
from entities.car_ad import CarAd
from entities.car_model import CarModel
from entities.user import User
from exceptions.ObjectDoesNotExistsException import ObjectDoesNotExistsException
from use_cases.CreateAdUseCase import CreateAdUseCase
from use_cases.GetAllAdUseCase import GetAllAdUseCase
from db.pg_gateway.PostgresCarAdGateway import PostgresCarAdGateway
from db.pg_gateway.PostgresCarGateway import PostgresCarGateway
from db.pg_gateway.PostgresUserGateway import PostgresUserGateway
from web.response import MAvitoResponse
from web.routers.auth_router import get_user_data_from_cookie
from web.schemas.car_schema import SCarCreate


router = APIRouter(prefix='/ads', tags=['Car Ads'])


@router.get('/all')
async def get_all_ads(response: Response):
    try:
        model_gw = PostgresCarModelGateway()
        image_gw = PostgresImageGateway()
        car_gw = PostgresCarGateway(model_gw, image_gw)

        user_gw = PostgresUserGateway()
        car_ad_gw = PostgresCarAdGateway(car_gw, user_gw)

        use_case = GetAllAdUseCase(car_ad_gw)
        ads = await use_case.run()

        response_list = []
        for i in ads:
            image = i[1]
            response_list.append(await get_response_dict_by_ad_entity(i[0], image))
    except ObjectDoesNotExistsException as not_exists_err:
        response.status_code = 401
        return await MAvitoResponse(None, not_exists_err.what()).as_dict()
    except Exception as err:
        response.status_code = 500
        return await MAvitoResponse(None, 'unknown exception').as_dict()

    response.status_code = 200
    return await MAvitoResponse(response_list, None).as_dict()


async def get_response_dict_by_ad_entity(entity: CarAd, image_url):
    dct = {
        'id': entity.get_id(),
        'user': await get_response_dict_by_user_entity(entity.get_user_entity()),
        'car': await get_response_dict_by_car_entity(entity.get_car_entity(), image_url)
    }
    return dct


async def get_response_dict_by_car_entity(entity: Car, image_url):
    dct = {
        'id': entity.get_id(),
        'name': entity.get_name(),
        'color': entity.get_color(),
        'price': entity.get_price(),
        'power': entity.get_power(),
        'transmission': entity.get_transmission(),
        'body': entity.get_body(),
        'volume': entity.get_volume(),
        'disk_raidus': entity.get_disk_radius(),
        'engine': entity.get_engine(),
        'drive': entity.get_drive(),
        'mileage': entity.get_mileage(),
        'model': await get_reponse_dict_by_model_entity(entity.get_model()),
        'image_url': image_url
    }

    return dct


async def get_response_dict_by_user_entity(entity: User):
    dct = {
        'id': entity.get_id(),
        'name': entity.get_name(),
        'contact_number': entity.get_number(),
    }

    return dct


async def get_reponse_dict_by_model_entity(entity: CarModel):
    dct = {
        'id': entity.get_id(),
        'name': entity.get_name(),
    }

    return dct


@router.post('/create')
async def create_ad(car: Annotated[SCarCreate, Depends()], image_url: str, response: Response, user_data=Depends(get_user_data_from_cookie)):
    try:
        model_gw = PostgresCarModelGateway()
        image_gw = PostgresImageGateway()
        car_gw = PostgresCarGateway(model_gw, image_gw)

        user_gw = PostgresUserGateway()
        car_ad_gw = PostgresCarAdGateway(car_gw, user_gw)

        use_case = CreateAdUseCase(car_ad_gw)
        await use_case.run(car, user_data.id, image_url)
    except ObjectDoesNotExistsException as not_exists_err:
        response.status_code = 401
        return await MAvitoResponse(None, not_exists_err.what()).as_dict()
    except Exception as err:
        print(err)
        response.status_code = 500
        return await MAvitoResponse(None, 'unknown exception').as_dict()

    response.status_code = 201
    return await MAvitoResponse(None, None).as_dict()
