# -*- coding: utf-8 -*-
# @Time : 2019/3/11 10:35
# @Author : 小雨点
# @Email: 1149750734@qq.com
# @File : study_request.py
import requests

class HttpRequest:
    '''该类完成http的get 、post请求，返回结果'''
    def http_request(self,method,url,param,cookies):#对象方法
        '''判断是get请求还是post请求'''

        if method.upper()=='GET':
            try:
                resp=requests.get(url,params=param,cookies=cookies)#传递cookies
            except Exception as e:
                print('get请求出错了：{}'.format(e))
        elif method.upper()=='POST':
            try:
                resp=requests.post(url,data=param,cookies=cookies)
            except Exception as e:
                print('post请求出错了：{}'.format(e))
        else:
            print('不支持该种方式')
            resp=None
        return resp

#测试代码
if __name__ == '__main__':
    url='http://47.107.168.87:8080/futureloan/mvc/api/member/register'
    param={'mobilephone':'13601676495','pwd':'123456'}
    method='get'
    resp=HttpRequest().http_request(method,url,param)
    print(resp.text)