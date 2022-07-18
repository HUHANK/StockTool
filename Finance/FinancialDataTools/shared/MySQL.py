#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/1821:19
# @File     : MySQL.py
# @Project  : Finance

import pymysql, traceback

class MySQL:
    def __init__(self, host, db, user, pwd):
        self.connection = None
        self.cursor = None
        self.Host = host
        self.DB = db
        self.User = user
        self.Pwd = pwd
        self.connect()

    def __del__(self):
        self.close()

    def close(self) -> None:
        if self.connection is not None:
            self.connection.close()

    def connect(self) -> bool:
        if self.connection is not None:
            self.close()

        self.connection = pymysql.connect(
            user=self.User, password=self.Pwd,
            host=self.Host, port=3306,
            db=self.DB, charset='utf8'
        )
        if self.connection.open:
            print('DB connect successed!')
            return True
        else:
            return False

    def commit(self) -> None:
        self.connection.commit()

    def select(self, sql):
        if self.cursor is not None:
            self.cursor.close()
        self.cursor = self.connection.cursor(cursor=pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        ret = self.cursor.fetchall()
        self.cursor.close()
        self.cursor = None
        return ret

    def batchInsert(self, sql, datas):
        if self.cursor is None:
            self.cursor = self.connection.cursor()
        ret = self.cursor.executemany(sql, datas)
        self.commit()
        return ret

    def execUpdate(self, sql):
        ret = False
        if self.cursor is None:
            self.cursor = self.connection.cursor()
        try:
            ret = self.cursor.execute(sql)
            self.commit()
            ret = True
        except:
            print(traceback.format_exc())
        return ret


# def test():
#     db = MySQL("172.31.114.22", "STK", "root", "123456")
#
# test()