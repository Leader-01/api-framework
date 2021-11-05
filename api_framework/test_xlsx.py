
import xlrd


# 打开Excel
wd = xlrd.open_workbook("test_water_data.xlsx")
# 选择sheet页
sh = wd.sheet_by_name("Testwater")
# 有效行数
print(sh.nrows)
# 有效列数
print(sh.nrows)
# 输出第一行第一列的值
print(sh.cell(0, 0).value)
# 输出第一行的所有值
print(sh.row_values(0))


# 将数据和标题组成字典
print(dict(zip(sh.row_values(0), sh.row_values(1))))

# 遍历Excel
for i in range(sh.nrows):
    print(sh.row_values(i))
