#-*- coding: utf-8 -*-

#getattr(Context,'normal_user') 获取类属性的值
#setattr(Context,'admin_user','abc') 添加属性
# hasattr(Context,'admin_user') 判断是否有这个属性
# delattr(Context,'admin_user') 删除这个属性


class People:
    number_eye = 2

    def __init__(self,name,age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    p = People('mongo',18)
    print(People.number_eye)
    print(p.number_eye)
    print(p.name)

    #添加属性
    print(hasattr(People,"number_leg")) #如果有返回True，没有返回False
    print(hasattr(People, "number_eye"))

    setattr(People,"number_leg",2)
    print(hasattr(People, "number_leg"))
    setattr(p,"name","huahua")
    print(getattr(p,"name"))

    # setattr(p,"dance",True)
    # print(p.dance)
    #
    # getattr(People,"number_leg") # 获取类属性
    # getattr(p,"dance")# 获取实例属性
    #
    # delattr(p,"dance")
    # getattr(p,"dance")# 获取实例属性
