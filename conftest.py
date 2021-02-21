# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : conftest.py
import pytest
from calc import Calculator

@pytest.fixture(scope="module")
def calc():
    print("开始计算")
    yield
    print("计算结束")


@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc=Calculator()
    return calc


