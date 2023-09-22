# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:12
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : user_profile.py
# @Software: PyCharm

from app.models.users import UserProfile
from ..base_repo import BaseRepo


class UserProfileRepository(BaseRepo):
    model = UserProfile
