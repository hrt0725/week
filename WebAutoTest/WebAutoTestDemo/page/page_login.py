# -*- coding: utf-8 -*-
# @Time    : 2025/9/18 18:33
# @Author  : Lan
# @File    : page_login.py
# @Software: PyCharm
# @Description :
from time import sleep

from selenium.webdriver.common.by import By

from Utils.Utils import captchaRecognition
from base.BasePage import BasePage
from base.Browser import Browser


class PageLogin(BasePage):
    LoginUrl = "http://127.0.0.1/upload/user.php"
    loc_login_username = (By.NAME, "username")
    loc_login_password = (By.NAME, "password")
    loc_login_remember = (By.ID, "remember")
    loc_login_captchaImg = (By.CSS_SELECTOR, "img[alt=captcha]")
    loc_login_captchaImgInput = (By.NAME, "captcha")
    loc_login_submit = (By.CLASS_NAME, "us_Submit")
    loc_login_assert_username = (By.CSS_SELECTOR, '#ECS_MEMBERZONE>a[href="user.php"]')

    def __init__(self, browser: Browser):
        super().__init__(browser)

    def ele_login_username(self, username: str):
        self.elementInput(self.loc_login_username, username)

    def ele_login_password(self, password: str):
        self.elementInput(self.loc_login_password, password)

    def ele_login_remember(self):
        self.elementClick(self.loc_login_remember)

    def ele_login_captcha(self):
        self.findElement(self.loc_login_captchaImg).screenshot("yzm.png")
        sleep(1)
        result = captchaRecognition("yzm.png")
        self.elementInput(self.loc_login_captchaImgInput, result)

    def ele_login_submit(self):
        self.elementClick(self.loc_login_submit)

    def get_assert_login(self):
        return self.eleGetText(self.loc_login_assert_username)

    def login(self, username, password):
        self.browser.openUrl(self.LoginUrl)
        self.ele_login_username(username)
        self.ele_login_password(password)
        self.ele_login_captcha()
        self.ele_login_submit()
        result = self.get_assert_login()
        return result
