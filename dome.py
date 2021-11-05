# 导入requests包

import requests
import json

# 1.请求地址
# url = "http://httpbin.org/get"
# # 2.发送请求,获取响应
# res = requests.get(url)
# # 3.解析响应
# print(res.text)

# get和传统表单类post(x-www-form-urlencoded)的都是一样的
# 1.请求地址
# url = "http://127.0.0.1:8091/services/testService/queryAccountNumber"
# 2.请求参数,字典格式,方便参数的修改
# params = {"tel": 18912348888, "address": "地址信息288"}
# res = requests.get(url=url, params=params)
# print(res.text)

# JSON类型的POST请求（application/json）

url = "http://httpbin.org/post"
data = {
        "name": "hanzhichao",
        "age": 18
        }  # 字典格式，方便添加
headers = {"Content-Type": "application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
res = requests.post(url=url, data=json.dumps(data), headers=headers) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
print(res.text)

