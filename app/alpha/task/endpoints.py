from typing import Any, Union
from fastapi import APIRouter, Depends, Header, UploadFile, BackgroundTasks
from .services import TaskService
from .models import Task
import os


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

def savefile(file: UploadFile):
    directory =  f"{os.getcwd()}/static/{file.filename}"
    with open(directory, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"info": f"file '{file.filename}' saved at '{directory}'"}

@router.post("/file")
async def upload_file(file: UploadFile, background_tasks: BackgroundTasks):
    background_tasks.add_task(savefile, file)
    return {"info": f"file '{file.filename}' saved"}


@router.get("/all")
async def get_all():
    return await TaskService.all()
