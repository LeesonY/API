# -*- coding: utf-8 -*- 
# @Time : 2019/4/1 22:34 
# @Author : 小雨点
# @Email: 1149750734@qq.com
# @File : re.py
import re
from pythonLX.week10.API_5.common.get_data import GetData

target="{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}"
p='normal_user'#元义字符的查找
p2='#(.*?)#'#圆括号代表正则表达式里组的概念

while re.search(p2,target):#查找参数的字符就匹配object
    m = re.search(p2,target)#在目标字符串里根据正则表达式来查找
    key = m.group(1)#传参就是只返回匹配的字符串，也就是当前组的匹配字符
    value = getattr(GetData,key)#拿到需要的去替换的值
    target = re.sub(p2,value,target,count=1)
print(target)