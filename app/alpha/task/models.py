from email.policy import default
from sqlalchemy import Column, String, BigInteger, DateTime, func
from sqlalchemy.ext.declarative import declared_attr

from core.db import Base
# from core.db.mixins import TimestampMixin


class Task(Base):
    __tablename__ = "tb_tasks"

    id = Column(BigInteger, primary_key=True, autoincrement='ignore_fk')
    name = Column(String(255), nullable=True)
    user_id = Column(BigInteger, nullable=False, default=1)

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