# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""

from selenium.webdriver.common.by import By


class LoginPageLocator(object):

    # 用户名输入框
    user_loc = By.XPATH, "//input[@type='text']"

    # 密码输入框
    pwd_loc = By.XPATH, "//input[@type='password']"

    # 登录按钮
    # login_button_loc = By.XPATH, "//button[@class='ivu-btn ivu-btn-primary']"
    login_button_loc = By.XPATH, "//span"

    # 表单错误提示
    form_error_loc = By.XPATH, "//div[@class='ivu-form-item-error-tip']"

    # 登录成功的提示
    # login_info_loc = By.XPATH, "//div[@class='ivu-message-notice-content-text']"
    login_info_loc = By.XPATH, "//div[@class='ivu-message-notice-content']"
