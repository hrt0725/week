# -*- coding: utf-8 -*-
# @Time    : 2025/9/19 17:48
# @Author  : Lan
# @File    : test_index.py
# @Software: PyCharm
# @Description :

import unittest
from Utils.log_util import createLoger
from base.Browser import Browser
from page.page_index import PageIndex


class TestIndex(unittest.TestCase):

    def setUp(self):
        self.logger = createLoger()
        self.browser = Browser()
        self.logger.info("TestIndex setup")

    def tearDown(self):
        self.logger.info("TestIndex tearDown")
        self.browser.quit(5)

    def test_Index(self):
        self.logger.info("开始 test_Index")
        pi = PageIndex(self.browser)
        self.logger.info("开始 搜索商品")
        pi.search_goods("连衣裙")


if __name__ == '__main__':
    unittest.main()
