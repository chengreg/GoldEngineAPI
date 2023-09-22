#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：test_python-decouple.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/21 00:00 
"""

from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY', default='defaultsecretkey')
DATABASE_URL = config('DATABASE_URL')

print(DEBUG)
print(SECRET_KEY)
print(DATABASE_URL)