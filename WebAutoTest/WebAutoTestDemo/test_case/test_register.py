# -*- coding: utf-8 -*-
# @Time    : 2025/9/19 10:02
# @Author  : Lan
# @File    : test_register.py
# @Software: PyCharm
# @Description : 

import unittest

from Utils.Utils import getRandomStr
from base.Browser import Browser
from page.page_register import PageRegister


class TestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = Browser()

    def tearDown(self):
        self.driver.quit(5)

    def test_register_success(self):
        pr = PageRegister(self.driver)
        userRegisterInfo = {
            "username": getRandomStr(10),
            "email": "{}@163.com".format(getRandomStr(7)),
            "password": "123123",
            "confirm_password": "123123",
            "extend_field1": "1325@163.com",
            "extend_field2": "18756325413",
            "extend_field3": "18756325414",
            "extend_field4": "18756325412",
            "extend_field5": "18756325412",
            "sel_question_index": 1,
            "passwd_answer": "answer11",
        }

        result = pr.register(isClickBtn=True, **userRegisterInfo)
        self.assertEqual("* 可以注册", result.get("username_notice"))
        self.assertEqual("* 可以注册", result.get("email_notice"))
        self.assertEqual("* 可以注册", result.get("password_notice"))
        self.assertEqual("* 可以注册", result.get("conform_password_notice"))
        print(result)


if __name__ == '__main__':
    unittest.main()
