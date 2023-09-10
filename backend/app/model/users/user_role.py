# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 12:49
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_role.py
# @Software: PyCharm

from typing import Optional
from sqlmodel import SQLModel, Field
from backend.app.model.mixins import TimeMixin


class UserRole(SQLModel,TimeMixin,table=True):
    __tablename__= "user_role"

    users_id: Optional[str] = Field(default=None, foreign_key="users.id",primary_key=True)
    role_id: Optional[int] = Field(default=None, foreign_key="role.id",primary_key=True)
