# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""

import os

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir = os.path.join(base_dir, "data")

testcases_dir = os.path.join(base_dir, "test_cases")

htmlreport_dir = os.path.join(base_dir, "outputs/reports")

logs_dir = os.path.join(base_dir, "outputs/logs")

screenshot_dir = os.path.join(base_dir, "outputs/imgs")
print(screenshot_dir)
