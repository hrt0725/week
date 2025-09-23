# -*- coding: utf-8 -*-
# @Time    : 2025/9/23 09:58
# @Author  : Lan
# @File    : test_demo_1.py
# @Software: PyCharm
# @Description :
import pytest


def setup_module():
    print("setup_module")


def teardown_module():
    print("tear_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def test_aa():
    print("test aa")


class TestDemo1:

    def setup_class(self):
        print("setup class")

    def teardown_class(self):
        print("teardown class")

    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    def test_1(self):
        print("test1")
        assert True

    def test_2(self):
        print("test2")
        assert True


if __name__ == '__main__':
    pytest.main()
