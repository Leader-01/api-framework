import pymysql

# 1.建立连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='water_meter_test',
    charset='utf8') # 如果查询有中文需要指定数据库编码

# 2.从连接建立游标
cur = conn.cursor()

# 3.查询数据库（读）
cur.execute("select * from i_w_customer where code = 'yu1111'")

# 4.获取查询结果
result = cur.fetchall()
print(result)
'''
# 3. 更改数据库（写）
cur.execute("delete from user where name='李四'")

# 4. 提交更改
conn.commit()  # 注意是用的conn不是cur
'''

# 5.关闭游标及连接
cur.close()
conn.close()




