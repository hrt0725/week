# -*- coding: utf-8 -*-
# @Time    : 2025/9/20 19:01
# @Author  : Lan
# @File    : test.py
# @Software: PyCharm
# @Description :

from typing import Literal, Callable

_AaName = Literal["session", "package", "module", "class", "function"]


def func(aa: _AaName | Callable[[str], _AaName] = "wd"):
    print(aa)


def func_2(a: str = "wd"):
    print(type(a))


def func_3():
    print("func_begin")
    yield "w"
    print("func_end")


# print(sys._getframe().f_lineno)
# print(sys._getframe().f_code.co_filename)
print(type(globals()))

username = ["tom", "jerry", "luck"]
password = ["111", "222", "333"]
zup = zip(username, password)
print(list(zup))

a = func_3()

