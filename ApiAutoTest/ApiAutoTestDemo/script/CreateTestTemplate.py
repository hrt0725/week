# -*- coding: utf-8 -*-
# @Time    : 2025/9/26 10:45
# @Author  : Lan
# @File    : CreateTestTemplate.py
# @Software: PyCharm
# @Description :
import getpass
import os
from typing import Literal

from config.config import getDataPath, getConfigPath, getTestCasePath, getCasesPath
from utils.common import getDate

templateName = Literal["TestCastTemplateYaml.py.txt", "TestCastTemplateDynamic.py.txt"]


def apiName2BaseName(apiName_: str):
    baseName = apiName_.replace(".yaml", "").replace("yml", "")
    baseName.strip()
    return baseName


def baseName2CaseFileName(baseName):
    return "test_{}.py".format(baseName)


def baseName2apiAddr(baseName: str):
    return baseName.upper()


def baseName2ClassName(baseName: str):
    parts = baseName.split('_')
    className = parts[0] + ''.join(part.capitalize() for part in parts[1:])
    className = className[0].upper() + className[1:]
    return className


def readTemplateDispose(fileName, params: dict):
    with open(fileName, "r", encoding='utf-8') as f:
        templateContent = f.read() % params
        return templateContent


def writeTemplate(templateContent, filePath):
    with open(filePath, "w", encoding='utf-8') as writefile:
        writefile.write(templateContent)
        return True


def createTemplates(yamlDir=getDataPath()):
    for fileName in os.listdir(yamlDir):
        if fileName.endswith(".yaml") or fileName.endswith(".yml"):
            baseName = apiName2BaseName(fileName)
            caseFileName = baseName2CaseFileName(baseName)
            if getTestCasePath().joinpath(caseFileName).is_file():
                continue
            caseName = baseName
            apiAddr = baseName2apiAddr(baseName)
            className = baseName2ClassName(baseName)
            params = {
                "className": className,
                "yamlName": fileName,
                "caseName": caseName,
                "apiAddr": apiAddr,
                "fileName": caseFileName,
                "userName": getpass.getuser(),
                "date": getDate("%Y/%m/%d %H:%M"),
            }
            templateContent = readTemplateDispose(getConfigPath().joinpath("TestCastTemplateYaml.py.txt"), params)
            writeTemplate(templateContent, getTestCasePath().joinpath(caseFileName))


def createTemplate(apiName_: str, templateFileName: templateName, casePath=getCasesPath()):
    baseName = apiName2BaseName(apiName_)
    caseFileName = baseName2CaseFileName(baseName)
    if casePath.joinpath(caseFileName).is_file():
        return False
    else:
        caseName = baseName
        apiAddr = baseName2apiAddr(baseName)
        className = baseName2ClassName(baseName)
        params = {
            "className": className,
            "caseName": caseName,
            "apiAddr": apiAddr,
            "fileName": caseFileName,
            "userName": getpass.getuser(),
            "date": getDate("%Y/%m/%d %H:%M"),
        }
        templateContent = readTemplateDispose(getConfigPath().joinpath(templateFileName), params)
        return writeTemplate(templateContent, casePath.joinpath(caseFileName))


if __name__ == '__main__':
    option = input("操作:")
    match option:
        case "1":
            createTemplates()
        case "2":
            apiName = input("apiName(ex:api_loing)：")
            createTemplate(apiName, "TestCastTemplateDynamic.py.txt")
