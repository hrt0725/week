# -*- coding: utf-8 -*-
# @Time    : 2025/9/24 17:38
# @Author  : Lan
# @File    : conftest.py
# @Software: PyCharm
# @Description :


import pytest
import requests

from config.config import HostName, AppKey
from utils.log_utils import createLoger


@pytest.fixture(scope="function", autouse=True)
def beginTest():
    loger = createLoger()
    loger.info("{}开始{}".format("=" * 30, "=" * 30))
    yield loger
    loger.info("{}结束{}".format("=" * 30, "=" * 30))


@pytest.fixture(params=[("ad", "123")])
def register_data(request):
    return request.param


@pytest.fixture(params=[("tom", "123")])
def login_data(request):
    return request.param


@pytest.fixture()
def user_login(login_data):
    url = HostName + "/api/App/User/LoginExt"
    data = {
        "app_key": AppKey,
        "username": login_data[0],
        "password": login_data[1]
    }
    resultData = requests.post(url=url, params=data).json()
    return resultData
