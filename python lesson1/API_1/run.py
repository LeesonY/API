#-*- coding: utf-8 -*-
from common.do_excel import DoExcel
from common.http_request import HttpRequest
from  API_1.common import project_path

#完成用例的测试

#1:读取到测试数据
test_data=DoExcel(project_path.case_path,'test_case').read_data()
#2:执行测试:遍历--根据Key取值
for case in test_data:
    method=case['Method']
    url=case['Url']
    param=eval(case['Params'])

    #发起测试
    print('------正在测试{}模里面第{}条测试用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
    resp=HttpRequest().http_request(method,url,param)
    print('实际结果为：{}'.format(resp.json()))


    #对比结果
    if resp.json()==eval(case['ExpectedResult']):
        TestResult='Pass'
    else:
        TestResult='Failed'
    print('该条用例测试结论是：{}'.format(TestResult))

    #需要写回什么？实际结果/测试结论
    t=DoExcel(project_path.case_path,'test_case')
    t.write_back(case['CaseId']+1,8,resp.text)
    t.write_back(case['CaseId']+1,9,TestResult)