# -*- coding: utf-8 -*-
# @Time    : 2025/9/19 09:55
# @Author  : Lan
# @File    : page_register.py
# @Software: PyCharm
# @Description :
from selenium.webdriver.common.by import By

from Utils.Utils import captchaRecognition
from base.BasePage import BasePage
from base.Browser import Browser


class PageRegister(BasePage):

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.__notice_assert = {
            "alertMsg": "",
            "registerUserName": "",
            "username_notice": "",
            "email_notice": "",
            "password_notice": "",
            "conform_password_notice": ""
        }

    RegisterUrl = "http://127.0.0.1/upload/user.php?act=register"
    loc_register_username = (By.NAME, "username")
    loc_register_email = (By.NAME, "email")
    loc_register_password = (By.NAME, "password")
    loc_register_confirm_password = (By.NAME, "confirm_password")
    loc_register_extend_field1 = (By.NAME, "extend_field1")
    loc_register_extend_field2 = (By.NAME, "extend_field2")
    loc_register_extend_field3 = (By.NAME, "extend_field3")
    loc_register_extend_field4 = (By.NAME, "extend_field4")
    loc_register_extend_field5 = (By.NAME, "extend_field5")
    loc_register_sel_question = (By.NAME, "sel_question")
    loc_register_passwd_answer = (By.NAME, "passwd_answer")
    loc_register_captchaImg = (By.CSS_SELECTOR, "img[alt=captcha]")
    loc_register_captchaInput = (By.NAME, "captcha")
    loc_register_submit = (By.CLASS_NAME, "us_Submit_reg")
    loc_register_username_notice = (By.ID, "username_notice")
    loc_register_email_notice = (By.ID, "email_notice")
    loc_register_password_notice = (By.ID, "password_notice")
    loc_register_conform_password_notice = (By.ID, "conform_password_notice")
    loc_register_username_show = (By.CSS_SELECTOR, '#ECS_MEMBERZONE a[href="user.php"]')

    def ele_register_username(self, username):
        self.elementInput(self.loc_register_username, username)

    def ele_register_email(self, email):
        self.elementInput(self.loc_register_email, email)

    def ele_register_password(self, password):
        self.elementInput(self.loc_register_password, password)

    def ele_register_confirm_password(self, confirm_password):
        self.elementInput(self.loc_register_confirm_password, confirm_password)

    def ele_register_extend_field1(self, extend_field1):
        self.elementInput(self.loc_register_extend_field1, extend_field1)

    def ele_register_extend_field2(self, extend_field2):
        self.elementInput(self.loc_register_extend_field2, extend_field2)

    def ele_register_extend_field3(self, extend_field3):
        self.elementInput(self.loc_register_extend_field3, extend_field3)

    def ele_register_extend_field4(self, extend_field4):
        self.elementInput(self.loc_register_extend_field4, extend_field4)

    def ele_register_extend_field5(self, extend_field5):
        self.elementInput(self.loc_register_extend_field5, extend_field5)

    def ele_register_sel_question(self, index: int):
        self.eleSelectByIndex(self.loc_register_sel_question, index)

    def ele_register_passwd_answer(self, passwd_answer):
        self.elementInput(self.loc_register_passwd_answer, passwd_answer)

    def ele_register_captcha(self):
        self.findElement(self.loc_register_captchaImg).screenshot("yzm.png")
        self.elementInput(self.loc_register_captchaInput, captchaRecognition("yzm.png"))

    def ele_register_submit(self):
        self.elementClick(self.loc_register_submit)

    def get_register_notice_assert(self):
        self.__notice_assert["username_notice"] = self.eleGetText(self.loc_register_username_notice)
        self.__notice_assert["email_notice"] = self.eleGetText(self.loc_register_email_notice)
        self.__notice_assert["password_notice"] = self.eleGetText(self.loc_register_password_notice)
        self.__notice_assert["conform_password_notice"] = self.eleGetText(self.loc_register_conform_password_notice)
        return self.__notice_assert



    def register(self, isClickBtn=False, **kwargs):
        self.browser.openUrl(self.RegisterUrl)
        self.ele_register_username(kwargs.get("username"))
        self.ele_register_email(kwargs.get("email"))
        self.ele_register_password(kwargs.get("password"))
        self.ele_register_confirm_password(kwargs.get("confirm_password"))
        self.ele_register_extend_field1(kwargs.get("extend_field1"))
        self.ele_register_extend_field2(kwargs.get("extend_field2"))
        self.ele_register_extend_field3(kwargs.get("extend_field3"))
        self.ele_register_extend_field4(kwargs.get("extend_field4"))
        self.ele_register_extend_field5(kwargs.get("extend_field5"))
        self.ele_register_sel_question(kwargs.get("sel_question_index"))
        self.ele_register_passwd_answer(kwargs.get("passwd_answer"))
        self.ele_register_captcha()
        self.get_register_notice_assert()
        if isClickBtn:
            self.ele_register_submit()

        return self.__notice_assert
