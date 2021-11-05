import unittest
import requests


class TestPay(unittest.TestCase):

    url = "http://127.0.0.1:8091/services/testService/queryUserInfo"

    # 返回结果成功
    def test_pay(self):
        data = {"meterCode": 289124456101}
        res = requests.get(url=self.url, params=data)
        self.assertNotEquals("1", res.text)


# 用例执行顺序：并非按书写顺序执行，而是按用例名ascii码先后顺序执行
if __name__ == '__main__':
    unittest.main(verbosity=2)
