import unittest
from test_info import TestInfo
from test_pay import TestPay

suite = unittest.TestSuite()
# 添加多个用例
suite.addTests([TestInfo("test_info1"), TestPay("test_pay")])
# suite.addTest(TestInfo("test_info1"))
# 运行测试集

unittest.TextTestRunner(verbosity=2).run(suite) # verbosity显示级别，运行顺序为添加到suite中的顺序

