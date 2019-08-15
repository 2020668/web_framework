# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/12
E-mail:keen2020@outlook.com
=================================

"""


from selenium.webdriver.common.by import By


class UserPageLocator:

    # 可用余额
    user_leftMoney = (By.XPATH,'//li[@class="color_sub"]')