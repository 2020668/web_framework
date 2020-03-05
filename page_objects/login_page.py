# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""

from common.basepage import BasePage
from page_locators.login_page_locator import LoginPageLocator as Loc


class LoginPage(BasePage):

    def login_action(self, username, pwd):
        self.input_text(loc=Loc.user_loc, value=username, img_desc="登陆页面_输入用户名")
        self.input_text(loc=Loc.pwd_loc, value=pwd, img_desc="登陆页面_输入密码")
        self.wait_ele_exists(loc=Loc.login_button_loc, img_desc="登陆页面_点击登陆按钮")
        self.click_element(loc=Loc.login_button_loc, img_desc="登陆页面_点击登陆按钮")
        # time.sleep(5)

    def get_form_error_info(self):
        return self.get_text(Loc.form_error_loc, "登陆页面_获取登陆表单的错误提示信息")

    def get_login_info(self):
        self.wait_ele_visible(loc=Loc.login_info_loc, img_desc="登录后的提示语")
        text = self.get_text(loc=Loc.login_info_loc, img_desc="登录后的提示语")
        if text == "登录成功":
            return True
        else:
            return False
