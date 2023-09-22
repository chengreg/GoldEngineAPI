#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：permission.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/23 01:50 
@Desc    ：
"""
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from app.models.users import TimeMixin
from sqlalchemy import Column, Integer, String


class Permission(SQLModel, TimeMixin, table=True):
    __tablename__ = "permission"

    id: int = Field(sa_column=Column("id", Integer, primary_key=True, unique=True, index=True, comment="权限ID"))
    name: str = Field(
        sa_column=Column("name", String(length=50), unique=True, nullable=False, index=True, comment="权限名称"))
    description: Optional[str] = Field(sa_column=Column("description", String(length=255), comment="权限描述"))

    roles: List["RolePermissionLink"] = Relationship(back_populates="permission")
