#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/28 17:57 PM
# @Author : 夏见。
# @File : dbUtil.py

import logging

import pymysql

from common.get_env import get_env


class DBUtil:

    def __init__(self, user, passwd, host, port, database):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.database = database
        self.conn = self.get_connection()
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)  # TODO 括号里的是干嘛的呀？

    def get_connection(self):
        return pymysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            port=self.port,
            database=self.database
        )

    def read_db(self, sql, fetch="all", desc="one仅返回一条数据，all返回全部数据，默认返回all数据"):
        self.cursor.execute(sql)
        if fetch == "all":
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def write_db(self, sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 向数据库提交
            self.conn.commit()
            logging.info(f"sql执行完毕,影响行数{self.cursor.rowcount}")
        except:
            # 发生错误时回滚
            self.conn.rollback()
            logging.error(f"sql执行失败！sql={sql}")

    def __del__(self):
        self.conn.close()
        self.cursor.close()


if __name__ == '__main__':
    from common.utils import init_log_config

    init_log_config()
    db_server = get_env(env="local", sections="db", parameter="server")
    db_user = get_env(env="local", sections="db", parameter="user")
    db_port = int(get_env(env="local", sections="db", parameter="port"))
    db_password = get_env(env="local", sections="db", parameter="password")

    # print(db_server, db_user, db_password, db_port)
    mysql = DBUtil(db_user, db_password, db_server, db_port, 'books')
    # mysql = DBUtil('root', 'Lemon123456!', 'api.mypeng.site', 3305, 'books')
    sql = "select * from t_book limit 1;"
    result = mysql.read_db(sql)
    print("select查询返回数据：", result)
    print("**" * 70)
    updatesql = 'update t_hero set name="山上有座庙" where id > 55'
    mysql.write_db(updatesql)
