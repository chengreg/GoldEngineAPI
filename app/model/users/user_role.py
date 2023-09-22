# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 12:49
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_role.py
# @Software: PyCharm

from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from app.model.users import TimeMixin
from sqlalchemy import Column, Integer, String


class UserRole(SQLModel, TimeMixin, table=True):
    __tablename__ = "user_role"

    id: int = Field(sa_column=Column("id", Integer, primary_key=True, unique=True, index=True, comment="角色ID"))
    name: str = Field(sa_column=Column("name", String(length=50), unique=True, nullable=False, index=True, comment="角色名称"))
    description: Optional[str] = Field(sa_column=Column("description", String(length=255), comment="角色描述"))

    users: List["UserRoleLink"] = Relationship(back_populates="role")
    permissions: List["RolePermissionLink"] = Relationship(back_populates="role")

