# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 17:45
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : auth_repo.py
# @Software: PyCharm


from datetime import datetime, timedelta
from typing import Optional
from jose import jwt

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from backend.app.config import settings


class JWTRepo:

    def __init__(self, data: dict = {}, token: str = None):
        self.data = data
        self.token = token

    def generate_token(self, expires_delta: Optional[timedelta] = None):
        to_encode = self.data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

        return encode_jwt

    def decode_token(self):
        try:
            decode_token = jwt.decode(
                self.token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            return decode_token if decode_token["expires"] >= datetime.time() else None
        except:
            return {}

    @staticmethod
    def extract_token(token: str):
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])


class JWTBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail={"status": "Forbidden", "message": "Invalid authentication schema."})
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail={"status": "Forbidden", "message": "Invalid token or expired token."})
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail={"status": "Forbidden", "message": "Invalid authorization code."})

    @staticmethod
    def verify_jwt(jwt_token: str):
        return True if jwt.decode(jwt_token, settings.SECRET_KEY,
                                  algorithms=[settings.ALGORITHM]) is not None else False