#-*- coding: utf-8 -*-
import os
#文件的路径 放到这里
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#配置用例的路径
case_path=os.path.join(project_path,'test_cases','test.api.xlsx')
print(case_path)