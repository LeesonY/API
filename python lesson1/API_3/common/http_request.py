#-*- coding: utf-8 -*-


import requests
class HttpRequest:
    '''该类完成http的get 以及post请求，并返回结果'''
    def http_request(self,method,url,param):
        '''根据请求方法来决定发起get请求还是post请求
        method:get post http 的请求方式
        url:发送请求的接口地址
        param:随接口发送的请求参数 以字典格式传递
        rtype：有返回值，返回结果是响应报文
        '''
        if method.upper() == 'GET':
            try:
                resp=requests.get(url,params=param)
            except Exception as e:
                print('get请求出错啦：{}'.format(e))
        elif method.upper()=='POST':
            try:
                resp=requests.post(url,data=param)
            except Exception as e:
                print('post请求出错啦：{}'.format(e))
        else:
            print('不支持该种方式')
            resp=None
        return resp

if __name__ == '__main__':
    url='http://39.105.94.71:8080/futureloan/mvc/api/member/register'
    param={'mobilephone':'18574379998','pwd':'123456','regname':'lemoncp'}
    method='get'

    resp=HttpRequest().http_request(method,url,param)
    print(resp.text)
    print(resp.headers)