import requests
# 在api package中是代表所有的接口信息的具体的实现，使用一个公共方法代表一个接口
import yaml
from string import Template
from test_apiobjeck.api.base_api import BaseApi


class GetInfo(BaseApi):
    _meterCode = 289124456101
    def template(self):
        data = {
            "meterCode": 289124456101
        }
        with open("get_info.yaml") as f:
            re = Template(f.read()).substitute(data)
            # re是str类型，下面将转换为字典
            return yaml.safe_load(re)

    def get_info(self):
        req = self.template()
        r = self.requests_http(req)
        print(r)
        return r
        # 将值返回
#        assert r.json()["meterCode"] == 28912445610

if __name__ == '__main__':
    gt = GetInfo()
    gt.get_info()
