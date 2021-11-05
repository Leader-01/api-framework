#!/usr/bin/python
# -*- coding: UTF-8 -*-
from api_test_framework.test.case.basecase import BaseCase


class TestMeterCode(BaseCase):
    def test_meter_code(self):
        '''手机号和地址正确'''
        case_data = self.get_case_data("test_water")
        self.send_request(case_data)
