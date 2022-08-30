from fastapi import APIRouter, Depends, HTTPException
import starlette.status as httpstatus
from starlette.responses import JSONResponse
from .models import User
from .schemas import CreateUserSchema, UserSchema, CreateUserSuccess
from .services import UserService
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/user"
)




@router.get("/all")
async def all():
    return await UserService.all()

@router.get("/{id}")
async def get(id: int):
    return await UserService.get(id)

@router.post("/", response_model=CreateUserSuccess)
async def index(body: CreateUserSchema):
    if await UserService.is_user_exist(body.username) == True:
        raise HTTPException(status_code=httpstatus.HTTP_409_CONFLICT, detail="Fuck you")

    a = User(username = body.username, password = body.password)
    new_user = await UserService.insert(a)

    return new_user.as_dict()

@router.delete("/{id}")
async def delete(id: int):
    return await UserService.delete(id)

@router.post("/{username}")
async def check_exist(username: str):
    return await UserService.is_user_exist(username)
    