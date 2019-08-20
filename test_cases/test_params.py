# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/12
E-mail:keen2020@outlook.com
=================================

"""


import pytest


@pytest.mark.parametrize("a,b,c",[(1,3,4),(10,35,45),(22.22,22.22,44.44)])
def test_add(a,b,c):
    res = a + b
    assert res == c

