# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/3/7

E-mail:keen2020@outlook.com

=================================


"""


import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


def taobao():

    before = datetime.datetime.now()

    # 模拟鼠标操作-鼠标拖动-滑动验证码
    driver = webdriver.Chrome()
    driver.get("https://reg.taobao.com/member/reg/fill_mobile.htm")
    driver.maximize_window()

    # 点击确定按钮
    element1 = driver.find_element_by_css_selector("#J_AgreementBtn")
    loc = By.XPATH, "//button[@id='J_AgreementBtn']"
    element1.click()
    sleep(1)

    # 获取滑动条的size
    span_background = driver.find_element_by_css_selector("#nc_1__scale_text > span")
    span_background_size = span_background.size
    print(span_background_size)

    # 获取滑块的位置
    button = driver.find_element_by_css_selector("#nc_1_n1z")
    button_location = button.location
    print(button_location)

    # 拖动操作：drag_and_drop_by_offset
    # 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）
    x_location = button_location["x"] + span_background_size["width"]
    y_location = button_location["y"]
    ActionChains(driver).drag_and_drop_by_offset(button, x_location, y_location).perform()

    sleep(3)

    after = datetime.datetime.now()
    print("合计耗时{}".format(after - before))


def taobao1():

    before = datetime.datetime.now()

    # 模拟鼠标操作-鼠标拖动-滑动验证码
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 访问京东注册页面
    driver.get("https://reg.jd.com/reg/person?ReturnUrl=https%3A//www.jd.com/")

    # 点击确定按钮
    loc = By.XPATH, "//div[@class='protocol-button']//button"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()
    sleep(1)

    # 输入手机号
    loc = By.XPATH, "//txt[text()='建议使用常用手机号']"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).send_keys("18971335925")

    # 点击跳转滑动条的按钮
    loc = By.XPATH, "//div[@class='form-item form-item-getcode']"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()

    # 获取滑动条的size
    loc = By.XPATH, "//div[@id='nc_1__scale_text']"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    span_background = driver.find_element(*loc)
    span_background_size = span_background.size
    print(span_background_size)

    # 获取滑块的位置
    loc = By.XPATH, "//span[@id='nc_1_n1z']"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    button = driver.find_element(*loc)
    button_location = button.location
    print(button_location)

    # 拖动操作：drag_and_drop_by_offset
    # 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）
    x_location = button_location["x"] + span_background_size["width"]
    y_location = button_location["y"]
    ActionChains(driver).drag_and_drop_by_offset(button, x_location, y_location).perform()

    sleep(3)

    after = datetime.datetime.now()

    print("合计耗时:{}".format(after - before))


if __name__ == '__main__':
    taobao1()
