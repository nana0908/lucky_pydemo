import os
import xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../test_case/testcase01.xlsx').replace('\\','/')
# print(excel_path)

workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_index(0)

# 获取excel信息并以列表的形式打印出来[[用例编号，用例名称...],[],[]...]
all_case_info = []
for i in range(1,sheet.nrows):#第一行是表头，从第二行开始
    case_info = []#单个case信息
    for j in range(sheet.ncols):
        case_info.append(sheet.cell_value(i,j))#
    all_case_info.append(case_info)
print(all_case_info)

# 获取excel信息并以字典的形式打印出来{ case_01:{case_name: ,...},case_02:{...},...}
# [{case_no:case_01,case_name:...,...},{},...]
all_case_info = []
for i in range(1,sheet.nrows):
    case_info_dict = dict(case_no=None, case_name=None,
                          case_modle=None, case_level=None,
                          case_step=None, case_expect=None)
    case_info_dict['case_no'] = sheet.cell_value(i, 0)
    case_info_dict['case_name'] = sheet.cell_value(i, 1)
    case_info_dict['case_modle'] = sheet.cell_value(i, 2)
    case_info_dict['case_level'] = sheet.cell_value(i, 3)
    case_info_dict['case_step'] = sheet.cell_value(i, 4)
    case_info_dict['case_expect'] = sheet.cell_value(i, 5)
    all_case_info.append(case_info_dict)
print(all_case_info)

#类的方式实现获取用例信息
class CaseInfo:
    def __init__(self, case_id, case_name, case_modle, case_level, case_step, expect_result):
        self.case_id = case_id
        self.case_name = case_name
        self.case_modle = case_modle
        self.case_level = case_level
        self.case_step = case_step
        self.expect_result = expect_result
    def caseinfo(self):
        return [self.case_id, self.case_name, self.case_modle,
                self.case_level, self.case_step, self.expect_result]
all_case_info = []
for i in range(1,sheet.nrows):
    case_id = sheet.cell_value(i, 0)
    case_name = sheet.cell_value(i, 1)
    case_modle = sheet.cell_value(i, 2)
    case_level = sheet.cell_value(i, 3)
    case_step = sheet.cell_value(i, 4)
    expect_result = sheet.cell_value(i, 5)

    case_info = CaseInfo(case_id, case_name, case_modle, case_level, case_step, expect_result)
    all_case_info.append(case_info.caseinfo())
print(all_case_info)





