
from fastapi import APIRouter
from .services import TaskService
from .models import Task

router = APIRouter(
    prefix="/task",
)

@router.get("/")
async def index():
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

