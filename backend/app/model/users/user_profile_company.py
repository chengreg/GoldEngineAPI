# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 15:35
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_profile_company.py
# @Software: PyCharm

from typing import Optional
from sqlmodel import SQLModel, Field, Relationship, Integer, Column, String
from backend.app.model.users import TimeMixin


class UserProfileCompany(SQLModel, TimeMixin, table=True):
    __tablename__ = "user_profile_company"

    id: int = Field(sa_column=Column("id", Integer, primary_key=True, unique=True, index=True, comment="用户公司ID"))
    name: str = Field(sa_column=Column("name", String(length=255), comment="公司名称"))
    address: str = Field(sa_column=Column("address", String(length=255), comment="公司地址"))
    phone_number: str = Field(sa_column=Column("phone_number", String(length=20), comment="公司电话"))

    user_profile_id: int = Field(foreign_key="user_profile.id")

    user_profile: Optional["UserProfile"] = Relationship(back_populates="user_profile_companies")