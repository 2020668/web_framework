# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/27

E-mail:keen2020@outlook.com

=================================


"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import datetime


"""
移动到元素element对象"底部" 与当前窗口的底部对齐
driver.execute_script("arguments[0].scrollIntoView(false);", element)

移动元素element对象的顶端与当前窗口的顶部对齐
driver.execute_script("arguments[0].scrollIntoView();", element)

移动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

移动到页面顶部
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

"""


# 在百度上搜索 汽车 然后练习使用js的滑动
def baidu_car():

    driver = webdriver.Chrome()

    driver.get("https://www.baidu.com")
    driver.maximize_window()

    driver.find_element_by_id("kw").send_keys("汽车", Keys.ENTER)
    # loc = By.XPATH, '//a[text()="之家_看车买车用车 都回"]'

    loc = By.XPATH, "//a[text()='_百度百科']"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    ele = driver.find_element(*loc)

    # 滑动到元素的底部
    driver.execute_script("arguments[0].scrollIntoView(false);", ele)

    time.sleep(3)

    # 滑动到页面底部
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(3)

    # 滑动到页面中部
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")

    time.sleep(3)

    # 滑动到页面顶部
    driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

    time.sleep(3)

    # 滑动指定距离
    driver.execute_script("window.scrollTo(0, 600);")

    time.sleep(3)

    driver.close()


# 由于12306网页做了限制  目前以下代码不可登录12306修改出发日期 但是使用方式是一样的
def demo_12306():
    # 12306 js修改日期输入框,可灵活更换日期(format) 或 a.value = arguments[0] driver.execute_script(js, "python当前时间")

    driver = webdriver.Chrome()

    driver.get("https://www.12306.cn")
    driver.maximize_window()

    js = """
    var a = document.getElementById("train_date");
    a.readOnly = false;
    a.value = arguments[0]
    
    """
    driver.execute_script(js, datetime.datetime.now().date() + datetime.timedelta(days=1))  # 明天

    driver.quit()


if __name__ == '__main__':
    baidu_car()
    # test_12306()
