# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:03
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : test_get_enum_values.py
# @Software: PyCharm


import random
from enum import Enum

class Status(str, Enum):
    ACTIVE = "A"  # 活跃状态，表示用户或对象处于活跃状态，通常表示用户可以正常使用平台或功能。
    INACTIVE = "I"  # 非活跃状态，表示用户或对象处于非活跃状态，通常表示用户暂时无法使用平台或功能。
    DELETED = "D"  # 用户已删除，该用户信息将从系统中删除，不再可用。
    BLOCKED = "B"  # 被封禁状态，表示用户或对象的访问或权限已被系统管理员或监管机构暂时封禁，通常是因为违反了规则或政策。
    LOCKED = "L"  # 已锁定状态，可能是指用户账户被临时锁定，通常需要解锁后才能继续使用。
    PENDING = "P"  # 待处理状态，通常用于表示用户或对象处于等待某种处理、验证或激活的状态。

random_status = random.choice(list(Status)).value
print(random_status)