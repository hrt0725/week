# -*- coding: utf-8 -*-
# @Time    : 2025/9/20 11:36
# @Author  : Lan
# @File    : page_goods_details.py
# @Software: PyCharm
# @Description :
from time import sleep

from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from base.Browser import Browser


class PageGoodsDetails(BasePage):

    def __init__(self, browser: Browser):
        super().__init__(browser)

    loc_index_buy_button = (By.CSS_SELECTOR, 'img[src$="goumai2.gif"]')

    def ele_buy_button(self):
        self.elementClick(self.loc_index_buy_button)
        sleep(2)
