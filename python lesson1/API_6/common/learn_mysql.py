#-*- coding: utf-8 -*-

#操作mysql
#mysql

#pymysql  mysql-connector-python
#pip install pymysql
#pip install mysql-connector-python

#navicat 界面工具 链接数据库 来做操作的
#数据库的链接信息：
#47.107.168.87  端口3306 用户名python   密码 python666

from mysql import connector

#第一步：链接数据库
#提供数据库的连接信息
db_config={'host':'120.78.128.25',
           'user':'lemon57',
           'password':'123456',
           'port':3306,
           'database':'lemon57',
           }

cnn=connector.connect(**db_config)#建立一个链接

#第二步：获取游标  获取操作数据库的权限
cursor=cnn.cursor()

#第三步：操作数据表
query='select Id,MobilePhone from member where Id<=23528 '
res=cursor.execute(query)

#第四步：获取查询的结果并打印结果  readline  readlines
#每一个符合条件的数据都会存在元组里面
res1=cursor.fetchone()#返回的元组
res2=cursor.fetchall()#返回的是列表嵌套元组
print('数据库的查询结果1：{}'.format(res1))
print('数据库的查询结果2：{}'.format(res2))



#增深改 update
#cursor.execute(query)
#cursor.execute('commit')提交
#查select











