# -*- coding: utf-8 -*-
# @Time    : 2025/9/18 15:42
# @Author  : Lan
# @File    : Browser.py
# @Software: PyCharm
# @Description :

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class Browser:

    def __init__(self, url="", browserName="Edge", delay=2):
        if browserName == "Edge":
            self.driver = webdriver.Edge()
        elif browserName == "Chrome":
            self.driver = webdriver.Chrome()
        elif browserName == "Firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        if url != "":
            self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        sleep(delay)

    def feById(self, id: str):
        return self.driver.find_element(By.ID, id)

    def feByName(self, name: str):
        return self.driver.find_element(By.NAME, name)

    def feByClassName(self, className: str):
        return self.driver.find_element(By.CLASS_NAME, className)

    def feByXPath(self, XPath: str):
        return self.driver.find_element(By.XPATH, XPath)

    def feByCssSelector(self, cssSelector: str):
        return self.driver.find_element(By.CSS_SELECTOR, cssSelector)

    def feByLinkText(self, text: str):
        return self.driver.find_element(By.LINK_TEXT, text)

    def fe(self, by: By, val: str):
        return self.driver.find_element(by, val)

    def fes(self, by: By, val: str):
        return self.driver.find_elements(by, val)

    def openUrl(self, url: str):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        return self

    def quit(self, delay=2):
        sleep(delay)
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    driver = Browser("http://127.0.0.1/upload/user.php")
