import requests
import pytest
# testcase是以pytest为测试为框架，一个method就是一个case
from test_apiobjeck.api.get_info import GetInfo
from test_apiobjeck.testcase.test_base import TestBase


class TestGet(TestBase):

    def test_get_info(self):
        assert self.getinfo.get_info().json()["data"]["meterCode"] == "289124456101"






