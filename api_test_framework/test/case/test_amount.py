#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import unittest
from api_test_framework.common.read_excel import *
import requests
from api_test_framework.common.case_log import *


class TestAmount(unittest.TestCase):

    data_list = excel_to_list("D:\PycharmProjects\mater_api\\api_test_framework\data\\test_water_data.xlsx", "Testwater")

    def test_amount(self):
        case_data = get_test_data(self.data_list, 'test_amount')
        if not case_data:
            print("用例不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        res = requests.get(url=url, params=json.loads(data))
        expect_res = case_data.get('expect_res')
        log_case_info('test_amount', url, data, expect_res, res.text)
        self.assertNotEquals(expect_res, res.text)
