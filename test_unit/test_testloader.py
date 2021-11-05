import unittest
from test_info import TestInfo

suite = unittest.TestLoader().loadTestsFromTestCase(TestInfo)  # 加载该测试类所有用例并生成测试集

unittest.TextTestRunner(verbosity=2).run(suite)
