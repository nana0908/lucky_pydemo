import os
import xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../test_case/testcase01.xlsx').replace('\\','/')
# print(excel_path)

def read_exceldata_convert_case(excel_path):#读取excel表数据并转成用例
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_index(0)
    all_case_info = []
    for i in range(1, sheet.nrows):  # 第一行是表头，从第二行开始
        case_info = []  # 单个case信息
        for j in range(sheet.ncols):
            case_info.append(sheet.cell_value(i, j))  #
        all_case_info.append(case_info)
    print(all_case_info)