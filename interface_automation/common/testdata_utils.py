from interface_automation.common.excel_utils import ExcelUtil
from interface_automation.common import config
from interface_automation.common.config_utils import ConfigUtils
import os

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, config.CASE_DATA_PATH)
print(excel_path)
class TestDataUtils:
    def __init__(self, excel_path, sheet):
        self.excelUtil = ExcelUtil(excel_path, sheet)

    def get_test_data(self):
        testdata = self.excelUtil.testcase_data_list()
        return testdata

if __name__ == '__main__':
    testcase = TestDataUtils(excel_path, 'Sheet1')
    print(testcase.get_test_data())

