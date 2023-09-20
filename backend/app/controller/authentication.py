# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:49
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : authentication.py
# @Software: PyCharm


from fastapi import APIRouter

# from backend.app.schema.users import RegisterSchema, LoginSchema, ForgotPasswordSchema, ResponseSchema
# from backend.app.service.auth_service import AuthService
# from backend.app.schema.register_schema import RegisterSchema
from backend.app.schema import RegisterByUsernameSchema, RegisterByPhoneNumberSchema
# from backend.app.service.register_service import register_service
from backend.app.service import register_by_username_service, register_by_phone_number_service
from backend.app.schema.response_schema import ResponseSchema

router = APIRouter(prefix="/auth", tags=['Authentication'])


@router.post("/register_username", response_model=RegisterByUsernameSchema, response_model_exclude_none=True)
async def register_username(request_body: RegisterByUsernameSchema):
    await register_by_username_service(request_body)
    return {"username": request_body.username, "hashed_password": request_body.hashed_password}


@router.post("/register_phone_number", response_model=RegisterByPhoneNumberSchema, response_model_exclude_none=True)
async def register_phone_number(request_body: RegisterByPhoneNumberSchema):
    await register_by_phone_number_service(request_body)
    return {"country_code": request_body.country_code, "phone_number": request_body.phone_number}

# @router.post("/register", response_model=RegisterSchema, response_model_exclude_none=True)
# async def register(request_body: RegisterSchema):
#     await register_service(request_body)
#     return ResponseSchema(detail="Successfully save data!")


# @router.post("/register", response_model=ResponseSchema, response_model_exclude_none=True)
# async def register(request_body: RegisterSchema):
#     await AuthService.register_service(request_body)
#     return ResponseSchema(detail="Successfully save data!")


# @router.post("/login", response_model=ResponseSchema)
# async def login(requset_body: LoginSchema):
#     token = await AuthService.logins_service(requset_body)
#     return ResponseSchema(detail="Successfully login", result={"token_type": "Bearer", "access_token": token})
#
#
# @router.post("/forgot-password", response_model=ResponseSchema, response_model_exclude_none=True)
# async def forgot_password(request_body: ForgotPasswordSchema):
#     await AuthService.forgot_password_service(request_body)
#     return ResponseSchema(detail="Successfully update data!")
