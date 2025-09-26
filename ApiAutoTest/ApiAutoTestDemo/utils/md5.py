# -*- coding: utf-8 -*-
# @Time    : 2025/9/24 16:43
# @Author  : Lan
# @File    : md5.py
# @Software: PyCharm
# @Description :
from hashlib import md5


def generateMD5(text: str):
    text = str(text)
    hashObj = md5()
    hashObj.update(text.encode("utf-8"))
    return hashObj.hexdigest()
