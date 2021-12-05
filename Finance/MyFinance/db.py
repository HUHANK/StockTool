#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 16:13
# @Author : HuYouLiang
# @File : db.py.py
# @Purpose :

from config import *
import  pymysql, traceback

class CMySQL:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect()

    def __del__(self):
        self.close()

    def close(self):
        if self.connection is not None:
            self.connection.close()

    def connect(self):
        if self.connection is not None:
            self.close()
        self.connection = pymysql.connect(
            user=MYSQL_USER, password=MYSQL_PWD,
            host=MYSQL_HOST, port=MYSQL_PORT,
            db=MYSQL_DB, charset='utf8'
        )
        if self.connection.open :
            return True
        else:
            return False

    def commit(self):
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

