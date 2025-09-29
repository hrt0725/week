# -*- coding: utf-8 -*-
# @Time    : 2025/9/24 16:24
# @Author  : Lan
# @File    : test_api_login.py
# @Software: PyCharm
# @Description :
import allure
import ddt
import pytest
import requests

from config.config import AppKey, getDataPath, API_LOGIN
from utils.assert_multi import caseAsserts
from utils.log_utils import createLoger
from utils.md5 import generateMD5


@ddt.ddt()
@allure.feature("用户模块")
class TestAPILogin:

    @allure.story("用户登录")
    @allure.title("用户登录成功")
    @ddt.file_data(getDataPath().joinpath("api_login.yaml"))
    def test_login_success(self, **caseData):
        loger = createLoger()
        # 数据处理
        caseData["data"]["app_key"] = AppKey
        caseData["data"]["password"] = generateMD5(caseData["data"]["password"])
        # 数据处理
        loger.info("开始请求({})：{}".format(caseData["method"], API_LOGIN))
        loger.info("请求参数：{}".format(caseData["data"]))
        resultData = requests.request(method=caseData["method"], url=API_LOGIN, params=caseData["data"]).json()
        loger.info("请求结果：{}".format(resultData))
        caseAsserts(caseData["assert_info"], resultData)


if __name__ == '__main__':
    pytest.main()
