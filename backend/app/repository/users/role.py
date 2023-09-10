# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:14
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : role.py
# @Software: PyCharm

from typing import List
from ..base_repo import BaseRepo
from backend.app.model.users import Role
from sqlalchemy.future import select
from backend.app.db.db_postgresql_asyncpg import db, commit_rollback


class RoleRepository(BaseRepo):
    model = Role

    @staticmethod
    async def find_by_role_name(role_name: str):
        query = select(Role).where(Role.role_name == role_name)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def find_by_list_role_name(role_name: List[str]):
        query = select(Role).where(Role.role_name.in_(role_name))
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def create_list(role_name: List[Role]):
        db.add_all(role_name)
        await commit_rollback()