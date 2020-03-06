# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/3/6

E-mail:keen2020@outlook.com

=================================


"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from pykeyboard import PyKeyboard
from pymouse import PyMouse


k = PyKeyboard()
m = PyMouse()
file_path_heard = "/"

# 打开谷歌浏览器
driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
# 访问自己写的alert页面

time.sleep(5)

driver.get("file:/Users/keen/PycharmProjects/web_framework/util/alert.html")

# 点击弹框触发按钮
loc = By.XPATH, "//button"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 等待弹框出现
# time.sleep(1)
WebDriverWait(driver, 20).until(ec.alert_is_present())

time.sleep(3)

# Alert类的实例化
alert = driver.switch_to.alert
# 点击 accept
alert.accept()

# 也可直接点击Enter 关闭弹窗
# k.press_key('Return')

time.sleep(5)

driver.quit()

