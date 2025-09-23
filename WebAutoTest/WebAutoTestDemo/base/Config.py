# -*- coding: utf-8 -*-
# @Time    : 2025/9/18 16:20
# @Author  : Lan
# @File    : Config.py
# @Software: PyCharm
# @Description :
from Utils import Utils


class Config:
    ScreenshotName = "Screenshot"
    ScreenshotCountPath = "data\\screenshotCount"


def getDataPath():
    return Utils.getProjectPath().joinpath("data")


def getLogPath():
    return Utils.getProjectPath().joinpath("log")


def getReportPath():
    return Utils.getProjectPath().joinpath("report")


def getTestCasePath():
    return Utils.getProjectPath().joinpath("test_case")


if __name__ == "__main__":
    print(getDataPath())
