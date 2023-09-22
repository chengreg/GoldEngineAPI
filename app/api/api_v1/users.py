#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：users.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/23 03:05 
@Desc    ：和用户相关的接口
"""
from fastapi import APIRouter

from app.schemas import RegisterByUsernameSchema, RegisterByPhoneNumberSchema
from app.services import register_by_username_service, register_by_phone_number_service

router = APIRouter()


@router.post("/register_username", response_model=RegisterByUsernameSchema, response_model_exclude_none=True)
async def register_username(request_body: RegisterByUsernameSchema):
    """
    使用用户名注册
    """
    await register_by_username_service(request_body)
    return {"username": request_body.username, "hashed_password": request_body.hashed_password}


@router.post("/register_phone_number", response_model=RegisterByPhoneNumberSchema, response_model_exclude_none=True)
async def register_phone_number(request_body: RegisterByPhoneNumberSchema):
    """
    使用手机号注册
    """
    await register_by_phone_number_service(request_body)
    return {"country_code": request_body.country_code, "phone_number": request_body.phone_number}
