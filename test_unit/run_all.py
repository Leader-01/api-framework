import unittest
from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunnerCN import HTMLTestReportCN

import HTMLTestRunnerCN
from test_info import TestInfo

suite = unittest.TestSuite()
suite.addTest(TestInfo("test_info1"))

f = open("report.html", "wb")  # 二进制写格式打开要生成的报告文件
# HTMLTestRunner(
#     stream=f,
#     title='{Test Report}',
#     description='这是备注'
# ).run(suite)

HTMLTestReportCN(
    stream=f,
    title='{Test Report}',
    description='这是备注',
    tester="测试然"
).run(suite)

f.close()

