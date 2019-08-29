#-*- coding: utf-8 -*-

class AddMethod:
    def add(self,a,b):
        return a+b

    def add_args(self,*args):
        sum=0
        for item in args:
            sum+=item
        return sum

if __name__ == '__main__':
    a,b=1,2
    a1,b1=-3,4
    a2,b2=0,0
    a3,b3=-1,-2