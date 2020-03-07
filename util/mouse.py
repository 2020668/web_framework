# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/3/7

E-mail:keen2020@outlook.com

=================================


"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


"""
百度首页 将鼠标悬浮到设置上 然后点击 高级搜索 搜索设置页 文本格式下拉框 选择
"""


# 打开谷歌浏览器
driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
# 访问百度
driver.get("https://www.baidu.com")

# 先等待元素出现 并找到该元素 生成元素对象
loc = By.XPATH, "//div[@id='u1']//a[@name='tj_settingicon']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
ele = driver.find_element(*loc)

# 实例化 Actionchains
ac = ActionChains(driver)
# 悬浮操作  也可在悬浮的同时对该元素执行其他操作 如 click
ac.move_to_element(ele)
# 执行鼠标操作  此时不要人为的去移动鼠标
ac.perform()

time.sleep(2)

# 点击高级搜索
loc = By.XPATH, "//a[text()='高级搜索']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

time.sleep(3)

# 先找到select元素 下拉框
loc = By.XPATH, '//select[@name="ft"]'
WebDriverWait(driver, 10).until(ec.visibility_of_element_located(loc))
select_ele = driver.find_element(*loc)

# 实例化Select类
s = Select(select_ele)

# 通过下标来选
s.select_by_index(4)
time.sleep(3)

# 通过value选择
s.select_by_value('all')
time.sleep(3)

# 通过文本选择
s.select_by_visible_text('Adobe Acrobat PDF (.pdf)')
time.sleep(3)
driver.quit()

time.sleep(10)

driver.quit()
