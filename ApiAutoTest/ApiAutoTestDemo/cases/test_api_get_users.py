# -*- coding: utf-8 -*-
# @Time    : 2025/09/26 16:22
# @Author  : Lan
# @File    : test_api_get_users.py
# @Software: PyCharm
# @Description : create by script.CreateTestTemplate.py

import ddt
import pytest
import requests

from config.config import AppKey, API_GET_USERS
from utils.assert_multi import caseAsserts
from utils.log_utils import createLoger


@ddt.ddt()
class TestApiGetUsers:

    def test_api_get_users(self):
        loger = createLoger()
        # 处理数据
        caseData = {
            "data": {
                "app_key": AppKey,
                "page": 3,
                "perpage": 20,
                "role": "all",
                "sort_type": 1
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

        # 处理数据
        loger.info("开始请求({})：{}".format(caseData["method"], API_GET_USERS))
        loger.info("请求参数：{}".format(caseData["data"]))
        # 发送请求
        resultData = requests.request(method=caseData["method"], url=API_GET_USERS, params=caseData["data"]).json()
        loger.info("请求结果：{}".format(resultData))
        # 断言
        caseAsserts(caseData["assert_info"], resultData)


if __name__ == '__main__':
    pytest.main()
