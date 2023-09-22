#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：register_schema.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/21 01:09 
"""

import logging
import re
from pydantic import BaseModel, validator
# from fastapi import HTTPException

logger = logging.getLogger(__name__)


class RegisterByUsernameSchema(BaseModel):
    username: str
    hashed_password: str


class RegisterByPhoneNumberSchema(BaseModel):
    country_code: str
    phone_number: str
    hashed_password: str

    @validator("phone_number")
    def phone_validation(cls, v):
        logger.debug(f"phone in validator: {v}")

        # regex phone number
        regex = r"^\d{1,20}$"  # 暂时使用：只包含数字、最多20位。
        if v and not re.search(regex, v, re.I):
            raise ValueError("Invalid input phone number!")
        return v

#
# class RegisterSchema(BaseModel):
#     username: str
#     email: str
#     hashed_password: str
#     country_code: str
#     phone_number: str
#     status: UsersStatusEnum
#
#     @validator("phone_number")
#     def phone_validation(cls, v):
#         logger.debug(f"phone in validator: {v}")
#
#         # regex phone number
#         regex = r"^\d{1,20}$"  # 暂时使用：只包含数字、最多20位。
#         if v and not re.search(regex, v, re.I):
#             raise ValueError("Invalid input phone number!")
#         return v

    # # Sex validation
    # @validator("status")
    # def status_validation(cls, v):
    #     if hasattr(UsersStatusEnum, v) is False:
    #         raise HTTPException(status_code=400, detail="Invalid input status")
    #     return v
