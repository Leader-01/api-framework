import unittest
from test_info import TestInfo


suite1 = unittest.TestSuite()
suite1.addTest(TestInfo("test_info1"))
suite2 = unittest.makeSuite(TestInfo, "test_info1")
suite = unittest.TestSuite([suite1], [suite2])  # 将两个测试集组合为一个
unittest.TextTestRunner(verbosity=2).run(suite)
