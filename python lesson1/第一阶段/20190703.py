#-*- coding: utf-8 -*-
# def football_team(x,y,k,sex_1='f'):
#     count=0
#     a=0
#     while True:
#         age=int(input('请输入你的年龄：'))
#         sex=input('请输入你的性别：')
#         if x<=age<=y and sex==sex_1:
#             count+=1
#         a+=1
#         if a==k:
#             break
#     print('符合条件的总人数{}'.format(count))
# football_team(10,18,5,'m')

class Grilfriend:
    def __init__(self,age,sex,name):
        self.age=age
        self.sex=sex
        self.name=name


    def sport(self,*args):
        print(self.age+'的'+self.name+'喜欢运动：{}'.format(args))

p=Grilfriend(22,'male','李佳阳')
p.sport('足球')




















