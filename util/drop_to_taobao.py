# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/3/7

E-mail:keen2020@outlook.com

=================================


"""


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


# 模拟鼠标操作-鼠标拖动-滑动验证码
driver = webdriver.Chrome()
driver.get("https://reg.taobao.com/member/reg/fill_mobile.htm")
driver.maximize_window()

# 点击确定按钮
element1 = driver.find_element_by_css_selector("#J_AgreementBtn")
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