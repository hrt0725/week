# -*- coding: utf-8 -*-
# @Time    : 2025/09/26 17:31
# @Author  : Lan
# @File    : test_api_get_user_profile.py
# @Software: PyCharm
# @Description : create by script.CreateTestTemplate.py

import ddt
import pytest
import requests

from config.config import AppKey, API_GET_USER_PROFILE
from utils.assert_multi import caseAsserts
from utils.log_utils import createLoger


@ddt.ddt()
class TestApiGetUserProfile:

    def test_api_get_user_profile(self):
        loger = createLoger()
        # 处理数据
        caseData = {
            "data": {
                "app_key": AppKey,
                "uuid":"",
                "token":""
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
        loger.info("开始请求({})：{}".format(caseData["method"], API_GET_USER_PROFILE))
        loger.info("请求参数：{}".format(caseData["data"]))
        # 发送请求
        resultData = requests.request(method=caseData["method"], url=API_GET_USER_PROFILE, params=caseData["data"]).json()
        loger.info("请求结果：{}".format(resultData))
        # 断言
        caseAsserts(caseData["assert_info"], resultData)

if __name__ == '__main__':
    pytest.main()
