# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/12
E-mail:keen2020@outlook.com
=================================

"""


from page_locators.bidPage_locator import BidPageLocator as Loc
from common.base_page import BasePage


class BidPage(BasePage):

    # 投资
    def invest(self,money):
        # 在输入框当中，输入金额
        self.input_text(Loc.money_input, money, "标页面_金额输入框")
        self.click_element(Loc.invest_button, "标页面_提交投资操作")

    # 获取用户余额
    def get_user_money(self):
        return self.get_element_attribute(Loc.money_input, "data-amount", "标页面_获取用户余额")

    # 投资成功的提示框 - 点击查看并激活
    def click_active_button_on_success_popup(self):
        self.click_element(Loc.active_button_on_successPop, "标页面_投资成功的提示框 - 点击查看并激活")

    # 错误提示框 - 页面中间
    def get_error_msg_from_page_center(self):
        msg = self.get_text(Loc.invest_failed_popup, "标页面_投资失败提示框 - 提示信息获取")
        self.click_element(Loc.invest_close_failed_popup_button, "标页面_关闭投资失败提示框")
        return msg

    # 获取提示信息 - 投标按钮上的
    def get_error_msg_from_invest_button(self):
        pass





