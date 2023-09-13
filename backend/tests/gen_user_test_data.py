#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：gen_user_test_data.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/13 00:07 
"""

import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.model import Users, UserProfile, UserProfileAddress, UserProfileCompany, SocialAccount, UserRoleLink, \
    UsersStatusEnum, SexEnum, ProviderEnum  # 请替换为你的模块名称
from backend.app.config import settings
from uuid import uuid4
from sqlalchemy.orm import Session

# 创建 Faker 实例
fake = Faker()

# 创建 SQLAlchemy 引擎和会话
DATABASE_URL = settings.MYSQL_DB  # 替换为你的数据库连接信息
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
engine = create_engine(DATABASE_URL)
session = Session(engine)

# 定义一个函数来生成测试用户数据
# def create_test_user():
#     username = fake.user_name()
#     email = fake.email()
#     hashed_password = fake.password()
#     country_code = fake.country_code()
#     phone_number = fake.phone_number()
#     status = "a"
#
#     return Users(
#         id=str(uuid4()),  # 使用uuid4生成id
#         username=username,
#         email=email,
#         hashed_password=hashed_password,
#         country_code=country_code,
#         phone_number=phone_number,
#         status=status
#     )
#
# # 指定要创建的测试用户数量
# num_users_to_create = 10  # 根据需要更改

# 创建测试数据并提交到数据库
# 将新用户添加到会话并将其提交到数据库
new_user = Users(username="john_doe", email="john@example.com", hashed_password="hashed_password_here")
session.add(new_user)
session.commit()

print(f"Successfully created and inserted 1 test users and related data.")
