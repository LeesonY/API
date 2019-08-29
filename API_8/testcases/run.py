#-*- coding: utf-8 -*-

import unittest
from API_8.testcases import test_register
from API_8.testcases import test_login
from API_8.common import contants
import HTMLTestRunnerNew

# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_register))
# suite.addTest(loader.loadTestsFromModule(test_login))

discover = unittest.defaultTestLoader.discover(contants.case_dir,"test_*.py")

with open(contants.report_dir + '/report.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="PYTHON15 API TEST REPORT",
                                              description="q前程贷API",
                                              tester="mongo")
    runner.run(discover)

















