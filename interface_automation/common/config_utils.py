import configparser
import os
class ConfigUtils:
    def __init__(self,config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path, encoding='utf-8')

    def read_value(self, section, key):
        value = self.cfg.get(section, key)
        return value

    @property# 把方法变为属性方法
    def URL(self):
        url = self.cfg.get('default', 'URL')
        return url

    @property
    def CASE_DATA_PATH(self):
        casedatapath = self.cfg.get('path', 'CASE_DATA_PATH')
        return casedatapath


# 测试类
if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    config_path = os.path.join(current_path, '../local_config/config.ini')
    conf = ConfigUtils(config_path)
    print(conf.read_value('default', 'URL'))
    print(conf.URL)
    print(conf.CASE_DATA_PATH)