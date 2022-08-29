from fastapi import FastAPI, Depends
from fastapi.requests import Request
from fastapi.routing import APIRouter
from typing import Any


router = APIRouter()

class Permission:
    def __init__(self) -> None:
        pass
    async def __call__(self, request:Request) -> Any:
        print(1)
        print(request, 1)
        print(request)
@router.get("/", dependencies=[Depends(Permission)])
async def test():
    return {"1": "2"}


app = FastAPI()
app.add_middleware(Permission)
app.include_router(router)

