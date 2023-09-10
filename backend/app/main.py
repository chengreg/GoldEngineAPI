# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 10:53
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : main.py
# @Software: PyCharm

from fastapi import FastAPI


def init_app():
    app = FastAPI()

    @app.on_event("startup")
    async def startup():
        pass

    @app.on_event("shutdown")
    async def shutdown():
        pass

    return app


app = init_app()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="localhost", port=8844, reload=True)
