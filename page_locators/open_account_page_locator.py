# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/25

E-mail:keen2020@outlook.com

=================================


"""

from selenium.webdriver.common.by import By


class OpenAccountPageLocator(object):
    # 手机号码输入框
    phone_input_loc = By.XPATH, "//input[@placeholder='请输入商户的手机号码']"

    # 测试管理员294（自己）
    self_loc = By.XPATH, "//label[text()= ('测试管理员294（自己）')]"

    # 其他合伙人人
    other_loc = By.XPATH, "//label[text()= ('其它合伙人')]"

    # 下一步
    next_step_loc = By.XPATH, "//span[text()= ('下一步')]"

    # 小微商户
    xiaowei_loc = By.XPATH, "//p[text()=('小微商户')]//following-sibling::p[text()='选择']"

    # 个体工商，结算同法人
    geti_same_loc = By.XPATH, "//p[text()=('个体工商户-结算同法人')]//following-sibling::p[text()='选择']"

    # 个体工商，结算非法人
    geti_different_loc = By.XPATH, "//p[text()=('个体工商户-结算非法人')]//following-sibling::p[text()='选择']"

    # 企业对公
    qiye_loc = By.XPATH, "//p[text()=('企业对公')]//following-sibling::p[text()='选择']"

    # 企业对私 结算同法人
    qiye_geti_same_loc = By.XPATH, "//p[text()=('企业对私-结算同法人')]//following-sibling::p[text()='选择']"

    # 企业对私 结算非法人
    qiye_geti_different_loc = By.XPATH, "//p[text()=('企业对私-结算非法人')]//following-sibling::p[text()='选择']"

    # 信用代码
    credit_code_input_loc = By.XPATH, "//input[@placeholder='请输入营业执照统一信用代码']"

    # 商户全称输入框
    shop_name_input_loc = By.XPATH, "//input[@placeholder='请输入商户全称']"

    # 商户简称输入框
    shop_nickname_input_loc = By.XPATH, "//input[@placeholder='请输入商户简称']"

    # 商户类型
    shop_type_loc = By.XPATH, "//span[@class='ivu-select-placeholder']"

    # 商户类型名称
    # shop_type_name_loc = By.XPATH, "//li[text()='休闲娱乐']"

    # 商户地区选择框
    shop_area_loc = By.XPATH, "//label[text()='商户地区']//following-sibling::*//div[@class='ivu-cascader-label']"

    # 省
    shop_area_province_loc = By.XPATH, "//label[text()='商户地区']//following-sibling::*//li[" \
                                       "@class='ivu-cascader-menu-item' and contains(text(),'北京')]"

    # 市
    shop_area_city_loc = By.XPATH, "//label[text()='商户地区']//following-sibling::*//li[contains(text(),'北京市') and " \
                                   "@class='ivu-cascader-menu-item']"

    # 区
    shop_area_district_loc = By.XPATH, "//label[text()='商户地区']//following-sibling::*//li[contains(text(),'东城区') and " \
                                       "@class='ivu-cascader-menu-item']"

    # 详细地址输入框
    address_input_loc = By.XPATH, "//input[@placeholder='请输入详细地址']"

    # 商户费率输入框
    rate_input_loc = By.XPATH, "//input[@placeholder='请输入商户费率']"

    # pos机按钮
    pos_loc = By.XPATH, "//span[text()='关闭']"

    # 法人姓名输入框
    corporate_name_input_loc = By.XPATH, "//input[@placeholder='请输入法人姓名']"

    # 法人身份证号输入框
    corporate_id_input_loc = By.XPATH, "//input[@placeholder='请输入法人身份证号']"

    # 借记卡费率输入框
    debit_rate_input_loc = By.XPATH, "//input[@placeholder='请输入借记卡费率']"

    # 借记卡费率输入框
    credit_rate_input_loc = By.XPATH, "//input[@placeholder='请输入贷记卡费率']"

    # 结算人姓名输入框
    js_name_input_loc = By.XPATH, "//input[@placeholder='请输入结算人姓名']"

    # 结算人身份证号输入框
    js_id_num_input_loc = By.XPATH, "//input[@placeholder='请输入结算人身份证号']"

    # 常用邮箱输入框
    e_mail_input_loc = By.XPATH, "//input[@placeholder='请输入常用邮箱']"

    # 支付宝名称输入框
    alipay_name_input_loc = By.XPATH, "//input[@placeholder='请输入支付宝名称']"

    # 支付宝账号输入框
    alipay_account_input_loc = By.XPATH, "//input[@placeholder='请输入支付宝账号']"

    # 微信号输入框
    wechat_num_input_loc = By.XPATH, "//input[@placeholder='请输入微信号']"

    # 银行卡号输入框
    bank_card_num_input_loc = By.XPATH, "//input[@placeholder='请输入银行卡号']"

    # 开户银行选择框
    kh_bank_loc = By.XPATH, "//label[text()='开户银行']//following-sibling::*//input[@placeholder='请选择']"

    # 银行名称
    bank_name_loc = By.XPATH, "//li[text()='中国工商银行']"

    # 开户地址选择框
    kh_address_loc = By.XPATH, "//label[text()='开户地址']//following-sibling::*//div[@class='ivu-cascader-label']"

    # 省
    kh_province_loc = By.XPATH, "//label[text()='开户地址']//following-sibling::*//li[@class='ivu-cascader-menu-item' " \
                                "and contains(text(),'北京')]"

    # 市
    kh_city_loc = By.XPATH, "//label[text()='开户地址']//following-sibling::*//li[contains(text(),'北京市') and " \
                            "@class='ivu-cascader-menu-item']"

    # 区
    kh_district_loc = By.XPATH, "//label[text()='开户地址']//following-sibling::*//li[contains(text(),'东城区') and " \
                                "@class='ivu-cascader-menu-item']"

    # 开户支行选择框
    kh_zhi_bank_loc = By.XPATH, "//label[text()='开户支行']//following-sibling::*//input[@placeholder='请选择']"

    # 支行名称
    kh_zhi_bank_name_loc = By.XPATH, "//li[text()='中国工商银行北京新中街支行']"

    # 企业名称输入框
    company_name_input_loc = By.XPATH, "//input[@placeholder='请输入企业名称']"

    # 持卡人姓名输入框
    card_username_input_loc = By.XPATH, "//input[@placeholder='请输入持卡人姓名']"

    # 持卡人身份证号输入框
    card_id_num_input_loc = By.XPATH, "//input[@placeholder='请输入持卡人身份证号']"

    # 持卡人地址输入框
    card_user_address_input_loc = By.XPATH, "//input[@placeholder='请输入持卡人地址']"

    # 法人地址输入框
    corporate_address_input_loc = By.XPATH, "//input[@placeholder='请输入法人地址']"

    # 结算人站店铺门头照上传按钮
    shop_head_img_loc = By.XPATH, "//p[text()='结算人站店铺门头照']//preceding-sibling::*//img[contains(@src,'png')]"

    # 门头照上传
    shop_head_person_same_img_loc = By.XPATH, "//p[text()='店铺门头照片']//preceding-sibling::*//img[contains(@src,'png')]"

    # 店内照片按钮
    shop_inner_img_loc = By.XPATH, "//p[text()='店内照片']//preceding-sibling::*//img[contains(@src,'png')]"

    # 收银台照片按钮
    cash_img_loc = By.XPATH, "//p[text()='收银台照片']//preceding-sibling::*//img[contains(@src,'png')]"

    # 手持身份证按钮
    hand_card_img_loc = By.XPATH, "//p[text()='手持身份证照片']//preceding-sibling::*//img[contains(@src,'png')]"

    # 营业执照照片上传按钮
    business_license_loc = By.XPATH, "//p[text()='营业执照照片']//preceding-sibling::*//img[contains(@src,'png')]"

    # 结算人身份证人像面
    person_face_img_loc = By.XPATH, "//p[text()='结算人身份证人像面']//preceding-sibling::*//img[contains(@src,'png')]"

    # 法人身份证人像面
    corporate_face_img_loc = By.XPATH, "//p[text()='法人身份证人像面']//preceding-sibling::*//img[contains(@src,'png')]"

    # 结算人身份证国徽面
    person_emblem_img_loc = By.XPATH, "//p[text()='结算人身份证国徽面']//preceding-sibling::*//img[contains(@src,'png')]"

    # 法人身份证国徽面
    corporate_emblem_img_loc = By.XPATH, "//p[text()='法人身份证国徽面']//preceding-sibling::*//img[contains(@src,'png')]"

    # 授权书
    settlement_book_loc = By.XPATH, "//p[text()='授权结算书照片']//preceding-sibling::*//img[contains(@src,'png')]"

    # 开户许可证
    open_permit_img_loc = By.XPATH, "//p[text()='开户许可证照片']//preceding-sibling::*//img[contains(@src,'png')]"

    # 结算人银行卡正面照片
    bank_card_img_loc = By.XPATH, "//p[text()='结算人银行卡正面照片']//preceding-sibling::*//img[contains(@src,'png')]"

    # 法人银行卡正面照片
    corporate_bank_card_img_loc = By.XPATH, "//p[text()='法人银行卡正面照片']//preceding-sibling::*//img[contains(@src,'png')]"

    # 保存按钮
    save_loc = By.XPATH, "//button[@class='btn btn-save ivu-btn ivu-btn-warning']//span[text()='保存']"

    # 个体工商户结算同法人的保存按钮
    person_same_save_loc = By.XPATH, "//span[text()='保存']//parent::button[@class='btn btn-save ivu-btn ivu-btn-warning']"

    # 提交审核
    submit_audit_button_loc = By.XPATH, "//span[text()='提交审核']//parent::button" \
                                        "[@class='btn btn-save ivu-btn ivu-btn-warning']"

    # 确定
    audit_sure_button_loc = By.XPATH, "//button[@class='ivu-btn ivu-btn-primary']//span[text()='确定']"

    # 状态
    status_loc = By.XPATH, "//p[@class='success']"
