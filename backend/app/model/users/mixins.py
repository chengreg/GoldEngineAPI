# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 11:18
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : mixins.py
# @Software: PyCharm

from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, DateTime
from sqlmodel import Field


class TimeMixin(BaseModel):
    """Mxin to for datetime value of when the entity was created and when it was last modified. """

    # created_at: datetime = Field(default_factory=datetime.now)
    # modified_at: datetime = Field(sa_column=Column(DateTime, default=datetime.now,
    #                                                onupdate=datetime.now, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime, default=datetime.now))
    modified_at: datetime = Field(
        sa_column=Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False))
