import unittest
import requests
from read_excel import *
# 用来转换Excel中的json字符串为字典
import json


class TestCode(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # 整个测试类只执行一次
        # 读取该测试类所有用例数据
        cls.data_list = excel_to_list("test_water_data.xlsx", "Testwater")
        # cls.data_list 同 self.data_list 都是该类的公共属性

    def test_water_code(self):
        #  从数据列表中查找到该用例数据
        case_data = get_test_data(self.data_list, "test_water")
        if not case_data:   # 有可能为None
            print("用例数据不存在")
        # 从字典中取数据，excel中的标题也必须是小写url
        url = case_data.get("url")
        #  注意字符串格式，需要用json.loads()转化为字典格式
        data = case_data.get("data")
        # 期望数据
        expect_res = case_data.get("expect_res")
        # print(expect_res)
        # # 表单请求，数据转为字典格式
        print(json.loads(data))
        params = {"tel": 18912345677, "address": "地址信息289"}
        res = requests.get(url=url, params=json.loads(data))
        # 改为assertEqual断言
        print(res.text)
        self.assertNotEquals(res.text, expect_res)


if __name__ == '__main__':
    unittest.main(verbosity=2)

