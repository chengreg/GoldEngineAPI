#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：gen_user_test_data.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/13 00:07 
"""

from faker import Faker
from uuid import uuid4
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session
from app.model.users.users import Users

# ...  (此处省略了前面的代码，您已经提供的部分...)

TX_MYSQL_URL = "mysql+pymysql://root:Chen0521@nj-cdb-mobsmdsb.sql.tencentcdb.com:63940/test?charset=utf8mb4"
LOCAL_MYSQL_URL = "mysql+pymysql://root:root@127.0.0.1/test01"

engine = create_engine(LOCAL_MYSQL_URL, echo=True)
fake = Faker()


def create_database():
    # This will create tables in the database (equivalent to "CREATE TABLE ...")
    SQLModel.metadata.create_all(engine)


def add_user():
    # Create a new user
    username = fake.user_name()
    hashed_password = fake.password(length=12)
    new_user = Users(id=str(uuid4()), username=username, hashed_password=hashed_password)

    # Start a session, add the new user and commit the transaction
    with Session(engine) as session:
        session.add(new_user)
        session.commit()


# This is a simple check to see if the script is being run directly
if __name__ == "__main__":
    create_database()

    for i in range(10):
        add_user()