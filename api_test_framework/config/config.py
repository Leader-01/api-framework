import logging
import os
import json

# 项目路径   当前文件的上一级的上一级目录(增加一级)
import time

pro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据目录
data_path = os.path.join(pro_path, 'data')
# 用例目录
test_path = os.path.join(pro_path, 'test')

today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())
# 日志更改路径到logs目录里下
log_file = os.path.join(pro_path, 'logs',  'log_{}.txt'.format(today))
# 报告更改到report目录下
report_file = os.path.join(pro_path, 'report', 'report_{}.html'.format(now))

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式


def log_case_info(case_name, url, data, expect_res, res_text):
    if isinstance(data, dict):
        data = json.dumps(data, ensure_ascii=False)  # 如果data是字典格式，转化为字符串
    logging.info("测试用例：{}".format(case_name))
    logging.info("url：{}".format(url))
    logging.info("请求参数：{}".format(data))
    logging.info("期望结果：{}".format(expect_res))
    logging.info("实际结果：{}".format(res_text))


if __name__ == '__main__':
    logging.info("logfile")
