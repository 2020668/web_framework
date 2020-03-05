# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/25

E-mail:keen2020@outlook.com

=================================


"""

import time
from selenium.webdriver.common.by import By

from common.basepage import BasePage
from common.tools import upload, address_match
from page_locators.open_account_page_locator import OpenAccountPageLocator as Loc


class OpenAccountPage(BasePage):

    def open_account(self, account_phone, jy_type, shop_name, shop_nickname, shop_type, area, address, rate,
                     pos, debit_card_rate, credit_card_rate, js_name, sf_id, e_mail, alipay_name, alipay_account,
                     wechat_account, company_name, bank_card, bank_name, bank_address, zhi_bank_name, people_address,
                     credit_code, corporate_name, corporate_id):

        shop_type_name_loc = By.XPATH, "//li[text()='{}']".format(shop_type)

        bank_name_loc = By.XPATH, "//li[text()='{}']".format(bank_name)

        kh_zhi_bank_name_loc = By.XPATH, "//li[text()='{}']".format(zhi_bank_name)

        province, city, district = address_match([area])

        shop_area_province_loc = By.XPATH, "//label[text()='商户地区']//following-sibling::*//li[" \
                                           "@class='ivu-cascader-menu-item' and contains(text(),'{}')]".format(province)

        shop_area_city_loc = By.XPATH, "//label[text()='商户地区']//following-sibling::*//li[contains(text(),'{}') and " \
                                       "@class='ivu-cascader-menu-item']".format(city)

        shop_area_district_loc = By.XPATH, "//label[text()='商户地区']//following-sibling::*//li[contains(text(),'{}') " \
                                           "and @class='ivu-cascader-menu-item']".format(district)

        bank_province, bank_city, bank_district = address_match([bank_address])

        bank_address_province_loc = By.XPATH, "//label[text()='开户地址']//following-sibling::*//li[@class=" \
                                              "'ivu-cascader-menu-item' and contains(text(),'{}')]".format(bank_province)

        bank_address_city_loc = By.XPATH, "//label[text()='开户地址']//following-sibling::*//li[contains(text(),'{}') " \
                                          "and @class='ivu-cascader-menu-item']".format(bank_city)

        bank_address_district_loc = By.XPATH, "//label[text()='开户地址']//following-sibling::*//li[contains(text(),'{}')" \
                                              " and @class='ivu-cascader-menu-item']".format(bank_district)

        # base_path = "C:\\Users\\keen\\Desktop\\FunPay\\资料\\253"

        base_path = "C:\\Users\\Administrator\\Desktop\\FunPay\\资料\\253"

        self.wait_ele_visible(loc=Loc.phone_input_loc, img_desc="手机号码输入框")
        self.input_text(loc=Loc.phone_input_loc, value=account_phone, img_desc="手机号码输入框")

        self.wait_ele_visible(loc=Loc.next_step_loc, img_desc="下一步按钮")
        self.click_element(loc=Loc.next_step_loc, img_desc="下一步按钮")

        if jy_type == "小微商户":

            self.wait_ele_visible(loc=Loc.xiaowei_loc, img_desc="小微商户的选择按钮")
            self.click_element(loc=Loc.xiaowei_loc, img_desc="小微商户的选择按钮")

            self.wait_ele_visible(loc=Loc.shop_name_input_loc, img_desc="商户全称输入框")
            self.input_text(loc=Loc.shop_name_input_loc, value=shop_name, img_desc="商户全称输入框")

            self.wait_ele_visible(loc=Loc.shop_nickname_input_loc, img_desc="商户简称输入框")
            self.input_text(loc=Loc.shop_nickname_input_loc, value=shop_nickname, img_desc="商户简称输入框")

            self.wait_ele_visible(loc=Loc.shop_type_loc, img_desc="商户类型选择框")
            self.click_element(loc=Loc.shop_type_loc, img_desc="商户类型选择框")

            self.select_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=shop_type_name_loc, img_desc="商户类型")
            self.click_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=Loc.shop_area_loc, img_desc="商户地区选择框")
            self.click_element(loc=Loc.shop_area_loc, img_desc="商户地区选择框")

            self.wait_ele_visible(loc=shop_area_province_loc, img_desc="选择省份")
            self.click_element(loc=shop_area_province_loc, img_desc="选择省份")

            self.wait_ele_visible(loc=shop_area_city_loc, img_desc="选择市")
            self.click_element(loc=shop_area_city_loc, img_desc="选择市")

            self.wait_ele_visible(loc=shop_area_district_loc, img_desc="选择区")
            self.click_element(loc=shop_area_district_loc, img_desc="选择区")

            self.wait_ele_visible(loc=Loc.address_input_loc, img_desc="详细地址输入框")
            self.input_text(loc=Loc.address_input_loc, value=address, img_desc="详细地址输入框")

            self.wait_ele_visible(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.double_click_element(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.input_text(loc=Loc.rate_input_loc, value=rate, img_desc="费率输入框")

            self.scroll_up_down(img_desc="滑动一页")

            if pos is True:
                self.wait_ele_visible(loc=Loc.pos_loc, img_desc="pos机按钮")
                self.click_element(loc=Loc.pos_loc, img_desc="pos机按钮")

                self.wait_ele_visible(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.double_click_element(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.input_text(loc=Loc.debit_rate_input_loc, value=debit_card_rate, img_desc="借记卡费率输入框")

                self.wait_ele_visible(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.double_click_element(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.input_text(loc=Loc.credit_rate_input_loc, value=credit_card_rate, img_desc="贷记卡费率输入框")

            else:
                pass

            self.wait_ele_visible(loc=Loc.js_name_input_loc, img_desc="结算人姓名输入框")
            self.input_text(loc=Loc.js_name_input_loc, value=js_name, img_desc="结算人姓名输入框")

            self.wait_ele_visible(loc=Loc.js_id_num_input_loc, img_desc="结算人身份证号输入框")
            self.input_text(loc=Loc.js_id_num_input_loc, value=sf_id, img_desc="结算人身份证号输入框")

            self.wait_ele_visible(loc=Loc.e_mail_input_loc, img_desc="常用邮箱输入框")
            self.input_text(loc=Loc.e_mail_input_loc, value=e_mail, img_desc="常用邮箱输入框")

            self.wait_ele_visible(loc=Loc.alipay_name_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_name_input_loc, value=alipay_name, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.alipay_account_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_account_input_loc, value=alipay_account, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.wechat_num_input_loc, img_desc="微信号输入框")
            self.input_text(loc=Loc.wechat_num_input_loc, value=wechat_account, img_desc="微信号输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.bank_card_num_input_loc, img_desc="银行卡号输入框")
            self.input_text(loc=Loc.bank_card_num_input_loc, value=bank_card, img_desc="银行卡号输入框")

            self.wait_ele_visible(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")
            self.click_element(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")

            self.wait_ele_visible(loc=bank_name_loc, img_desc="银行名称")
            self.click_element(loc=bank_name_loc, img_desc="银行名称")

            self.wait_ele_visible(loc=Loc.kh_address_loc, img_desc="开户地址选择框")
            self.click_element(loc=Loc.kh_address_loc, img_desc="开户地址选择框")

            self.wait_ele_visible(loc=bank_address_province_loc, img_desc="开户银行的省份")
            self.click_element(loc=bank_address_province_loc, img_desc="开户银行的省份")

            self.wait_ele_visible(loc=bank_address_city_loc, img_desc="开户银行的市")
            self.click_element(loc=bank_address_city_loc, img_desc="开户银行的市")

            self.wait_ele_visible(loc=bank_address_district_loc, img_desc="开户银行的区")
            self.click_element(loc=bank_address_district_loc, img_desc="开户银行的区")

            self.wait_ele_visible(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")
            self.click_element(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")

            self.wait_ele_visible(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")
            self.click_element(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")

            self.wait_ele_visible(loc=Loc.card_username_input_loc, img_desc="持卡人姓名输入框")
            self.input_text(loc=Loc.card_username_input_loc, value=js_name, img_desc="持卡人姓名输入框")

            self.wait_ele_visible(loc=Loc.card_id_num_input_loc, img_desc="持卡人身份证号输入框")
            self.input_text(loc=Loc.card_id_num_input_loc, value=sf_id, img_desc="持卡人身份证号输入框")

            self.wait_ele_visible(loc=Loc.card_user_address_input_loc, img_desc="持卡人地址输入框")
            self.input_text(loc=Loc.card_user_address_input_loc, value=people_address, img_desc="持卡人地址输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.shop_head_img_loc, img_desc="门头照图片上传按钮")
            self.click_element(loc=Loc.shop_head_img_loc, img_desc="门头照图片上传按钮")
            upload(base_path + "\\门头.jpg")

            self.wait_ele_visible(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            self.click_element(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            upload(base_path + "\\店内.jpg")

            self.wait_ele_visible(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            self.click_element(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            upload(base_path + "\\收银台.jpg")

            self.wait_ele_visible(loc=Loc.hand_card_img_loc, img_desc="手持身份证图片上传按钮")
            self.click_element(loc=Loc.hand_card_img_loc, img_desc="手持身份证图片上传按钮")
            upload(base_path + "\\手持.jpg")

            self.wait_ele_visible(loc=Loc.person_face_img_loc, img_desc="结算人身份证人像面图片上传按钮")
            self.click_element(loc=Loc.person_face_img_loc, img_desc="结算人身份证人像面图片上传按钮")
            upload(base_path + "\\身正.jpg")

            self.wait_ele_visible(loc=Loc.person_emblem_img_loc, img_desc="结算人身份证国徽面图片上传按钮")
            self.click_element(loc=Loc.person_emblem_img_loc, img_desc="结算人身份证国徽面图片上传按钮")
            upload(base_path + "\\身反.jpg")

            self.wait_ele_visible(loc=Loc.bank_card_img_loc, img_desc="结算人银行卡正面图片上传按钮")
            self.click_element(loc=Loc.bank_card_img_loc, img_desc="结算人银行卡正面图片上传按钮")
            upload(base_path + "\\银行卡.jpg")

            self.wait_ele_visible(loc=Loc.save_loc, img_desc="保存按钮")
            self.click_element(loc=Loc.save_loc, img_desc="保存按钮")

            time.sleep(3)

            self.select_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            self.wait_ele_visible(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")
            self.click_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            time.sleep(2)

            self.wait_ele_visible(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")
            self.click_element(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")

            time.sleep(5)

        if jy_type == "个体工商-结算同法人":

            self.wait_ele_visible(loc=Loc.geti_same_loc, img_desc="个体商户-结算同法人")
            self.click_element(loc=Loc.geti_same_loc, img_desc="个体商户-结算同法人")

            self.wait_ele_visible(loc=Loc.credit_code_input_loc, img_desc="信用代码输入框")
            self.input_text(loc=Loc.credit_code_input_loc, value=credit_code, img_desc="信用代码输入框")

            self.wait_ele_visible(loc=Loc.shop_name_input_loc, img_desc="商户全称输入框")
            self.input_text(loc=Loc.shop_name_input_loc, value=shop_name, img_desc="商户全称输入框")

            self.wait_ele_visible(loc=Loc.shop_nickname_input_loc, img_desc="商户简称输入框")
            self.input_text(loc=Loc.shop_nickname_input_loc, value=shop_nickname, img_desc="商户简称输入框")

            self.wait_ele_visible(loc=Loc.shop_type_loc, img_desc="商户类型选择框")
            self.click_element(loc=Loc.shop_type_loc, img_desc="商户类型选择框")

            self.select_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=shop_type_name_loc, img_desc="商户类型")
            self.click_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=Loc.shop_area_loc, img_desc="商户地区选择框")
            self.click_element(loc=Loc.shop_area_loc, img_desc="商户地区选择框")

            self.wait_ele_visible(loc=shop_area_province_loc, img_desc="选择省份")
            self.click_element(loc=shop_area_province_loc, img_desc="选择省份")

            self.wait_ele_visible(loc=shop_area_city_loc, img_desc="选择市")
            self.click_element(loc=shop_area_city_loc, img_desc="选择市")

            self.wait_ele_visible(loc=shop_area_district_loc, img_desc="选择区")
            self.click_element(loc=shop_area_district_loc, img_desc="选择区")

            self.wait_ele_visible(loc=Loc.address_input_loc, img_desc="详细地址输入框")
            self.input_text(loc=Loc.address_input_loc, value=address, img_desc="详细地址输入框")

            self.wait_ele_visible(loc=Loc.rate_input_loc, img_desc="费率输入框")
            # self.double_click_element(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.clean_element_text(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.input_text(loc=Loc.rate_input_loc, value=rate, img_desc="费率输入框")

            self.scroll_up_down(img_desc="滑动一页")

            if pos is True:
                self.wait_ele_visible(loc=Loc.pos_loc, img_desc="pos机按钮")
                self.click_element(loc=Loc.pos_loc, img_desc="pos机按钮")

                self.wait_ele_visible(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.double_click_element(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.input_text(loc=Loc.debit_rate_input_loc, value=debit_card_rate, img_desc="借记卡费率输入框")

                self.wait_ele_visible(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.double_click_element(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.input_text(loc=Loc.credit_rate_input_loc, value=credit_card_rate, img_desc="贷记卡费率输入框")

            else:
                pass

            self.wait_ele_visible(loc=Loc.corporate_name_input_loc, img_desc="法人姓名输入框")
            self.input_text(loc=Loc.corporate_name_input_loc, value=corporate_name, img_desc="法人姓名输入框")

            self.wait_ele_visible(loc=Loc.corporate_id_input_loc, img_desc="法人身份证号输入框")
            self.input_text(loc=Loc.corporate_id_input_loc, value=corporate_id, img_desc="法人身份证号输入框")

            self.wait_ele_visible(loc=Loc.e_mail_input_loc, img_desc="常用邮箱输入框")
            self.input_text(loc=Loc.e_mail_input_loc, value=e_mail, img_desc="常用邮箱输入框")

            self.wait_ele_visible(loc=Loc.alipay_name_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_name_input_loc, value=alipay_name, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.alipay_account_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_account_input_loc, value=alipay_account, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.wechat_num_input_loc, img_desc="微信号输入框")
            self.input_text(loc=Loc.wechat_num_input_loc, value=wechat_account, img_desc="微信号输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.bank_card_num_input_loc, img_desc="银行卡号输入框")
            self.input_text(loc=Loc.bank_card_num_input_loc, value=bank_card, img_desc="银行卡号输入框")

            self.wait_ele_visible(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")
            self.click_element(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")

            self.wait_ele_visible(loc=bank_name_loc, img_desc="银行名称")
            self.click_element(loc=bank_name_loc, img_desc="银行名称")

            self.wait_ele_visible(loc=Loc.kh_address_loc, img_desc="开户地址选择框")
            self.click_element(loc=Loc.kh_address_loc, img_desc="开户地址选择框")

            self.wait_ele_visible(loc=bank_address_province_loc, img_desc="开户银行的省份")
            self.click_element(loc=bank_address_province_loc, img_desc="开户银行的省份")

            self.wait_ele_visible(loc=bank_address_city_loc, img_desc="开户银行的市")
            self.click_element(loc=bank_address_city_loc, img_desc="开户银行的市")

            self.wait_ele_visible(loc=bank_address_district_loc, img_desc="开户银行的区")
            self.click_element(loc=bank_address_district_loc, img_desc="开户银行的区")

            self.wait_ele_visible(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")
            self.click_element(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")

            self.wait_ele_visible(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")
            self.click_element(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")

            self.wait_ele_visible(loc=Loc.card_username_input_loc, img_desc="持卡人姓名输入框")
            self.input_text(loc=Loc.card_username_input_loc, value=js_name, img_desc="持卡人姓名输入框")

            self.wait_ele_visible(loc=Loc.card_id_num_input_loc, img_desc="持卡人身份证号输入框")
            self.input_text(loc=Loc.card_id_num_input_loc, value=sf_id, img_desc="持卡人身份证号输入框")

            self.wait_ele_visible(loc=Loc.card_user_address_input_loc, img_desc="持卡人地址输入框")
            self.input_text(loc=Loc.card_user_address_input_loc, value=people_address, img_desc="持卡人地址输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.shop_head_person_same_img_loc, img_desc="门头照图片上传按钮")
            self.click_element(loc=Loc.shop_head_person_same_img_loc, img_desc="门头照图片上传按钮")
            upload(base_path + "\\门头.jpg")

            self.wait_ele_visible(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            self.click_element(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            upload(base_path + "\\店内.jpg")

            self.wait_ele_visible(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            self.click_element(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            upload(base_path + "\\收银台.jpg")

            self.wait_ele_visible(loc=Loc.business_license_loc, img_desc="营业执照图片上传按钮")
            self.click_element(loc=Loc.business_license_loc, img_desc="营业执照图片上传按钮")
            upload(base_path + "\\将营业执照.jpg")

            self.wait_ele_visible(loc=Loc.corporate_face_img_loc, img_desc="法人身份证人像面图片上传按钮")
            self.click_element(loc=Loc.corporate_face_img_loc, img_desc="法人身份证人像面图片上传按钮")
            upload(base_path + "\\身正.jpg")

            self.wait_ele_visible(loc=Loc.corporate_emblem_img_loc, img_desc="法人身份证国徽面图片上传按钮")
            self.click_element(loc=Loc.corporate_emblem_img_loc, img_desc="法人身份证国徽面图片上传按钮")
            upload(base_path + "\\身反.jpg")

            self.wait_ele_visible(loc=Loc.corporate_bank_card_img_loc, img_desc="结算人银行卡正面图片上传按钮")
            self.click_element(loc=Loc.corporate_bank_card_img_loc, img_desc="结算人银行卡正面图片上传按钮")
            upload(base_path + "\\银行卡.jpg")

            self.wait_ele_visible(loc=Loc.person_same_save_loc, img_desc="保存按钮")
            self.click_element(loc=Loc.person_same_save_loc, img_desc="保存按钮")

            time.sleep(3)

            self.select_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            self.wait_ele_visible(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")
            self.click_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            time.sleep(2)

            self.wait_ele_visible(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")
            self.click_element(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")

            time.sleep(5)

        if jy_type == "个体工商-结算非法人":

            self.wait_ele_visible(loc=Loc.geti_different_loc, img_desc="个体商户-结算非法人")
            self.click_element(loc=Loc.geti_different_loc, img_desc="个体商户-结算非法人")

            self.wait_ele_visible(loc=Loc.credit_code_input_loc, img_desc="信用代码输入框")
            self.input_text(loc=Loc.credit_code_input_loc, value=credit_code, img_desc="信用代码输入框")

            self.wait_ele_visible(loc=Loc.shop_name_input_loc, img_desc="商户全称输入框")
            self.input_text(loc=Loc.shop_name_input_loc, value=shop_name, img_desc="商户全称输入框")

            self.wait_ele_visible(loc=Loc.shop_nickname_input_loc, img_desc="商户简称输入框")
            self.input_text(loc=Loc.shop_nickname_input_loc, value=shop_nickname, img_desc="商户简称输入框")

            self.wait_ele_visible(loc=Loc.shop_type_loc, img_desc="商户类型选择框")
            self.click_element(loc=Loc.shop_type_loc, img_desc="商户类型选择框")

            self.select_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=shop_type_name_loc, img_desc="商户类型")
            self.click_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=Loc.shop_area_loc, img_desc="商户地区选择框")
            self.click_element(loc=Loc.shop_area_loc, img_desc="商户地区选择框")

            self.wait_ele_visible(loc=shop_area_province_loc, img_desc="选择省份")
            self.click_element(loc=shop_area_province_loc, img_desc="选择省份")

            self.wait_ele_visible(loc=shop_area_city_loc, img_desc="选择市")
            self.click_element(loc=shop_area_city_loc, img_desc="选择市")

            self.wait_ele_visible(loc=shop_area_district_loc, img_desc="选择区")
            self.click_element(loc=shop_area_district_loc, img_desc="选择区")

            self.wait_ele_visible(loc=Loc.address_input_loc, img_desc="详细地址输入框")
            self.input_text(loc=Loc.address_input_loc, value=address, img_desc="详细地址输入框")

            self.wait_ele_visible(loc=Loc.rate_input_loc, img_desc="费率输入框")
            # self.double_click_element(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.clean_element_text(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.input_text(loc=Loc.rate_input_loc, value=rate, img_desc="费率输入框")

            self.scroll_up_down(img_desc="滑动一页")

            if pos is True:
                self.wait_ele_visible(loc=Loc.pos_loc, img_desc="pos机按钮")
                self.click_element(loc=Loc.pos_loc, img_desc="pos机按钮")

                self.wait_ele_visible(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.double_click_element(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.input_text(loc=Loc.debit_rate_input_loc, value=debit_card_rate, img_desc="借记卡费率输入框")

                self.wait_ele_visible(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.double_click_element(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.input_text(loc=Loc.credit_rate_input_loc, value=credit_card_rate, img_desc="贷记卡费率输入框")

            else:
                pass

            self.wait_ele_visible(loc=Loc.corporate_name_input_loc, img_desc="法人姓名输入框")
            self.input_text(loc=Loc.corporate_name_input_loc, value=corporate_name, img_desc="法人姓名输入框")

            self.wait_ele_visible(loc=Loc.corporate_id_input_loc, img_desc="法人身份证号输入框")
            self.input_text(loc=Loc.corporate_id_input_loc, value=corporate_id, img_desc="法人身份证号输入框")

            self.wait_ele_visible(loc=Loc.js_name_input_loc, img_desc="结算人姓名输入框")
            self.input_text(loc=Loc.js_name_input_loc, value=js_name, img_desc="结算人姓名输入框")

            self.wait_ele_visible(loc=Loc.js_id_num_input_loc, img_desc="结算人身份证号输入框")
            self.input_text(loc=Loc.js_id_num_input_loc, value=sf_id, img_desc="结算人身份证号输入框")

            self.wait_ele_visible(loc=Loc.e_mail_input_loc, img_desc="常用邮箱输入框")
            self.input_text(loc=Loc.e_mail_input_loc, value=e_mail, img_desc="常用邮箱输入框")

            self.wait_ele_visible(loc=Loc.alipay_name_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_name_input_loc, value=alipay_name, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.alipay_account_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_account_input_loc, value=alipay_account, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.wechat_num_input_loc, img_desc="微信号输入框")
            self.input_text(loc=Loc.wechat_num_input_loc, value=wechat_account, img_desc="微信号输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.bank_card_num_input_loc, img_desc="银行卡号输入框")
            self.input_text(loc=Loc.bank_card_num_input_loc, value=bank_card, img_desc="银行卡号输入框")

            self.wait_ele_visible(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")
            self.click_element(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")

            self.wait_ele_visible(loc=bank_name_loc, img_desc="银行名称")
            self.click_element(loc=bank_name_loc, img_desc="银行名称")

            self.wait_ele_visible(loc=Loc.kh_address_loc, img_desc="开户地址选择框")
            self.click_element(loc=Loc.kh_address_loc, img_desc="开户地址选择框")

            self.wait_ele_visible(loc=bank_address_province_loc, img_desc="开户银行的省份")
            self.click_element(loc=bank_address_province_loc, img_desc="开户银行的省份")

            self.wait_ele_visible(loc=bank_address_city_loc, img_desc="开户银行的市")
            self.click_element(loc=bank_address_city_loc, img_desc="开户银行的市")

            self.wait_ele_visible(loc=bank_address_district_loc, img_desc="开户银行的区")
            self.click_element(loc=bank_address_district_loc, img_desc="开户银行的区")

            self.wait_ele_visible(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")
            self.click_element(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")

            self.wait_ele_visible(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")
            self.click_element(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")

            self.wait_ele_visible(loc=Loc.card_username_input_loc, img_desc="持卡人姓名输入框")
            self.input_text(loc=Loc.card_username_input_loc, value=js_name, img_desc="持卡人姓名输入框")

            self.wait_ele_visible(loc=Loc.card_id_num_input_loc, img_desc="持卡人身份证号输入框")
            self.input_text(loc=Loc.card_id_num_input_loc, value=sf_id, img_desc="持卡人身份证号输入框")

            self.wait_ele_visible(loc=Loc.card_user_address_input_loc, img_desc="持卡人地址输入框")
            self.input_text(loc=Loc.card_user_address_input_loc, value=people_address, img_desc="持卡人地址输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.shop_head_person_same_img_loc, img_desc="门头照图片上传按钮")
            self.click_element(loc=Loc.shop_head_person_same_img_loc, img_desc="门头照图片上传按钮")
            upload(base_path + "\\门头.jpg")

            self.wait_ele_visible(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            self.click_element(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            upload(base_path + "\\店内.jpg")

            self.wait_ele_visible(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            self.click_element(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            upload(base_path + "\\收银台.jpg")

            self.wait_ele_visible(loc=Loc.business_license_loc, img_desc="营业执照图片上传按钮")
            self.click_element(loc=Loc.business_license_loc, img_desc="营业执照图片上传按钮")
            upload(base_path + "\\将营业执照.jpg")

            self.wait_ele_visible(loc=Loc.corporate_face_img_loc, img_desc="法人身份证人像面图片上传按钮")
            self.click_element(loc=Loc.corporate_face_img_loc, img_desc="法人身份证人像面图片上传按钮")
            upload(base_path + "\\身正.jpg")

            self.wait_ele_visible(loc=Loc.corporate_emblem_img_loc, img_desc="法人身份证国徽面图片上传按钮")
            self.click_element(loc=Loc.corporate_emblem_img_loc, img_desc="法人身份证国徽面图片上传按钮")
            upload(base_path + "\\身反.jpg")

            self.wait_ele_visible(loc=Loc.person_face_img_loc, img_desc="结算人身份证人像面图片上传按钮")
            self.click_element(loc=Loc.person_face_img_loc, img_desc="结算人身份证人像面图片上传按钮")
            upload(base_path + "\\身正1.jpg")

            self.wait_ele_visible(loc=Loc.person_emblem_img_loc, img_desc="结算人身份证国徽面图片上传按钮")
            self.click_element(loc=Loc.person_emblem_img_loc, img_desc="结算人身份证国徽面图片上传按钮")
            upload(base_path + "\\身反1.jpg")

            self.wait_ele_visible(loc=Loc.settlement_book_loc, img_desc="结算授权书照片上传按钮")
            self.click_element(loc=Loc.settlement_book_loc, img_desc="结算授权书照片上传按钮")
            upload(base_path + "\\授权书.jpg")

            self.wait_ele_visible(loc=Loc.bank_card_img_loc, img_desc="结算人银行卡正面图片上传按钮")
            self.click_element(loc=Loc.bank_card_img_loc, img_desc="结算人银行卡正面图片上传按钮")
            upload(base_path + "\\银行卡.jpg")

            self.wait_ele_visible(loc=Loc.person_same_save_loc, img_desc="保存按钮")
            self.click_element(loc=Loc.person_same_save_loc, img_desc="保存按钮")

            time.sleep(3)

            self.select_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            self.wait_ele_visible(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")
            self.click_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            time.sleep(2)

            self.wait_ele_visible(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")
            self.click_element(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")

            time.sleep(5)

        if jy_type == "企业对私-结算同法人":

            self.wait_ele_visible(loc=Loc.qiye_geti_same_loc, img_desc="个体商户-结算同法人")
            self.click_element(loc=Loc.qiye_geti_same_loc, img_desc="个体商户-结算同法人")

            self.wait_ele_visible(loc=Loc.credit_code_input_loc, img_desc="信用代码输入框")
            self.input_text(loc=Loc.credit_code_input_loc, value=credit_code, img_desc="信用代码输入框")

            self.wait_ele_visible(loc=Loc.shop_name_input_loc, img_desc="商户全称输入框")
            self.input_text(loc=Loc.shop_name_input_loc, value=shop_name, img_desc="商户全称输入框")

            self.wait_ele_visible(loc=Loc.shop_nickname_input_loc, img_desc="商户简称输入框")
            self.input_text(loc=Loc.shop_nickname_input_loc, value=shop_nickname, img_desc="商户简称输入框")

            self.wait_ele_visible(loc=Loc.shop_type_loc, img_desc="商户类型选择框")
            self.click_element(loc=Loc.shop_type_loc, img_desc="商户类型选择框")

            self.select_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=shop_type_name_loc, img_desc="商户类型")
            self.click_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=Loc.shop_area_loc, img_desc="商户地区选择框")
            self.click_element(loc=Loc.shop_area_loc, img_desc="商户地区选择框")

            self.wait_ele_visible(loc=shop_area_province_loc, img_desc="选择省份")
            self.click_element(loc=shop_area_province_loc, img_desc="选择省份")

            self.wait_ele_visible(loc=shop_area_city_loc, img_desc="选择市")
            self.click_element(loc=shop_area_city_loc, img_desc="选择市")

            self.wait_ele_visible(loc=shop_area_district_loc, img_desc="选择区")
            self.click_element(loc=shop_area_district_loc, img_desc="选择区")

            self.wait_ele_visible(loc=Loc.address_input_loc, img_desc="详细地址输入框")
            self.input_text(loc=Loc.address_input_loc, value=address, img_desc="详细地址输入框")

            self.wait_ele_visible(loc=Loc.rate_input_loc, img_desc="费率输入框")
            # self.double_click_element(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.clean_element_text(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.input_text(loc=Loc.rate_input_loc, value=rate, img_desc="费率输入框")

            self.scroll_up_down(img_desc="滑动一页")

            if pos is True:
                self.wait_ele_visible(loc=Loc.pos_loc, img_desc="pos机按钮")
                self.click_element(loc=Loc.pos_loc, img_desc="pos机按钮")

                self.wait_ele_visible(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.double_click_element(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.input_text(loc=Loc.debit_rate_input_loc, value=debit_card_rate, img_desc="借记卡费率输入框")

                self.wait_ele_visible(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.double_click_element(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.input_text(loc=Loc.credit_rate_input_loc, value=credit_card_rate, img_desc="贷记卡费率输入框")

            else:
                pass

            self.wait_ele_visible(loc=Loc.corporate_name_input_loc, img_desc="法人姓名输入框")
            self.input_text(loc=Loc.corporate_name_input_loc, value=corporate_name, img_desc="法人姓名输入框")

            self.wait_ele_visible(loc=Loc.corporate_id_input_loc, img_desc="法人身份证号输入框")
            self.input_text(loc=Loc.corporate_id_input_loc, value=corporate_id, img_desc="法人身份证号输入框")

            self.wait_ele_visible(loc=Loc.e_mail_input_loc, img_desc="常用邮箱输入框")
            self.input_text(loc=Loc.e_mail_input_loc, value=e_mail, img_desc="常用邮箱输入框")

            self.wait_ele_visible(loc=Loc.alipay_name_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_name_input_loc, value=alipay_name, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.alipay_account_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_account_input_loc, value=alipay_account, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.wechat_num_input_loc, img_desc="微信号输入框")
            self.input_text(loc=Loc.wechat_num_input_loc, value=wechat_account, img_desc="微信号输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.bank_card_num_input_loc, img_desc="银行卡号输入框")
            self.input_text(loc=Loc.bank_card_num_input_loc, value=bank_card, img_desc="银行卡号输入框")

            self.wait_ele_visible(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")
            self.click_element(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")

            self.wait_ele_visible(loc=bank_name_loc, img_desc="银行名称")
            self.click_element(loc=bank_name_loc, img_desc="银行名称")

            self.wait_ele_visible(loc=Loc.kh_address_loc, img_desc="开户地址选择框")
            self.click_element(loc=Loc.kh_address_loc, img_desc="开户地址选择框")

            self.wait_ele_visible(loc=bank_address_province_loc, img_desc="开户银行的省份")
            self.click_element(loc=bank_address_province_loc, img_desc="开户银行的省份")

            self.wait_ele_visible(loc=bank_address_city_loc, img_desc="开户银行的市")
            self.click_element(loc=bank_address_city_loc, img_desc="开户银行的市")

            self.wait_ele_visible(loc=bank_address_district_loc, img_desc="开户银行的区")
            self.click_element(loc=bank_address_district_loc, img_desc="开户银行的区")

            self.wait_ele_visible(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")
            self.click_element(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")

            self.wait_ele_visible(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")
            self.click_element(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")

            self.wait_ele_visible(loc=Loc.card_username_input_loc, img_desc="持卡人姓名输入框")
            self.input_text(loc=Loc.card_username_input_loc, value=js_name, img_desc="持卡人姓名输入框")

            self.wait_ele_visible(loc=Loc.card_id_num_input_loc, img_desc="持卡人身份证号输入框")
            self.input_text(loc=Loc.card_id_num_input_loc, value=sf_id, img_desc="持卡人身份证号输入框")

            self.wait_ele_visible(loc=Loc.card_user_address_input_loc, img_desc="持卡人地址输入框")
            self.input_text(loc=Loc.card_user_address_input_loc, value=people_address, img_desc="持卡人地址输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.shop_head_person_same_img_loc, img_desc="门头照图片上传按钮")
            self.click_element(loc=Loc.shop_head_person_same_img_loc, img_desc="门头照图片上传按钮")
            upload(base_path + "\\门头.jpg")

            self.wait_ele_visible(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            self.click_element(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            upload(base_path + "\\店内.jpg")

            self.wait_ele_visible(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            self.click_element(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            upload(base_path + "\\收银台.jpg")

            self.wait_ele_visible(loc=Loc.business_license_loc, img_desc="营业执照图片上传按钮")
            self.click_element(loc=Loc.business_license_loc, img_desc="营业执照图片上传按钮")
            upload(base_path + "\\将营业执照.jpg")

            self.wait_ele_visible(loc=Loc.corporate_face_img_loc, img_desc="法人身份证人像面图片上传按钮")
            self.click_element(loc=Loc.corporate_face_img_loc, img_desc="法人身份证人像面图片上传按钮")
            upload(base_path + "\\身正.jpg")

            self.wait_ele_visible(loc=Loc.corporate_emblem_img_loc, img_desc="法人身份证国徽面图片上传按钮")
            self.click_element(loc=Loc.corporate_emblem_img_loc, img_desc="法人身份证国徽面图片上传按钮")
            upload(base_path + "\\身反.jpg")

            self.wait_ele_visible(loc=Loc.corporate_bank_card_img_loc, img_desc="结算人银行卡正面图片上传按钮")
            self.click_element(loc=Loc.corporate_bank_card_img_loc, img_desc="结算人银行卡正面图片上传按钮")
            upload(base_path + "\\银行卡.jpg")

            self.wait_ele_visible(loc=Loc.person_same_save_loc, img_desc="保存按钮")
            self.click_element(loc=Loc.person_same_save_loc, img_desc="保存按钮")

            time.sleep(3)

            self.select_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            self.wait_ele_visible(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")
            self.click_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            time.sleep(2)

            self.wait_ele_visible(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")
            self.click_element(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")

            time.sleep(5)

        if jy_type == "企业对私-结算非法人":

            self.wait_ele_visible(loc=Loc.qiye_geti_different_loc, img_desc="个体商户-结算非法人")
            self.click_element(loc=Loc.qiye_geti_different_loc, img_desc="个体商户-结算非法人")

            self.wait_ele_visible(loc=Loc.credit_code_input_loc, img_desc="信用代码输入框")
            self.input_text(loc=Loc.credit_code_input_loc, value=credit_code, img_desc="信用代码输入框")

            self.wait_ele_visible(loc=Loc.shop_name_input_loc, img_desc="商户全称输入框")
            self.input_text(loc=Loc.shop_name_input_loc, value=shop_name, img_desc="商户全称输入框")

            self.wait_ele_visible(loc=Loc.shop_nickname_input_loc, img_desc="商户简称输入框")
            self.input_text(loc=Loc.shop_nickname_input_loc, value=shop_nickname, img_desc="商户简称输入框")

            self.wait_ele_visible(loc=Loc.shop_type_loc, img_desc="商户类型选择框")
            self.click_element(loc=Loc.shop_type_loc, img_desc="商户类型选择框")

            self.select_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=shop_type_name_loc, img_desc="商户类型")
            self.click_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=Loc.shop_area_loc, img_desc="商户地区选择框")
            self.click_element(loc=Loc.shop_area_loc, img_desc="商户地区选择框")

            self.wait_ele_visible(loc=shop_area_province_loc, img_desc="选择省份")
            self.click_element(loc=shop_area_province_loc, img_desc="选择省份")

            self.wait_ele_visible(loc=shop_area_city_loc, img_desc="选择市")
            self.click_element(loc=shop_area_city_loc, img_desc="选择市")

            self.wait_ele_visible(loc=shop_area_district_loc, img_desc="选择区")
            self.click_element(loc=shop_area_district_loc, img_desc="选择区")

            self.wait_ele_visible(loc=Loc.address_input_loc, img_desc="详细地址输入框")
            self.input_text(loc=Loc.address_input_loc, value=address, img_desc="详细地址输入框")

            self.wait_ele_visible(loc=Loc.rate_input_loc, img_desc="费率输入框")
            # self.double_click_element(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.clean_element_text(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.input_text(loc=Loc.rate_input_loc, value=rate, img_desc="费率输入框")

            self.scroll_up_down(img_desc="滑动一页")

            if pos is True:
                self.wait_ele_visible(loc=Loc.pos_loc, img_desc="pos机按钮")
                self.click_element(loc=Loc.pos_loc, img_desc="pos机按钮")

                self.wait_ele_visible(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.double_click_element(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.input_text(loc=Loc.debit_rate_input_loc, value=debit_card_rate, img_desc="借记卡费率输入框")

                self.wait_ele_visible(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.double_click_element(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.input_text(loc=Loc.credit_rate_input_loc, value=credit_card_rate, img_desc="贷记卡费率输入框")

            else:
                pass

            self.wait_ele_visible(loc=Loc.corporate_name_input_loc, img_desc="法人姓名输入框")
            self.input_text(loc=Loc.corporate_name_input_loc, value=corporate_name, img_desc="法人姓名输入框")

            self.wait_ele_visible(loc=Loc.corporate_id_input_loc, img_desc="法人身份证号输入框")
            self.input_text(loc=Loc.corporate_id_input_loc, value=corporate_id, img_desc="法人身份证号输入框")

            self.wait_ele_visible(loc=Loc.js_name_input_loc, img_desc="结算人姓名输入框")
            self.input_text(loc=Loc.js_name_input_loc, value=js_name, img_desc="结算人姓名输入框")

            self.wait_ele_visible(loc=Loc.js_id_num_input_loc, img_desc="结算人身份证号输入框")
            self.input_text(loc=Loc.js_id_num_input_loc, value=sf_id, img_desc="结算人身份证号输入框")

            self.wait_ele_visible(loc=Loc.e_mail_input_loc, img_desc="常用邮箱输入框")
            self.input_text(loc=Loc.e_mail_input_loc, value=e_mail, img_desc="常用邮箱输入框")

            self.wait_ele_visible(loc=Loc.alipay_name_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_name_input_loc, value=alipay_name, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.alipay_account_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_account_input_loc, value=alipay_account, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.wechat_num_input_loc, img_desc="微信号输入框")
            self.input_text(loc=Loc.wechat_num_input_loc, value=wechat_account, img_desc="微信号输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.bank_card_num_input_loc, img_desc="银行卡号输入框")
            self.input_text(loc=Loc.bank_card_num_input_loc, value=bank_card, img_desc="银行卡号输入框")

            self.wait_ele_visible(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")
            self.click_element(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")

            self.wait_ele_visible(loc=bank_name_loc, img_desc="银行名称")
            self.click_element(loc=bank_name_loc, img_desc="银行名称")

            self.wait_ele_visible(loc=Loc.kh_address_loc, img_desc="开户地址选择框")
            self.click_element(loc=Loc.kh_address_loc, img_desc="开户地址选择框")

            self.wait_ele_visible(loc=bank_address_province_loc, img_desc="开户银行的省份")
            self.click_element(loc=bank_address_province_loc, img_desc="开户银行的省份")

            self.wait_ele_visible(loc=bank_address_city_loc, img_desc="开户银行的市")
            self.click_element(loc=bank_address_city_loc, img_desc="开户银行的市")

            self.wait_ele_visible(loc=bank_address_district_loc, img_desc="开户银行的区")
            self.click_element(loc=bank_address_district_loc, img_desc="开户银行的区")

            self.wait_ele_visible(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")
            self.click_element(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")

            self.wait_ele_visible(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")
            self.click_element(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")

            self.wait_ele_visible(loc=Loc.card_username_input_loc, img_desc="持卡人姓名输入框")
            self.input_text(loc=Loc.card_username_input_loc, value=js_name, img_desc="持卡人姓名输入框")

            self.wait_ele_visible(loc=Loc.card_id_num_input_loc, img_desc="持卡人身份证号输入框")
            self.input_text(loc=Loc.card_id_num_input_loc, value=sf_id, img_desc="持卡人身份证号输入框")

            self.wait_ele_visible(loc=Loc.card_user_address_input_loc, img_desc="持卡人地址输入框")
            self.input_text(loc=Loc.card_user_address_input_loc, value=people_address, img_desc="持卡人地址输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.shop_head_person_same_img_loc, img_desc="门头照图片上传按钮")
            self.click_element(loc=Loc.shop_head_person_same_img_loc, img_desc="门头照图片上传按钮")
            upload(base_path + "\\门头.jpg")

            self.wait_ele_visible(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            self.click_element(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            upload(base_path + "\\店内.jpg")

            self.wait_ele_visible(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            self.click_element(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            upload(base_path + "\\收银台.jpg")

            self.wait_ele_visible(loc=Loc.business_license_loc, img_desc="营业执照图片上传按钮")
            self.click_element(loc=Loc.business_license_loc, img_desc="营业执照图片上传按钮")
            upload(base_path + "\\将营业执照.jpg")

            self.wait_ele_visible(loc=Loc.corporate_face_img_loc, img_desc="法人身份证人像面图片上传按钮")
            self.click_element(loc=Loc.corporate_face_img_loc, img_desc="法人身份证人像面图片上传按钮")
            upload(base_path + "\\身正.jpg")

            self.wait_ele_visible(loc=Loc.corporate_emblem_img_loc, img_desc="法人身份证国徽面图片上传按钮")
            self.click_element(loc=Loc.corporate_emblem_img_loc, img_desc="法人身份证国徽面图片上传按钮")
            upload(base_path + "\\身反.jpg")

            self.wait_ele_visible(loc=Loc.person_face_img_loc, img_desc="结算人身份证人像面图片上传按钮")
            self.click_element(loc=Loc.person_face_img_loc, img_desc="结算人身份证人像面图片上传按钮")
            upload(base_path + "\\身正1.jpg")

            self.wait_ele_visible(loc=Loc.person_emblem_img_loc, img_desc="结算人身份证国徽面图片上传按钮")
            self.click_element(loc=Loc.person_emblem_img_loc, img_desc="结算人身份证国徽面图片上传按钮")
            upload(base_path + "\\身反1.jpg")

            self.wait_ele_visible(loc=Loc.settlement_book_loc, img_desc="结算授权书照片上传按钮")
            self.click_element(loc=Loc.settlement_book_loc, img_desc="结算授权书照片上传按钮")
            upload(base_path + "\\授权书.jpg")

            self.wait_ele_visible(loc=Loc.bank_card_img_loc, img_desc="结算人银行卡正面图片上传按钮")
            self.click_element(loc=Loc.bank_card_img_loc, img_desc="结算人银行卡正面图片上传按钮")
            upload(base_path + "\\银行卡.jpg")

            self.wait_ele_visible(loc=Loc.person_same_save_loc, img_desc="保存按钮")
            self.click_element(loc=Loc.person_same_save_loc, img_desc="保存按钮")

            time.sleep(3)

            self.select_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            self.wait_ele_visible(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")
            self.click_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            time.sleep(2)

            self.wait_ele_visible(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")
            self.click_element(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")

            time.sleep(5)

        if jy_type == "企业对公":

            self.wait_ele_visible(loc=Loc.qiye_loc, img_desc="企业对公")
            self.click_element(loc=Loc.qiye_loc, img_desc="企业对公")

            self.wait_ele_visible(loc=Loc.credit_code_input_loc, img_desc="信用代码输入框")
            self.input_text(loc=Loc.credit_code_input_loc, value=credit_code, img_desc="信用代码输入框")

            self.wait_ele_visible(loc=Loc.shop_name_input_loc, img_desc="商户全称输入框")
            self.input_text(loc=Loc.shop_name_input_loc, value=shop_name, img_desc="商户全称输入框")

            self.wait_ele_visible(loc=Loc.shop_nickname_input_loc, img_desc="商户简称输入框")
            self.input_text(loc=Loc.shop_nickname_input_loc, value=shop_nickname, img_desc="商户简称输入框")

            self.wait_ele_visible(loc=Loc.shop_type_loc, img_desc="商户类型选择框")
            self.click_element(loc=Loc.shop_type_loc, img_desc="商户类型选择框")

            self.select_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=shop_type_name_loc, img_desc="商户类型")
            self.click_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=Loc.shop_area_loc, img_desc="商户地区选择框")
            self.click_element(loc=Loc.shop_area_loc, img_desc="商户地区选择框")

            self.wait_ele_visible(loc=shop_area_province_loc, img_desc="选择省份")
            self.click_element(loc=shop_area_province_loc, img_desc="选择省份")

            self.wait_ele_visible(loc=shop_area_city_loc, img_desc="选择市")
            self.click_element(loc=shop_area_city_loc, img_desc="选择市")

            self.wait_ele_visible(loc=shop_area_district_loc, img_desc="选择区")
            self.click_element(loc=shop_area_district_loc, img_desc="选择区")

            self.wait_ele_visible(loc=Loc.address_input_loc, img_desc="详细地址输入框")
            self.input_text(loc=Loc.address_input_loc, value=address, img_desc="详细地址输入框")

            self.wait_ele_visible(loc=Loc.rate_input_loc, img_desc="费率输入框")
            # self.double_click_element(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.clean_element_text(loc=Loc.rate_input_loc, img_desc="费率输入框")
            self.input_text(loc=Loc.rate_input_loc, value=rate, img_desc="费率输入框")

            self.scroll_up_down(img_desc="滑动一页")

            if pos is True:
                self.wait_ele_visible(loc=Loc.pos_loc, img_desc="pos机按钮")
                self.click_element(loc=Loc.pos_loc, img_desc="pos机按钮")

                self.wait_ele_visible(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.double_click_element(loc=Loc.debit_rate_input_loc, img_desc="借记卡费率输入框")
                self.input_text(loc=Loc.debit_rate_input_loc, value=debit_card_rate, img_desc="借记卡费率输入框")

                self.wait_ele_visible(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.double_click_element(loc=Loc.credit_rate_input_loc, img_desc="贷记卡费率输入框")
                self.input_text(loc=Loc.credit_rate_input_loc, value=credit_card_rate, img_desc="贷记卡费率输入框")

            else:
                pass

            self.wait_ele_visible(loc=Loc.corporate_name_input_loc, img_desc="法人姓名输入框")
            self.input_text(loc=Loc.corporate_name_input_loc, value=corporate_name, img_desc="法人姓名输入框")

            self.wait_ele_visible(loc=Loc.corporate_id_input_loc, img_desc="法人身份证号输入框")
            self.input_text(loc=Loc.corporate_id_input_loc, value=corporate_id, img_desc="法人身份证号输入框")

            self.wait_ele_visible(loc=Loc.e_mail_input_loc, img_desc="常用邮箱输入框")
            self.input_text(loc=Loc.e_mail_input_loc, value=e_mail, img_desc="常用邮箱输入框")

            self.wait_ele_visible(loc=Loc.alipay_name_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_name_input_loc, value=alipay_name, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.alipay_account_input_loc, img_desc="支付宝账号输入框")
            self.input_text(loc=Loc.alipay_account_input_loc, value=alipay_account, img_desc="支付宝账号输入框")

            self.wait_ele_visible(loc=Loc.wechat_num_input_loc, img_desc="微信号输入框")
            self.input_text(loc=Loc.wechat_num_input_loc, value=wechat_account, img_desc="微信号输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.bank_card_num_input_loc, img_desc="银行卡号输入框")
            self.input_text(loc=Loc.bank_card_num_input_loc, value=bank_card, img_desc="银行卡号输入框")

            self.wait_ele_visible(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")
            self.click_element(loc=Loc.kh_bank_loc, img_desc="开户银行选择框")

            self.wait_ele_visible(loc=bank_name_loc, img_desc="银行名称")
            self.click_element(loc=bank_name_loc, img_desc="银行名称")

            self.wait_ele_visible(loc=Loc.kh_address_loc, img_desc="开户地址选择框")
            self.click_element(loc=Loc.kh_address_loc, img_desc="开户地址选择框")

            self.wait_ele_visible(loc=bank_address_province_loc, img_desc="开户银行的省份")
            self.click_element(loc=bank_address_province_loc, img_desc="开户银行的省份")

            self.wait_ele_visible(loc=bank_address_city_loc, img_desc="开户银行的市")
            self.click_element(loc=bank_address_city_loc, img_desc="开户银行的市")

            self.wait_ele_visible(loc=bank_address_district_loc, img_desc="开户银行的区")
            self.click_element(loc=bank_address_district_loc, img_desc="开户银行的区")

            self.wait_ele_visible(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")
            self.click_element(loc=Loc.kh_zhi_bank_loc, img_desc="开户支行选择框")

            self.wait_ele_visible(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")
            self.click_element(loc=kh_zhi_bank_name_loc, img_desc="开户支行名称")

            self.wait_ele_visible(loc=Loc.company_name_input_loc, img_desc="企业名称输入框")
            self.input_text(loc=Loc.company_name_input_loc, value=company_name, img_desc="企业名称输入框")

            # self.wait_ele_visible(loc=Loc.corporate_id_input_loc, img_desc="法人身份证号输入框")
            # self.input_text(loc=Loc.corporate_id_input_loc, value=corporate_id, img_desc="法人身份证号输入框")
            #
            # self.wait_ele_visible(loc=Loc.corporate_name_input_loc, img_desc="法人姓名输入框")
            # self.input_text(loc=Loc.corporate_name_input_loc, value=corporate_name, img_desc="法人姓名输入框")

            self.wait_ele_visible(loc=Loc.corporate_address_input_loc, img_desc="法人地址输入框")
            self.input_text(loc=Loc.corporate_address_input_loc, value=people_address, img_desc="法人地址输入框")

            self.scroll_up_down(img_desc="滑动一页")

            self.wait_ele_visible(loc=Loc.shop_head_person_same_img_loc, img_desc="门头照图片上传按钮")
            self.click_element(loc=Loc.shop_head_person_same_img_loc, img_desc="门头照图片上传按钮")
            upload(base_path + "\\门头.jpg")

            self.wait_ele_visible(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            self.click_element(loc=Loc.shop_inner_img_loc, img_desc="店内图片上传按钮")
            upload(base_path + "\\店内.jpg")

            self.wait_ele_visible(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            self.click_element(loc=Loc.cash_img_loc, img_desc="收银台图片上传按钮")
            upload(base_path + "\\收银台.jpg")

            self.wait_ele_visible(loc=Loc.business_license_loc, img_desc="营业执照图片上传按钮")
            self.click_element(loc=Loc.business_license_loc, img_desc="营业执照图片上传按钮")
            upload(base_path + "\\将营业执照.jpg")

            self.wait_ele_visible(loc=Loc.corporate_face_img_loc, img_desc="法人身份证人像面图片上传按钮")
            self.click_element(loc=Loc.corporate_face_img_loc, img_desc="法人身份证人像面图片上传按钮")
            upload(base_path + "\\身正.jpg")

            self.wait_ele_visible(loc=Loc.corporate_emblem_img_loc, img_desc="法人身份证国徽面图片上传按钮")
            self.click_element(loc=Loc.corporate_emblem_img_loc, img_desc="法人身份证国徽面图片上传按钮")
            upload(base_path + "\\身反1.jpg")

            self.wait_ele_visible(loc=Loc.open_permit_img_loc, img_desc="开户许可证照片上传按钮")
            self.click_element(loc=Loc.open_permit_img_loc, img_desc="开户许可证照片上传按钮")
            upload(base_path + "\\开户许可证.jpg")

            self.wait_ele_visible(loc=Loc.person_same_save_loc, img_desc="保存按钮")
            self.click_element(loc=Loc.person_same_save_loc, img_desc="保存按钮")

            time.sleep(3)

            self.select_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            self.wait_ele_visible(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")
            self.click_element(loc=Loc.submit_audit_button_loc, img_desc="提交审核按钮")

            time.sleep(2)

            self.wait_ele_visible(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")
            self.click_element(loc=Loc.audit_sure_button_loc, img_desc="提交审核的确定按钮")

            time.sleep(5)

    def get_open_status(self):
        self.wait_ele_visible(loc=Loc.status_loc, img_desc="开户进件结果")
        text = self.get_text(loc=Loc.status_loc, img_desc="开户进件结果")
        return text
