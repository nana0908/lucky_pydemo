# 使用config工具包
import os
# from Utils.config_utils import ReadConfigFile
from Utils.config_utils import config#直接导入对象
# conf_obj = ReadConfigFile()
from PyModule.class_encapsulation import ReadExcel

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, config.read_excel_path())

excel_info = ReadExcel(excel_path)
excel_info_list = excel_info.read_excel_save_list()
excel_info_list_obj = excel_info.read_excel_save_list_obj()
for i in range(len(excel_info_list)):
    print(excel_info_list[i])
for i in range(len(excel_info_list_obj)):
    print(excel_info_list_obj[i].stu_name)

