import unittest
from test_info import TestInfo

suite1 = unittest.makeSuite(TestInfo, "test_info1")  # 使用测试类的单条用例制作测试集
suite2 = unittest.makeSuite(TestInfo)  # 使用整个测试类制作测试集合(包含改测试类的所有用例)

unittest.TextTestRunner(verbosity=2).run(suite2)
