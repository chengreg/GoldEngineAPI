#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：response_schema.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/21 01:30 
"""

from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')


class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None