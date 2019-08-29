# -*- coding: utf-8 -*-
# @Time : 2019/3/21 08:35
# @Author : 小雨点
# @Email: 1149750734@qq.com
# @File : run.py


import unittest
import HTMLTestRunner
from pythonLX.week10.API_5.common import project_path
from pythonLX.week10.API_5.test_cases import test_login#导入模块
from pythonLX.week10.API_5.test_cases import test_register#导入模块
from pythonLX.week10.API_5.test_cases import test_recharge#导入模块
from pythonLX.week10.API_5.test_cases import test_withdraw#导入模块
from pythonLX.week10.API_5.test_cases import test_bidLoan#导入模块

#新建一个测试集
suite=unittest.TestSuite()

#添加用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_login))#注意使用Module
suite.addTest(loader.loadTestsFromModule(test_register))
suite.addTest(loader.loadTestsFromModule(test_recharge))
suite.addTest(loader.loadTestsFromModule(test_withdraw))
suite.addTest(loader.loadTestsFromModule(test_bidLoan))

#执行用例 生成测试报告
with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='小雨点-测试报告',
                                            description='测试前程贷接口')
    runner.run(suite)#执行用例
