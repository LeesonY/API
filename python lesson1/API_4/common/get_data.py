#-*- coding: utf-8 -*-

class GetData:
    '''可以用来动态的更改 删除 获取数据'''
    COOKIE=None

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
















