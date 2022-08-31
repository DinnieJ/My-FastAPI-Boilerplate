import strawberry
from .scalars import User
from typing import List
from .resolvers import get_users
from strawberry.types import Info

@strawberry.type
class UserQuery:
    @strawberry.field
    async def users(self, info: Info) -> List[User]:
        users = await get_users(info)
        return users