# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""


import pytest

from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage
from data import login_data as ld


# 测试用例 = 测试对象的功能 + 测试数据
@pytest.mark.usefixtures("init_driver")
class TestLogin(object):

    @pytest.mark.parametrize("data", ld.success_data)
    def test_login_success(self, data, init_driver):
        # 用例 = 登陆页的登陆功能 - 首页的 检查用户昵称存在的功能

        # 步骤
        LoginPage(init_driver).login_action(data["user"], data["pwd"])

        # 断言
        assert IndexPage(init_driver).get_user_name() == data["username"]
        # self.assertTrue(LoginPage(self.driver).get_login_info())
