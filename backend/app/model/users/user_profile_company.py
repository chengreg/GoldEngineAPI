# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 15:35
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_profile_company.py
# @Software: PyCharm

from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from backend.app.model.mixins import TimeMixin


class UserProfileCompany(SQLModel, TimeMixin, table=True):
    __tablename__ = "user_profile_company"

    id: Optional[int] = Field(default="autoincrement", primary_key=True)
    name: str
    address: str
    phone_number: str

    user_profile_id: int = Field(foreign_key="user_profile.id")

    user_profile: Optional["UserProfile"] = Relationship(
        sa_relationship_kwargs={'uselist': False}, back_populates="user_profile_company")