# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:15
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : social_account.py
# @Software: PyCharm

from backend.app.model.users import SocialAccount
from ..base_repo import BaseRepo


class SocialAccountRepository(BaseRepo):
    model = SocialAccount
