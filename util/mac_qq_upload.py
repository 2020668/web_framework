# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/3/5

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
import os

from common.tools import upload_mac
from common.dir_config import testdatas_dir


def mac_upload():

    # 打开浏览器，访问网址
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 直接访问qq空间
    driver.get("https://user.qzone.qq.com/3023087535")

    time.sleep(8)

    # 点击相册按钮
    loc = By.XPATH, "//a[@title='相册']"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()

    time.sleep(3)

    # 切换iframe
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])

    time.sleep(3)

    # 点击上传照片按钮
    # loc = By.XPATH, "//a[text()='上传照片/视频']"
    loc = By.XPATH, "//div[@class='photo-op-item j-album-new-upload-btn']"
    WebDriverWait(driver, 20).until(ec.presence_of_element_located(loc))
    driver.find_element(*loc).click()

    time.sleep(3)

    # driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[1])

    # 退出iframe
    driver.switch_to.default_content()

    time.sleep(3)

    # driver.switch_to.frame("userData_iframe__Y_popTips")
    # time.sleep(3)

    driver.switch_to.frame("photoUploadDialog")

    time.sleep(3)

    # 点击 选择照片和视频 按钮
    # loc = By.XPATH, "//a[text()='选择照片和视频']"
    # loc = By.XPATH, "//a//input[@class='j-input-add']"
    loc = By.XPATH, "//a[@class='btn-select-img']"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()

    time.sleep(3)

    upload_mac(os.path.join(testdatas_dir, "demo.png"))

    loc = By.XPATH, "//a[@class='op-btn btn-upload j-btn-start j-uploading-hide']"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()

    time.sleep(3)

    driver.quit()


if __name__ == '__main__':
    # a = os.path.join(testdatas_dir, "demo.png")  "/Users/keen/PycharmProjects/web_framework/data/demo.png"
    # print(a)
    mac_upload()


