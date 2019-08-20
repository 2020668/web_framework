# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/12
E-mail:keen2020@outlook.com
=================================

"""

import os

# 框架项目顶层目录
# base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
base_dir = os.path.dirname(os.path.dirname(__file__))

test_data_dir = os.path.join(base_dir, "data")

test_cases_dir = os.path.join(base_dir, "testcases")

htmlreport_dir = os.path.join(base_dir, "outputs/reports")

logs_dir = os.path.join(base_dir, "outputs/logs")

# config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir, "outputs/screenshots")
print(screenshot_dir)


if __name__ == '__main__':
    print(base_dir)

