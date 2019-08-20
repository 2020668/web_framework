# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/12
E-mail:keen2020@outlook.com
=================================

"""

from selenium.webdriver.common.by import By


class LoginPageLocator:

    # 用户名输入框
    user_loc = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    pwd_loc = (By.XPATH, '//input[@name="password"]')
    # w登陆按钮
    login_button_loc = (By.TAG_NAME, "button")
    # 提示框 - 登陆表单区域
    error_notify_from_login_form = (By.XPATH, '//div[@class="form-error-info"]')
    # 提示框 - 页面中间区域
    error_notify_from_page_center = (By.XPATH, '//div[@class="layui-layer-content"]')
