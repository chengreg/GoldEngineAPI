# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 12:48
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : role.py
# @Software: PyCharm

from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field
from .mixins import TimeMixin
from .user_role import UserRole


class Role(SQLModel, TimeMixin, table=True):
    __tablename__ = "role"

    id: Optional[str] = Field(None, primary_key=True, nullable=True)
    role_name: str

    users: List["Users"] = Relationship(back_populates="roles", link_model=UserRole)
