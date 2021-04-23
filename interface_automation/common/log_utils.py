# 日志封装
import os
import time
import logging
from interface_automation.common.config_utils import configUtils
current_path = os.path.dirname(__file__)
log_output_path = os.path.join(current_path, configUtils.LOG_PATH)
# print(log_output_path)

class LogUtils:
    def __init__(self, log_path = log_output_path):
        self.log_name = os.path.join(log_output_path, 'ApiTest_%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger("ApiTestLog")
        self.logger.setLevel(configUtils.LOG_LEVEL) # 设置日志级别

        console_handler = logging.StreamHandler() # 控制台输出日志
        file_handler = logging.FileHandler(self.log_name, 'a', encoding='utf-8') # 文件输出日志
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]: %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        console_handler.close() # 防止日志打印重复
        file_handler.close()

    def get_logger(self):
        return self.logger

logger = LogUtils().get_logger() # 防止日志打印重复

if __name__ == '__main__':
    logger.info("hello")