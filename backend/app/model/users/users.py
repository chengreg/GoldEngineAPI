# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 12:04
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : users.py
# @Software: PyCharm

from typing import List, Optional
from sqlalchemy import Column, String, UniqueConstraint
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Enum

from backend.app.model.mixins import TimeMixin
from .user_role import UserRole


class Status(str, Enum):
    ACTIVE = "A"  # 活跃状态，表示用户或对象处于活跃状态，通常表示用户可以正常使用平台或功能。
    INACTIVE = "I"  # 非活跃状态，表示用户或对象处于非活跃状态，通常表示用户暂时无法使用平台或功能。
    DELETED = "D"  # 用户已删除，该用户信息将从系统中删除，不再可用。
    BLOCKED = "B"  # 被封禁状态，表示用户或对象的访问或权限已被系统管理员或监管机构暂时封禁，通常是因为违反了规则或政策
    LOCKED = "L"  # 已锁定状态，可能是指用户账户被临时锁定，通常需要解锁后才能继续使用。
    PENDING = "P"  # 待处理状态，通常用于表示用户或对象处于等待某种处理、验证或激活的状态。


class Users(SQLModel, TimeMixin, table=True):
    __tablename__ = "users"

    id: Optional[str] = Field(None, primary_key=True, nullable=False)
    username: str = Field(sa_column=Column("username", String, unique=True))
    email: str = Field(sa_column=Column("email", String, unique=True))
    hashed_password: str = Field(sa_column=Column("hashed_password", String))

    country_code: str
    phone_number: str

    status: Status

    user_profile_id: Optional[int] = Field(None, foreign_key="user_profile.id")
    user_profile: Optional["UserProfile"] = Relationship(back_populates="users")

    roles: List["Role"] = Relationship(back_populates="users", link_model=UserRole)

    social_accounts: List["SocialAccount"] = Relationship(back_populates="users")

    __table_args__ = (UniqueConstraint('country_code', 'phone_number', name='uq_countrycode_phonenumber'),)
