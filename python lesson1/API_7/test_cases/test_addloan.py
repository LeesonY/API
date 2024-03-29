#-*- coding: utf-8 -*-
import unittest
from API_7.common.http_request import HttpRequest
from API_7.common.do_excel import DoExcel
from API_7.common import project_path
from API_7.common.my_log import MyLog
from ddt import ddt,data,unpack
from API_7.common.get_data import GetData
from API_7.common.do_mysql import DoMysql

#测试充值
test_data = DoExcel(project_path.case_path, 'recharge').read_data('RechargeCASE')
my_log=MyLog()

# COOKIES=None# 设置cookies的初始值为None
@ddt
class TestCases(unittest.TestCase):

    def setUp(self):#测试之前的准备工作
        self.t=DoExcel(project_path.case_path, 'add_loan')#写入测试结果的对象

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
        # param = eval(case['Params'])#请求参数
        #替换loan_id
        if case['Params'].find('loanid')!=-1:
            param=eval(case['Params'].replace('loanid',str(getattr(GetData,'LOAN_ID'))))#因为拿到的数据是int类型 replace只能用在字符串之间的替换 所以用str强转一下
        else:
            param=eval(case['Params'])
        #发起测试
        my_log.info('------正在测试{}模里面第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
        my_log.info('测试数据是：{}'.format(case))

        resp = HttpRequest().http_request(method, url, param,cookies=getattr(GetData,'COOKIE'))

        #判断是否要查询数据库
        if case['sql']!=None:#如果sql语句不为None  那就要进行数据库的查询操作
            loan_id=DoMysql().do_mysql(eval(case['sql'])['sql'],1)#返回的是元组，所以我们存储数据的时候 最好是根据索引拿到值之后 再去做进一步的操作
            setattr(GetData, 'LOAN_ID',loan_id[0])#利用反射
        #实实在在的http请求发生之后才去加一个判断，判断是否产生了cookies
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
            self.t.write_back(case['CaseId'] + 1, 9, resp.text)#请注意这里
            self.t.write_back(case['CaseId'] + 1, 10, TestResult)

        my_log.info('实际结果为：{}'.format(resp.json()))#http发送请求拿到的实际返回值
