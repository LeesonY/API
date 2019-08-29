#-*- coding: utf-8 -*-
#1)我们可以来测试我们自己的代码
#2)我们可以利用单元测试来完成我们的自动化

#unuttest pytest
import  unittest

#测试用例===测试期望结果 expected
#执行测试  类：TestSuite   类：TestTextRunner
#一致pass，不一致Failed===测试结果<=== 实际结果与期望结果进行比对<===assert 断言   pass Failed
#测试报告 类:TestTextRunner 执行/出具报告

#开始对加法进行单元测试了
class TestAdd(unittest.TestCase):#继承
    def setUp(self):#开始-->在每一条用例执行之前
        print('开始执行测试了')
        #准备工作/准备测试环境

    def tearDown(self):#结束-->在每一条用例执行结束之后
        print('测试执行完毕了')
        #清场工作/清除测试环境

       #写用例 test_一定用这个开头！！！！
    def test_001(self):#测试两个正数相加
        a=1
        b=2
        c=a+b
        print('测试结果是：{}'.format(c))

    def test_002(self):#测试一正一负相加
        a=-1
        b=2
        c=a+b
        print('测试结果是：{}'.format(c))

    def test_003(self):#测试两个负数相加
        a=-1
        b=2
        c=a+b
        print('测试结果是：{}'.format(c))

    def test_004(self):#测试两个0相加
        a=0
        b=0
        c=a+b
        print('测试结果是：{}'.format(c))




#开始对减法进行单元测试了
class TestSub(unittest.TestCase):
    pass










