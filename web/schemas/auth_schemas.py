from pydantic import BaseModel

from dtos.user_dto import UserDTO


class SUserCreate(BaseModel, UserDTO):
    class Config:
        from_attributes=True

class SUser(SUserCreate):
    id: int


class SUserLogin(BaseModel):
    name: str
    password: str
