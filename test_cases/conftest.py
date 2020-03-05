# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/29
E-mail:keen2020@outlook.com
=================================

"""

import pytest
from selenium import webdriver
from data import common_data as cd


# 声明以下的函数是pytest的前置后置
@pytest.fixture         # scope = "class"
def init_driver():
    # 启动参数
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.login_url)
    yield driver
    driver.quit()
