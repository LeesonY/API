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
from pythonLX.week10.API_5.common  import get_data
'''充值'''
test_data=DoExcel(project_path.case_path,'recharge').readexcel('RechargeCASE')
my_log=MyLog()
COOKIES=None#设置cookies的初始值为None
@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        self.t=DoExcel(project_path.case_path,'recharge')#写入测试结果的对象

    def tearDown(self):
        pass

    #写用例
    @data(*test_data)
    def test_cases(self,case):
        global TestResult#全局变量
        global COOKIES#声明全局变量
        method=case['Method']
        url=case['Url']
        param=eval(get_data.replace(case['Params']))


        #发起测试
        my_log.info('-------正在测试{}模块里面第{}条测试用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        my_log.info('测试数据是：{}'.format(case))
        '''充值前查询数据库获取的余额，进行保存'''
        if case['Sql'] is not None:
            sql=eval(case['Sql'])['sql']#case['Sql']取出来是个字符串，经过转换获取后得到sql语句
            before_amount=DoMysql().do_mysql(sql)[0]#充值之前的金额

        resp=HttpRequest().http_request(method,url,param,cookies=COOKIES)
        if resp.cookies:#判断请求的cookies是否为空，不为空就是True
            COOKIES=resp.cookies#更新COOKIES这个全局变量的值
        try:
            '''充值后查询数据库获取的余额，进行保存'''
            if case['Sql'] is not None:
                sql=eval(case['Sql'])['sql']#case['Sql']取出来是个字符串，经过转换获取后得到sql语句
                after_amount=DoMysql().do_mysql(sql)[0]#充值之后的金额
                recharge_amount=int(param['amount'])#转换成int
                expect_amount=before_amount + recharge_amount
                self.assertEqual(expect_amount,after_amount)#进行断言比较

            if case['ExpectedResult'].find('expect_amount')>-1:#判断是否需要做期望值的替换，find找到amount
                case['ExpectedResult'] = case['ExpectedResult'].replace('expect_amount',str(expect_amount))#进行新旧值替换
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

