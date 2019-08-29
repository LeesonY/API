# -*- coding: utf-8 -*- 
# @Time : 2019/3/31 20:15 
# @Author : 小雨点
# @Email: 1149750734@qq.com
# @File : do_mysql.py
from mysql import connector
from pythonLX.week10.API_5.common import project_path
from pythonLX.week10.API_5.common.read_config import ReadConfig
class DoMysql:
    '''操作数据库，进行数据的读取'''
    def do_mysql(self,query,flag=1):
        '''query:sql查询语句；flag:标志 1代表获取一条数据，2代表获取多条数据'''
        db_config=ReadConfig(project_path.conf_path).get_data('DB','db_config')
        cnn=connector.connect(** db_config)#建立数据连接
        cursor=cnn.cursor()
        cursor.execute(query)
        if flag==1:
            resp=cursor.fetchone()#返回元组
        else:
            resp=cursor.fetchall()#返回的是列表嵌套元组
        return resp
if __name__=='__main__':
    query='select LeaveAmount from future.member where MobilePhone="13601676495"'
    resp=DoMysql().do_mysql(query,1)
    print('数据库的查询结果为：{}'.format(resp))