#-*- coding: utf-8 -*-

import requests

#登录请求
url='http://39.105.94.71:8080/futureloan/mvc/api/member/login'
param={'mobilephone':'18574379999','pwd':'123456',}

#头部
headers = {'user-agent': 'Chrome/72.0.3626.81'}#模拟从浏览器发送出去的
resp_1=requests.post(url,data=param,headers=headers)#返回一个消息实体
print(resp_1.text)#字符串类型
# print(resp.json())#字典类型


#响应结果：状态码 响应报文 响应头 cookies
# print('状态码',resp_1.status_code)
# print('响应头',resp_1.headers)
print('cookies',resp_1.cookies)

# print('请求头',resp_1.request.headers)


#充值
url='http://39.105.94.71:8080/futureloan/mvc/api/member/recharge'
param={'mobilephone':'18574379999','amount':'10000',}

resp=requests.post(url,data=param,cookies=resp_1.cookies)#返回一个消息实体
print(resp.text)#字符串类型