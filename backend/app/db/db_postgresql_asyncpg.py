# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 11:00
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : db_postgresql_asyncpg.py
# @Software: PyCharm

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from backend.app.config import settings


class AsyncDatabaseSession:

    def __init__(self) -> None:
        self.session = None
        self.engine = None

    def __getattr__(self, name):
        return getattr(self.session, name)

    def init(self):
        self.engine = create_async_engine(settings.POSTGRESQL_DB, future=True, echo=True)
        self.session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)()


    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)


db = AsyncDatabaseSession()


async def commit_rollback():
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
