# -*- coding: utf-8 -*-
# @Time    : 2025/9/20 16:19
# @Author  : Lan
# @File    : test_ddt_demo.py
# @Software: PyCharm
# @Description :

import unittest

import ddt
from base.Config import getDataPath


@ddt.ddt
class TestDdtDemo(unittest.TestCase):

    @ddt.data("11", "22")
    def test_ddt_1(self, p1):
        print("{}".format(p1))

    @ddt.data(("1", "11"), ("2", "22"))
    @ddt.unpack
    def test_ddt_2(self, p1, p2):
        print(f"{p1}-{p2}")

    @ddt.file_data(getDataPath().joinpath("login_data.json"))
    def test_ddt_login(self, username, password):
        print(f"{username}-{password}")


if __name__ == '__main__':
    unittest.main()
