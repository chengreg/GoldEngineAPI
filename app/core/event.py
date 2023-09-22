#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：event.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/22 16:32 
@Desc    ：
"""

from typing import Callable
from fastapi import FastAPI
from loguru import logger

from app.db.db_mysql_aiomysql import db


def startup(app: FastAPI) -> Callable:
    async def app_startup() -> None:
        logger.info("项目启动，初始化数据库...")
        db.init()
        await db.create_all()

    return app_startup


def shutdown(app: FastAPI) -> Callable:
    async def app_shutdown() -> None:
        logger.info("项目结束，关闭数据库...")
        await db.close()

    return app_shutdown
