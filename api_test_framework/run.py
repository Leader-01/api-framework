#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import unittest
from api_test_framework.common.HTMLTestRunnerCN import HTMLTestReportCN
from config.config import *
# from api_test_framework.common.send_email import send_email
from test.suite.test_suites import *


def discover():
    return unittest.defaultTestLoader.discover(test_case_path)


def run(suite):
    logging.info("================================== 测试开始 ==================================")
    with open(report_file, 'wb') as f:
        HTMLTestReportCN(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)

    # send_email(report_file)
    logging.info("================================== 测试结束 ==================================")


def run_all():  # 运行所用用例
    run(discover())


def run_suite(suite_name):  # 运行`test/suite/test_suites.py`文件中自定义的TestSuite
    suite = get_suite(suite_name)
    if suite:
        run(suite)
    else:
        print("TestSuite不存在")


def collect():   # 由于使用discover() 组装的TestSuite是按文件夹目录多级嵌套的，我们把所有用例取出，放到一个无嵌套的TestSuite中，方便之后操作
    suite = unittest.TestSuite()

    def _collect(tests):   # 递归，如果下级元素还是TestSuite则继续往下找
        if isinstance(tests, unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)  # 如果下级元素是TestCase，则添加到TestSuite中

    _collect(discover())
    return suite


def collect_only():   # 仅列出所用用例
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i), case.id()))
    print("----------------------------------------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i), time.time()-t0))


def makesuite_by_testlist(testlist_file):  # test_list_file配置在config/config.py中
    with open(testlist_file) as f:
        testlist = f.readlines()

    testlist = [i.strip() for i in testlist if not i.startswith("#")]   # 去掉每行结尾的"/n"和 #号开头的行

    suite = unittest.TestSuite()
    all_cases = collect()  # 所有用例
    for case in all_cases:  # 从所有用例中匹配用例方法名
        if case._testMethodName in testlist:
            suite.addTest(case)
    return suite