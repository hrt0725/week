# -*- coding: utf-8 -*-
# @Time    : 2025/9/25 12:30
# @Author  : Lan
# @File    : common.py
# @Software: PyCharm
# @Description :
import random
import string
from datetime import datetime
from pathlib import Path


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


def get_nested_value(data, keyStr: str):
    """
    根据键列表获取嵌套字典的值
    :param data: 字典数据
    :param keyStr: 键字符串，如  'data.err_code'
    :return: 对应的值，如果路径不存在返回 None
    """
    current = data
    for _key in keyStr.split("."):
        if isinstance(current, dict) and _key in current:
            current = current[_key]
        else:
            return None  # 路径不存在
    return current


if __name__ == '__main__':
    result = {
        "ret": 200,
        "data":
            {
                "err_code": 0,
                "err_msg": "no error"
            }
    }

    keys = ["data", "err_msg"]
    key = 'data.err_msg'

    print(get_nested_value(result, key))
