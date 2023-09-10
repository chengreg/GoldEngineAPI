# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 11:33
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_profile.py
# @Software: PyCharm

from datetime import date
from typing import Optional
from sqlalchemy import Enum
from sqlmodel import SQLModel, Field, Relationship
from .mixins import TimeMixin


class Sex(str, Enum):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"


class UserProfile(SQLModel, TimeMixin, table=True):
    __tablename__ = "user_profile"

    id: Optional[str] = Field(default=None, primary_key=True, nullable=False)
    name: str
    date_of_birth: date
    gender: Sex
    avatar: str
    bio: str

    users: Optional["Users"] = Relationship(
        sa_relationship_kwargs={'uselist': False}, back_populates="user_profile")


