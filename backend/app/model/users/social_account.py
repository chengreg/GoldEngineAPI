# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 13:43
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : social_account.py
# @Software: PyCharm

from datetime import date
from typing import Optional
from sqlalchemy import Enum
from sqlmodel import SQLModel, Field, Relationship
from backend.app.model.mixins import TimeMixin


# 定义第三方提供者的枚举
class ProviderEnum(str, Enum):
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

    id: Optional[int] = Field(default="autoincrement", primary_key=True)
    user_id: str = Field(foreign_key="users.id")
    provider: ProviderEnum
    provider_user_id: str
    access_token: str
    refresh_token: str
    expires_at: date

    users: Optional["Users"] = Relationship(
        sa_relationship_kwargs={'uselist': False}, back_populates="social_account")