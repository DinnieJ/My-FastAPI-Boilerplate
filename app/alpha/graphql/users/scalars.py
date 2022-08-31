import strawberry
from pydantic import Field, typing

@strawberry.type
class User:
    id: int
    username: typing.Optional[str] = ""
    # stickynotes: typing.Optional[typing.List[StickyNotes]] = Field(default_factory=list)