#-*- coding: utf-8 -*-

import unittest
from API_8.common.http_request import HTTPRequest2
from API_8.common import do_excel
from API_8.common import logger
from API_8.common import contants
from ddt import ddt,data

logger = logger.get_logger(__name__)

@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'login')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = HTTPRequest2()

    @data(*cases)
    def test_login(self,case):
            logger.info('开始测试{0}'.format(case.title))
            resp = self.http_request.request(case.method, case.url, case.data)

            try:
                self.assertEqual(case.expected,resp.text)
                self.excel.write_result(case.case_id + 1,resp.text,'PASS')
            except AssertionError as e:
                self.excel.write_result(case.case_id + 1,resp.text,'FAIL')
                logger.error("报错了，{0}".format(e))
                raise e

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()

























