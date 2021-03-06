# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time
import os
import datetime

from common.dir_config import screenshot_dir
from common import logger


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self, loc, img_desc, timeout=30, frequency=0.5):
        start = datetime.datetime.now()  # 用datetime模块获取时间
        try:
            WebDriverWait(self.driver, timeout, frequency).until(ec.visibility_of_element_located(loc))
        except:
            # 日志
            logging.exception("等待元素 {} 可见 失败！".format(loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        else:
            end = datetime.datetime.now()  # 用datetime模块获取当前时间
            logging.info("等待 {}  元素  {} 可见成功。耗时：{}".format(img_desc, loc, end - start))

    # 等待元素存在
    def wait_ele_exists(self, loc, img_desc, timeout=30, frequency=0.5):
        start = datetime.datetime.now()  # 用datetime模块获取时间
        try:
            WebDriverWait(self.driver, timeout, frequency).until(ec.presence_of_element_located(loc))
        except:
            # 日志
            logging.exception("等待元素 {} 存在 失败！".format(loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        else:
            end = datetime.datetime.now()  # 用datetime模块获取当前时间
            logging.info("等待 {}  元素  {} 存在成功。耗时：{}".format(img_desc, loc, end - start))

    # 查找元素
    def get_element(self, loc, img_desc, find_all=False):
        """
        :param loc: 元组类型。元素定位表达式: (定位类型,定位表达式)
        :param img_desc: 截图命名
        :param find_all: 是否查找所有匹配的元素。为False表示只匹配一个。为True表示获取匹配所有。
        :return: Webelement对象。当find_all为True时，返回的是列表。
        """
        try:
            if find_all is True:
                ele = self.driver.find_elements(*loc)
            else:
                ele = self.driver.find_element(*loc)
        except:
            # 日志
            logging.exception("查找  {} 元素 {} 失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        else:
            logging.info("查找  {} 元素 {} 成功！".format(img_desc, loc))
            return ele

    # 元素可以是通过元素定位查找，也可以是直接是webElement对象。
    def _deal_element(self, loc, img_desc, timeout=30, frequency=0.5, wait_type="visible"):
        # 先等待可见,再查找元素
        if isinstance(loc, tuple):  # 元素定位表达式类型
            if wait_type == "visible":  # 等待元素可见
                self.wait_ele_visible(loc, img_desc, timeout, frequency)
            else:  # 等待元素存在
                self.wait_ele_exists(loc, img_desc, timeout, frequency)
            return self.get_element(loc, img_desc)
        elif isinstance(loc, WebElement):  # WebElement对象
            return loc
        else:
            logging.error("参数loc: {} 即不是元组，也不是WebElement对象，无法根据此参数找到元素。".format(loc))
            raise

    # 点击元素
    def click_element(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency)
        time.sleep(1)
        # 操作
        try:
            ele.click()  # 点击操作
            logging.info("点击  {} 元素 {} 成功！".format(img_desc, loc))
        except:
            # 日志
            logging.exception("点击  {} 元素 {} 失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    # 双击元素
    def double_click_element(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency)
        ac = ActionChains(driver=self.driver)
        # 操作
        try:
            ac.double_click(ele).perform()  # 双击操作
            logging.info("双击  {} 元素 {} 成功！".format(img_desc, loc))
        except:
            # 日志
            logging.exception("双击  {} 元素 {} 失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    # 清除文本
    def clean_element_text(self, loc, img_desc):
        ele = self.driver.find_element(*loc)
        # 操作
        try:
            ele.clear()  # 清除文本操作
            logging.info("清除  {} 元素的 文本 {} 成功！".format(img_desc, loc))
        except:
            # 日志
            logging.exception("清除  {} 元素 的文本 {} 失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    # 输入文本
    def input_text(self, loc, value, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency)
        # 操作
        try:
            ele.send_keys(value)  # 点击操作
            logging.info("在 {} 元素 {} 上输入文本值：{} 成功！".format(img_desc, loc, value))
        except:
            # 日志
            logging.exception("在 {} 元素 {} 上输入文本值：{} 失败！".format(img_desc, loc, value))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    def select_element(self, loc, img_desc, timeout=30, frequency=0.5):
        # ele = self._deal_element(loc, img_desc, timeout, frequency)
        ele = self.driver.find_element(*loc)
        # 操作
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
            logging.info("滑动到  {} 元素 {} 成功！".format(img_desc, loc))
        except:
            # 日志
            logging.exception("滑动到  {} 元素 {} 失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    def scroll_up_down(self, img_desc):
        time.sleep(1)
        # ele = self._deal_element(loc, img_desc, timeout, frequency)
        # 操作
        try:
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); ")
            self.driver.execute_script("window.scrollTo(0, 650); ")
            logging.info("滑动到  {} 元素 成功！".format(img_desc))
        except:
            # 日志
            logging.exception("滑动到  {} 元素 失败！".format(img_desc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        time.sleep(1)

    # 滑动到页面底部
    def scroll_to_page_down(self, img_desc):
        # ele = self._deal_element(loc, img_desc, timeout, frequency)
        # 操作
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); ")
            logging.info("滑动到  {} 元素 成功！".format(img_desc))
        except:
            # 日志
            logging.exception("滑动到  {} 元素 失败！".format(img_desc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        time.sleep(1)

    # 使用js滑动
    def scroll_up(self, img_desc):
        # ele = self._deal_element(loc, img_desc, timeout, frequency)
        # 操作
        try:
            self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0); ")
            logging.info("滑动到  {} 元素 成功！".format(img_desc))
        except:
            # 日志
            logging.exception("滑动到  {} 元素 失败！".format(img_desc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        time.sleep(1)

    # 获取元素的属性值
    def get_element_attribute(self, loc, attr_name, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency, wait_type="precence")
        # 获取属性
        try:
            attr_value = ele.get_attribute(attr_name)
        except:
            # 日志
            logging.exception("获取 {} 元素 {} 的属性 {} 失败！".format(img_desc, loc, attr_name))
            # 截图
            self.save_img(img_desc)
            raise
        else:
            logging.info("获取 {} 元素 {} 的属性 {} 值为:{}".format(img_desc, loc, attr_name, attr_value))
            return attr_value

    # 获取元素的文本值。
    def get_text(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency, wait_type="precence")
        # 获取属性
        try:
            text = ele.text
        except:
            # 日志
            logging.exception("获取 {} 元素 {} 的文本失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise
        else:
            logging.info("获取 {} 元素 {} 的文本值为:{}".format(img_desc, loc, text))
            return text

    # 获取隐藏元素的文本值。
    def get_hide_text(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency, wait_type="precence")
        # 获取属性
        try:
            text = ele.get_attribute("textContent")
        except:
            # 日志
            logging.exception("获取 {} 元素 {} 的文本失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise
        else:
            logging.info("获取 {} 元素 {} 的文本值为:{}".format(img_desc, loc, text))
        return text

    def save_img(self, img_description):
        """
        :param img_description: 图片的描述 。格式为 页面名称_功能名
        :return:
        """
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 时间戳 time模块  不要有:
        filepath = "{}_{}.png".format(img_description, now)
        img_path = os.path.join(screenshot_dir, filepath)
        try:
            self.driver.save_screenshot(img_path)
        except:
            logging.exception("网页截图失败！")
        else:
            logging.info("截图成功，截图存放在：{}".format(img_path))

    # toast获取
    def get_toast_msg(self, part_str, model_name="model"):
        xpath = '//*[contains(@text,"{}")]'.format(part_str)
        logging.info("获取toast信息，toast表达式为：{}".format(xpath))
        try:
            WebDriverWait(self.driver, 10, 0.01).until(ec.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element(By.XPATH, xpath)
        except:
            logging.exception("获取toast信息失败！！")
            raise

    # 获取设备的大小
    def get_device_size(self):
        try:
            size = self.driver.get_window_size()
            logging.info("当前设备的大小为：{}".format(size))
            return size
        except:
            logging.exception("获取设备大小失败。")
            raise

# class BasePage(object):
#
#     def __init__(self, driver: WebDriver):
#         self.driver = driver
#
#     # 等待元素可见
#     def wait_ele_visible(self, loc, img_desc, timeout=30, frequency=0.5):
#         start = datetime.datetime.now()  # 用datetime模块获取时间
#         try:
#             WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
#         except:
#             # 日志
#             logging.exception("等待元素 {} 可见 失败！".format(loc))
#             # 截图
#             self.save_img(img_desc)
#             raise  # 抛出异常，让用例识别到异常将用例状态为失败。
#         else:
#             end = datetime.datetime.now()  # 用datetime模块获取当前时间
#             logging.info("等待 {}  元素  {} 可见成功。耗时：{}".format(img_desc, loc, end - start))
#
#     # 等待元素存在
#     def wait_ele_exists(self, loc, img_desc, timeout=30, frequency=0.5):
#         start = datetime.datetime.now()  # 用datetime模块获取时间
#         try:
#             WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(loc))
#         except TimeoutError:
#             # 日志
#             logging.exception("等待元素 {} 存在 失败！".format(loc))
#             # 截图
#             self.save_img(img_desc)
#             raise  # 抛出异常，让用例识别到异常将用例状态为失败。
#         else:
#             end = datetime.datetime.now()  # 用datetime模块获取当前时间
#             logging.info("等待 {}  元素  {} 存在成功。耗时：{}".format(img_desc, loc, end - start))
#
#     # 查找元素
#     def get_element(self, loc, img_desc):
#         try:
#             ele = self.driver.find_element(*loc)
#         except:
#             # 日志
#             logging.exception("查找  {} 元素 {} 失败！".format(img_desc, loc))
#             # 截图
#             self.save_img(img_desc)
#             raise  # 抛出异常，让用例识别到异常将用例状态为失败。
#         else:
#             logging.info("查找  {} 元素 {} 成功！".format(img_desc, loc))
#             return ele
#
#     def click_element(self, loc, img_desc, timeout=30, frequency=0.5):
#         # 先等待可见
#         self.wait_ele_visible(loc, img_desc, timeout, frequency)
#         # 再查找元素
#         ele = self.get_element(loc, img_desc)
#         # 操作
#         try:
#             ele.click()  # 点击操作
#             logging.info("点击  {} 元素 {} 成功！".format(img_desc, loc))
#         except:
#             # 日志
#             logging.exception("点击  {} 元素 {} 失败！".format(img_desc, loc))
#             # 截图
#             self.save_img(img_desc)
#             raise  # 抛出异常，让用例识别到异常将用例状态为失败。
#
#     def input_text(self, loc, value, img_desc, timeout=30, frequency=0.5):
#         # 先等待可见
#         self.wait_ele_visible(loc, img_desc, timeout, frequency)
#         # 再查找元素
#         ele = self.get_element(loc, img_desc)
#         # 操作
#         try:
#             ele.send_keys(value)  # 点击操作
#             logging.info("在 {} 元素 {} 上输入文本值：{} 成功！".format(img_desc, loc, value))
#         except:
#             # 日志
#             logging.exception("在 {} 元素 {} 上输入文本值：{} 失败！".format(img_desc, loc, value))
#             # 截图
#             self.save_img(img_desc)
#             raise  # 抛出异常，让用例识别到异常将用例状态为失败。
#
#     # 获取元素的属性值
#     def get_element_attribute(self, loc, attr_name, img_desc, timeout=30, frequency=0.5):
#         self.wait_ele_exists(loc, img_desc, timeout, frequency)  # 等待元素存在
#         ele = self.get_element(loc, img_desc)  # 查找元素
#         # 获取属性
#         try:
#             attr_value = ele.get_attribute(attr_name)
#         except:
#             # 日志
#             logging.exception("获取 {} 元素 {} 的属性 {} 失败！".format(img_desc, loc, attr_name))
#             # 截图
#             self.save_img(img_desc)
#             raise
#         else:
#             logging.info("获取 {} 元素 {} 的属性 {} 值为:{}".format(img_desc, loc, attr_name, attr_value))
#             return attr_value
#
#     # 获取元素的文本值。
#     def get_text(self, loc, img_desc, timeout=30, frequency=0.5):
#         self.wait_ele_exists(loc, img_desc, timeout, frequency)  # 等待元素存在
#         ele = self.get_element(loc, img_desc)  # 查找元素
#         # 获取属性
#         try:
#             text = ele.text
#         except:
#             # 日志
#             logging.exception("获取 {} 元素 {} 的文本失败！".format(img_desc, loc))
#             # 截图
#             self.save_img(img_desc)
#             raise
#         else:
#             logging.info("获取 {} 元素 {} 的文本值为:{}".format(img_desc, loc, text))
#             return text
#
#     def save_img(self, img_description):
#         """
#         :param img_description: 图片的描述 。格式为 页面名称_功能名
#         :return:
#         """
#         now = time.strftime("%Y-%m-%d %H_%M_%S")
#         # 时间戳 time模块  不要有:
#         filepath = "{}_{}.png".format(img_description, now)
#         img_path = os.path.join(screenshot_dir, filepath)
#         try:
#             self.driver.save_screenshot(img_path)
#         except:
#             logging.exception("网页截图失败！")
#         else:
#             logging.info("截图成功，截图存放在：{}".format(img_path))
#
#     def switch_iframe(self, refrence, img_desc):
#         """
#         :param refrence: 识别iframe。可以是iframe的下标、name属性、WebElement对象、元组形式的定位表达。
#         :return: 无
#         """
#         try:
#             WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(refrence))
#         except:
#             # 日志
#             logging.exception("切换到 {} 的iframe: {} 失败！".format(img_desc, refrence))
#             # 截图
#             self.save_img(img_desc)
#             raise
#         else:
#             logging.exception("切换到 {} 的iframe: {} 成功！".format(img_desc, refrence))
