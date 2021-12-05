#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/29 22:47
# @Author : HuYouLiang
# @File : FileOpt.py
# @Purpose :

import os

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    if not os.path.exists(path):
        os.makedirs(path)
