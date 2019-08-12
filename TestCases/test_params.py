# -*- encoding: utf-8 -*-
"""
@File    : test_params.py
@Time    : 2019/8/9 21:44
@Author  : 柠檬班-小简
@Email   : XXXX@163.com
@Company: 湖南省零檬信息技术有限公司
"""
import pytest


@pytest.mark.parametrize("a,b,c",[(1,3,4),(10,35,45),(22.22,22.22,44.44)])
def test_add(a,b,c):
    res = a + b
    assert res == c

