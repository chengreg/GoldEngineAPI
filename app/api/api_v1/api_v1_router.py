#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：api_v1_router.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/23 03:07 
@Desc    ：api_v1的路由文件
"""

from fastapi import APIRouter
from .users import router as users_router

router = APIRouter()

# 将users_router注册到api_v1_router中
router.include_router(users_router, prefix="/users", tags=['Users'])
