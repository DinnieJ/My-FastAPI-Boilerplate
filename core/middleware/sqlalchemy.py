
from uuid import uuid4

from starlette.types import ASGIApp, Receive, Scope, Send

from ..db.session import set_session, reset_session, session


class SQLAlchemyMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        session_id = str(uuid4())
        context = set_session(ssid=session_id)

        try:
            print(session_id)
            await self.app(scope, receive, send)
        except Exception as e:
            raise e
        finally:
            await session.remove()
            reset_session(context=context)