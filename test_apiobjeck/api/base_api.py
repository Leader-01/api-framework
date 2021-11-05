import requests


class BaseApi():

    def requests_http(self, req):
        # 直接使用python关键字传参的方式，将请求结构体传给requests.request方法

        # 解包类似下面这种
        # requests.request(method="get"......)
        r = requests.request(**req)
        print(r.json())
        return r

if __name__ == '__main__':
    ba = BaseApi()
    ba.requests_http()
