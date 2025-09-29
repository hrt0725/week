# -*- coding: utf-8 -*-
# @Time    : 2025/9/24 16:37
# @Author  : Lan
# @File    : test_api_register.py
# @Software: PyCharm
# @Description :
import allure
import ddt
import pytest
import requests
from cases.conftest import HostName
from config.config import getDataPath, AppKey, API_REGISTER
from utils.assert_multi import am, caseAsserts
from utils.common import get_nested_value
from utils.log_utils import createLoger
from utils.md5 import generateMD5


@ddt.ddt()
@allure.feature("用户模块")
class TestAPIRegister:
    @allure.story("用户注册")
    @allure.title("用户注册成功")
    @ddt.file_data(getDataPath().joinpath("api_register.yaml"))
    def test_api_register(self, **caseData):
        loger = createLoger()
        # 处理数据
        caseData["data"]["password"] = generateMD5(caseData["data"]["password"])
        caseData["data"]["app_key"] = AppKey
        # 处理数据
        loger.info("开始发送请求({})：{}".format(caseData["method"], API_REGISTER))
        loger.info("请求参数：{}".format(caseData["data"]))
        # 发送请求
        resultData = requests.request(method=caseData["method"], url=API_REGISTER, params=caseData["data"]).json()
        loger.info("请求结果：{}".format(resultData))
        # 断言
        caseAsserts(caseData["assert_info"], resultData)

        if __name__ == '__main__':
            pytest.main()
