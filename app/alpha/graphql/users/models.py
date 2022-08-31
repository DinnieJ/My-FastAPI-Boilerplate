from ...users.models import User
from typing import Any

class GUser(User):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        pass