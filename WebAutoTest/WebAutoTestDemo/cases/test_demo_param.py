# -*- coding: utf-8 -*-
# @Time    : 2025/9/23 17:38
# @Author  : Lan
# @File    : test_demo_param.py
# @Software: PyCharm
# @Description :
import pytest

username = ["tom", "jerry", "luck"]
password = ["111", "222", "333"]


class TestDemoParam:
    @pytest.mark.parametrize("username", ["tom", "jerry"])
    def test_login(self, username, session_fixture):
        print("test_login:{}".format(username))
        assert username == "jerry"

    @pytest.mark.parametrize("username,password", zip(username, password))
    def test_register(self, username, password):
        assert (username == "tom" and password == "111") or (username == "jerry" and password == "222") or (
                username == "luck" and password == "333")

    def test_order_info(self, order_info, session_fixture, send_data):
        print(order_info)
        print("=====================" + send_data)


if __name__ == '__main__':
    pytest.main([__file__])
