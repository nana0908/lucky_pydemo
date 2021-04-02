import os
from interface_automation.common.config_utils import ConfigUtils

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '../local_config/config.ini')
configUtils = ConfigUtils(config_path)
# 读取数据
URL = configUtils.read_value('default', 'URL')
CASE_DATA_PATH = configUtils.read_value('path', 'CASE_DATA_PATH')
