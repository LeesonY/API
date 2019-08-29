# -*- coding: utf-8 -*-
# @Time : 2019/2/28 14:35
# @Author : 小雨点
# @Email: 1149750734@qq.com
# @File : my_log.py

import logging
from pythonLX.week10.API_5.common import project_path
class MyLog:
    def my_log(self,level,msg):
        my_logger=logging.getLogger('api-log')
        my_logger.setLevel('DEBUG')


        formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-[日志信息]:%(message)s')
        ch=logging.StreamHandler()
        ch.setLevel('INFO')#设置级别
        ch.setFormatter(formatter)#设置格式

        fh=logging.FileHandler(project_path.log_path,encoding='utf-8')#写入到指定的文件
        fh.setLevel('INFO')#设置级别
        fh.setFormatter(formatter)#设置格式

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(fh)
        my_logger.removeHandler(ch)#移除掉

    def debug(self,msg):
        self.my_log('DEBUG',msg)

    def info(self,msg):
        self.my_log('INFO',msg)

    def error(self,msg):
        self.my_log('ERROR',msg)

if __name__ == '__main__':
    test_logger=MyLog()
    test_logger.info('今天天气好晴朗！')