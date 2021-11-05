import unittest


suite = unittest.defaultTestLoader.discover("./")  # 遍历当前目录及子包中所有Test_*.py中的所有用例

# 子目录中需要包含__init__.py文件，及应为的Python包
# 所有用例因为test_*.py,包含测试类应以Test开头，并继承unittest.TestCase, 用例应以test_开头
unittest.TextTestRunner(verbosity=2).run(suite)
