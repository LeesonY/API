#-*- coding: utf-8 -*-

'''
两种传递cookie的方式
1.单独的session，把上一个请求的返回cookies，指定传递到下一个请求的入参cookie中
2.使用同一个session，就会自动传递cookies
'''


import requests

session = requests.sessions.session()
#登录
params = {'mobilephone':'18574379913','pwd':'123456'}
resp = session.request('post',
                       url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                       data=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)

#充值
params = {'mobilephone':'18574379913','amount':'10000'}
resp = session.request('post',
                       url='http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                       data=params)

print(resp.status_code)
print(resp.text)
print(resp.cookies)






