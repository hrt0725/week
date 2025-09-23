# -*- coding: utf-8 -*-
# @Time    : 2025/9/20 17:54
# @Author  : Lan
# @File    : test_faker.py
# @Software: PyCharm
# @Description :
import json
import unittest

from faker import Faker


class TestFaker(unittest.TestCase):
    def test_something(self):
        fk = Faker("zh-CN")

        userinfo = {
            "username": fk.user_name(),
            "email": fk.email()
        }
        print(json.dumps(userinfo))


if __name__ == '__main__':
    unittest.main()
