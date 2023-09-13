# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 13:43
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : social_account.py
# @Software: PyCharm

from datetime import date
from typing import Optional
from sqlalchemy import Enum as sa_enum
from sqlmodel import SQLModel, Field, Relationship, Column, Integer, String, Date
from backend.app.model.mixins import TimeMixin


# 定义第三方提供者的枚举
class ProviderEnum(sa_enum):
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
    # provider: ProviderEnum = Field(sa_column=Column("provider", sa_enum(ProviderEnum),  nullable=False, comment="第三方平台"))
    provider: str = Field(sa_column=Column("provider", String(length=50), nullable=False, comment="第三方平台"))
    provider_user_id: str = Field(sa_column=Column("provider_user_id", String(length=255), nullable=False, comment="第三方平台用户ID"))
    access_token: str = Field(sa_column=Column("access_token", String(length=255), nullable=False, comment="第三方平台用户访问令牌"))
    refresh_token: str = Field(sa_column=Column("refresh_token", String(length=255), nullable=False, comment="第三方平台用户刷新令牌"))
    expires_at: date = Field(sa_column=Column("expires_at", Date, nullable=False, comment="第三方平台用户令牌过期时间"))

    user_id: str = Field(foreign_key="users.id")

    users: Optional["Users"] = Relationship(
        sa_relationship_kwargs={'uselist': False}, back_populates="social_accounts")

    # class Config:
    #     arbitrary_types_allowed = True