#-*- coding: utf-8 -*-
import requests
res=requests.get('http://www.baidu.com')
print(res.text)



# res_2=requests.post('http://www.baidu.com')
# print(res_2)