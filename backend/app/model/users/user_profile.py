# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 11:33
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_profile.py
# @Software: PyCharm

from datetime import date
from typing import Optional, List
from sqlalchemy import Enum, Column, String, Integer, Date
from sqlmodel import SQLModel, Field, Relationship
from backend.app.model.mixins import TimeMixin


class SexEnum(str, Enum):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"


class UserProfile(SQLModel, TimeMixin, table=True):
    """用户详情表"""
    __tablename__ = "user_profile"

    id: int = Field(sa_column=Column("id", Integer, primary_key=True, unique=True, index=True, comment="用户档案ID"))
    name: Optional[str] = Field(sa_column=Column("name", String(length=50), index=True, comment="用户姓名"))
    nickname: Optional[str] = Field(sa_column=Column("nickname", String(length=50), index=True, comment="用户昵称"))
    date_of_birth: date = Field(sa_column=Column("date_of_birth", Date, comment="出生日期"))
    # gender: SexEnum = Field(sa_column=Column("sex", Enum(SexEnum), comment="性别"))
    gender: Optional[str] = Field(sa_column=Column("gender", String(length=2), comment="性别"))
    avatar: Optional[str] = Field(sa_column=Column("avatar", String(length=255), comment="用户头像"))
    bio: Optional[str] = Field(sa_column=Column("bio", String(length=255), comment="用户简介"))
    province: Optional[str] = Field(sa_column=Column("province", String(length=50), comment="省份"))
    city: Optional[str] = Field(sa_column=Column("city", String(length=50), comment="城市"))
    country: Optional[str] = Field(sa_column=Column("country", String(length=50), comment="国家"))

    user_profile_address: List["UserProfileAddress"] = Relationship(back_populates="user_profile")
    user_profile_company: List["UserProfileCompany"] = Relationship(back_populates="user_profile")

    users: Optional["Users"] = Relationship(
        sa_relationship_kwargs={'uselist': False}, back_populates="user_profile")
