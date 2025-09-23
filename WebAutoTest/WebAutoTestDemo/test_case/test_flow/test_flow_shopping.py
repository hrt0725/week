# -*- coding: utf-8 -*-
# @Time    : 2025/9/20 11:01
# @Author  : Lan
# @File    : test_flow_shopping.py
# @Software: PyCharm
# @Description : 

import unittest
from time import sleep

from base.Browser import Browser
from page.page_goods_details import PageGoodsDetails
from page.page_index import PageIndex
from page.page_login import PageLogin
from page.page_payment import PagePayment
from page.page_search import PageSearch
from page.page_shopping_car import PageShoppingCar


class TestFlowShopping(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()

    def tearDown(self):
        self.browser.quit(5)

    def test_flow_shopping(self):
        pl = PageLogin(self.browser)
        pl.login("thr", "123")
        sleep(2)
        pi = PageIndex(self.browser)
        pi.search_goods("连衣裙")

        ps = PageSearch(self.browser)
        ps.ele_select_goods(0)

        pgd = PageGoodsDetails(self.browser)
        pgd.ele_buy_button()

        psg = PageShoppingCar(self.browser)
        psg.ele_check_button()

        pp = PagePayment(self.browser)
        pp.ele_select_shipping()
        pp.ele_select_payment()
        pp.ele_submit()


if __name__ == '__main__':
    unittest.main()
