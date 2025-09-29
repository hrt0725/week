# -*- coding: utf-8 -*-
# @Time    : 2025/9/26 17:34
# @Author  : Lan
# @File    : test_flow_user.py
# @Software: PyCharm
# @Description :
import allure
import requests

from config.config import API_LOGIN, AppKey, API_USER_CHECK
from utils.assert_multi import caseAssert
from utils.md5 import generateMD5

@allure.feature("流程测试")
class TestFlowUser:
    @allure.story("用户流程-登录-检查")
    def test_flow_user(self):
        """
        :param username
        :param passowrd
        :return:
        """
        loginData = {
            "app_key": AppKey,
            "username": "tom",
            "password": generateMD5("123")
        }
        loginResult = requests.request(method="POST", url=API_LOGIN, params=loginData).json()
        caseAssert(loginResult, "ret", 200)

        checkData = {
            "app_key": AppKey,
            "uuid": loginResult["data"]["uuid"],
            "token": loginResult["data"]["token"]
        }
        userCheckResult = requests.request(method="POST", url=API_USER_CHECK, params=checkData).json()
        caseAssert(userCheckResult, "ret", 200)


if __name__ == '__main__':
    pass
