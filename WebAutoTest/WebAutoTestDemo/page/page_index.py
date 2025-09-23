# -*- coding: utf-8 -*-
# @Time    : 2025/9/19 16:49
# @Author  : Lan
# @File    : page_index.py
# @Software: PyCharm
# @Description :
from time import sleep

from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from base.Browser import Browser


class PageIndex(BasePage):
    def __init__(self, browser: Browser):
        super().__init__(browser)

    IndexUrl = "http://127.0.0.1/upload/"
    loc_index_keywordInput = (By.ID, "keyword")
    loc_index_searchBtn = (By.CSS_SELECTOR, ".ipt2>input[name=imageField]")

    def ele_search_input(self, keyword):
        self.elementInput(self.loc_index_keywordInput, keyword)

    def ele_search_button(self):
        self.elementClick(self.loc_index_searchBtn)

    def search_goods(self, keyword):
        self.browser.openUrl(self.IndexUrl)
        self.ele_search_input(keyword)
        self.ele_search_button()
        sleep(2)
