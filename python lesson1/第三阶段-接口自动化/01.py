#-*- coding: utf-8 -*-

import  requests

#18574379999
# url='http://39.105.94.71:8080/futureloan/mvc/api/member/register'
# param={'mobilephone':'18574379999','pwd':'123456','regname':'lemoncp'}#字典的形式存储参数数据

#发送一个get请求
# resp=requests.get(url,params=param)#返回一个消息实体
# print(resp.text)#字符串类型
# print(resp.json)#字典类型

#发送一个post请求
# resp=requests.post(url,data=param)#返回一个消息实体
# print(resp.text)#字符串类型
# print(resp.json())#字典类型

# ===登录请求===
url='http://39.105.94.71:8080/futureloan/mvc/api/member/login'
param={'mobilephone':'18574379999','pwd':'123456',}

#发送一个get请求
resp=requests.get(url,params=param)#返回一个消息实体
print(resp.text)#字符串类型
print(resp.json())#字典类型

#发送一个post请求
resp=requests.post(url,data=param)#返回一个消息实体
print(resp.text)#字符串类型
print(resp.json())#字典类型


#{"status":1,"code":"10001","data":null,"msg":"登录成功"} text
# {'code': '10001', 'msg': '登录成功', 'data': None, 'status': 1}  json

# import json
# s='{"status":1,"code":"10001","data":null,"msg":"登录成功"}'
# value=json.loads(s)
# print(value)

#字符串---字典 json.loads() key:value 都必须是双引号 null-->None
#字典---字符串 json格式的字符串 json.dumps()














