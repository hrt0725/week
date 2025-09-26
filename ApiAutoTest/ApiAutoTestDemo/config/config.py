# -*- coding: utf-8 -*-
# @Time    : 2025/9/25 14:53
# @Author  : Lan
# @File    : config.py
# @Software: PyCharm
# @Description :
from utils.common import getProjectPath

HostName = "http://api.yesapi.net"
AppKey = "F2402005A90D70AEB649F409C8D68D85"

API_LOGIN = HostName + "/api/App/User/Login"
API_REGISTER = HostName + "/api/App/User/Register"
API_GET_LAST_LOGIN_USER = HostName + "/api/App/User/GetLastestLoginList"
API_USER_CHECK = HostName + "/api/App/User/Check"
API_GET_USERS = HostName + "/api/App/User/GetList"
API_GET_USER_PROFILE = HostName + "/api/App/User/Profile"


def getDataPath():
    return getProjectPath().joinpath("data")


def getConfigPath():
    return getProjectPath().joinpath("config")


def getLogPath():
    return getProjectPath().joinpath("log")


def getReportPath():
    return getProjectPath().joinpath("report")


def getCasesPath():
    return getProjectPath().joinpath("cases")


def getTestCasePath():
    return getProjectPath().joinpath("TestCase")
