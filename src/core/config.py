import os
from logging import config as logging_config

from core.logger import LOGGING

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

logging_config.dictConfig(LOGGING)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class AppSettings(BaseSettings):
    app_title: str = "FastAPI exp app"
    database_dsn: PostgresDsn = "postgresql+asyncpg://me:1111111@localhost:5832/my"
    BLACK_LIST: list[str] = []
    PROJECT_HOST: str = '0.0.0.0'
    PROJECT_PORT: int = 8000

    echo_query: str = "select 1"

    class Config:
        env_file = '../.env'


app_settings = AppSettings()
