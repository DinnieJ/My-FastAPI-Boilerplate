from urllib import response
from starlette.types import ASGIApp, Receive, Scope, Send
from starlette.responses import JSONResponse

class JsonExceptionMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        try:
            await self.app(scope, receive, send)
        except Exception as e:
            trace = []
            tb = e.__traceback__
            while tb is not None:
                trace.append({
                    "filename": tb.tb_frame.f_code.co_filename,
                    "name": tb.tb_frame.f_code.co_name,
                    "lineno": tb.tb_lineno
                })
                tb = tb.tb_next
            
            response = JSONResponse({
                "exception_type": str(type(e)),
                "exeception_message": str(e),
                "trace": trace
            })

            await response(scope, receive, send) 
        pass
