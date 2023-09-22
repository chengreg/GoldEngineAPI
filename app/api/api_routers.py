#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：api_routes.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/23 03:00 
@Desc    ：总的路由文件
"""

from fastapi import APIRouter
from .api_v1.api_v1_router import router as api_v1_router
from .api_v2.api_v2_router import router as api_v2_router

# 创建总路由文件
router = APIRouter()

# 将api_v1_router和api_v2_router注册到总路由文件中
router.include_router(api_v1_router, prefix="/v1")
router.include_router(api_v2_router, prefix="/v2")
