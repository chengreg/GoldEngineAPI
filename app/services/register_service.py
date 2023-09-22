#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：register.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/21 01:02 
"""

from datetime import datetime, timedelta
from fastapi import HTTPException
from uuid import uuid4
from passlib.context import CryptContext
from jose import JWTError, jwt

from app.models.users.users import Users
from app.schemas.register_schema import RegisterByUsernameSchema, RegisterByPhoneNumberSchema
from app.repositories.users.users import UsersRepository
from app.config import settings

# Encrypt password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def register_by_username_service(register: RegisterByUsernameSchema):
    _user_id = str(uuid4())

    _users = Users(id=_user_id,
                   username=register.username,
                   hashed_password=pwd_context.hash(register.hashed_password), )

    # Checking the same username
    _username = await UsersRepository.find_by_username(register.username)
    if _username:
        raise HTTPException(status_code=400, detail="Username already exists!")
    else:
        #  insert to tables
        await UsersRepository.create(**_users.dict())


async def register_by_phone_number_service(register: RegisterByPhoneNumberSchema):
    _user_id = str(uuid4())

    _users = Users(id=_user_id,
                   country_code=register.country_code,
                   phone_number=register.phone_number, )

    # Checking the same username
    _full_phone_number = register.country_code + register.phone_number
    _full_phone_number = await UsersRepository.find_by_country_code_and_phone_number(register.country_code,
                                                                                     register.phone_number)
    if _full_phone_number:
        raise HTTPException(status_code=400, detail="phone_number already exists!")
    else:
        #  insert to tables
        await UsersRepository.create(**_users.dict())
