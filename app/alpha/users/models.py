from typing import Dict, Optional
from core.security.models import CryptPassword
from core.db import Base
from sqlalchemy import Column, BigInteger, String, func, DateTime
from sqlalchemy.ext.declarative import declared_attr

class User(Base):
    __tablename__ = "tb_users"

    id: Optional[int] = Column(BigInteger, primary_key=True)
    username: str = Column(String(255))
    password: str = Column(CryptPassword)

    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=func.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime,
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
    )

    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }