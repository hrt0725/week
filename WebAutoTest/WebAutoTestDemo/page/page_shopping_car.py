# -*- coding: utf-8 -*-
# @Time    : 2025/9/20 11:38
# @Author  : Lan
# @File    : page_shopping_car.py
# @Software: PyCharm
# @Description :

from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from base.Browser import Browser


class PageShoppingCar(BasePage):

    def __init__(self, browser: Browser):
        super().__init__(browser)

    loc_index_checkout_button = (By.CSS_SELECTOR, 'img[src$="checkout.gif"]')
    loc_index_continue_shopping_button = (By.CSS_SELECTOR, 'img[src$="continue.gif"]')

    def ele_check_button(self):
        self.elementClick(self.loc_index_checkout_button)

    def ele_continue_shopping_button(self):
        self.elementClick(self.loc_index_continue_shopping_button)
