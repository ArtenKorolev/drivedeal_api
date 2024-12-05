from fastapi import FastAPI
from web.routers.car_ad_router import router as ad_router
from starlette.middleware.cors import CORSMiddleware

from web.routers.auth_router import auth_router 


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ad_router)
app.include_router(auth_router)
