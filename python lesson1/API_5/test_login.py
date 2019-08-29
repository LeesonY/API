# -*- coding: utf-8 -*-
# @Time : 2019/3/10 16:35
# @Author : 小雨点
# @Email: 1149750734@qq.com
# @File : test_cases.py
import unittest
from ddt import ddt,data
from pythonLX.week10.API_5.common.my_log import MyLog
from pythonLX.week10.API_5.common.http_request import HttpRequest
from pythonLX.week10.API_5.common.do_excel import DoExcel
from pythonLX.week10.API_5.common import project_path
from pythonLX.week10.API_5.common  import get_data
'''测试登陆'''
test_data=DoExcel(project_path.case_path,'login').readexcel('LoginCASE')
my_log=MyLog()
COOKIES=None#设置cookies的初始值为None
@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        self.t=DoExcel(project_path.case_path,'login')#写入测试结果的对象

    def tearDown(self):
        pass

    #写用例
    @data(*test_data)
    def test_cases(self,case):
        global TestResult#全局变量
        global COOKIES
        method=case['Method']
        url=case['Url']
        # param=eval(case['Params'])
        param=eval(get_data.replace(case['Params']))

        #发起测试
        my_log.info('-------正在测试{}模块里面第{}条测试用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        my_log.info('测试数据是：{}'.format(case))
        resp=HttpRequest().http_request(method,url,param,cookies=COOKIES)
        if resp.cookies:#判断请求的cookies是否为空，不为空就是True
            COOKIES=resp.cookies#更新COOKIES这个全局变量的值
        try:
            self.assertEqual(eval(case['ExpectedResult']),resp.json())
            TestResult='Pass'
        except AssertionError as e:
            TestResult = 'Failed'
            my_log.error('http请求测试用例出错了，错误是：{}'.format(e))
            raise e#处理完异常之后要抛出去！ raise e
        finally:
            #写回结果
            self.t.write_back(case['CaseId']+1, 9, resp.text)
            self.t.write_back(case['CaseId']+1, 10, TestResult)


        my_log.info('实际结果：{}'.format(resp.json()))#实际返回值

