# -*- coding: utf-8 -*- 
# @Time : 2019/4/1 22:13 
# @Author : 小雨点
# @Email: 1149750734@qq.com
# @File : get_data.py
from pythonLX.week10.API_5.common import read_config
from pythonLX.week10.API_5.common import project_path
import re
config=read_config.ReadConfig(project_path.conf_path)#配置文件地址

class GetData:
    '''用来动态的更改、删除、获取数据'''
    COOKIE=None
    LOAN_ID=None #新添加的标id初始值
    normal_user= config.get_str('data','normal_user')#读取配置文件中的值
    normal_pwd= config.get_str('data','normal_pwd')
    normal_member_id=config.get_str('data','normal_member_id')
def replace(target):#target代表replace需要参数化的
    p2='#(.*?)#'#圆括号代表正则表达式里组的概念
    while re.search(p2,target):#查找参数的字符就匹配object
        m = re.search(p2,target)#在目标字符串里根据正则表达式来查找
        key = m.group(1)#传参就是只返回匹配的字符串，也就是当前组的匹配字符
        value = getattr(GetData,key)#拿到需要的去替换的值
        target = re.sub(p2,value,target,count=1)
    return target #返回