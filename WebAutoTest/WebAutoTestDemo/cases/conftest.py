# -*- coding: utf-8 -*-
# @Time    : 2025/9/24 10:54
# @Author  : Lan
# @File    : conftest.py
# @Software: PyCharm
# @Description :
import time

import pytest


@pytest.fixture()
def order_info():
    print("----order_info")
    datas = {'orderId":"2012912001"，"price":"188999.99"，"msg': "订单已完成", "orderStatus": "已支付"}
    return datas


@pytest.fixture(scope="session")
def session_fixture():
    print("begin session fixture")
    yield
    print("end session fixture")


@pytest.fixture(scope="function", autouse=True)
def timer(request):
    startTime = time.time()
    yield
    endTime = time.time()
    print("{}:执行时间：{:.6f}".format(request.function.__name__, endTime - startTime))


@pytest.fixture(params=['open', 'close', 'fixed'])
def send_data(request):
    return request.param
