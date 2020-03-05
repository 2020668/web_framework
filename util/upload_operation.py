# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/28

E-mail:keen2020@outlook.com

=================================


"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import win32gui
import win32con


# edit – combobox – comboboxex32 - #32770
# 前提 windows上传窗口 sleep2秒等待弹框的出现


def upload(file_path, browser_type="chrome"):
    if browser_type == "chrome":
        title = "打开"
    else:
        title = ""

    # 找元素
    # 一级窗口 "#32770", "打开"
    dialog = win32gui.FindWindow("#32770", title)
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级窗口,0代表从第一个开始找,后面是class和title
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级窗口
    # 编辑按钮
    edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)  # 四级窗口
    # 打开按钮
    button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")

    # 往编辑当中输入文件路径
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)  # 发送文件路径
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮


if __name__ == '__main__':

    time.sleep(3)
    upload("C:\\aow_drv.log")
