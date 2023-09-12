# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 12:49
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_role.py
# @Software: PyCharm

from typing import Optional
from sqlmodel import SQLModel, Field, JSON as sq_Json, Relationship
from backend.app.model.mixins import TimeMixin
from sqlalchemy import Column, Integer, String


class UserRole(SQLModel, TimeMixin, table=True):
    __tablename__ = "user_role"

    id: int = Field(sa_column=Column("id", Integer, primary_key=True, unique=True, index=True, comment="用户权限ID"))
    name: str = Field(sa_column=Column("name", String(length=50), unique=True, nullable=False, index=True, comment="用户权限名称"))
    description: Optional[str] = Field(sa_column=Column("description", String(length=255), comment="用户权限描述"))
    permission: str = Field(sa_column=Column("permission", String(length=255), comment="用户权限"))

    users: Optional["Users"] = Relationship(back_populates="roles")


# # 示例用法
# role_data = {
#     "role_name": "管理员",
#     "description": "具有管理员权限",
#     "permissions": {
#         "can_view_dashboard": True,
#         "can_edit_profile": True,
#         "can_create_post": True,
#         "can_delete_post": True,
#         "can_approve_comments": True,
#         "can_manage_users": True
#     }
# }