import yagmail


# 定义用户名、授权码、服务器地址且连接服务器
mail_server =  yagmail.SMTP(user='983811956@qq.com', password='vtpvldgfstcpbfce', host='smtp.qq.com')

# 发送对象列表
Email_to = ['116260429@qq.com']
subject = '任意填写'
Email_text = '任意内容填写'

# 多个附件用逗号隔开
attachments = ['D:\PycharmProjects\mater_api\\test_unit\\report.html']

# 发送邮件
mail_server.send(Email_to, subject, Email_text, attachments)
print("发送成功")

