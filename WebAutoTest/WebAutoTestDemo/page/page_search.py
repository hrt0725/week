# -*- coding: utf-8 -*-
# @Time    : 2025/9/20 11:31
# @Author  : Lan
# @File    : page_search.py
# @Software: PyCharm
# @Description :
from time import sleep

from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from base.Browser import Browser


class PageSearch(BasePage):
    def __init__(self, browser: Browser):
        super().__init__(browser)

    loc_index_goods_items = (By.CLASS_NAME, "goodsItem")

    def ele_select_goods(self, index):
        self.findElements(self.loc_index_goods_items)[index].click()
        sleep(2)
