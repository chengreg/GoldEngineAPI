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
# from enum import Enum

from backend.app.model.mixins import TimeMixin
from .user_role import UserRole

from sqlalchemy.orm import relationship


class UsersStatusEnum(str, Enum):
    ACTIVE = "A"  # 活跃状态，表示用户或对象处于活跃状态，通常表示用户可以正常使用平台或功能。
    INACTIVE = "I"  # 非活跃状态，表示用户或对象处于非活跃状态，通常表示用户暂时无法使用平台或功能。
    DELETED = "D"  # 用户已删除，该用户信息将从系统中删除，不再可用。
    BLOCKED = "B"  # 被封禁状态，表示用户或对象的访问或权限已被系统管理员或监管机构暂时封禁，通常是因为违反了规则或政策
    LOCKED = "L"  # 已锁定状态，可能是指用户账户被临时锁定，通常需要解锁后才能继续使用。
    PENDING = "P"  # 待处理状态，通常用于表示用户或对象处于等待某种处理、验证或激活的状态。


class Users(SQLModel, TimeMixin, table=True):
    """
    用户表: 用于存储用户的基本信息
    primary_key: 主键
    unique: 唯一
    index: 索引
    nullable: 可空
    comment: 注释
    Optional: 可选
    """
    __tablename__ = "users"

    id: str = Field(sa_column=Column("id", String(length=128), primary_key=True, unique=True, index=True, comment="用户ID"))
    username: str = Field(sa_column=Column("username", String(length=50), unique=True, nullable=False, index=True, comment="用户名"))
    email: Optional[str] = Field(sa_column=Column("email", String(length=254), unique=True, nullable=True, index=True, comment="用户邮箱"))
    hashed_password: str = Field(sa_column=Column("hashed_password", String(length=128), nullable=False, comment="用户密码"))
    country_code: Optional[str] = Field(sa_column=Column("country_code", String(length=10), nullable=False, comment="国家代码"))
    phone_number: Optional[str] = Field(sa_column=Column("phone_number", String(length=20), nullable=False, comment="手机号码"))
    # todo: 通过枚举来定义用户状态有bug未解决，先用str代替
    # status: UsersStatusEnum = Field(sa_column=Column("status", Enum(UsersStatusEnum), nullable=False, comment="用户状态"))
    status: str = Field(sa_column=Column("status", String(length=10), nullable=False, comment="用户状态"))

    user_profile_id: Optional[int] = Field(None, foreign_key="user_profile.id")

    user_profile: Optional["UserProfile"] = Relationship(back_populates="users")
    user_role: Optional[UserRole] = Relationship(back_populates="users")
    social_accounts: List["SocialAccount"] = Relationship(back_populates="users")

    # social_accounts: List["SocialAccount"] = relationship("SocialAccount", back_populates="user")

    __table_args__ = (UniqueConstraint('country_code', 'phone_number', name='uq_countrycode_phonenumber'),)
