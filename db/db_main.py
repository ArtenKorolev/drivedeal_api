from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from config.settings import settings


class DB:
    def __init__(self):
        self.engine = create_async_engine(settings.async_db_url)
        self.session_factory = async_sessionmaker(bind=self.engine,
                                                    autoflush=False,
                                                    autocommit=False,
                                                    expire_on_commit=False)

db = DB()