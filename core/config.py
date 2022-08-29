from os import getenv;
from dotenv import load_dotenv

load_dotenv("../.env")
class Config:
    DB_HOST: str = getenv("DB_HOST", "localhost")
    DB_PORT: str = getenv("DB_PORT", 3306)
    DB_USERNAME: str = getenv("DB_USERNAME", "root")
    DB_PASSWORD: str = getenv("DB_PASSWORD", "root")
    DB_NAME: str = getenv("DB_NAME", "todos")
    