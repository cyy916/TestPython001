# -*- coding:utf-8 -*-
'''
@ File: http_request.py
@ DATE:2022/7/24
@ Author: chenyuanyuan
@ version: python 3
'''
import logging
from tools.project_path import ProjectPath
import time

class MyLogger():
    def __init__(self,level=logging.DEBUG):
        self.my_logger = logging.getLogger("MyLogger")
        self.my_logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - 第%(lineno)d行 - 日志信息：%(message)s')
        self.ch = logging.StreamHandler()
        self.ch.setLevel(level)
        self.ch.setFormatter(formatter)
        now = time.strftime("%Y%m%d", time.localtime())
        file_name = "TestLog_"+now+".txt"
        file_path = ProjectPath().get_file_path("/test_result/log/", file_name, "one_layer")
        self.fh = logging.FileHandler(file_path, encoding="utf-8")
        self.fh.setLevel(level)
        self.fh.setFormatter(formatter)
        self.my_logger.addHandler(self.ch)
        self.my_logger.addHandler(self.fh)

    def debug(self, msg):
        self.my_logger.debug(msg)
        self.my_logger.removeHandler(self.fh)
        self.my_logger.removeHandler(self.ch)

    def info(self, msg):
        self.my_logger.info(msg)
        self.my_logger.removeHandler(self.fh)
        self.my_logger.removeHandler(self.ch)

    def warning(self, msg):
        self.my_logger.warning(msg)
        self.my_logger.removeHandler(self.fh)
        self.my_logger.removeHandler(self.ch)

    def error(self, msg):
        self.my_logger.error(msg)
        self.my_logger.removeHandler(self.fh)
        self.my_logger.removeHandler(self.ch)

    def critical(self, msg):
        self.my_logger.critical(msg)
        self.my_logger.removeHandler(self.fh)
        self.my_logger.removeHandler(self.ch)


if __name__ == '__main__':
    MyLogger().info("cesi00001")
    MyLogger().warning("cesi00002")
