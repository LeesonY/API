#-*- coding: utf-8 -*-

import unittest
from API_4.common.http_request import HTTPRequest2
from API_4.common import do_excel
from API_4.common import contants
from ddt import ddt,data

@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'login')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()

    @data(*cases)
    def test_login(self,case):

            resp = self.http_request.request(case.method, case.url, case.data)

            try:
                self.assertEqual(case.expected,resp.text)
                self.excel.write_result(case.case_id + 1,resp.text,'PASS')
            except AssertionError as e:
                self.excel.write_result(case.case_id + 1,resp.text,'FAIL')
                raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()

























