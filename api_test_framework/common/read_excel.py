import xlrd


def excel_to_list(data_file, sheet):
    # 新建一个空列表,
    data_list = []
    # 打开Excel
    wd = xlrd.open_workbook(data_file)
    # 获取工作簿
    sh = wd.sheet_by_name(sheet)
    # 获取标题行数据
    header = sh.row_values(0)
    # 跳过标题行,从第二行开始取数据
    for i in range(1, sh.nrows):
        # 将标题和每行数据组装成字典
        d = dict(zip(header, sh.row_values(i)))
        data_list.append(d)
    return data_list


def get_test_data(data_list, case_name):
    for case_data in data_list:
        # 如果字典数据中case_name与参数一致
        if case_name == case_data['case_name']:
            return case_data
            # 如果查询不到会返回None


if __name__ == '__main__':
    data_list = excel_to_list("test_water_data.xlsx", "Testwater")
    case_data = get_test_data(data_list=data_list, case_name="test_water")
    print(case_data)
