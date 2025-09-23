# -*- coding: utf-8 -*-
# @Time    : 2025/9/18 16:01
# @Author  : Lan
# @File    : Utils.py
# @Software: PyCharm
# @Description :

import random
import string
from datetime import datetime
from pathlib import Path
import ddddocr


def captchaRecognition(file):
    dd = ddddocr.DdddOcr()
    with open(file, 'rb') as f:
        pic = f.read()
        result = dd.classification(pic)
        f.close()
    return result


def getProjectPath():
    return Path(__file__).parent.parent


def getDate(formatStr="%Y-%m-%d-%H-%M-%S"):
    return datetime.now().strftime(formatStr)


def getRandomStr(length=5, include_digits=True, include_special=False):
    """生成指定长度的随机字符串
    :param length: 字符串长度
    :param include_digits: 是否包含数字
    :param include_special: 是否包含特殊字符
    :return: str 随机生成的字符串
    """
    if length <= 0:
        return ""
    # 基础字符集（字母）
    characters = string.ascii_letters
    # 添加数字
    if include_digits:
        characters += string.digits
    # 添加特殊字符
    if include_special:
        characters += string.punctuation
    # 确保字符集不为空
    if not characters:
        characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))


def initScreenshotDir(ScreenshotName: str, ScreenshotCountPath: str):
    ssPath = getProjectPath().joinpath(ScreenshotName)
    sscPath = getProjectPath().joinpath(ScreenshotCountPath)
    if not ssPath.is_dir():
        ssPath.mkdir()
    num = None
    with open(sscPath, "r") as f:
        num = int(f.read())
        num += 1
        newScreenshotPath = ssPath.joinpath("{}_{}".format(num, getDate()))
        newScreenshotPath.mkdir()
        f.close()
    with open(sscPath, "w") as f:
        f.write(str(num))
        f.close()
    return newScreenshotPath


# Test
if __name__ == "__main__":
    print(getProjectPath())
