#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/28 22:32
# @Author : HuYouLiang
# @File : CProcess.py
# @Purpose :

from abc import ABCMeta, abstractmethod
from multiprocessing import Process, Queue
import os

class CProcess:
    __metaclass__ = ABCMeta
    def __init__(self):
        self.process = None

    def __del__(self):
        # self.stop()
        pass

    @abstractmethod
    def run(self):
        print("CProcess PID: %s" % os.getpid())

    def start(self):
        self.process = Process(target=self.run, args=())
        self.process.start()

    def stop(self):
        try:
            if self.process.is_alive():
                self.process.kill()
            self.process.close()
        except ... as e:
            import traceback
            traceback.print_exc()

# if __name__ == "__main__":
#     p = CProcess()
#     p.start()
#     print("Main Process PID: %s" % os.getpid())