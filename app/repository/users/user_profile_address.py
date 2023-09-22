# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:15
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_profile_address.py
# @Software: PyCharm

from app.model.users import UserProfileAddress
from ..base_repo import BaseRepo


class UserProfileAddressRepository(BaseRepo):
    model = UserProfileAddress
