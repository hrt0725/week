# -*- coding: utf-8 -*-
# @Time    : 2025/9/28 15:54
# @Author  : Lan
# @File    : test_allure_user.py
# @Software: PyCharm
# @Description :
import allure
import pytest


@allure.feature("allure-用户模块")
class TestAllureUser:

    @allure.link("http://baidu.com")
    @allure.story("allure-用户登录")
    @allure.title("allure-用户登录成功")
    @pytest.mark.parametrize("username,password", zip(["tom", "jerry"], ["123", "qwe"]))
    def test_allure_demo_login(self, username, password):
        print("username:{};password{}".format(username, password))
        assert 2 == 2

    @allure.story("allure-用户注册")
    @allure.title("allure-用户注册成功")
    @pytest.mark.parametrize("username,password", zip(["tom", "jerry"], ["123", "qwe"]))
    def test_allure_demo_login(self, username, password):
        print("username:{};password{}".format(username, password))
        assert 2 == 2


if __name__ == '__main__':
    pass
