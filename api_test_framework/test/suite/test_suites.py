#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import sys
sys.path.append("../..")
from api_test_framework.test.case.test_query_meter_code import TestMeterCode

smoke_suite = unittest.TestSuite()  # 自定义的TestSuite
smoke_suite.addTests([TestMeterCode('test_meter_code')])


def get_suite(suite_name):  # 获取TestSuite方法
    return globals().get(suite_name)


