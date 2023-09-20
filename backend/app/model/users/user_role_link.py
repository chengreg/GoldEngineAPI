# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 12:48
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : role.py
# @Software: PyCharm

from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from backend.app.model.users import TimeMixin


class UserRoleLink(SQLModel, TimeMixin, table=True):
    __tablename__ = "user_role_link"

    users_id: Optional[str] = Field(default=None, foreign_key="users.id", primary_key=True)
    role_id: Optional[int] = Field(default=None, foreign_key="user_role.id", primary_key=True)

    user: "Users" = Relationship(back_populates="user_roles")
    role: "UserRole" = Relationship(back_populates="users")
