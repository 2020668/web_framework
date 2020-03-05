# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""


from page_locators.index_page_locator import IndexPageLocator as Loc


from common.basepage import BasePage


class IndexPage(BasePage):

    def click_open_account(self):

        self.wait_ele_visible(loc=Loc.open_account_button, img_desc="首页_开户进件按钮")
        self.click_element(loc=Loc.open_account_button, img_desc="首页_开户进件按钮")

    def get_user_name(self):

        self.wait_ele_visible(loc=Loc.user_name_loc, img_desc="首页_用户名")
        text = self.get_text(loc=Loc.user_name_loc, img_desc="首页_用户名")
        return text
