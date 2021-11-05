
import requests
import json
'''

序列化： 内存对象 -> 文本/文件
反序列化： 文本 -> 内存对象
JSON对象（Python字典） -> 转为文本请求 -> 发送请求
-> 服务器收到文本请求 -> 将文本请求转化为对象，获取其中的参数，处理业务
-> 返回文本格式的响应 -> 客户端转为对象格式来从响应中取值

'''

# 序列化

# data = {
#     "name": "weixing",
#     "pwd": "123456",
#     "male": True,
#     "money": None
# }
# str_data = json.dumps(data)
# print(str_data)

# json.dumps()支持将json文本格式化输出
# 1.请求地址
url = "http://127.0.0.1:8091/services/testService/queryAccountNumber"
# 2.请求参数,字典格式,方便参数的修改
params = {"tel": 18912345677, "address": "地址信息289"}
res = requests.get(url=url, params=params)
print(res.text)
res_dict = res.json()# 将响应转为json对象（字典）等同于`json.loads(res.text)`
"""
indent: 缩进空格数，indent=0输出为一行
sork_keys=True: 将json结果的key按ascii码排序
ensure_ascii=Fasle: 不确保ascii码，如果返回格式为utf-8包含中文，不转化为
"""
# print(json.dumps(res_dict, indent=2, sort_keys=True, ensure_ascii=False))# 重新转为文本



# 反序列化
# res_text = '{"name": "\u5f20\u4e09", "password": "123456", "male": true, "money": null}'  # JSON文本格式的响应信息
# res_dict = json.loads(res_text) # 转化为字典
# print(res_dict['name'])  # 方便获取其中的参数值

# res_dict = {'name': '张三', 'password': '123456', "male": True, "money": None} # 字典格式
# f = open("demo1.json","w")
# json.dump(res_dict, f)
# f.close()

# f = open("demo2.json", "r", encoding="utf-8")  # 文件中有中文需要指定编码
# f_dict = json.load(f) # 反序列化将文件句柄转化为字典
# print(f_dict['name']) # 读取其中参数
# f.close()
