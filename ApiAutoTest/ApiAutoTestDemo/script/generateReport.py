# -*- coding: utf-8 -*-
# @Time    : 2025/9/28 16:50
# @Author  : Lan
# @File    : generateReport.py
# @Software: PyCharm
# @Description :
import os

from utils.common import getProjectPath


def generateReport():
    os.chdir(getProjectPath())
    os.system("{}\\.venv\\Scripts\\activate".format(getProjectPath()))
    os.system("pytest")
    os.system(r"allure generate .\report\allure-results\ -o .\report\allure-html")


def openAllureReport():
    # os.system("allure open -h 192.168.120.4 -p 8888 ./allure-html")
    pass


def serveAllureReport():
    # os.system("allure serve ./allure-results")
    pass


if __name__ == '__main__':
    generateReport()
