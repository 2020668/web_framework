# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/12
E-mail:keen2020@outlook.com
=================================

"""

from common.basepage import BasePage
from page_locators.indexPage_locator import IndexPageLocator as loc
import time

class IndexPage(BasePage):


    # 检测昵称是否存在
    def check_nick_name_exists(self):
        """
        :return: 存在返回True,不存在返回False
        """
        try:
            self.wait_ele_visible(loc.user_link,"首页_找用户昵称元素",timeout=10)
            return True
        except:
            return False

    # 点击投标按钮
    def click_invest_button(self):
        self.click_element(loc.bid_button, "首页_点击第一个抢投标按钮")
