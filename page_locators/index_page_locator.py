# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""

from selenium.webdriver.common.by import By


class IndexPageLocator:

    # 开户进件按钮
    open_account_button = By.XPATH, "//img[@src='/dist/9cd2c604c1914c2a0ac3f2f5cffde56c.png']"

    # 用户名
    user_name_loc = By.XPATH, "//strong"
