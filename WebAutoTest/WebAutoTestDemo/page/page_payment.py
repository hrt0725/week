# -*- coding: utf-8 -*-
# @Time    : 2025/9/20 11:41
# @Author  : Lan
# @File    : page_payment.py
# @Software: PyCharm
# @Description :
from time import sleep

from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from base.Browser import Browser


class PagePayment(BasePage):

    def __init__(self, browser: Browser):
        super().__init__(browser)

    loc_index_shipping_radio = (By.NAME, 'shipping')
    loc_index_payment_radio = (By.NAME, 'payment')
    loc_index_submit = (By.CSS_SELECTOR, 'input[src$="bnt_subOrder.gif"]')

    def ele_select_shipping(self, index=0):
        self.findElements(self.loc_index_shipping_radio)[index].click()

    def ele_select_payment(self, index=0):
        self.findElements(self.loc_index_payment_radio)[index].click()

    def ele_submit(self):
        self.findElement(self.loc_index_submit).click()
        sleep(2)
