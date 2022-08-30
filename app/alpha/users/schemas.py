from pydantic import BaseModel, Field, validator
from .services import UserService
from re import match

class UserSchema(BaseModel):
    username: str



class CreateUserSuccess(BaseModel):
    username: str
    created_at: str
    updated_at: str


class CreateUserSchema(UserSchema):
    username: str = Field(max_length=32)
    password: str = Field(min_length=8)

    @validator('password')
    def password_format(cls, v):
        if not match("^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$", v):
            raise ValueError("Password must be alphanumeric")
        return v.title()

    class Config:
        orm_mode = True
    
