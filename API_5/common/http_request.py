#-*- coding: utf-8 -*-

import requests
from API_5.common.config import config

class HTTPRequest:
    '''
    使用这类的request方法去完成不同的HTTP请求，并且返回响应结果
    '''

    def request(self,method,url,data=None,json=None,cookies=None):

        method = method.upper() #强制转成全大写

        if type(data) == str:
            data = eval(data)# str 转成字典

        #拼接请求的url
        url = config.get('api','pre_url') + url

        if method == 'GET':
            resp = requests.get(url,params=data,cookies=cookies) # resp 是Response对象
        elif method == 'POST':
            if json:
                resp = requests.post(url,json=json,cookies=cookies)
            else:
                resp = requests.post(url,data=data,cookies=cookies)
        else:
            print('UN-support method')


        return resp

class HTTPRequest2:

    def __init__(self):
        self.session = requests.sessions.session()#打开一个session

    def request(self,method,url,data=None,json=None):
        method = method.upper()

        # 拼接请求的url
        url = config.get('api', 'pre_url') + url

        if type(data) == str:
            data = eval(data)  # str 转成字典

        if method == 'GET':
            resp = self.session.request(method=method,url=url,params=data)
        elif method == 'POST':
            if json:
                resp = self.session.request(method=method,url=url, json=json)
            else:
                resp = self.session.request(method=method,url=url, data=data)
        else:
            resp=None
            print('UN-support method')
        return resp

    def close(self):
        self.session.close() # 用完记得关闭

if __name__ == '__main__':
    # params = {'mobilephone':'18574379913','pwd':'123456'}
    # http_request = HTTPRequest()
    # #调用登录接口
    # resp = http_request.request('GET','http://test.lemonban.com/futureloan/mvc/api/member/login',
    #                             data=params)
    # print(resp.status_code)
    # print(resp.text)
    # print(resp.cookies)

    # # 调用充值接口
    # params = {'mobilephone': '18574379913', 'amount': '10000'}
    # resp2 = http_request.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge',
    #                             data=params,cookies=resp.cookies)
    # print(resp2.status_code)
    # print(resp2.text)
    # print(resp2.cookies)


    http_request2 = HTTPRequest2()
    params = {'mobilephone':'18574379913','pwd':'123456'}
    resp = http_request2.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/register',
                                    data=params)
    params = {'mobilephone':'19000000000','amount':'10000'}
    resp2 = http_request2.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/register',
                                 data=params)

    print(resp.status_code)
    print(resp.text)
    print(resp.cookies)














