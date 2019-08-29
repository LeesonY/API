# -*- coding: utf-8 -*-
'''
1.什么是正则表达式？编写一些 规范查找需要的字符串
2.正则表达式的一个组成：原义字符和元字符
3.如何Python来解析？
4.正则表达式的场景？
---参数化
---查找一些特殊的字符：邮箱，手机号号码，
'''
from API_7.common.get_data import GetData

import re
target  ="{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}"
p = 'normal_user'#原义字符的查找
p2 = '#(.*?)#' #圆括号代表正则表达式里面组的概念
# m = re.search(p2,target)
# print(m)
# print(m.group())#不传参的时候返回表达式和匹配的字符串一起
# print(m.group(1))#传参就是只返回匹配的字符串，也就是当前组的匹配字符
# mm = re.findall(p2,target)#找到所有的匹配的字符，返回是一个列表
# print(mm)

# target2 = re.sub(p2,'18574379913',target,count=1)
# print(target2)

while re.search(p2,target): #查找参数的字符就matach object, True
    m = re.search(p2, target)
    key = m.group(1)
    print(key)
    value = getattr(GetData,key) # 拿到我们要去覆盖的值
    target = re.sub(p2,value,target,count=1)

print(target)

