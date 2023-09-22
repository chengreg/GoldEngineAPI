# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:16
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_role.py
# @Software: PyCharm


from app.model.users import UserRole
from ..base_repo import BaseRepo


class UserRoleRepository(BaseRepo):
    model = UserRole