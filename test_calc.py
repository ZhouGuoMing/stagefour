# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : test_calc.py
import allure
import pytest
import yaml

with open("./calc.yaml") as f:
    datas=yaml.safe_load(f)['calc']
    add_data=datas['adddatas']
    div_data=datas['divdatas']
    sub_data=datas['subdatas']
    mul_data=datas['muldatas']
    myid=datas['myid']

@pytest.fixture(params=add_data, ids=myid)
def get_adddatas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data

@pytest.fixture(params=div_data, ids=myid)
def get_divdatas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data

@pytest.fixture(params=sub_data, ids=myid)
def get_subdatas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data

@pytest.fixture(params=mul_data, ids=myid)
def get_muldatas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data
@allure.feature("测试计算器")
class TestCalc:
    @allure.story("测试加法")
    @pytest.mark.add
    @pytest.mark.run(order=1)
    def test_add(self,get_calc,get_adddatas,calc):
        #调用加法方法
        with allure.step("计算两个数的相加和"):
            result= get_calc.add(get_adddatas[0], get_adddatas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == get_adddatas[2]

    @allure.story("测试除法")
    @pytest.mark.div
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_divdatas):
        #调用除法方法
        with allure.step("计算两个数的相除商"):
            result = get_calc.div(get_divdatas[0], get_divdatas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相除结果之后写断言
        assert result == get_divdatas[2]

    @allure.story("测试减法")
    @pytest.mark.sub
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_subdatas):
        # 调用除法方法
        with allure.step("计算两个数的相减差"):
            result = get_calc.sub(get_subdatas[0], get_subdatas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相减结果之后写断言
        assert result == get_subdatas[2]

    @allure.story("测试乘法")
    @pytest.mark.mul
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_muldatas):
        # 调用除法方法
        with allure.step("计算两个数的相乘积"):
            result = get_calc.mul(get_muldatas[0], get_muldatas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相乘结果之后写断言
        assert result == get_muldatas[2]