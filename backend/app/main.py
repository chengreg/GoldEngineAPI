# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 10:53
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : main.py
# @Software: PyCharm

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.config import settings
from backend.app.db.db_postgresql_asyncpg import db


def init_app():
    # 初始化数据库
    db.init()

    # 初始化FastAPI
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
    )

    # 跨域设置
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 允许所有域名访问 #TODO: 上线时需要修改
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # 事件
    @_app.on_event("startup")
    async def startup():
        pass

    @_app.on_event("shutdown")
    async def shutdown():
        pass

    return _app


app = init_app()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host="localhost", port=8844, reload=True)
