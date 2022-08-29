from contextvars import ContextVar, Token
from typing import Union, Any


from sqlalchemy.ext.asyncio import (AsyncSession, create_async_engine, async_scoped_session)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from core.config import Config

session_context: ContextVar[str] = ContextVar("session_context")

def get_session() -> str:
    return session_context.get()

def set_session(ssid: str) -> Token:
    return session_context.set(ssid)

def reset_session(context: Token) -> None:
    session_context.reset(context)


db_url = f"mysql+aiomysql://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
print(db_url)

engines = {
    "master": create_async_engine(db_url, pool_recycle=3600)
}

class RoutingSession(Session):
    def get_bind(self,mapper=None, clause=None, **kw):
        return engines["master"].sync_engine

async_session_factory = sessionmaker(class_=AsyncSession, sync_session_class=RoutingSession)

session = async_scoped_session(
    session_factory=async_session_factory,
    scopefunc=get_session
)

Base = declarative_base()