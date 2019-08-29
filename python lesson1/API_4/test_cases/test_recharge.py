#-*- coding: utf-8 -*-
import unittest
from API_4.common.http_request import HttpRequest
from API_4.common.do_excel import DoExcel
from API_4.common import project_path
from API_4.common.my_log import MyLog
from ddt import ddt,data,unpack
from API_4.common.get_data import GetData

#测试充值
test_data = DoExcel(project_path.case_path, 'recharge').read_data('RechargeCASE')
my_log=MyLog()

# COOKIES=None# 设置cookies的初始值为None
@ddt
class TestCases(unittest.TestCase):

    def setUp(self):#测试之前的准备工作
        self.t=DoExcel(project_path.case_path, 'recharge')#写入测试结果的对象

    def tearDown(self):
        pass

    #写用例
    @data(*test_data)
    #@unpack
    def test_cases(self,case):
        global TestResult#全局变量
        # global COOKIES#声明是一个全局变量
        # 1:读取到测试数据
        # 2:执行测试:遍历--根据Key取值
        method = case['Method']
        url = case['Url']
        param = eval(case['Params'])

        # 发起测试
        my_log.info('------正在测试{}模里面第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
        my_log.info('测试数据是：{}'.format(case))
        resp = HttpRequest().http_request(method, url, param,cookies=getattr(GetData,'COOKIE'))
        #加一个判断
        if resp.cookies:#判断请求的cookies是否为空 不为空其实就是为True
            setattr(GetData,'COOKIE',resp.cookies)#我们可以更新COOKIES这个全局变量的值
        try:
            self.assertEqual(eval(case['ExpectedResult']),resp.json())#http发送请求拿到的实际返回结果
            TestResult='Pass'
        except AssertionError as e:
            TestResult = 'Failed'
            my_log.error('http请求出错了，错误是：{}'.format(str(e)))
            raise e#处理完异常之后  不要留在家里 要抛出去
        finally:
            #写回结果
            self.t.write_back(case['CaseId'] + 1, 8, resp.text)#请注意这里
            self.t.write_back(case['CaseId'] + 1, 9, TestResult)

        my_log.info('实际结果为：{}'.format(resp.json()))#http发送请求拿到的实际返回值
