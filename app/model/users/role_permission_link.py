#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：role_permission_link.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/23 01:51 
@Desc    ：
"""

from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from app.model.users import TimeMixin


class RolePermissionLink(SQLModel, TimeMixin, table=True):
    __tablename__ = "role_permission_link"

    role_id: Optional[int] = Field(default=None, foreign_key="user_role.id", primary_key=True)
    permission_id: Optional[int] = Field(default=None, foreign_key="permission.id", primary_key=True)

    role: "UserRole" = Relationship(back_populates="permissions")
    permission: "Permission" = Relationship(back_populates="roles")