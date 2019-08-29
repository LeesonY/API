#-*- coding: utf-8 -*-

import unittest
from API_6.common.http_request import HTTPRequest2
from API_6.common import do_excel
from API_6.common import contants
from ddt import ddt,data

@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'recharge')
    cases = excel.get_cases()


    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()

    @data(*cases)
    def test_recharge(self,case):
            print(case.title)
            resp = self.http_request.request(case.method, case.url, case.data)
            actual_code = resp.json()['code']
            try:
                self.assertEqual(str(case.expected),actual_code)
                self.excel.write_result(case.case_id + 1,resp.text,'PASS')
            except AssertionError as e:
                self.excel.write_result(case.case_id + 1,resp.text,'FAIL')
                raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()























