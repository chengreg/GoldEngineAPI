#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：app.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/22 16:17 
@Desc    ：
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.core import startup, shutdown
from app.controller.authentication import router as authentication_router

# 实例化fastapi
app = FastAPI(debug=settings.DEBUG, title=settings.TITLE, version=settings.VERSION, description=settings.DESCRIPTION)


# 事件监听
app.add_event_handler("startup", startup(app))
app.add_event_handler("shutdown", shutdown(app))

# 路由
app.include_router(authentication_router)

# 跨域设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名访问 #TODO: 上线时需要修改
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)