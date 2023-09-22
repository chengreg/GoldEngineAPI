# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:16
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_profile_company.py
# @Software: PyCharm

from app.model.users import UserProfileCompany
from ..base_repo import BaseRepo


class UserProfileCompanyRepository(BaseRepo):
    model = UserProfileCompany