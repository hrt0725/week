# -*- coding: utf-8 -*-
# @Time    : 2025/9/23 09:44
# @Author  : Lan
# @File    : main.py
# @Software: PyCharm
# @Description :
import unittest

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    discover = unittest.defaultTestLoader.discover(start_dir="cases", pattern='test*.py')
    runner.run(discover)

    # HTMLTestRunner执行用例生成报告
    # 匹配需要执行的用例
    # discover = unittest.defaultTestLoader.discover(
    #     start_dir="cases",
    #     pattern="test_*.py",  # 匹配测试用例所在文件
    #     top_level_dir="cases")  # 测试用例的顶级目录

    # with open("report/report.html", 'w', encoding='utf-8') as f:
    #     runner = HtmlTestRunner.runner.HTMLTestRunner(
    #         stream=f,
    #         output='report',
    #         report_title="web自动化测试报告",
    #         report_name="EsCWebAutoTest")
    #     runner.run(discover)

    # BeautifulReport(discover).report(
    #     filename="report-{}.html".format(getDate()),
    #     report_dir=getReportPath(),
    #     description="自动化测试详情"
    # )
