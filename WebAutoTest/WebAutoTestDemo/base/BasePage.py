# -*- coding: utf-8 -*-
# @Time    : 2025/9/20 14:37
# @Author  : Lan
# @File    : BasePage.py
# @Software: PyCharm
# @Description :
from time import sleep

from selenium.webdriver.support.select import Select

from base.Browser import Browser


class BasePage:
    def __init__(self, browser: Browser):
        self.browser = browser

    def findElement(self, locator):
        return self.browser.fe(*locator)

    def findElements(self, locator):
        return self.browser.fes(*locator)

    def elementInput(self, locator, inputStr: str):
        self.findElement(locator).send_keys(inputStr)

    def elementClick(self, locator, delay=2):
        sleep(delay)
        self.findElement(locator).click()

    def eleSelectByIndex(self, locator, index):
        selectEle = self.findElement(locator)
        selectEleSelect = Select(selectEle)
        selectEleSelect.select_by_index(index)
 
    def eleGetText(self, locator):
        try:
            return self.findElement(locator).text
        except:
            return None

    def getAlertText(self, delay=1):
        sleep(delay)
        return self.browser.driver.switch_to.alert.text

    def alertAccept(self, delay=1):
        sleep(delay)
        self.browser.driver.switch_to.alert.accept()
        return self.getAlertText()

    def alertDismiss(self, delay=1):
        sleep(delay)
        self.browser.driver.switch_to.alert.dismiss()
        return self.getAlertText()

    def openUrl(self, url: str):
        self.browser.openUrl(url)
