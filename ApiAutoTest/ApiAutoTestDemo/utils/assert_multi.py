# -*- coding: utf-8 -*-
# @Time    : 2025/9/25 12:43
# @Author  : Lan
# @File    : assert_multi.py
# @Software: PyCharm
# @Description :
from typing import Literal

from utils.common import get_nested_value
from utils.log_utils import createLoger

methodL = Literal["equal", "in", "not in", "has"]


def am(realityValue, expectValue, method: methodL = "equal"):
    if method == "equal":
        assert realityValue == expectValue
    elif method == "in":
        assert expectValue in realityValue
    elif method == "not in":
        assert expectValue not in realityValue
    elif method == "has":
        assert realityValue is not None


def caseAsserts(assertInfo: list, resultData: dict):
    loger = createLoger()
    loger.info("开始断言:")
    for assertItem in assertInfo:
        loger.info("{}:实际值：{}".format(assertItem["key"], get_nested_value(resultData, assertItem["key"])))
        loger.info("{}:期望值：{}".format(assertItem["key"], assertItem["expect_value"]))
        loger.info("断言方式:{}".format(assertItem["assert_method"]))
        am(get_nested_value(resultData, assertItem["key"]),
           assertItem["expect_value"],
           assertItem["assert_method"])


def caseAssert(jsonData: str, keys: str, expect_value, assertMethod: methodL = "equal"):
    loger = createLoger()
    loger.info("开始断言:")
    loger.info("{}:实际值：{}".format(keys, get_nested_value(jsonData, keys)))
    loger.info("{}:期望值：{}".format(keys, expect_value))
    loger.info("断言方式:{}".format(assertMethod))
    am(get_nested_value(jsonData, keys), expect_value, assertMethod)


if __name__ == '__main__':
    am(2, 1 + 1, method="equal")
    am(5, [2, 6, 5], method="in")
    am("fwf", "11fwf", method="in")
    am(7, [2, 6, 5], method="not in")
