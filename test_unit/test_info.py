import unittest
import requests


class TestInfo(unittest.TestCase):

    url = "http://127.0.0.1:8091/services/testService/queryAccountNumber"

    # 返回结果成功
    def test_info1(self):
        data = {"tel": 18912345677, "address": "地址信息289"}
        res = requests.get(url=self.url, params=data)
        self.assertNotEquals("1", res.text)


# 用例执行顺序：并非按书写顺序执行，而是按用例名ascii码先后顺序执行
if __name__ == '__main__':
    unittest.main(verbosity=2)
