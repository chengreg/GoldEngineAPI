# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 13:43
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : social_account.py
# @Software: PyCharm

from datetime import datetime
from typing import Optional
from sqlalchemy import Enum as saEnum
from enum import Enum as pyEnum
from sqlmodel import SQLModel, Field, Relationship, Column, Integer, String, DateTime
from app.model.users import TimeMixin
from sqlalchemy.schema import UniqueConstraint


# 定义第三方提供者的枚举
class ProviderEnum(pyEnum):
    GOOGLE = "Google"
    FACEBOOK = "Facebook"
    TWITTER = "Twitter"
    GITHUB = "Github"
    LINKEDIN = "Linkedin"
    WEIBO = "Weibo"
    WEIXIN = "Weixin"
    QQ = "QQ"
    ALIPAY = "Alipay"


class SocialAccount(SQLModel, TimeMixin, table=True):
    __tablename__ = "social_account"

    id: int = Field(sa_column=Column("id", Integer, primary_key=True, unique=True, index=True, comment="用户社交ID"))
    provider: ProviderEnum = Field(
        sa_column=Column("provider", saEnum(ProviderEnum), nullable=False, comment="第三方平台"))
    provider_user_id: str = Field(
        sa_column=Column("provider_user_id", String(length=255), nullable=False, comment="第三方平台用户ID"))
    access_token: str = Field(
        sa_column=Column("access_token", String(length=255), nullable=False, comment="第三方平台用户访问令牌"))
    refresh_token: str = Field(
        sa_column=Column("refresh_token", String(length=255), nullable=False, comment="第三方平台用户刷新令牌"))

    # 使用DateTime代替Date以精确到时间
    expires_at: datetime = Field(
        sa_column=Column("expires_at", DateTime, nullable=False, comment="第三方平台用户令牌过期时间"))

    user_id: str = Field(foreign_key="users.id")

    users: Optional["Users"] = Relationship(back_populates="social_accounts")

    # 每个用户对于每个社交帐号只有一个唯一的记录
    __table_args__ = (UniqueConstraint('user_id', 'provider'),)