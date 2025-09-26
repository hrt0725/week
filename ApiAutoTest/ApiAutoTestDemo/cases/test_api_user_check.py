# -*- coding: utf-8 -*-
# @Time    : 2025/09/26 13:59
# @Author  : Lan
# @File    : test_api_user_check.py
# @Software: PyCharm
# @Description :

import ddt
import pytest
import requests

from config.config import AppKey, API_USER_CHECK
from utils.assert_multi import caseAsserts
from utils.log_utils import createLoger


@ddt.ddt()
class TestApiUserCheck:

    def test_api_user_check_success(self, user_login):
        loger = createLoger()
        # 数据处理
        caseData = {
            "data": {
                "app_key": AppKey,
                "uuid": user_login["data"]["uuid"],
                "token": user_login["data"]["token"]
            },
            "method": "POST",
            "assert_info": [
                {
                    "key": "ret",
                    "expect_value": 200,
                    "assert_method": "equal"
                }
            ]
        }
        # 数据处理
        loger.info("开始请求({})：{}".format(caseData["method"], API_USER_CHECK))
        loger.info("请求参数：{}".format(caseData))
        # 发送请求
        resultData = requests.request(method=caseData["method"], url=API_USER_CHECK, params=caseData["data"]).json()
        loger.info("请求结果：{}".format(resultData))
        # 断言
        caseAsserts(caseData["assert_info"], resultData)

    def test_api_user_check_uuid_none(self, user_login):
        loger = createLoger()
        # 数据处理
        caseData = {
            "data": {
                "app_key": AppKey,
                "uuid": "",
                "token": user_login["data"]["token"]
            },
            "method": "POST",
            "assert_info": [
                {
                    "key": "ret",
                    "expect_value": 400,
                    "assert_method": "equal"
                }
            ]
        }
        # 数据处理
        loger.info("开始请求({})：{}".format(caseData["method"], API_USER_CHECK))
        loger.info("请求参数：{}".format(caseData))
        # 发送请求
        resultData = requests.request(method=caseData["method"], url=API_USER_CHECK, params=caseData["data"]).json()
        loger.info("请求结果：{}".format(resultData))
        # 断言
        caseAsserts(caseData["assert_info"], resultData)


if __name__ == '__main__':
    pytest.main()
