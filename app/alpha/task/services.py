from core.db import session
# from sqlalchemy.future import select
from .models import Task
from sqlalchemy.sql.expression import delete, select
from typing import List


class TaskService:
    def __init__(self) -> None:
        pass

    async def all(self):
        query = select(Task)
        result = await session.execute(query)
        return result.scalars().first()

    async def create(task: Task) -> bool:
        session.add(task)
        await session.commit()

    async def delete(id: int) -> bool:
        query = delete(Task).where(Task.id == id)
        await session.execute(Task)
