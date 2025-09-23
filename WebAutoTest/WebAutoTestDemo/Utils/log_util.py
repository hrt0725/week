# -*- coding: utf-8 -*-
# @Time    : 2025/9/22 11:26
# @Author  : Lan
# @File    : log_util.py
# @Software: PyCharm
# @Description :
import logging

from Utils.Utils import getDate
from base.Config import Config, getLogPath


def createLoger():
    logger = logging.Logger("log")
    formatter = logging.Formatter('%(asctime)s - %(filename)s[%(lineno)s] - %(levelname)s : %(message)s')
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)
    logFileName = getLogPath().joinpath("{}.log".format(getDate("%Y%m%d"))).name
    fileHandler = logging.FileHandler(filename=logFileName, mode='a', encoding='utf8')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
