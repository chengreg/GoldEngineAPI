# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 14:59
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_profile_address.py
# @Software: PyCharm

from typing import Optional
from sqlmodel import SQLModel, Field, Relationship, Column, Integer, String
from app.models.users import TimeMixin


class UserProfileAddress(SQLModel, TimeMixin, table=True):
    __tablename__ = "user_profile_address"

    id: int = Field(sa_column=Column("id", Integer, primary_key=True, unique=True, index=True, comment="用户地址ID"))
    street: str = Field(sa_column=Column("street", String(length=255), comment="街道"))
    city: str = Field(sa_column=Column("city", String(length=50), comment="城市"))
    state: str = Field(sa_column=Column("state", String(length=50), comment="省份"))
    postal_code: str = Field(sa_column=Column("postal_code", String(length=20), comment="邮政编码"))
    country: str = Field(sa_column=Column("country", String(length=50), comment="国家"))

    user_profile_id: int = Field(foreign_key="user_profile.id")

    user_profile: Optional["UserProfile"] = Relationship(back_populates="user_profile_address")
    # user_profile: Optional["UserProfile"] = Relationship(
    #     sa_relationship_kwargs={'uselist': False}, back_populates="user_profile_address")