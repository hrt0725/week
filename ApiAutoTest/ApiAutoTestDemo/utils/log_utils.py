# -*- coding: utf-8 -*-
# @Time    : 2025/9/25 15:44
# @Author  : Lan
# @File    : log_utils.py
# @Software: PyCharm
# @Description :
import logging

from config.config import getLogPath
from utils.common import getDate


def createLoger():
    logger = logging.Logger("log")
    formatter = logging.Formatter('%(asctime)s - %(filename)s[%(lineno)s] - %(levelname)s : %(message)s')
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)
    logFileName = getLogPath().joinpath("{}.log".format(getDate("%Y%m%d")))
    fileHandler = logging.FileHandler(filename=logFileName, mode='a', encoding='utf8')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger


if __name__ == '__main__':
    loger = createLoger()
    loger.info("info")
    loger.error("error")
