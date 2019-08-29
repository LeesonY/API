#-*- coding: utf-8 -*-
from cProfile import run

from API_6.common.do_excel import DoExcel
from API_6.common.http_request import HttpRequest
from API_6.common import project_path

#执行用例 生成测试报告
import unittest
import HTMLTestRunnerNew
from API_6.common import project_path
from API_6.test_cases import test_register
from API_6.test_cases import test_recharge

#新建一个测试集
suite=unittest.TestSuite()

#添加用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_register))
suite.addTest(loader.loadTestsFromModule(test_recharge))

#执行用例 生成测试报告
with open(project_path.report_path,'wb')as file:

    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='lemon 0717测试报告',
                                            description='lemon 0717测试报告',
                                            tester='最爱宝宝的Tuosang')
    runner.run(suite)#执行用例 传入suite suite里面是我们收集的测试用例

