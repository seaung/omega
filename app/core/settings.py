from functools import lru_cache
import pathlib

from pydantic_settings import BaseSettings

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


class ConfigSettings(BaseSettings):

    DB_TYPE = 'postgres'

    DB_USERNAME = 'postgres'

    DB_PASSWORD = 'postgres123456'

    DB_HOST = '0.0.0.0'

    DB_PORT = 5432

    DB_NAME = 'omega_db'

    DB_DRIVERNAME = 'postgres+asyncpg'

    DB_ECHO = True

    DB_ECHO_POOL = True

    DB_POOL_SIZE = 10

    DB_FUTURE = True

    DB_MAX_OVERFLOW = 20

    DB_POOL_TIMEOUT = 30

    DB_POOL_RECYCLE = 3600

    DB_POOL_PRE_PING = True

    DB_POOL_USE_INFO = False



@lru_cache
def get_settings() -> ConfigSettings:
    return ConfigSettings()


settings = get_settings()

