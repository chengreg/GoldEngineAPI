# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 11:14
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : test_SECRET_KEY.py
# @Software: PyCharm

import secrets

secret_key = secrets.token_hex(24)
print(secret_key)