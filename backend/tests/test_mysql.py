#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：GoldEngineAPI 
@File    ：test_mysql.py
@IDE     ：PyCharm 
@Author  ：Chen GangQiang
@Date    ：2023/9/12 23:24 
"""

import pymysql

try:
    # 连接到MySQL数据库
    connection = pymysql.connect(
        host="nj-cdb-mobsmdsb.sql.tencentcdb.com",
        port=63940,
        user="root",
        password="Chen0521",
        database="test"
    )

    with connection.cursor() as cursor:
        # 执行一些数据库操作
        cursor.execute("SELECT VERSION()")
        db_version = cursor.fetchone()
        print("MySQL数据库版本:", db_version[0])

except pymysql.Error as error:
    print("连接到MySQL数据库时出错:", error)

finally:
    if connection:
        connection.close()
        print("MySQL连接已关闭")