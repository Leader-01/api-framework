import unittest
from unittest import TestCase
from env import Api


class TestApi(unittest.TestCase):
    data = {
        "method": "get",
        "url": "http://domin:8091/services/testService/queryUserInfo?meterCode=289124456101",
        "headers": None
    }

    def test_send(self):
        apr = Api()
        print(apr.send(self.data).text)
