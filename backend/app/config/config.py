# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 11:01
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : config.py
# @Software: PyCharm

import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    # 项目配置
    PROJECT_NAME: str = "GoldEngine API"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "GoldEngine API"

    # token配置
    SECRET_KEY: str = secrets.token_hex(24)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
