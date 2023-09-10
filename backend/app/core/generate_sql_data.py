# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:22
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : generate_sql_data.py
# @Software: PyCharm


from backend.app.repository.users.role import RoleRepository
from backend.app.model.users import Role


# Generate roles manually
async def generate_role():
    _role = await RoleRepository.find_by_list_role_name(["admin", "user"])
    if not _role:
        await RoleRepository.create_list(
            [Role(id=1, role_name="admin"), Role(id=2, role_name="user")])
