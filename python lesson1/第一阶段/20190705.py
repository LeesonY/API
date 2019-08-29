#-*- coding: utf-8 -*-
import random
class HumanVsPC:

    def __init__(self):
        self.fist_dict={'1':'剪刀','2':'石头','3':'布'}

    def choose_role(self):
        '''选择角色'''
        role_dict={'1':'曹操','2':'刘备','3':'张飞'}
        while True:
            num=input('请输入要选择的角色：1.曹操 2.张飞 3 刘备')
            if num in role_dict.keys():
                print('获取的角色是{}'.format(role_dict[num]))
                return role_dict[num]
            else:
                print('输入的角色不正确,请重新选择')
                continue

    def human_fist(self,role):
        '''角色猜拳1.剪刀 2.石头 3.布 玩家输入1-3的数字'''

        while True:
            num=input('请出拳：1剪刀。2石头。3布')
            if num in self.fist_dict.keys():
                print('{}出拳为:{}'.format(role,self.fist_dict[num]))
                return int(num)
            else:
                print('出拳错误,请重新出拳')
                continue

    def pc_fist(self):
        '''电脑出拳 随机产生一个1-3的数字，提示电脑出拳结果'''
        num = random.randint(1,3)
        print('PC出拳为{}'.format(self.fist_dict[str(num)]))
        return num


    def human_vs_pc(self):
        '''人机对战
        a 记录human赢
        b 记录pc赢
        c 记录平局'''
        a = 0
        b = 0
        c = 0
        role=self.choose_role()

        while True:
            human_fist=self.human_fist(role)
            pc_fist=self.pc_fist()
            if human_fist-pc_fist in (1,-2):
                a+=1
                print('{}赢了'.format(role))
            elif human_fist-pc_fist in (-1,2):
                b+=1
                print('pc赢了')
            else:
                c+=1
                print('两者平局')

            choice=input('是否继续对战,y:继续，任意键:退出')
            if choice=='y':
                continue
            else:
                break
        print('这次对战，{}角色赢了{}局，电脑赢了{}局，平局{}次'.format(role,a,b,c))



if __name__ == '__main__':
    HumanVsPC().human_vs_pc()