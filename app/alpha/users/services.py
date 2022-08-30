from core.db import session
# from sqlalchemy.future import select
from .models import User
from sqlalchemy.sql.expression import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from core.db import session


class UserService:
    def __init__(self) -> None:
        self.db_instance = session
        pass

    async def all():
        query = select([User.username, User.created_at])
        result = await session.execute(query)
        return result.scalars().all()

    async def get(id: int):
        query = select(User).where(User.id == id)
        result = await session.execute(query)
        return result.scalars().first()

    async def insert(user: User) -> User:
        # try:
        session.add(user)
        # await self.db_instance.flush([user])
        await session.commit()
        print(dict(user))
        # print(res.scalars())
        return user
    
    async def update(id, user: User):
        query = update(User).where(User.id == id).values()

    async def delete(id: int) -> bool:
        find_query = select(User).where(User.id == id)
        result = await session.execute(find_query)

        user_model_found = result.scalars().first()
        if user_model_found is None:
            return False
        delete_query = delete(User).where(User.id == id)
        await session.execute(delete_query)
        await session.commit()
        return True

    async def is_user_exist(username: str):
        query = select(User).where(User.username == username)
        result = await session.execute(query)

        return False if result.scalars().first() is None else True