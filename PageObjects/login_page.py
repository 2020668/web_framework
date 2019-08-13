# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/12
E-mail:keen2020@outlook.com
=================================

"""



from PageLocators.login_page_locator import LoginPageLocator as loc
from Common.basepage import BasePage
# 一个用例，一次浏览器的打开和结束。
class LoginPage(BasePage):


    # 登陆功能
    def login(self,user,passwd):
        self.input_text(loc.user_loc,user,"登陆页面_输入用户名")
        self.input_text(loc.passwd_loc,passwd,"登陆页面_输入密码")
        self.click_element(loc.login_button_loc,"登陆页面_点击登陆按钮")


    # //div[@class="form-error-info"]
    # 获取表单区域的错误信息
    def get_error_msg_from_loginForm(self):
        return self.get_text(loc.error_notify_from_loginForm,"登陆页面_表单区域错误信息")

    # 获取页面中间的错误信息
    def get_error_msg_from_pageCenter(self):
        return self.get_text(loc.error_notify_from_pageCenter,"登陆页面_页面中间错误信息")

