from core.app.application import Application
from routers import routers
from dotenv import load_dotenv
import uvicorn
from os import getenv


load_dotenv(".env")
app = Application.load_app(
    routers=routers,
    static_dir="static",
    static_path="/static"
)

def main() -> None:
    if getenv("APP_DEBUG") == "True":
        print("Application running with debugger mode")
        uvicorn.run(
            "dev_server:app", 
            host=getenv("APP_HOST"), 
            port=int(getenv("APP_PORT")),
            reload=True,
            reload_excludes=["./docker/*"]
        )
    else:
        uvicorn.run(
            app, 
            host=getenv("APP_HOST"), 
            port=int(getenv("APP_PORT")),
        )


if __name__ == "__main__":
    main()
