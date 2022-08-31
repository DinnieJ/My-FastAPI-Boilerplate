from ..utils import get_only_selected_fields
from .models import GUser
from core.db import session
from sqlalchemy import select
from sqlalchemy.orm import load_only
from typing import List

async def get_users(info) -> List[GUser]:
    selected_fields = get_only_selected_fields(GUser, info)
    sql = select(GUser).options(load_only(*selected_fields)).order_by(GUser.username)
    
    result = await session.execute(sql)
    return result.scalars().all()