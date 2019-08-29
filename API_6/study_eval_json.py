#-*- coding: utf-8 -*-

import  json
#正常的json格式
#{"key":[]}

params = '{"status":1,"code":"10001","data":null,"msg":"登录成功"}'# 返回
p = '{"mobilephone":"18574379913","pwd":None}'#请求入参
d = eval(p)
print(d)

# json.loads()
# d = eval(params)# 根据的python的数据类型来做转换
# print(d['status'])

d1 = json.loads(params)
print(type(d1),d1)
print(d1['msg'])