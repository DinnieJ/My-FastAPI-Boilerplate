from typing import List, Dict
from fastapi import APIRouter
from app.alpha.task import router as alpha_task
from app.alpha.graphql import router as alpha_graphql
from app.alpha.users import router as alpha_user


routers : Dict[str, List[APIRouter]] = {
    "alpha": [alpha_task, alpha_graphql, alpha_user]
}