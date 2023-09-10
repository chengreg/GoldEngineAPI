# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:49
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : authentication.py
# @Software: PyCharm


from fastapi import APIRouter

from backend.app.schema.users import RegisterSchema, LoginSchema, ForgotPasswordSchema, ResponseSchema
from app.service.auth_service import AuthService
from backend.app.service.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=['Authentication'])


@router.post("/register", response_model=ResponseSchema, response_model_exclude_none=True)
async def register(request_body: RegisterSchema):
    await AuthService.register_service(request_body)
    return ResponseSchema(detail="Successfully save data!")


@router.post("/login", response_model=ResponseSchema)
async def login(requset_body: LoginSchema):
    token = await AuthService.logins_service(requset_body)
    return ResponseSchema(detail="Successfully login", result={"token_type": "Bearer", "access_token": token})


@router.post("/forgot-password", response_model=ResponseSchema, response_model_exclude_none=True)
async def forgot_password(request_body: ForgotPasswordSchema):
    await AuthService.forgot_password_service(request_body)
    return ResponseSchema(detail="Successfully update data!")