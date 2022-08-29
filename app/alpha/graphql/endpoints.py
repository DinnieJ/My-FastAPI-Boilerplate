from strawberry.fastapi import GraphQLRouter
import strawberry

@strawberry.type
class Query:
    @strawberry.field
    async def hello() -> str:
        return "ok"

schema = strawberry.Schema(query=Query)
router = GraphQLRouter(schema=schema, path="/graphql")