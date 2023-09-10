# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 16:30
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : generate_test_sql_data.py
# @Software: PyCharm


from backend.app.model.users import Role, SocialAccount, UserProfile, UserRole, Users, UserProfileAddress, \
    UserProfileCompany, Status, ProviderEnum
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import random
from sqlmodel import SQLModel

# 设置数据库连接
DATABASE_URL = "postgresql+asyncpg://root:Chen0521@43.137.2.28:5432/test05"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(bind=engine, class_=AsyncSession)

fake = Faker()


async def generate_and_insert_users(num=20):
    async with async_session() as session:
        for _ in range(num):
            user = Users(
                id=fake.uuid4(),
                username=fake.unique.user_name(),
                email=fake.unique.email(),
                hashed_password=fake.password(),
                country_code=fake.country_code(),
                phone_number=fake.unique.phone_number(),
                status="A"
            )
            session.add(user)
        await session.commit()


# 创建表格 (仅运行一次)
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


# 运行函数来创建表格和添加测试数据
import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(create_tables())  # 仅运行一次
loop.run_until_complete(generate_and_insert_users())
