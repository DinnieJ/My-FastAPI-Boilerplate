from typing import Any, Union
from fastapi import APIRouter, Depends, Header
from .services import TaskService
from .models import Task


class CheckQueryDependency:
    def __init__(self) -> None:
        pass

    def __call__(self, user_agent: Union[str, None] = Header(default=None)) -> bool:
        print(user_agent)
        return False


router = APIRouter(
    prefix="/task",
)


@router.get("/")
async def index(check: bool = Depends(CheckQueryDependency())):
    return {"Task": "Hello"}


@router.post("/")
async def insert():
    task = Task(user_id=2, name="hello")
    is_created = await TaskService.create(task=task)


@router.delete("/{id}")
async def delete(id: int):
    print(id)
    await TaskService.delete(id)


@router.get("/all")
async def get_all():
    return await TaskService.all()
