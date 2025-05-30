import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    API_TITLE = os.getenv("API_TITLE")
    API_DESCRIPTION = os.getenv("API_DESCRIPTION")
    API_VERSION = os.getenv("API_VERSION")
    PROJECT_VERSION = os.getenv("PROJECT_VERSION")

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    DATABASE_URL = (f"postgresql+asyncpg://"
                    f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:"
                    f"{POSTGRES_PORT}/"
                    f"{POSTGRES_DB}")

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    STORAGE_API = os.getenv("STORAGE_API")
