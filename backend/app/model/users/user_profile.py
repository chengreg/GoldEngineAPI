# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 11:33
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_profile.py
# @Software: PyCharm

from datetime import date
from typing import Optional, List
from sqlalchemy import Enum
from sqlmodel import SQLModel, Field, Relationship
from backend.app.model.mixins import TimeMixin


class Sex(str, Enum):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"


class UserProfile(SQLModel, TimeMixin, table=True):
    __tablename__ = "user_profile"

    id: Optional[int] = Field(default="autoincrement", primary_key=True)
    name: str
    nickname: str
    date_of_birth: date
    gender: Sex
    avatar: str
    bio: str

    province: str
    city: str
    country: str

    #user_profile_address_id: Optional[int] = Field(None, foreign_key="user_profile_address.id")
    # user_profile_address: Optional["UserProfileAddress"] = Relationship(back_populates="user_profile")
    user_profile_address: List["UserProfileAddress"] = Relationship(back_populates="user_profile")

    #user_profile_company_id: Optional[int] = Field(None, foreign_key="user_profile_company.id")
    # user_profile_company: Optional["UserProfileCompany"] = Relationship(back_populates="user_profile")
    user_profile_company: List["UserProfileCompany"] = Relationship(back_populates="user_profile")

    users: Optional["Users"] = Relationship(
        sa_relationship_kwargs={'uselist': False}, back_populates="user_profile")
