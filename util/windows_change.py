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
from selenium.webdriver.common.action_chains import ActionChains
import time


# 打开谷歌浏览器
driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
# 访问百度
driver.get("https://www.baidu.com")

# 获取当前窗口尺寸 调试用 与此处功能无关
size = driver.get_window_size()
print(size)

# 获取当前窗口
print(driver.current_window_handle)
# 打印全部窗口
wins = driver.window_handles
print(wins)


# 在搜索输入框输入 腾讯 并点击回车
driver.find_element_by_id("kw").send_keys("腾讯", Keys.ENTER)

# 点击腾讯视频官网
loc = By.XPATH, "//*[text()='视频 - 中国领先的在线视频媒体平台,海量高清视频在线观看']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 等待产生新窗口  注意窗口名称每次运行都会变化的 所以一般不使用窗口名称来切换
# time.sleep(3)
# 还可使用以下方法 等待新窗口产生 再执行后续操作
WebDriverWait(driver, 20).until(ec.new_window_is_opened(wins))


# 获取当前窗口
print(driver.current_window_handle)
# 打印全部窗口
wins = driver.window_handles
print(wins)

# 切换到新窗口 腾讯视频 网页
driver.switch_to.window(wins[-1])

time.sleep(1)

# 点击国漫
loc = By.XPATH, "//*[text()='国漫']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 切换回百度窗口 原来默认的窗口
# driver.switch_to.default_content()
driver.switch_to.window(wins[0])

time.sleep(2)

wins = driver.window_handles
print(wins)

# 点击 腾讯首页
loc = By.XPATH, "//*[text()='首页']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 等待产生新的窗口
WebDriverWait(driver, 20).until(ec.new_window_is_opened(wins))

wins = driver.window_handles
print(wins)

# 切换到新窗口 腾讯首页 网页 此时腾讯首页排在第三的位置
driver.switch_to.window(wins[2])

time.sleep(1)

# 点击娱乐
loc = By.XPATH, "//*[text()='娱乐']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()


time.sleep(10)

driver.quit()


