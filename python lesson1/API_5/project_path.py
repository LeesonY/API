# -*- coding: utf-8 -*-
# @Time : 2019/3/11 08:35
# @Author : 小雨点
# @Email: 1149750734@qq.com
# @File : project_path.py

import os
#文件的路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试用例的路径
case_path=os.path.join(project_path,'test_cases','cases.xlsx')
# print(case_path)

#测试报告的路径
report_path=os.path.join(project_path,'test_result','test_report','test_report.html')

#日志的路径
log_path=os.path.join(project_path,'test_result','test_log','test.log')

#配置文件的路径
conf_path=os.path.join(project_path,'conf','case.conf')
