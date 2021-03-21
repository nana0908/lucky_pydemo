# 读取配置文件的工具包

import os, configparser

current_path = os.path.dirname(__file__)
default_path = os.path.join(current_path, '../Config/config.ini')#设置默认路径
class ReadConfigFile:
    def __init__(self,config_path = default_path):
        self.config_path = config_path
        self.conf = configparser.ConfigParser() # 创建对象
        self.conf.read(config_path, encoding= 'utf-8')
    #读取ini配置文件的方法
    def read_ini(self, group, option):
        return self.conf.get(group, option)

    def read_excel_path(self):
        return self.read_ini('default', 'excel_path')

    def read_config_path(self):
        return self.read_ini('default', 'config_path')

    def read_log_path(self):
        return self.read_ini('default', 'log_path')

config = ReadConfigFile()#在类中直接创建对象

#测试类

if __name__ == '__main__':
    cf = ReadConfigFile()
    print(cf.read_config_path())
    print(cf.read_excel_path())