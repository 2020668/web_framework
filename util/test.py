# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/20
E-mail:keen2020@outlook.com
=================================

"""


import datetime
import time
import datetime
import os

# time = time.strftime("%Y%m%d%H%M%S")
# # print(time)
#
#
# from common.dir_config import testdatas_dir
#
# names = os.path.dirname(testdatas_dir)
#
# print(names)

now = datetime.datetime.now()
print(now)
for i in range(100):
    print("我爱你")
after = datetime.datetime.now()
delta = after - now
print(delta)
