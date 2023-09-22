# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 10:53
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : main.py
# @Software: PyCharm

from app.app import app

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host="localhost", port=8844, reload=True)
