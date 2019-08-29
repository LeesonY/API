#-*- coding: utf-8 -*-
#什么是日志？

#日志的作用是什么
#日志的等级 debug-info-warning-error-critical/fatal


import logging

class Mylog:
    def __init__(self,Level="DEBUG"):
        self.Level=Level
    def my_log(self):


    #日志收集器logger        默认日志收集器 root logger
    #日志输出渠道 handlers    控制台console file txt test.log

    #1：定义一个日志收集器并且还要设置级别 getlogger
        my_logger=logging.getLogger('python16')
        # my_logger.setLevel('INFO')
        my_logger.setLevel(self.Level)

        #2:指定输出渠道还要设置级别 streamHandler--控制台 FileHandler 输出指定文件
        ch=logging.StreamHandler()
        ch.setLevel(self.Level)

        fh=logging.FileHandler('test.log',encoding='utf-8')

        # fh.setLevel('INFO')
        fh.setLevel(self.Level)

        #3:对接  最终输出的信息是取两者的交集
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        my_logger.debug('this is debug mas')
        my_logger.info('我是python14期的主讲老师：华华')
        my_logger.warning('this is warning msg')
        my_logger.error('我今天缺课了')
        my_logger.critical('this is critical msg')

        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

if __name__ == '__main__':
    Mylog("INFO").my_log()








# from  configparser import  ConfigParser
# class ReadConfig:
#     cf=ConfigParser()
#     cf.read('case.conf',encoding='utf-8')
#
#     def get_int(self):
#         '''从配置文件里获取一个整数'''
#         value=self.cf.getint('CASE','age')#sectiion   option
#         return value