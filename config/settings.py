import os
from dotenv import load_dotenv


class Settings:
    def __init__(self):
        load_dotenv()

        self.__db_port = os.getenv('DB_PORT')
        self.__db_name = os.getenv('DB_NAME')
        self.__db_user = os.getenv('DB_USER')
        self.__db_password = os.getenv('DB_PASS')
        self.__db_host = os.getenv('DB_HOST')
        self.cookie_session_key = 'user-session-id'
        self.session_id_size=20

    @property
    def async_db_url(self):
        return f'postgresql+asyncpg://{self.__db_user}:{self.__db_password}@{self.__db_host}:{self.__db_port}/{self.__db_name}'

settings = Settings()
print(settings.async_db_url)