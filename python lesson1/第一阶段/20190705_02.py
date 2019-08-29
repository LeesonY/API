#-*- coding: utf-8 -*-
import requests

class HttpRequest:
    def __init__(self,url,method='get'):
        self.url=url
        self.method=method

    def http_request(self):
        if self.method.lower()=='get':
            print('正在发起get请求')
            try:
                resp=requests.get(self.url)
            except Exception as e:
                print('错误是{}'.format(e))

        else:
            print('正在发起post请求')
            resp=requests.post(self.url)

        return resp.text

if __name__ == '__main__':
    result=HttpRequest('http://www.lemfix.com').http_request()
    print(result)
