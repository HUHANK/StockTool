#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/12 19:16
# @Author : HuYouLiang
# @File : test1.py
# @Purpose :
import os
import shutil


for root, dirs, files in os.walk(r"N:\boost\x64\lib"):
    for file in files:
        if (not file.startswith("lib")) and (file.endswith(".lib")):
            fpath = os.path.join(root, file)
            fpath2 = os.path.join(root, "lib"+file);
            shutil.copy(fpath, fpath2);
            print (fpath2)
