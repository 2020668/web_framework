# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/21
E-mail:keen2020@outlook.com
=================================

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
import logging
import time
import os
import datetime


# 打开浏览器，访问网址
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://test-agent.hczypay.com")
#
# loc = By.XPATH, "//input[@type='text']"
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).send_keys("18627787716")
#
# loc = By.XPATH, "//input[@type='password']"
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).send_keys("123456")
#
# loc = By.XPATH, "//span"
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
#
# time.sleep(8)
#
# driver.quit()


from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.oschina.net/blog")

time.sleep(5)


x = browser.get_window_size("current")
print(x)
browser.execute_script(
    "window.scrollTo(0, 600);")
# driver.execute_script(
#     "window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
time.sleep(3)
browser.close()
