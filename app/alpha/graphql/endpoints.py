from strawberry.fastapi import GraphQLRouter
import strawberry
from strawberry.tools import merge_types
from .users import UserQuery

@strawberry.type
class Query:
    @strawberry.field
    async def hello() -> str:
        return "ok"

RootQuery = merge_types("RootQuery", (UserQuery, Query))


schema = strawberry.Schema(query=RootQuery)
router = GraphQLRouter(schema=schema, path="/graphql")