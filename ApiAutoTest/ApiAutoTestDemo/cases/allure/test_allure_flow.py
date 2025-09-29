# -*- coding: utf-8 -*-
# @Time    : 2025/9/28 17:12
# @Author  : Lan
# @File    : test_allure_flow.py
# @Software: PyCharm
# @Description :
import allure
import requests
from allure_commons.types import LinkType

from config.config import AppKey, API_LOGIN, API_USER_CHECK
from utils.assert_multi import caseAssert
from utils.md5 import generateMD5


@allure.feature("allure流程")
class TestAllureFlow:
    @allure.story("allure购物流程")
    def test_allure_flow_step(self):
        # 1.登录
        with allure.step("<1.登录>"):
            print("Testing allure flow step")
        # 2.搜索
        with allure.step("<2.搜索 >"):
            print("Testing allure flow step")
        # 3.加购
        with allure.step("<3.加购>"):
            print("Testing allure flow step")
        assert True

    @allure.story("allure购物流程api")
    @allure.link("http://baidu.com")
    def test_allure_flow_user_(self):
        # 1.登录
        with allure.step("<1.登录>"):
            loginData = {
                "app_key": AppKey,
                "username": "tom",
                "password": generateMD5("123")
            }
            loginResult = requests.request(method="POST", url=API_LOGIN, params=loginData).json()
            caseAssert(loginResult, "ret", 200)
            allure.attach.file(name="sea", source=r"C:\Users\Lan\Desktop\week\ApiAutoTest\ApiAutoTestDemo\data\sea.png",
                               attachment_type=allure.attachment_type.PNG)
            allure.attach(name="baidu", body="http://baidu.com")
        # 2.搜索
        with allure.step("<2.检查状态 >"):
            checkData = {
                "app_key": AppKey,
                "uuid": loginResult["data"]["uuid"],
                "token": loginResult["data"]["token"]
            }
            userCheckResult = requests.request(method="POST", url=API_USER_CHECK, params=checkData).json()
            caseAssert(userCheckResult, "ret", 200)
            allure.attach.file(r"C:\Users\Lan\Desktop\week\ApiAutoTest\ApiAutoTestDemo\pytest.ini")
            allure.link(url="http://baidu.com", link_type=LinkType.LINK, name="baidu")
