#-*- coding: utf-8 -*-
#ddt data driver test
#数据驱动测试
#安装：pip install ddt

import unittest
from ddt import ddt,data,unpack

@ddt #装饰测试类
class TestPringMsg(unittest.TestCase):

    @data([1,2,3],(4,5,6))
    @unpack#对data传递过来的元组子元素进行拆分 要求是可迭代
    def test_001(self,a,b,expected=0):#如果用了unpack 必须用对应个数的参数名来进行接收
        print('我在执行第{}条用例'.format(a))
        c = a + b
        self.assertEqual(c,expected)
        # print('b:',b)
        # print('c:',c)
