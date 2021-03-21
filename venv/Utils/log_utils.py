# 日志工具包
import os, logging
from Utils.config_utils import config

current_path = os.path.dirname(__file__)
default_path = os.path.join(current_path, config.read_log_path())

class LogUtils:
    def __init__(self, log_path = default_path):
        self.log_path = log_path
        self.logger = logging.getLogger('python实战日志')
        self.logger.setLevel(level= logging.DEBUG)

        file_log = logging.FileHandler(self.log_path, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelno)s - %(levelname)s - %(lineno)d - %(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)# 写入文件中

    def info(self, message): # 写入正确的日志信息
        self.logger.info(message)

    def error(self, message): # 写入错误的日志信息
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def critical(self, message):
        self.logger.critical(message)

log_obj = LogUtils(default_path)

# 测试类
if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    log_path = os.path.join(current_path, config.read_log_path())
    log_obj = LogUtils(log_path)
    log_obj.info('我是log工具包打印的info级别的日志')
    log_obj.error('我是log工具包打印的error级别的日志')
    log_obj.warning('我是log工具包打印的warning级别的日志')