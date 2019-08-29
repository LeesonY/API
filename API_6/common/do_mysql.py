#-*- coding: utf-8 -*-

import pymysql

class DoMysql:
    '''
    完成与mysql数据库的一个交互
    '''

    def __init__(self):
        #把这些参数放到配置文件里面去做，然后在这里读取配置文件
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        port = 3306
        #创建连接
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=3306)
        self.cursor = self.mysql.cursor()

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()


    def fetch_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def close(self):
        self.cursor.close()#关闭游标
        self.mysql.close()#关闭连接

if __name__ == '__main__':
    mysql = DoMysql()
    result = mysql.fetch_one('select max(mobilephone) from future.member ')
    print(result)
    mysql.close()
