#-*- coding: utf-8 -*-
try:
    a=int(input('请输入你的年龄'))
except Exception as e:
    print('输入的数据有误，发送错误{}'.format(e))
else:
    if a>18:
        print('你已经成年')
    else:
        print('未成年')