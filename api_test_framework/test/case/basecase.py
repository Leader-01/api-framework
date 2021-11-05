#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 因为每条用例都需要从Excel中读取、解析、发送请求、断言响应结果。封装一个BaseCase的用例基础类，对一些
# 方法进行封装，来简化用例编写
import unittest
import requests
import json
import sys
sys.path.append("../..")  # 统一将包的搜索路径提升到项目根目录下

from api_test_framework.common.read_excel import *
from api_test_framework.common.case_log import log_case_info


class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        data_file = "D:\PycharmProjects\mater_api\\api_test_framework\data\\test_water_data.xlsx"
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(data_file, cls.__name__)

    def get_case_data(self, case_name):
        return get_test_data(self.data_list, case_name)

    def send_request(self, case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        args = case_data.get('args')
        headers = case_data.get('headers')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')

        if method.upper() == 'GET':  # GET请求
            res = requests.get(url, params=json.loads(args))

        elif data_type.upper() == 'FORM':  # 表单格式请求
            res = requests.post(url=url, data=json.loads(args), headers=headers)
            log_case_info(case_name, url, args, expect_res, res.text)
            self.assertEqual(expect_res, res.text)
        else:
            res = requests.post(url=url, json=json.loads(args), headers=json.loads(headers))  # json格式请求
            log_case_info(case_name, url, args, json.dumps(json.loads(expect_res), sort_keys=True),
                          json.dumps(res.json(), ensure_ascii=False, sort_keys=True))
            self.assertDictEqual(res.json(), json.loads(expect_res))




