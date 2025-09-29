# -*- coding: utf-8 -*-
# @Time    : 2025/9/28 18:07
# @Author  : Lan
# @File    : run_test.py
# @Software: PyCharm
# @Description :
import os
from subprocess import call

from utils.common import getProjectPath
from config.config import getReportPath

if __name__ == '__main__':
    os.system("{}\\.venv\\Scripts\\activate".format(getProjectPath()))
    ALLURE_RESULTS = getReportPath().joinpath("allure-results")
    ALLURE_HTML = getReportPath().joinpath("allure-html")
    call("pytest")
    # "allure generate .\report\allure-results\ -o .\report\allure-html"

    call("allure generate {} -o {}".format(ALLURE_RESULTS, ALLURE_HTML), shell=True)
    call("allure serve {}".format(ALLURE_RESULTS), shell=True)
