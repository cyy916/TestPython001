# -*- coding:utf-8 -*-
'''
@ File: http_request.py
@ DATE:2022/7/24
@ Author: chenyuanyuan
@ version: python 3
'''
import os
"""专门来读取路径的值"""


class ProjectPath():
    def get_file_path(self, directory="", file_name="", path_type="one_layer"):
        if path_type == "one_layer":
            path = os.path.dirname(os.path.dirname(__file__))
        elif path_type == "two_layer":
            path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        else:
            path = os.path.dirname(__file__)
        base_dir = path.replace("\\", "/")
        file_path = base_dir + directory + file_name
        return file_path


if __name__ == "__main__":
    print(ProjectPath().get_file_path())
    print(ProjectPath().get_file_path("/test_data", "test_data.xlsx", ""))
    print(ProjectPath().get_file_path(path_type="two_layer"))