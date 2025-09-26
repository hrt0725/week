# -*- coding: utf-8 -*-
# @Time    : 2025/9/24 16:58
# @Author  : Lan
# @File    : test_get_last_login_user.py
# @Software: PyCharm
# @Description : 
import ddt
import pytest
import requests

from config.config import AppKey, getDataPath, API_GET_LAST_LOGIN_USER
from utils.assert_multi import caseAsserts
from utils.log_utils import createLoger


@ddt.ddt
class TestGetLastLoginUser:
    @ddt.file_data(getDataPath().joinpath("api_get_last_login_user.yaml"))
    def test_get_last_login_user(self, **caseData):
        loger = createLoger()
        # 数据处理
        caseData["data"]["app_key"] = AppKey
        # 数据处理
        loger.info("开始请求({})：{}".format(caseData["method"], API_GET_LAST_LOGIN_USER))
        loger.info("请求参数：{}".format(caseData["data"]))
        # 发送请求
        resultData = requests.request(method=caseData["method"],
                                      url=API_GET_LAST_LOGIN_USER,
                                      params=caseData["data"]).json()
        print() or print(resultData)
        for item in resultData["data"]["members"]:
            print(item)
        loger.info("请求结果：{}".format(resultData))
        # 断言
        caseAsserts(caseData["assert_info"], resultData)


if __name__ == '__main__':
    pytest.main()
