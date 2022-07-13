#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil

while True:
    cpu_res = psutil.cpu_percent(interval=1)
    print(cpu_res)