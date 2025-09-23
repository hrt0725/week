# -*- coding: utf-8 -*-
# @Time    : 2025/9/23 11:08
# @Author  : Lan
# @File    : test_demo_one.py
# @Software: PyCharm
# @Description :
import pytest


class TestDemoOne:

    @pytest.mark.smoke
    def test_login(self):
        assert True

    def test_register(self):
        assert False

    @pytest.mark.flow
    def test_register_and_login(self):
        self.test_register()
        self.test_login()
