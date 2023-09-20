# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:49
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : authentication.py
# @Software: PyCharm


from fastapi import APIRouter

from backend.app.schema import RegisterByUsernameSchema, RegisterByPhoneNumberSchema
from backend.app.service import register_by_username_service, register_by_phone_number_service

router = APIRouter(prefix="/auth", tags=['Authentication'])


@router.post("/register_username", response_model=RegisterByUsernameSchema, response_model_exclude_none=True)
async def register_username(request_body: RegisterByUsernameSchema):
    await register_by_username_service(request_body)
    return {"username": request_body.username, "hashed_password": request_body.hashed_password}


@router.post("/register_phone_number", response_model=RegisterByPhoneNumberSchema, response_model_exclude_none=True)
async def register_phone_number(request_body: RegisterByPhoneNumberSchema):
    await register_by_phone_number_service(request_body)
    return {"country_code": request_body.country_code, "phone_number": request_body.phone_number}


