import unittest
from test_info import TestInfo

suite = unittest.TestSuite()
suite.addTest(TestInfo("test_info1"))

# 输出测试结果到文本文件
with open("result.txt", "w") as f:
    unittest.TextTestRunner(stream=f, verbosity=2).run(suite)  # 将输出流stream输出到文件

