import imp
from fastapi import FastAPI
from starlette.types import ASGIApp
from starlette.staticfiles import StaticFiles
from core.middleware import JsonExceptionMiddleware, SQLAlchemyMiddleware

class Application:
    app: FastAPI

    @classmethod
    def get_application_instance(self) -> ASGIApp:
        return self.app
    
    @classmethod
    def load_app(self, **kwargs) -> ASGIApp:
        self.app = FastAPI(debug=kwargs.get("debug"))
        self.load_router(routers=kwargs.get("routers"))
        self.load_static_route(dir=kwargs.get("static_dir"), path=kwargs.get("static_path"))

        self.app.add_middleware(SQLAlchemyMiddleware)
        self.app.add_middleware(JsonExceptionMiddleware)
        return self.app

    @classmethod
    def load_router(self, *, routers) -> None:
        for version, r in routers.items():
            for router in r:
                self.app.include_router(router=router, prefix= "/" + version, tags=[version])
        pass
    
    @classmethod
    def load_static_route(self, *, dir, path) -> None:
        self.app.mount(path=path, app=StaticFiles(directory=dir), name="static")
        pass

