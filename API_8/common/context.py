#-*- coding: utf-8 -*-

import re
from API_8.common.config import config
import configparser

class Context:

    loan_id = None


def replace(data):
    p = "#(.*?)#"  # 正则表达式
    while re.search(p, data):
        print(data)
        m = re.search(p, data)  # 从任意位置开始找，找到第一个就返回Match object,如果没有找None
        print(m.group(0))  # 返回表达式和组里面的内容
        print(m.group(1))  # 只返回指定组的内容
        g = m.group(1)  # 拿到参数化的key
        try:
            v = config.get('data', g)  # 根据key取配置文件里面的值
        except configparser.NoOptionError as e: #如果配置文件里面没有的时候，去Context取
            if hasattr(Context,g):
                v = getattr(Context,g)
            else:
                print('找不到参数化的值')
                raise e
        print(v)
        # 记得替换后的内容,继续用data接收
        data = re.sub(p, v, data, count=1)  # 查找替换,count查找替换的次数


    return data
