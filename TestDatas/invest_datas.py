# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/12
E-mail:keen2020@outlook.com
=================================

"""

#投资成功
success={'money':1000}

#投资失败投标置灰  非100整数倍且大于100，非100整数倍且小于100，字母，符号
no10 =[{'money':456,'check':'请输入10的整数倍'},
              {'money':54,'check':'请输入10的整数倍'},
              {'money':'a','check':'请输入10的整数倍'},
              {'money':'$','check':'请输入10的整数倍'}
              ]

#投资失败弹框提示  负数100整数倍金额，0，空格，100整数倍且小于100,投标的金额大于标剩余金额，购买标的金额大于标总金额，投标金额大于可用金额
wrong_format_money =[{'money':-10,'check':'请正确填写投标金额'},
                    {'money':0,'check':'请正确填写投标金额'},
                    {'money':' ','check':'请正确填写投标金额'},
                    {'money':50,'check':'投标金额必须为100的倍数'},
                    ]

'''
  {'money':50000000,'check':'购买标的金额不能大于标剩余金额'},
            {'money':80000000,'check':'购买标的金额不能大于标总金额'},
            {'money':1000000000,'check':'投标金额大于可用金额'}
'''