# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:10
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : users.py
# @Software: PyCharm

from sqlalchemy import update as sql_update
from sqlalchemy.future import select


from app.db.db_mysql_aiomysql import db, commit_rollback

from app.models.users.users import Users
from ..base_repo import BaseRepo


class UsersRepository(BaseRepo):
    model = Users

    @staticmethod
    async def find_by_username(username: str):
        query = select(Users).where(Users.username == username)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def find_by_email(email: str):
        query = select(Users).where(Users.email == email)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def update_password(email: str, password: str):
        query = sql_update(Users).where(Users.email == email).values(
            password=password).execution_options(synchronize_session="fetch")
        await db.execute(query)
        await commit_rollback()

    @staticmethod
    async def find_by_phone_number(phone_number: str):
        query = select(Users).where(Users.phone_number == phone_number)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def find_by_country_code_and_phone_number(country_code: str, phone_number: str):
        query = select(Users).where(Users.country_code == country_code, Users.phone_number == phone_number)
        return (await db.execute(query)).scalar_one_or_none()