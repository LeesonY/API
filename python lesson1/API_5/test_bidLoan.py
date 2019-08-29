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
from pythonLX.week10.API_5.common.do_mysql import DoMysql
from pythonLX.week10.API_5.common.get_data import GetData
from pythonLX.week10.API_5.common  import get_data
'''测试投资、加标'''
test_data=DoExcel(project_path.case_path,'bidLoan').readexcel('BidLoadCASE')
my_log=MyLog()
COOKIES=None#设置cookies的初始值为None
@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        self.t=DoExcel(project_path.case_path,'bidLoan')#写入测试结果的对象

    def tearDown(self):
        pass

    #写用例
    @data(*test_data)
    def test_cases(self,case):
        global TestResult#全局变量
        global COOKIES#声明全局变量
        method=case['Method']
        url=case['Url']
        #替换mobilephone,pwd
        param=eval(get_data.replace(case['Params']))

        #发起测试
        my_log.info('-------正在测试{}模块里面第{}条测试用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        my_log.info('测试数据是：{}'.format(case))
        '''投资前查询数据库获取的余额，进行保存'''
        if case['Sql'] is not None:#如果sql语句不为None,就要进行数据库查询
            sql=eval(case['Sql'])['sql']#case['Sql']取出来是个字符串，经过转换获取后得到sql语句
            before_amount=DoMysql().do_mysql(sql)[0]#投资之前的金额
        resp=HttpRequest().http_request(method,url,param,cookies=COOKIES)
        if resp.cookies:#判断请求的cookies是否为空，不为空就是True
            COOKIES=resp.cookies#更新COOKIES这个全局变量的值
        try:
            self.assertEqual(eval(case['ExpectedResult']),resp.json())
            #投资后的查询数据据的余额
            if case['Sql'] is not None:
                sql=eval(case['Sql'])['sql']
                after_amount=DoMysql().do_mysql(sql)[0]
            #加一个断言，投资前后的余额断言
                invest_amount= param['amount']#投资金额
                except_amount= before_amount - invest_amount #投资前的金额减投资金额
                self.assertEqual(except_amount,after_amount)
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

