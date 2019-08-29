#-*- coding: utf-8 -*-


from API_7.common import read_config
from API_7.common import project_path
import re

config = read_config.ReadConfig(project_path.conf_path)

class GetData:
    '''可以用来动态的更改 删除 获取数据'''
    COOKIE=None
    LOAN_ID=None#新添加的标id初始值
    normal_uesr = config.get_str('data','normal_user')
    normal_pwd = config.get_str('data','normal_pwd')
    normal_member_id = config.get_str('data','normal_member_id')

def replace(target):
    p2 = '#(.*?)#'
    while re.search(p2, target):  # 查找参数的字符就matach object, True
        m = re.search(p2, target)
        key = m.group(1)
        print(key)
        value = getattr(GetData, key)  # 拿到我们要去覆盖的值
        target = re.sub(p2, value, target, count=1)
    return  target

#类属性
# print(GetData.COOKIE)

#利用反射的方法来哪值
# print(getattr(GetData,'COOKIE'))#第一个参数是类名  第二个参数是属性的参数名
# print(hasattr(GetData,'COOKIE'))#第一个参数是类名  第二个参数是属性的参数名  返回值是布尔值
# print(setattr(GetData,'COOKIE','123456'))#第一个参数是类名  第二个参数是属性的参数名 第三个你要设置的新值
# #第一个参数是类名  第二个参数是属性的参数名 第三个你要设置的新值
# print(getattr(GetData,'COOKIE'))
# print(delattr(GetData,'COOKIE'))#删除类的某个属性值 第一个参数是类名  第二个参数是属性的参数名
# #不常用
# print(getattr(GetData,'COOKIE'))
















