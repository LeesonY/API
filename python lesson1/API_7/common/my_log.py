#-*- coding: utf-8 -*-

import logging
from  API_7.common import project_path

class MyLog:

    def my_log(self,level,msg):
        my_logger=logging.getLogger('api-log')
        my_logger.setLevel('INFO')


        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-[日志信息]:%(message)s')
        ch=logging.StreamHandler()
        ch.setLevel('INFO')#设置级别
        ch.setFormatter(formatter)#设置格式

        fh=logging.FileHandler(project_path.log_path,encoding='utf-8')#写到指定的文件里面去
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

        my_logger.removeHandler(fh)#fh ch
        my_logger.removeHandler(ch)#一定要记得移除掉

    def debug(self,msg):
        self.my_log('DEBUG',msg)

    def info(self,msg):
        self.my_log('INFO',msg)

    def error(self,msg):
        self.my_log('ERROP',msg)

if __name__ == '__main__':
    # test_logger=MyLog("1.log")
    test_logger=MyLog()
    test_logger.info('凡王之血，必以剑终！')












