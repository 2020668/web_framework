# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/27

E-mail:keen2020@outlook.com

=================================


"""


import time
# import win32gui
# import win32con
import cpca
import pyperclip
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import logging


from common import logger


# windows下上传文件 mac无法运行 请注释掉
# def upload_win(file_path, browser_type="chrome"):
#     time.sleep(1)
#     if browser_type == "chrome":
#         title = "打开"
#     else:
#         title = ""
#
#     # 找元素
#     # 一级窗口 "#32770", "打开"
#     dialog = win32gui.FindWindow("#32770", title)
#     ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)    # 二级窗口,0代表从第一个开始找,后面是class和title
#     ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)    # 三级窗口
#     # 编辑按钮
#     edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)       # 四级窗口
#     # 打开按钮
#     button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")
#
#     # 往编辑当中输入文件路径
#     win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)     # 发送文件路径
#     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)      # 点击打开按钮
#
#     logging.info("上传图片 {} 成功".format(file_path))


def upload_mac(file_path):

    k = PyKeyboard()
    m = PyMouse()
    file_path_heard = '/'
    # 利用 Command + Shift + G 组合调起文件路径输入框
    k.press_keys(['Command', 'Shift', 'G'])
    x_dim, y_dim = m.screen_size()
    m.click(x_dim // 2, y_dim // 2, 1)
    # 复制文件路径开头的斜杠/
    pyperclip.copy(file_path_heard)
    time.sleep(2)
    # 粘贴斜杠/
    k.press_keys(['Command', 'V'])
    time.sleep(2)
    # 输入文件全路径进去
    k.type_string(file_path)
    k.press_key('Return')
    time.sleep(2)
    k.press_key('Return')
    time.sleep(2)
    k.press_key('Return')
    time.sleep(2)


# 输入地址,自动获取省市区
def address_match(delivery_addresses):

    result = cpca.transform(delivery_addresses)
    r = result.to_dict("records")
    data0 = r[0]['省'].split("市")[0]
    data1 = r[0]["市"]
    data2 = r[0]["区"]
    return data0, data1, data2


if __name__ == '__main__':

    demo = "北京市东城区"
    province, city, area = address_match([demo])
    print(province, city, area)

