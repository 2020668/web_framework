# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""

# 登录成功
success_data = [{"user": "18627787716", "pwd": "123456", "username": "测试管理员294"}]

# 手机号为空/密码为空/手机号格式不正确/非数字。。。。
invalid_data = [
    {"user": "18684720553", "passwd": "", "check": "请输入密码"},
    {"user": "", "passwd": "python", "check": "请输入手机号"},
    {"user": "1868472055", "passwd": "python", "check": "请输入正确的手机号"}
]

# 密码错误 /手机号未注册
